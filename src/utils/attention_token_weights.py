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
def build_token_vgr_weights_for_batch(
    outputs_attentions: Any,
    input_ids: torch.Tensor,
    sequences: torch.Tensor,
    processor: Any,
    image_grid_thw: Optional[torch.Tensor] = None,
    exclude_special: bool = True,
    smooth_sigma: float = 0.0,
    clip_range: Tuple[float, float] = (0.2, 3.0),
    last_k_layers: Optional[int] = None,
) -> Tuple[List[List[float]], Dict[str, List[List[float]]]]:
    """
    Compute per-token weights for each generated token in the batch using VGR logic.

    Returns weights list and debug dict.
    """
    device = input_ids.device
    batch_size = input_ids.size(0)
    results: List[List[float]] = []
    debug: Dict[str, List[List[float]]] = {"vgr_token": [], "p_text": [], "p_vision": []}

    special_token_ids = get_qwen_special_token_ids(processor) if exclude_special else {}

    # Prepare grids list
    if image_grid_thw is not None and isinstance(image_grid_thw, torch.Tensor):
        if image_grid_thw.dim() == 3:
            grids = [image_grid_thw[i] for i in range(image_grid_thw.size(0))]
        elif image_grid_thw.dim() == 2:
            grids = [image_grid_thw[i] for i in range(image_grid_thw.size(0))]
        else:
            grids = [None] * batch_size
    else:
        grids = [None] * batch_size

    eps = 1e-6

    for b in range(batch_size):
        per_layer = _collect_llm_attention_for_sample(outputs_attentions, b, last_k_layers=last_k_layers)
        if not per_layer:
            results.append([])
            debug["vgr_token"].append([])
            debug["p_text"].append([])
            debug["p_vision"].append([])
            continue

        ids_sample = input_ids[b].detach().cpu()
        spans = extract_vision_token_spans_qwen(None, processor, ids_sample, grids[b] if grids else None)
        instruction_mask, vision_mask = _build_modality_masks(ids_sample, spans, special_token_ids)
        actual_prompt_length = instruction_mask.numel()
        num_prompt_queries = max(actual_prompt_length - 1, 0)

        any_layer = next(iter(per_layer.values()))
        if any_layer is None or any_layer.numel() == 0:
            results.extend([[]])
            debug["vgr_token"].append([])
            debug["p_text"].append([])
            debug["p_vision"].append([])
            continue

        total_queries = any_layer.shape[0]
        num_generated_tokens = max(total_queries - num_prompt_queries, 0)
        if num_generated_tokens <= 0:
            results.append([])
            debug["vgr_token"].append([])
            debug["p_text"].append([])
            debug["p_vision"].append([])
            continue

        attn_text = torch.zeros(num_generated_tokens, dtype=torch.float32, device=device)
        attn_vision = torch.zeros(num_generated_tokens, dtype=torch.float32, device=device)
        layers_with_data = 0

        # Decide which layer indices to use (preserve numeric order)
        layer_indices_sorted = sorted(list(per_layer.keys()))
        if last_k_layers is not None and last_k_layers > 0:
            layer_indices_sorted = layer_indices_sorted[-min(last_k_layers, len(layer_indices_sorted)) :]

        for layer_idx in layer_indices_sorted:
            attn = per_layer.get(layer_idx)
            if attn is None or attn.shape[0] == 0:
                continue
            prompt_cols = min(actual_prompt_length, attn.shape[1])
            rows = attn[num_prompt_queries:, :prompt_cols].to(device)
            if rows.numel() == 0:
                continue
            row_sum = rows.sum(dim=1, keepdim=True)
            row_sum = torch.where(row_sum > 1e-12, row_sum, torch.ones_like(row_sum))
            rows = rows / row_sum

            vmask = vision_mask[:prompt_cols] if vision_mask.shape[0] != prompt_cols else vision_mask
            imask = instruction_mask[:prompt_cols] if instruction_mask.shape[0] != prompt_cols else instruction_mask
            vmask = vmask.to(device)
            imask = imask.to(device)

            attn_text += rows[:, imask].sum(dim=1)
            attn_vision += rows[:, vmask].sum(dim=1)
            layers_with_data += 1

        if layers_with_data == 0:
            results.append([])
            debug["vgr_token"].append([])
            debug["p_text"].append([])
            debug["p_vision"].append([])
            continue

        attn_text = attn_text / layers_with_data
        attn_vision = attn_vision / layers_with_data

        num_text_tokens = max(int(instruction_mask.sum().item()), 1)
        num_vision_tokens = int(vision_mask.sum().item())

        if num_vision_tokens <= 0:
            weights = torch.ones(num_generated_tokens, dtype=torch.float32, device=device)
            vgr_tok = torch.ones_like(weights)
            p_text = torch.zeros_like(weights)
            p_vision = torch.zeros_like(weights)
        else:
            p_text = attn_text / (attn_text + attn_vision + eps)
            p_vision = attn_vision / (attn_text + attn_vision + eps)
            text_density = attn_text / max(num_text_tokens, 1)
            vision_density = attn_vision / max(num_vision_tokens, 1)
            vgr_tok = text_density / (vision_density + eps)
            vgr_tok = torch.where(torch.isfinite(vgr_tok) & (vgr_tok > 0), vgr_tok, torch.ones_like(vgr_tok))
            weights = 1.0 / (vgr_tok + eps)

        if smooth_sigma > 0.0:
            weights = _gaussian_smooth_1d(weights, smooth_sigma)

        mean_w = weights.mean() if weights.numel() > 0 else torch.tensor(1.0, device=device)
        if mean_w.abs() > 1e-12:
            weights = weights / mean_w
        lo, hi = clip_range
        weights = torch.clamp(weights, min=lo, max=hi)

        results.append(weights.detach().cpu().tolist())
        debug["vgr_token"].append(vgr_tok.detach().cpu().tolist())
        debug["p_text"].append(p_text.detach().cpu().tolist())
        debug["p_vision"].append(p_vision.detach().cpu().tolist())

    return results, debug
