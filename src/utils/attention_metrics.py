from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

import torch


@dataclass
class AttentionSegmentResult:
    """Attention metrics for a specific layer segment."""
    vgr: float
    attention_text: float
    attention_vision: float


@dataclass
class AttentionSampleResult:
    """Attention metrics for a single sample across all layer segments."""
    segments: Dict[str, AttentionSegmentResult]
    num_instruction_tokens: int
    num_vision_tokens: int
    num_generated_tokens: int
    num_prompt_queries: int
    total_queries: int
    actual_prompt_length: int


def _row_normalize(values: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    """Normalize tensor rows to sum to 1."""
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
    last_k_layers: Optional[int] = None,
) -> Dict[int, torch.Tensor]:
    """Extract and process attention weights for a single sample."""
    if outputs_attentions is None:
        return {}

    outputs_attentions = list(outputs_attentions)
    
    if len(outputs_attentions) == 0:
        return {}

    first_step_layers = outputs_attentions[0]
    num_layers = len(first_step_layers)
    # Select layer indices: all or only last-K
    if last_k_layers is not None and last_k_layers > 0:
        last = min(last_k_layers, num_layers)
        selected_indices = list(range(num_layers))[-last:]
    else:
        selected_indices = list(range(num_layers))
    selected_set = set(selected_indices)
    per_layer_rows: Dict[int, List[torch.Tensor]] = {i: [] for i in selected_indices}

    # Process first step attention
    for layer_idx, layer_attn in enumerate(first_step_layers):
        if layer_idx not in selected_set:
            continue
        if layer_attn is None:
            continue
        # 提前搬到 CPU 再做 mean，避免在 GPU 上保留大矩阵 (B, H, T, S)
        attn_cpu = layer_attn[sample_idx].detach().cpu()  # [num_heads, tgt_len, src_len]
        attn_avg = attn_cpu.mean(dim=0)  # [tgt_len, src_len] on CPU
        # 及时释放 GPU/CPU 临时变量
        del attn_cpu
        
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
        # cur 已经在 CPU 上，不需要再次 .cpu()
        for row in cur:
            per_layer_rows[layer_idx].append(row)
        del attn_avg, cur

    # Process subsequent steps
    for step_layers in outputs_attentions[1:]:
        for layer_idx, layer_attn in enumerate(step_layers):
            if layer_idx not in selected_set:
                continue
            if layer_attn is None:
                continue
            # 同样先搬 CPU，再求 mean
            attn_cpu = layer_attn[sample_idx].detach().cpu()
            attn_avg = attn_cpu.mean(dim=0)
            del attn_cpu
            if attn_avg.shape[0] == 0:
                continue
            row = attn_avg[-1].clone()
            if zero_bos and row.shape[0] >= 1:
                row[0] = 0.0
            if normalize_rows:
                row = _row_normalize(row)
            # row 已经在 CPU 上，不需要再次 .cpu()
            row = torch.cat([row, torch.zeros(1, dtype=row.dtype)])
            per_layer_rows[layer_idx].append(row)
            del attn_avg, row

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
        del padded_rows
    
    del per_layer_rows
    return result


# ----------------- 核心指标计算 -----------------

def _compute_vgr(attn_text: float, attn_vision: float, tokens_text: int, tokens_vision: int) -> float:
    """Compute Vision-Text Gain Ratio (VGR): (attn_text/tokens_text) / (attn_vision/tokens_vision)."""
    assert tokens_text > 0, "tokens_text must be > 0"
    assert tokens_vision >= 0, "tokens_vision must be >= 0"
    
    if tokens_vision == 0:
        return float("inf")
    
    text_ratio = attn_text / tokens_text
    vision_ratio = attn_vision / tokens_vision
    vgr = text_ratio / vision_ratio
    
    if not (vgr > 0) or not (vgr < float("inf")):
        return float("nan")
    
    return vgr


def _compute_aei(
    attn_text: float, attn_vision: float, tokens_text: int, tokens_vision: int, modality: str = "text"
) -> float:
    """Compute Attention Efficiency Index: attention_share / token_share for given modality."""
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
    """Build boolean masks for instruction and vision tokens."""
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
        # 仅保留视觉patch内部区域，不包含 <|vision_start|> 与 <|vision_end|>
        inner_start = s + 1
        inner_end = e - 1
        if inner_end > inner_start:
            vision_mask[inner_start:inner_end] = True

    instruction_mask = torch.ones(seq_len, dtype=torch.bool, device=device)
    instruction_mask &= ~vision_mask

    specials = set(special_token_ids.values()) if special_token_ids is not None else set()
    if specials:
        input_list = input_ids.tolist()
        for idx, token_id in enumerate(input_list):
            if token_id in specials:
                instruction_mask[idx] = False

    # 从文本池剔除第一个 system 段（<|im_start|> ... <|im_end|> 之间）
    if special_token_ids is not None:
        im_start_id = special_token_ids.get("im_start")
        im_end_id = special_token_ids.get("im_end")
        if im_start_id is not None and im_end_id is not None:
            ids_list = input_ids.tolist()
            try:
                start_idx = ids_list.index(im_start_id)
                # 寻找 start_idx 之后的第一个 im_end
                try:
                    end_rel = ids_list[start_idx + 1 :].index(im_end_id)
                    end_idx = start_idx + 1 + end_rel
                    if 0 <= start_idx < end_idx <= seq_len - 1:
                        # 剔除系统段（包含起止，特殊符号已在上面剔除，这里包含也无妨）
                        instruction_mask[start_idx : end_idx + 1] = False
                except ValueError:
                    pass
            except ValueError:
                pass

    return instruction_mask, vision_mask


def _split_layers_to_segments(num_layers: int) -> Dict[str, List[int]]:
    """Return only a single 'all' segment over all layers (0..num_layers-1)."""
    if num_layers < 0:
        raise ValueError("num_layers must be >= 0")
    return {"all": list(range(num_layers))}

def _split_indices_to_segments(layer_indices: List[int]) -> Dict[str, List[int]]:
    """Return only a single 'all' segment over the provided layer indices."""
    return {"all": list(layer_indices)}


def _compute_segment_metrics(
    per_layer_attn: Dict[int, torch.Tensor],
    instruction_mask: torch.Tensor,
    vision_mask: torch.Tensor,
    layer_indices: List[int],
    num_prompt_queries: int,
    actual_prompt_length: int,
) -> AttentionSegmentResult:
    """Compute attention metrics for a specific layer segment using generation queries."""
    if not layer_indices:
        return AttentionSegmentResult(float("nan"), 0.0, 0.0)

    total_queries = 0
    for layer_idx in layer_indices:
        attn = per_layer_attn.get(layer_idx)
        if attn is not None and attn.numel() > 0:
            total_queries = attn.shape[0]
            break
    if total_queries == 0:
        return AttentionSegmentResult(float("nan"), 0.0, 0.0)

    gen_row_start = max(num_prompt_queries, 0)
    if gen_row_start >= total_queries:
        return AttentionSegmentResult(float("nan"), 0.0, 0.0)

    generated_tokens = total_queries - num_prompt_queries
    if generated_tokens <= 0:
        return AttentionSegmentResult(float("nan"), 0.0, 0.0)

    attn_text_total = 0.0
    attn_vision_total = 0.0
    num_layers_with_data = 0

    for layer_idx in layer_indices:
        attn = per_layer_attn.get(layer_idx)
        if attn is None or attn.shape[0] == 0:
            continue

        gen_attn = attn[gen_row_start:, :actual_prompt_length]

        # 对齐到 prompt 长度
        if vision_mask.shape[0] != actual_prompt_length:
            if vision_mask.shape[0] < actual_prompt_length:
                pad_v = torch.zeros(actual_prompt_length - vision_mask.shape[0], dtype=vision_mask.dtype)
                vision_mask_prompt = torch.cat([vision_mask, pad_v], dim=0)
            else:
                vision_mask_prompt = vision_mask[:actual_prompt_length]
        else:
            vision_mask_prompt = vision_mask

        if instruction_mask.shape[0] != actual_prompt_length:
            if instruction_mask.shape[0] < actual_prompt_length:
                pad_i = torch.zeros(actual_prompt_length - instruction_mask.shape[0], dtype=instruction_mask.dtype)
                instruction_mask_prompt = torch.cat([instruction_mask, pad_i], dim=0)
            else:
                instruction_mask_prompt = instruction_mask[:actual_prompt_length]
        else:
            instruction_mask_prompt = instruction_mask

        # 文本keys严格使用 instruction_mask（已剔除special、system等），视觉keys使用 vision_mask
        text_keys_mask = instruction_mask_prompt.to(gen_attn.device)
        vision_keys_mask = vision_mask_prompt.to(gen_attn.device)

        gen_attn_sum = gen_attn.sum(dim=1, keepdim=True)
        gen_attn_sum = torch.where(gen_attn_sum > 1e-12, gen_attn_sum, torch.ones_like(gen_attn_sum))
        gen_attn_norm = gen_attn / gen_attn_sum

        attn_text_total += gen_attn_norm[:, text_keys_mask].sum().item()
        attn_vision_total += gen_attn_norm[:, vision_keys_mask].sum().item()
        num_layers_with_data += 1

        del gen_attn, gen_attn_norm, text_keys_mask, vision_keys_mask

    if num_layers_with_data == 0:
        return AttentionSegmentResult(float("nan"), 0.0, 0.0)

    # Length-normalize by the number of generated queries so attention statistics
    # are comparable across samples with different completion lengths.
    attn_text_avg = attn_text_total / num_layers_with_data / generated_tokens
    attn_vision_avg = attn_vision_total / num_layers_with_data / generated_tokens

    num_instruction = int(instruction_mask.sum().item())
    num_vision = int(vision_mask.sum().item())

    vgr = _compute_vgr(attn_text_avg, attn_vision_avg, max(num_instruction, 1), max(num_vision, 0))
    return AttentionSegmentResult(vgr, attn_text_avg, attn_vision_avg)


def _compute_token_weights_for_sample(
    per_layer_attn: Dict[int, torch.Tensor],
    instruction_mask: torch.Tensor,
    vision_mask: torch.Tensor,
    num_prompt_queries: int,
    actual_prompt_length: int,
    smooth_sigma: float,
    clip_range: Tuple[float, float],
) -> List[float]:
    """Compute token-level VGR-based weights for a single sample."""
    if not per_layer_attn:
        return []

    any_layer = next(iter(per_layer_attn.values()))
    if any_layer is None or any_layer.numel() == 0:
        return []

    total_queries = int(any_layer.shape[0])
    num_generated_tokens = max(total_queries - num_prompt_queries, 0)
    if num_generated_tokens <= 0:
        return []

    attn_text = torch.zeros(num_generated_tokens, dtype=torch.float32)
    attn_vision = torch.zeros(num_generated_tokens, dtype=torch.float32)
    layers_with_data = 0

    layer_indices_sorted = sorted(list(per_layer_attn.keys()))

    for layer_idx in layer_indices_sorted:
        attn = per_layer_attn.get(layer_idx)
        if attn is None or attn.shape[0] == 0:
            continue

        prompt_cols = min(actual_prompt_length, attn.shape[1])
        rows = attn[num_prompt_queries:, :prompt_cols]
        if rows.numel() == 0:
            continue

        row_sum = rows.sum(dim=1, keepdim=True)
        row_sum = torch.where(row_sum > 1e-12, row_sum, torch.ones_like(row_sum))
        rows = rows / row_sum

        vmask = vision_mask[:prompt_cols] if vision_mask.shape[0] != prompt_cols else vision_mask
        imask = instruction_mask[:prompt_cols] if instruction_mask.shape[0] != prompt_cols else instruction_mask

        vmask = vmask.to(dtype=torch.bool)
        imask = imask.to(dtype=torch.bool)

        attn_text += rows[:, imask].sum(dim=1)
        attn_vision += rows[:, vmask].sum(dim=1)
        layers_with_data += 1

    if layers_with_data == 0:
        return []

    attn_text = attn_text / layers_with_data
    attn_vision = attn_vision / layers_with_data

    num_text_tokens = max(int(instruction_mask.sum().item()), 1)
    num_vision_tokens = int(vision_mask.sum().item())

    if num_vision_tokens <= 0:
        return [1.0] * num_generated_tokens

    eps = 1e-6
    text_density = attn_text / max(num_text_tokens, 1)
    vision_density = attn_vision / max(num_vision_tokens, 1)
    vgr_tok = text_density / (vision_density + eps)
    vgr_tok = torch.where(torch.isfinite(vgr_tok) & (vgr_tok > 0), vgr_tok, torch.ones_like(vgr_tok))

    weights = 1.0 / (vgr_tok + eps)

    if smooth_sigma > 0.0 and weights.numel() > 2:
        half = max(1, int(3 * smooth_sigma))
        xs = torch.arange(-half, half + 1, dtype=weights.dtype)
        kernel = torch.exp(-0.5 * (xs / (smooth_sigma + 1e-6)) ** 2)
        kernel = kernel / kernel.sum()
        pad_left = half
        pad_right = half
        padded = torch.nn.functional.pad(weights[None, None, :], (pad_left, pad_right), mode="replicate")
        smoothed = torch.nn.functional.conv1d(padded, kernel[None, None, :])[0, 0]
        weights = smoothed

    mean_w = weights.mean() if weights.numel() > 0 else torch.tensor(1.0)
    if mean_w.abs() > 1e-12:
        weights = weights / mean_w
    lo, hi = clip_range
    weights = torch.clamp(weights, min=lo, max=hi)

    return weights.detach().cpu().tolist()


def compute_qwen_attention_metrics_for_batch(
    _model,
    processor,
    outputs_attentions,
    input_ids: torch.Tensor,
    sequences: torch.Tensor,
    image_grid_thw: Optional[torch.Tensor] = None,
    last_k_layers: Optional[int] = None,
    compute_token_weights: bool = False,
    token_weights_smooth_sigma: float = 0.0,
    token_weights_clip: Tuple[float, float] = (0.2, 3.0),
) -> Tuple[List[Optional[AttentionSampleResult]], List[Optional[str]], Optional[List[List[float]]]]:
    """Compute Qwen attention metrics for a batch of samples.

    When `compute_token_weights=True`, token-level VGR 权重会在同一次
    attention 遍历中一并计算出来，避免额外的二次遍历。
    """
    batch_size = input_ids.size(0)
    results: List[Optional[AttentionSampleResult]] = []
    skip_reasons: List[Optional[str]] = []
    token_weights_batch: Optional[List[List[float]]] = [] if compute_token_weights else None

    if outputs_attentions is None or len(outputs_attentions) == 0:
        return results, skip_reasons, token_weights_batch

    # Determine which layers to use: either all, or only the last-k layers
    total_layers = len(outputs_attentions[0])
    if last_k_layers is not None:
        if last_k_layers <= 0:
            selected = list(range(total_layers))
        else:
            last = min(last_k_layers, total_layers)
            selected = list(range(total_layers))[-last:]
        segments = _split_indices_to_segments(selected)
    else:
        segments = _split_layers_to_segments(total_layers)
    special_token_ids = get_qwen_special_token_ids(processor)

    if image_grid_thw is not None and image_grid_thw.dim() == 3:
        grid_items = [image_grid_thw[i] for i in range(image_grid_thw.size(0))]
    elif image_grid_thw is not None and image_grid_thw.dim() == 2:
        grid_items = [image_grid_thw[i] for i in range(image_grid_thw.size(0))]
    else:
        grid_items = [None] * batch_size

    for batch_idx in range(batch_size):
        per_layer_attn = _collect_llm_attention_for_sample(
            outputs_attentions, batch_idx, last_k_layers=last_k_layers
        )
        if not per_layer_attn:
            results.append(None)
            skip_reasons.append("no_attention")
            if token_weights_batch is not None:
                token_weights_batch.append([])
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
            if token_weights_batch is not None:
                token_weights_batch.append([])
            continue
        if num_vision_tokens <= 0:
            results.append(None)
            skip_reasons.append("no_vision_tokens")
            if token_weights_batch is not None:
                token_weights_batch.append([])
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
                num_instruction_tokens=num_text_tokens,
                num_vision_tokens=num_vision_tokens,
                num_generated_tokens=num_generated_tokens,
                num_prompt_queries=num_prompt_queries,
                total_queries=total_queries,
                actual_prompt_length=actual_prompt_length,
            )
        )
        skip_reasons.append(None)

        if token_weights_batch is not None:
            weights = _compute_token_weights_for_sample(
                per_layer_attn=per_layer_attn,
                instruction_mask=instruction_mask,
                vision_mask=vision_mask,
                num_prompt_queries=num_prompt_queries,
                actual_prompt_length=actual_prompt_length,
                smooth_sigma=token_weights_smooth_sigma,
                clip_range=token_weights_clip,
            )
            token_weights_batch.append(weights)

        del per_layer_attn, input_ids_sample, spans, instruction_mask, vision_mask

    return results, skip_reasons, token_weights_batch


def process_attention_context(
    attention_context: Optional[dict],
    model: Any,
    processor: Any,
    args: Any,
    attention_deque: Optional[Any] = None,
    attention_skip_reasons_deque: Optional[Any] = None,
    token_weights_deque: Optional[Any] = None,
) -> Optional[list]:
    """Process attention outputs: compute per-sample metrics and optional token weights, update deques.

    This function mutates the passed deques in-place (if provided) and clears heavy attention tensors in the context.
    
    Returns:
        Optional[list]: Token weights list for the current batch if token_weights is enabled, None otherwise.
    """
    if attention_context is None:
        return None
    try:
        outputs = attention_context.get("outputs")
        generate_inputs = attention_context.get("inputs")
        if outputs is None or getattr(outputs, "attentions", None) is None:
            return None
        if generate_inputs is None or "input_ids" not in generate_inputs:
            return None

        input_ids = generate_inputs["input_ids"].detach().cpu()
        sequences = outputs.sequences.detach().cpu()
        image_grid_thw = generate_inputs.get("image_grid_thw")
        image_grid_thw_cpu = image_grid_thw.detach().cpu() if isinstance(image_grid_thw, torch.Tensor) else None

        last_k = getattr(args, "attention_last_k_layers", None)
        want_token_weights = bool(getattr(args, "token_weights", False))
        samples_tuple = compute_qwen_attention_metrics_for_batch(
            model,
            processor,
            outputs.attentions,
            input_ids,
            sequences,
            image_grid_thw=image_grid_thw_cpu,
            last_k_layers=last_k,
            compute_token_weights=want_token_weights,
            token_weights_smooth_sigma=float(getattr(args, "token_weights_smooth_sigma", 0.0)),
            token_weights_clip=tuple(getattr(args, "token_weights_clip", (0.2, 3.0))),
        )

        # 解包（向后兼容：旧版本可能只返回两个元素）
        tw_list = None
        if isinstance(samples_tuple, tuple):
            if len(samples_tuple) == 3:
                sample_results, skip_reasons, tw_list = samples_tuple
            else:
                sample_results, skip_reasons = samples_tuple
        else:
            sample_results = samples_tuple
            skip_reasons = [None] * len(sample_results)

        if token_weights_deque is not None and hasattr(token_weights_deque, "extend") and tw_list:
            token_weights_deque.extend(tw_list)

        # Free heavy tensors promptly
        outputs.attentions = None
        attention_context["outputs"] = None
        attention_context["inputs"] = None

        if sample_results and attention_deque is not None and hasattr(attention_deque, "extend"):
            attention_deque.extend(sample_results)
        if skip_reasons and attention_skip_reasons_deque is not None and hasattr(attention_skip_reasons_deque, "extend"):
            attention_skip_reasons_deque.extend(skip_reasons)
        
        return tw_list
    except Exception:
        # Swallow diagnostics exceptions to avoid training failure
        pass
    
    return None


def get_qwen_special_token_ids(processor) -> Dict[str, int]:
    """Extract Qwen special token IDs from processor."""
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
    """Extract vision token spans from input_ids using Qwen special tokens."""
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
        span = (pos, end_pos + 1)
        spans.append(span)
    
    return spans
