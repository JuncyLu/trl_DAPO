from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple

import torch


@dataclass
class AttentionSegmentResult:
    """注意力层段结果数据类
    
    Attributes:
        mdi: 模态主导指数 (Modality Dominance Index)
        aei_text: 文本注意力效率指数 (Attention Efficiency Index for text)
        aei_vision: 视觉注意力效率指数 (Attention Efficiency Index for vision)
        attention_text: 对文本的总注意力
        attention_vision: 对视觉的总注意力
    """
    mdi: float
    aei_text: float
    aei_vision: float
    attention_text: float
    attention_vision: float


@dataclass
class AttentionSampleResult:
    """注意力样本结果数据类
    
    Attributes:
        segments: 按层段分组的结果字典
        num_instruction_tokens: 指令（文本）tokens 数量
        num_vision_tokens: 视觉 tokens 数量
        num_generated_tokens: 生成的 tokens 数量
        num_prompt_queries: 提示词查询数量
        total_queries: 总查询数量
        actual_prompt_length: 实际提示词长度
    """
    segments: Dict[str, AttentionSegmentResult]
    num_instruction_tokens: int
    num_vision_tokens: int
    num_generated_tokens: int
    num_prompt_queries: int
    total_queries: int
    actual_prompt_length: int


def _row_normalize(values: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    """对张量进行行归一化
    
    Args:
        values: 输入张量
        eps: 防止除零的小常数
        
    Returns:
        归一化后的张量
    """
    if values.ndim == 1:
        denom = values.sum()
        if torch.abs(denom) < eps:
            return values
        return values / denom
    if values.ndim != 2:
        raise ValueError("Expected a 2D tensor for row normalization")
    denom = values.sum(dim=-1, keepdim=True)
    denom = torch.where(torch.abs(denom) < eps, torch.ones_like(denom), denom)
    return values / denom


def _collect_llm_attention_for_sample(
    outputs_attentions: Iterable,
    sample_idx: int,
    normalize_rows: bool = True,
    zero_bos: bool = True,
) -> Dict[int, torch.Tensor]:
    """收集单个样本的注意力数据
    
    Args:
        outputs_attentions: 模型输出的注意力数据
        sample_idx: 样本索引
        normalize_rows: 是否对行进行归一化
        zero_bos: 是否将 BOS token 的注意力置零
        
    Returns:
        按层索引的注意力张量字典
    """
    if outputs_attentions is None:
        return {}

    outputs_attentions = list(outputs_attentions)
    if len(outputs_attentions) == 0:
        return {}

    first_step_layers = outputs_attentions[0]
    num_layers = len(first_step_layers)
    per_layer_rows: Dict[int, List[torch.Tensor]] = {i: [] for i in range(num_layers)}

    # 处理第一步的注意力
    for layer_idx, layer_attn in enumerate(first_step_layers):
        if layer_attn is None:
            continue
        attn = layer_attn[sample_idx]  # [num_heads, tgt_len, src_len]
        attn_avg = attn.mean(dim=0)  # [tgt_len, src_len]
        if attn_avg.shape[0] > 0:
            cur = attn_avg[:-1].clone()
        else:
            cur = attn_avg.clone()
        if cur.numel() == 0:
            continue
        if zero_bos and cur.shape[1] >= 1 and cur.shape[0] >= 2:
            cur[1:, 0] = 0.0
        if normalize_rows:
            cur = _row_normalize(cur)
        # 直接移动到CPU，避免在GPU上逐行操作
        cur_cpu = cur.detach().cpu()
        for row in cur_cpu:
            per_layer_rows[layer_idx].append(row)
        # 清理中间张量
        del attn, attn_avg, cur

    # 处理后续步骤的注意力
    for step_layers in outputs_attentions[1:]:
        for layer_idx, layer_attn in enumerate(step_layers):
            if layer_attn is None:
                continue
            attn = layer_attn[sample_idx]  # [num_heads, tgt_len, src_len]
            attn_avg = attn.mean(dim=0)  # [tgt_len, src_len]
            if attn_avg.shape[0] == 0:
                continue
            row = attn_avg[-1].clone()
            if zero_bos and row.shape[0] >= 1:
                row[0] = 0.0
            if normalize_rows:
                row = _row_normalize(row)
            # 直接移动到CPU，避免GPU上的cat操作
            row_cpu = row.detach().cpu()
            # 在CPU上添加padding
            row_cpu = torch.cat([row_cpu, torch.zeros(1, dtype=row_cpu.dtype)])
            per_layer_rows[layer_idx].append(row_cpu)
            # 清理中间张量
            del attn, attn_avg, row

    result: Dict[int, torch.Tensor] = {}
    for layer_idx, rows in per_layer_rows.items():
        if len(rows) == 0:
            result[layer_idx] = torch.zeros(0, 0)
            continue
        max_len = max(row.shape[0] for row in rows)
        padded_rows = []
        for row in rows:
            if row.shape[0] < max_len:
                pad = torch.zeros(max_len - row.shape[0], dtype=row.dtype)
                row = torch.cat([row, pad], dim=0)
            padded_rows.append(row)
        result[layer_idx] = torch.stack(padded_rows, dim=0)
        # 清理中间数据
        del padded_rows
    
    # 清理所有中间数据
    del per_layer_rows
    return result


def _compute_mdi(attn_text: float, attn_vision: float, tokens_text: int, tokens_vision: int) -> float:
    """计算模态主导指数 (MDI)
    
    MDI = (A_T/|T|) / (A_O/|O|)
    其中 A_T 是对文本 tokens 的总注意力，A_O 是对视觉 tokens 的总注意力
    
    Args:
        attn_text: 对文本 tokens 的总注意力
        attn_vision: 对视觉 tokens 的总注意力
        tokens_text: 文本 tokens 数量
        tokens_vision: 视觉 tokens 数量
        
    Returns:
        MDI 值
    """
    assert tokens_text > 0, "tokens_text must be > 0"
    assert tokens_vision >= 0, "tokens_vision must be >= 0"
    
    if tokens_vision == 0:
        return float("inf")
    
    text_ratio = attn_text / tokens_text
    vision_ratio = attn_vision / tokens_vision
    mdi = text_ratio / vision_ratio
    
    if not (mdi > 0) or not (mdi < float("inf")):
        return float("nan")
    
    return mdi


def _compute_aei(
    attn_text: float, attn_vision: float, tokens_text: int, tokens_vision: int, modality: str = "text"
) -> float:
    """计算注意力效率指数 (AEI)
    
    AEI = attention_share / token_share
    其中 attention_share 是某模态的注意力占比，token_share 是某模态的 token 占比
    
    Args:
        attn_text: 对文本 tokens 的总注意力
        attn_vision: 对视觉 tokens 的总注意力
        tokens_text: 文本 tokens 数量
        tokens_vision: 视觉 tokens 数量
        modality: 计算哪个模态的 AEI ("text" 或 "vision")
        
    Returns:
        AEI 值
    """
    if modality not in {"text", "vision"}:
        raise ValueError("modality must be 'text' or 'vision'")
    if tokens_text < 0 or tokens_vision < 0:
        raise ValueError("token counts must be >= 0")
    total_attn = attn_text + attn_vision
    total_tokens = tokens_text + tokens_vision
    if total_tokens == 0:
        return float("inf")

    if modality == "text":
        token_share = tokens_text / total_tokens if total_tokens > 0 else 0.0
        attention_share = attn_text / total_attn if total_attn > 0 else 0.0
    else:
        token_share = tokens_vision / total_tokens if total_tokens > 0 else 0.0
        attention_share = attn_vision / total_attn if total_attn > 0 else 0.0
    if token_share == 0:
        return float("inf")
    return attention_share / token_share


def _build_modality_masks(
    input_ids: torch.Tensor,
    vision_token_spans: List[Tuple[int, int]],
    special_token_ids: Dict[str, int],
) -> Tuple[torch.Tensor, torch.Tensor]:
    """构建文本和视觉模态的掩码
    
    Args:
        input_ids: 输入 token IDs
        vision_token_spans: 视觉 token 的起始和结束位置
        special_token_ids: 特殊 token 的 ID 映射
        
    Returns:
        (instruction_mask, vision_mask) 元组
    """
    if input_ids.ndim != 1:
        raise ValueError("input_ids must be 1D")

    if input_ids.device.type != "cpu":
        input_ids = input_ids.cpu()

    seq_len = int(input_ids.shape[0])
    if seq_len <= 0:
        raise ValueError("Sequence length must be > 0 to build masks")

    device = torch.device("cpu")

    vision_mask = torch.zeros(seq_len, dtype=torch.bool, device=device)
    for start, end in vision_token_spans:
        if start is None or end is None:
            continue
        s = max(0, int(start))
        e = min(seq_len, int(end))
        if e > s:
            vision_mask[s:e] = True

    instruction_mask = torch.ones(seq_len, dtype=torch.bool, device=device)
    instruction_mask &= ~vision_mask

    specials = set(special_token_ids.values()) if special_token_ids is not None else set()
    if specials:
        input_list = input_ids.tolist()
        for idx, token_id in enumerate(input_list):
            if token_id in specials:
                instruction_mask[idx] = False

    return instruction_mask, vision_mask


def _split_layers_to_segments(num_layers: int) -> Dict[str, List[int]]:
    """将模型层分割为不同的段
    
    Args:
        num_layers: 总层数
        
    Returns:
        包含 "early", "middle", "late", "all" 段层索引的字典
    """
    if num_layers < 0:
        raise ValueError("num_layers must be >= 0")
    k = num_layers // 3 if num_layers > 0 else 0
    return {
        "early": list(range(0, k)),
        "middle": list(range(k, 2 * k)),
        "late": list(range(2 * k, num_layers)),
        "all": list(range(num_layers)),
    }


def _compute_segment_metrics(
    per_layer_attn: Dict[int, torch.Tensor],
    instruction_mask: torch.Tensor,
    vision_mask: torch.Tensor,
    layer_indices: List[int],
    num_prompt_queries: int,
    actual_prompt_length: int,
) -> AttentionSegmentResult:
    """计算指定层段的注意力指标
    
    严格参考本地Qwen流程：
    - 使用"生成阶段"的query行（即从num_prompt_queries开始的行）
    - 仅对"提示词键"（前actual_prompt_length列）累积注意力，并按行归一化
    - 按文本/视觉键掩码分别汇总，再在层维度做平均
    
    Args:
        per_layer_attn: 每层的注意力张量
        instruction_mask: 指令（文本）token 掩码
        vision_mask: 视觉 token 掩码
        layer_indices: 要计算的层索引列表
        num_prompt_queries: 提示词查询数量
        actual_prompt_length: 实际提示词长度
        
    Returns:
        注意力段结果
    """
    if not layer_indices:
        return AttentionSegmentResult(float("nan"), float("nan"), float("nan"), 0.0, 0.0)

    total_queries = 0
    for layer_idx in layer_indices:
        attn = per_layer_attn.get(layer_idx)
        if attn is not None and attn.numel() > 0:
            total_queries = attn.shape[0]
            break
    if total_queries == 0:
        return AttentionSegmentResult(float("nan"), float("nan"), float("nan"), 0.0, 0.0)

    # 生成阶段的query行数
    gen_row_start = max(num_prompt_queries, 0)
    if gen_row_start >= total_queries:
        return AttentionSegmentResult(float("nan"), float("nan"), float("nan"), 0.0, 0.0)
    
    # 验证生成阶段是否有足够的tokens
    generated_tokens = total_queries - num_prompt_queries
    if generated_tokens <= 0:
        return AttentionSegmentResult(float("nan"), float("nan"), float("nan"), 0.0, 0.0)

    attn_text_total = 0.0
    attn_vision_total = 0.0
    num_layers_with_data = 0

    for layer_idx in layer_indices:
        attn = per_layer_attn.get(layer_idx)
        if attn is None or attn.shape[0] == 0:
            continue

        # 取生成阶段queries对应的注意力行，并裁剪到提示词键列
        gen_attn = attn[gen_row_start:, :actual_prompt_length]

        # 将vision/text键掩码对齐到actual_prompt_length
        if vision_mask.shape[0] != actual_prompt_length:
            if vision_mask.shape[0] < actual_prompt_length:
                pad = torch.zeros(actual_prompt_length - vision_mask.shape[0], dtype=vision_mask.dtype)
                vision_mask_prompt = torch.cat([vision_mask, pad], dim=0)
            else:
                vision_mask_prompt = vision_mask[:actual_prompt_length]
        else:
            vision_mask_prompt = vision_mask

        text_keys_mask = (~vision_mask_prompt).to(gen_attn.device)
        vision_keys_mask = vision_mask_prompt.to(gen_attn.device)

        # 行归一化
        gen_attn_sum = gen_attn.sum(dim=1, keepdim=True)
        gen_attn_sum = torch.where(gen_attn_sum > 1e-12, gen_attn_sum, torch.ones_like(gen_attn_sum))
        gen_attn_norm = gen_attn / gen_attn_sum

        attn_text_total += gen_attn_norm[:, text_keys_mask].sum().item()
        attn_vision_total += gen_attn_norm[:, vision_keys_mask].sum().item()
        num_layers_with_data += 1
        
        # 清理中间张量
        del gen_attn, gen_attn_norm, text_keys_mask, vision_keys_mask

    if num_layers_with_data == 0:
        return AttentionSegmentResult(float("nan"), float("nan"), float("nan"), 0.0, 0.0)

    attn_text_avg = attn_text_total / num_layers_with_data
    attn_vision_avg = attn_vision_total / num_layers_with_data

    num_instruction = int(instruction_mask.sum().item())
    num_vision = int(vision_mask.sum().item())

    mdi = _compute_mdi(attn_text_avg, attn_vision_avg, max(num_instruction, 1), max(num_vision, 0))
    aei_text = _compute_aei(attn_text_avg, attn_vision_avg, max(num_instruction, 0), max(num_vision, 0), "text")
    aei_vision = _compute_aei(attn_text_avg, attn_vision_avg, max(num_instruction, 0), max(num_vision, 0), "vision")

    return AttentionSegmentResult(mdi, aei_text, aei_vision, attn_text_avg, attn_vision_avg)


def compute_qwen_attention_metrics_for_batch(
    _model,
    processor,
    outputs_attentions,
    input_ids: torch.Tensor,
    sequences: torch.Tensor,
    image_grid_thw: Optional[torch.Tensor] = None,
) -> Tuple[List[Optional[AttentionSampleResult]], List[Optional[str]]]:
    """为批次计算 Qwen 注意力指标
    
    Args:
        _model: 模型实例（未使用，保持接口兼容性）
        processor: 处理器实例
        outputs_attentions: 模型输出的注意力数据
        input_ids: 输入 token IDs
        sequences: 生成的序列
        image_grid_thw: 图像网格信息
        
    Returns:
        (样本结果列表, 跳过原因列表) 元组
    """
    batch_size = input_ids.size(0)
    results: List[Optional[AttentionSampleResult]] = []
    skip_reasons: List[Optional[str]] = []

    if outputs_attentions is None or len(outputs_attentions) == 0:
        return results, skip_reasons

    segments = _split_layers_to_segments(len(outputs_attentions[0]))
    special_token_ids = get_qwen_special_token_ids(processor)

    if image_grid_thw is not None and image_grid_thw.dim() == 3:
        grid_items = [image_grid_thw[i] for i in range(image_grid_thw.size(0))]
    elif image_grid_thw is not None and image_grid_thw.dim() == 2:
        grid_items = [image_grid_thw[i] for i in range(image_grid_thw.size(0))]
    else:
        grid_items = [None] * batch_size

    for batch_idx in range(batch_size):
        per_layer_attn = _collect_llm_attention_for_sample(outputs_attentions, batch_idx)
        if not per_layer_attn:
            results.append(None)
            skip_reasons.append("no_attention")
            continue

        input_ids_sample = input_ids[batch_idx].detach().cpu()
        spans = extract_vision_token_spans_qwen(
            _model,
            processor,
            input_ids_sample,
            grid_items[batch_idx] if grid_items else None,
        )

        instruction_mask, vision_mask = _build_modality_masks(
            input_ids_sample,
            spans,
            special_token_ids,
        )

        num_text_tokens = int(instruction_mask.sum().item())
        num_vision_tokens = int(vision_mask.sum().item())
        actual_prompt_length = instruction_mask.numel()
        num_prompt_queries = max(actual_prompt_length - 1, 0)

        total_queries = 0
        any_layer = next(iter(per_layer_attn.values()), None)
        if any_layer is not None and any_layer.numel() > 0:
            total_queries = any_layer.shape[0]
        num_generated_tokens = max(total_queries - num_prompt_queries, 0)

        if total_queries <= num_prompt_queries:
            results.append(None)
            skip_reasons.append("no_generated_queries")
            continue
        if num_vision_tokens <= 0:
            results.append(None)
            skip_reasons.append("no_vision_tokens")
            continue

        segment_results: Dict[str, AttentionSegmentResult] = {}
        for segment_name, layer_indices in segments.items():
            segment_results[segment_name] = _compute_segment_metrics(
                per_layer_attn,
                instruction_mask,
                vision_mask,
                layer_indices,
                num_prompt_queries=num_prompt_queries,
                actual_prompt_length=actual_prompt_length,
            )

        results.append(
            AttentionSampleResult(
                segments=segment_results,
                num_instruction_tokens=int(instruction_mask.sum().item()),
                num_vision_tokens=int(vision_mask.sum().item()),
                num_generated_tokens=num_generated_tokens,
                num_prompt_queries=num_prompt_queries,
                total_queries=total_queries,
                actual_prompt_length=actual_prompt_length,
            )
        )
        skip_reasons.append(None)
        
        # 清理中间数据
        del per_layer_attn, input_ids_sample, spans, instruction_mask, vision_mask

    return results, skip_reasons


def get_qwen_special_token_ids(processor) -> Dict[str, int]:
    """获取 Qwen 特殊 token IDs
    
    Args:
        processor: 处理器实例
        
    Returns:
        特殊 token ID 字典
    """
    tokenizer = processor.tokenizer
    special_ids: Dict[str, int] = {}

    basic_tokens = {
        "bos": tokenizer.bos_token_id,
        "eos": tokenizer.eos_token_id,
        "pad": tokenizer.pad_token_id,
    }
    for name, token_id in basic_tokens.items():
        if token_id is not None:
            special_ids[name] = token_id

    special_tokens = {
        "im_start": "<|im_start|>",
        "im_end": "<|im_end|>",
        "vision_start": "<|vision_start|>",
        "vision_end": "<|vision_end|>",
    }
    for name, token_str in special_tokens.items():
        try:
            token_id = tokenizer.convert_tokens_to_ids(token_str)
            if token_id is not None and token_id != tokenizer.unk_token_id and token_id >= 0:
                special_ids[name] = token_id
        except Exception:
            continue

    return special_ids


def extract_vision_token_spans_qwen(
    _model,
    processor,
    input_ids: torch.Tensor,
    image_grid_thw: Optional[torch.Tensor] = None,
) -> List[Tuple[int, int]]:
    """提取 Qwen 视觉 token 的跨度
    
    Args:
        _model: 模型实例（未使用，保持接口兼容性）
        processor: 处理器实例
        input_ids: 输入 token IDs
        image_grid_thw: 图像网格信息（未使用，保持接口兼容性）
        
    Returns:
        视觉 token 跨度列表
    """
    special_ids = get_qwen_special_token_ids(processor)
    vision_start_id = special_ids.get("vision_start")
    vision_end_id = special_ids.get("vision_end")
    if vision_start_id is None or vision_end_id is None:
        return []

    positions = (input_ids == vision_start_id).nonzero(as_tuple=False).flatten().tolist()
    if not positions:
        return []

    spans: List[Tuple[int, int]] = []
    for pos in positions:
        search_start = pos + 1
        remaining = input_ids[search_start:]
        relative = (remaining == vision_end_id).nonzero(as_tuple=False).flatten()
        if len(relative) == 0:
            continue
        end_pos = search_start + relative[0].item()
        spans.append((pos, end_pos + 1))
    return spans
