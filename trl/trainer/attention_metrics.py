from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple

import torch


@dataclass
class AttentionSegmentResult:
    mdi: float
    aei_text: float
    aei_vision: float
    attention_text: float
    attention_vision: float


@dataclass
class AttentionSampleResult:
    segments: Dict[str, AttentionSegmentResult]
    num_instruction_tokens: int
    num_vision_tokens: int
    num_generated_tokens: int
    num_prompt_queries: int
    total_queries: int
    actual_prompt_length: int


def _row_normalize(values: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
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
    if outputs_attentions is None:
        return {}

    outputs_attentions = list(outputs_attentions)
    if len(outputs_attentions) == 0:
        return {}

    first_step_layers = outputs_attentions[0]
    num_layers = len(first_step_layers)
    per_layer_rows: Dict[int, List[torch.Tensor]] = {i: [] for i in range(num_layers)}

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
        for row in cur:
            per_layer_rows[layer_idx].append(row.detach().cpu())

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
            row = torch.cat([row, torch.zeros(1, dtype=row.dtype, device=row.device)])
            per_layer_rows[layer_idx].append(row.detach().cpu())

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
    return result


def _compute_mdi(attn_text: float, attn_vision: float, tokens_text: int, tokens_vision: int) -> float:
    if tokens_text <= 0:
        raise ValueError("tokens_text must be > 0")
    if tokens_vision < 0:
        raise ValueError("tokens_vision must be >= 0")
    if tokens_vision == 0:
        return float("inf")
    return (attn_text / tokens_text) / (attn_vision / tokens_vision)


def _compute_aei(
    attn_text: float, attn_vision: float, tokens_text: int, tokens_vision: int, modality: str = "text"
) -> float:
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
    image_token_index: int = -200,
) -> Tuple[torch.Tensor, torch.Tensor]:
    if input_ids.ndim != 1:
        raise ValueError("input_ids must be 1D")

    if input_ids.device.type != "cpu":
        input_ids = input_ids.cpu()

    num_placeholders = int((input_ids == image_token_index).sum().item())
    num_text = len(input_ids) - num_placeholders
    num_vision = sum(max(0, end - start) for start, end in vision_token_spans)
    seq_len = num_text + num_vision
    if seq_len <= 0:
        raise ValueError("Sequence length must be > 0 to build masks")

    device = torch.device("cpu")

    vision_mask = torch.zeros(seq_len, dtype=torch.bool, device=device)
    for start, end in vision_token_spans:
        if start is None or end is None or start < 0 or end <= start:
            continue
        s = max(0, start)
        e = min(seq_len, end)
        if e > s:
            vision_mask[s:e] = True

    instruction_mask = torch.ones(seq_len, dtype=torch.bool, device=device)
    instruction_mask &= ~vision_mask

    if special_token_ids is not None:
        specials = set(special_token_ids.values())
    else:
        specials = set()

    expanded_pos = 0
    for token_id in input_ids.tolist():
        if token_id == image_token_index:
            matched = False
            for start, end in vision_token_spans:
                if expanded_pos == start:
                    expanded_pos = end
                    matched = True
                    break
            if not matched:
                continue
        else:
            if token_id in specials and 0 <= expanded_pos < instruction_mask.shape[0]:
                instruction_mask[expanded_pos] = False
            expanded_pos += 1

    return instruction_mask, vision_mask


def _split_layers_to_segments(num_layers: int) -> Dict[str, List[int]]:
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

    # Use prompt-only attention rows (ignore generated tokens). This computes metrics from
    # attentions of the prompt query positions over the prompt keys.
    prompt_tokens = min(total_queries, max(num_prompt_queries, 0))
    if prompt_tokens <= 0:
        return AttentionSegmentResult(float("nan"), float("nan"), float("nan"), 0.0, 0.0)

    attn_text_total = 0.0
    attn_vision_total = 0.0
    num_layers_with_data = 0

    for layer_idx in layer_indices:
        attn = per_layer_attn.get(layer_idx)
        if attn is None or attn.shape[0] == 0:
            continue
        # Select the prompt query rows and restrict attention to prompt keys only
        prompt_attn = attn[:prompt_tokens, :actual_prompt_length]

        if vision_mask.shape[0] != actual_prompt_length:
            if vision_mask.shape[0] < actual_prompt_length:
                pad = torch.zeros(actual_prompt_length - vision_mask.shape[0], dtype=vision_mask.dtype)
                vision_mask_prompt = torch.cat([vision_mask, pad], dim=0)
            else:
                vision_mask_prompt = vision_mask[:actual_prompt_length]
        else:
            vision_mask_prompt = vision_mask

        text_keys_mask = (~vision_mask_prompt).to(prompt_attn.device)
        vision_keys_mask = vision_mask_prompt.to(prompt_attn.device)

        prompt_attn_sum = prompt_attn.sum(dim=1, keepdim=True)
        prompt_attn_sum = torch.where(prompt_attn_sum > 1e-12, prompt_attn_sum, torch.ones_like(prompt_attn_sum))
        prompt_attn_norm = prompt_attn / prompt_attn_sum

        attn_text_total += prompt_attn_norm[:, text_keys_mask].sum().item()
        attn_vision_total += prompt_attn_norm[:, vision_keys_mask].sum().item()
        num_layers_with_data += 1

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
    model,
    processor,
    outputs_attentions,
    input_ids: torch.Tensor,
    sequences: torch.Tensor,
    image_grid_thw: Optional[torch.Tensor] = None,
) -> List[AttentionSampleResult]:
    batch_size = input_ids.size(0)
    results: List[AttentionSampleResult] = []

    if outputs_attentions is None or len(outputs_attentions) == 0:
        return results

    segments = _split_layers_to_segments(len(outputs_attentions[0]))
    special_token_ids = get_qwen_special_token_ids(processor)
    image_token_id = getattr(model.config, "image_token_id", -200)

    if image_grid_thw is not None and image_grid_thw.dim() == 3:
        grid_items = [image_grid_thw[i] for i in range(image_grid_thw.size(0))]
    elif image_grid_thw is not None and image_grid_thw.dim() == 2:
        grid_items = [image_grid_thw[i] for i in range(image_grid_thw.size(0))]
    else:
        grid_items = [None] * batch_size

    for batch_idx in range(batch_size):
        per_layer_attn = _collect_llm_attention_for_sample(outputs_attentions, batch_idx)
        if not per_layer_attn:
            continue

        input_ids_sample = input_ids[batch_idx].detach().cpu()
        spans = extract_vision_token_spans_qwen(
            model,
            processor,
            input_ids_sample,
            grid_items[batch_idx] if grid_items else None,
        )

        instruction_mask, vision_mask = _build_modality_masks(
            input_ids_sample,
            spans,
            special_token_ids,
            image_token_index=image_token_id,
        )

        num_text_tokens = int((input_ids_sample != image_token_id).sum().item())
        num_vision_tokens = sum(max(0, end - start) for start, end in spans)
        actual_prompt_length = num_text_tokens + num_vision_tokens
        num_prompt_queries = max(actual_prompt_length - 1, 0)

        total_queries = 0
        any_layer = next(iter(per_layer_attn.values()))
        if any_layer is not None:
            total_queries = any_layer.shape[0]
        num_generated_tokens = max(total_queries - num_prompt_queries, 0)

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

    return results


def get_qwen_special_token_ids(processor) -> Dict[str, int]:
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
    model,
    processor,
    input_ids: torch.Tensor,
    image_grid_thw: Optional[torch.Tensor] = None,
) -> List[Tuple[int, int]]:
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

