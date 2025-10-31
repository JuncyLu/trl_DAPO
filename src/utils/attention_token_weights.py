from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

import math
import torch

from .attention_metrics import (
    _collect_llm_attention_for_sample,
    _build_modality_masks,
    get_qwen_special_token_ids,
    extract_vision_token_spans_qwen,
)


def _gaussian_smooth_1d(values: torch.Tensor, sigma: float) -> torch.Tensor:
    if sigma <= 0.0 or values.numel() <= 2:
        return values
    # Kernel size ~ 3*sigma on each side, odd length
    half = max(1, int(3 * sigma))
    ksize = 2 * half + 1
    xs = torch.arange(-half, half + 1, device=values.device, dtype=values.dtype)
    kernel = torch.exp(-0.5 * (xs / (sigma + 1e-6)) ** 2)
    kernel = kernel / kernel.sum()
    pad_left = half
    pad_right = half
    padded = torch.nn.functional.pad(values[None, None, :], (pad_left, pad_right), mode="replicate")
    smoothed = torch.nn.functional.conv1d(padded, kernel[None, None, :])[0, 0]
    return smoothed


@torch.no_grad()
def build_token_mdi_weights_for_batch(
    outputs_attentions: Any,
    input_ids: torch.Tensor,
    sequences: torch.Tensor,
    processor: Any,
    image_grid_thw: Optional[torch.Tensor] = None,
    exclude_special: bool = True,
    smooth_sigma: float = 0.0,
    clip_range: Tuple[float, float] = (0.2, 3.0),
) -> Tuple[List[List[float]], Dict[str, List[List[float]]]]:
    """
    Compute per-token weights for each generated token in the batch using MDI logic aligned with
    utils/attention_metrics: only prompt columns are considered; system/special tokens excluded from text pool; 
    generated columns are ignored.

    Returns a list per sample of weights aligned to generated tokens, and a debug dict with mdi_token/p_vision/p_text.
    """
    device = input_ids.device
    batch_size = input_ids.size(0)
    results: List[List[float]] = []
    debug: Dict[str, List[List[float]]] = {"mdi_token": [], "p_text": [], "p_vision": []}

    special_token_ids = get_qwen_special_token_ids(processor)

    if image_grid_thw is not None and isinstance(image_grid_thw, torch.Tensor):
        if image_grid_thw.dim() == 3:
            grids = [image_grid_thw[i] for i in range(image_grid_thw.size(0))]
        elif image_grid_thw.dim() == 2:
            grids = [image_grid_thw[i] for i in range(image_grid_thw.size(0))]
        else:
            grids = [None] * batch_size
    else:
        grids = [None] * batch_size

    # Helper to normalize a row to sum=1 safely
    def _row_normalize(row: torch.Tensor) -> torch.Tensor:
        denom = row.sum()
        if torch.abs(denom) < 1e-12:
            return row
        return row / denom

    # Iterate per sample
    for b in range(batch_size):
        per_layer = _collect_llm_attention_for_sample(outputs_attentions, b)
        if not per_layer:
            results.append([])
            debug["mdi_token"].append([])
            debug["p_text"].append([])
            debug["p_vision"].append([])
            continue

        ids_sample = input_ids[b].detach().cpu()
        spans = extract_vision_token_spans_qwen(
            None,  # model not needed for span extraction in current util
            processor,
            ids_sample,
            grids[b] if grids else None,
        )

        instruction_mask, vision_mask = _build_modality_masks(ids_sample, spans, special_token_ids)
        actual_prompt_length = instruction_mask.numel()

        # Determine number of prompt queries and generated queries as in metrics util
        num_prompt_queries = max(actual_prompt_length - 1, 0)

        # Figure out total queries from any layer
        any_layer = next(iter(per_layer.values()))
        if any_layer is None or any_layer.numel() == 0:
            results.append([])
            debug["mdi_token"].append([])
            debug["p_text"].append([])
            debug["p_vision"].append([])
            continue

        total_queries = any_layer.shape[0]
        num_generated_tokens = max(total_queries - num_prompt_queries, 0)
        if num_generated_tokens <= 0:
            results.append([])
            debug["mdi_token"].append([])
            debug["p_text"].append([])
            debug["p_vision"].append([])
            continue

        # Accumulate per-token attention to text/vision across layers
        attn_text = torch.zeros(num_generated_tokens, dtype=torch.float32, device=device)
        attn_vision = torch.zeros(num_generated_tokens, dtype=torch.float32, device=device)
        layers_with_data = 0

        for layer_idx, attn in per_layer.items():
            if attn is None or attn.shape[0] == 0:
                continue
            # Only consider prompt columns
            prompt_cols = min(actual_prompt_length, attn.shape[1])
            rows = attn[num_prompt_queries:, :prompt_cols].to(device)
            if rows.numel() == 0:
                continue
            # Row-normalize
            row_sum = rows.sum(dim=1, keepdim=True)
            row_sum = torch.where(row_sum > 1e-12, row_sum, torch.ones_like(row_sum))
            rows = rows / row_sum

            # Align masks to prompt length used
            if vision_mask.shape[0] != prompt_cols:
                vmask = vision_mask[:prompt_cols]
            else:
                vmask = vision_mask
            if instruction_mask.shape[0] != prompt_cols:
                imask = instruction_mask[:prompt_cols]
            else:
                imask = instruction_mask

            vmask = vmask.to(device)
            imask = imask.to(device)

            attn_text += rows[:, imask].sum(dim=1)
            attn_vision += rows[:, vmask].sum(dim=1)
            layers_with_data += 1

        if layers_with_data == 0:
            results.append([])
            debug["mdi_token"].append([])
            debug["p_text"].append([])
            debug["p_vision"].append([])
            continue

        attn_text = attn_text / layers_with_data
        attn_vision = attn_vision / layers_with_data

        num_text_tokens = max(int(instruction_mask.sum().item()), 1)
        num_vision_tokens = int(vision_mask.sum().item())

        # Compute per-token mdi and weights
        eps = 1e-6
        if num_vision_tokens <= 0:
            # No vision tokens → fallback to uniform weights 1.0
            weights = torch.ones(num_generated_tokens, dtype=torch.float32, device=device)
            mdi_tok = torch.ones_like(weights)
            p_text = torch.zeros_like(weights)
            p_vision = torch.zeros_like(weights)
        else:
            p_text = attn_text / (attn_text + attn_vision + eps)
            p_vision = attn_vision / (attn_text + attn_vision + eps)
            text_density = attn_text / max(num_text_tokens, 1)
            vision_density = attn_vision / max(num_vision_tokens, 1)
            mdi_tok = text_density / (vision_density + eps)
            mdi_tok = torch.where(torch.isfinite(mdi_tok) & (mdi_tok > 0), mdi_tok, torch.ones_like(mdi_tok))
            weights = 1.0 / (mdi_tok + eps)

        # Optional smoothing
        if smooth_sigma > 0.0:
            weights = _gaussian_smooth_1d(weights, smooth_sigma)

        # Normalize mean≈1 over valid tokens and clip
        mean_w = weights.mean() if weights.numel() > 0 else torch.tensor(1.0, device=device)
        if mean_w.abs() > 1e-12:
            weights = weights / mean_w
        lo, hi = clip_range
        weights = torch.clamp(weights, min=lo, max=hi)

        results.append(weights.detach().cpu().tolist())
        debug["mdi_token"].append(mdi_tok.detach().cpu().tolist())
        debug["p_text"].append(p_text.detach().cpu().tolist())
        debug["p_vision"].append(p_vision.detach().cpu().tolist())

    return results, debug


