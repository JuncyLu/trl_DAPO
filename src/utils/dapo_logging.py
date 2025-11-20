"""DAPO 日志：rollout、evaluation 与注意力诊断输出。"""

import json
import math
import os
from datetime import datetime
from typing import Any, Dict, List, Optional

import numpy as np
import torch
from trl.data_utils import is_conversational, apply_chat_template


def compute_real_vgr_metrics(
    sample_results: List[Any],
    skip_reasons: Optional[List[Optional[str]]] = None,
) -> List[Dict[str, Any]]:
    """Compute minimal per-sample VGR metrics for logging and rewards.

    Returns a list of dicts with keys:
      - vgr, attention_distribution [text_ratio, vision_ratio]
      - attention_text, attention_vision
      - num_text_tokens, num_vision_tokens
      - skip_reason
    """
    results: List[Dict[str, Any]] = []
    if skip_reasons is None:
        skip_reasons = [None] * len(sample_results)

    for idx, res in enumerate(sample_results):
        if res is None:
            results.append({
                "vgr": 1.0,
                "attention_distribution": [0.5, 0.5],
                "num_vision_tokens": 0,
                "num_text_tokens": 0,
                "attention_text": 0.0,
                "attention_vision": 0.0,
                "skip_reason": skip_reasons[idx] if idx < len(skip_reasons) else None,
            })
            continue

        segments = getattr(res, "segments", {}) or {}
        seg = segments.get("all")
        num_vision_tokens = int(getattr(res, "num_vision_tokens", 0) or 0)
        num_text_tokens = int(getattr(res, "num_instruction_tokens", getattr(res, "num_text_tokens", 0)) or 0)

        if seg is None or not hasattr(seg, "attention_text"):
            results.append({
                "vgr": 1.0,
                "attention_distribution": [0.5, 0.5],
                "num_vision_tokens": num_vision_tokens,
                "num_text_tokens": num_text_tokens,
                "attention_text": 0.0,
                "attention_vision": 0.0,
                "skip_reason": None,
            })
            continue

        attn_text = float(getattr(seg, "attention_text", 0.0) or 0.0)
        attn_vision = float(getattr(seg, "attention_vision", 0.0) or 0.0)
        t = max(1, int(num_text_tokens))
        o = int(num_vision_tokens)
        if o <= 0:
            vgr = float("inf")
        else:
            text_density = attn_text / t
            vision_density = attn_vision / max(1, o)
            vgr = text_density / (vision_density if vision_density > 0 else float("inf"))
        if not (vgr > 0) or not math.isfinite(vgr):
            vgr = 1.0
        text_ratio = vgr / (1.0 + vgr)
        vision_ratio = 1.0 / (1.0 + vgr)

        results.append({
            "vgr": round(float(vgr), 6),
            "attention_distribution": [round(float(text_ratio), 6), round(float(vision_ratio), 6)],
            "num_vision_tokens": num_vision_tokens,
            "num_text_tokens": num_text_tokens,
            "attention_text": round(float(attn_text), 6),
            "attention_vision": round(float(attn_vision), 6),
            "skip_reason": None,
        })

    return results



try:
    # Optional accelerate imports for distributed logging. When unavailable
    # (e.g., in lightweight environments), we fall back to local-only logs.
    from accelerate.utils import gather as accel_gather, gather_object as accel_gather_object  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    accel_gather = None  # type: ignore
    accel_gather_object = None  # type: ignore


def record_vgr_raw_stats(
    vgr_metrics: List[Dict[str, Any]],
    metrics_store: Dict[str, Any],
    mode: str,
    accelerator,
) -> None:
    """
    聚合一批 attention 导出的 vgr 原始值，并写入 metrics_store[mode]，供 wandb/tensorboard 记录。
    """
    if not vgr_metrics:
        return
    try:
        values: List[float] = []
        for entry in vgr_metrics:
            if not entry:
                continue
            val = entry.get("vgr")
            if not isinstance(val, (int, float)):
                continue
            val_f = float(val)
            if val_f <= 0 or not math.isfinite(val_f):
                continue
            values.append(val_f)
        if not values:
            return
        device = accelerator.device
        vals_tensor = torch.tensor(values, dtype=torch.float32, device=device)
        local_count = torch.tensor([float(vals_tensor.numel())], dtype=torch.float32, device=device)
        local_sum = vals_tensor.sum().unsqueeze(0)
        local_sq_sum = (vals_tensor * vals_tensor).sum().unsqueeze(0)
        try:
            total_count = accelerator.gather(local_count).sum()
            total_sum = accelerator.gather(local_sum).sum()
            total_sq_sum = accelerator.gather(local_sq_sum).sum()
        except Exception:
            total_count = local_count.sum()
            total_sum = local_sum.sum()
            total_sq_sum = local_sq_sum.sum()
        if total_count.item() <= 0:
            return
        mean = (total_sum / total_count).item()
        variance = (total_sq_sum / total_count).item() - mean**2
        if variance < 0:
            variance = 0.0
        std = math.sqrt(variance)
        metrics_store[mode]["attention/vgr_raw/mean"].append(mean)
        metrics_store[mode]["attention/vgr_raw/std"].append(std)
    except Exception:
        pass



def emit_rollout_logs(
    prompts_text: List[str],
    completions_text: List[str],
    solutions: List[str],
    rewards_per_func_local: torch.Tensor,
    total_rewards_local: torch.Tensor,
    reward_names: List[str],
    vgr_info: List[Dict[str, Any]],
    log_path: Optional[str] = None,
    prompt_preview_chars: int = 2000,
    completion_preview_chars: int = 2000,
    vgr_as_coefficient: int = 0,
    step: int = 0,
    epoch: float = 0.0,
    advantages_local: Optional[List[float]] = None,
    adv_desc: str = "unweighted",
    resampled_flags: Optional[List[bool]] = None,
) -> None:
    """将 rollout 信息写入 markdown。

    仅保留必要字段说明：rewards_per_func_local 与 reward_names 一一对应；vgr_info
    为 compute_real_vgr_metrics 输出，用于展示分段与汇总 VGR。
    """
    # If caller provides a path, respect it; else fallback to default
    if not log_path:
        # 默认单独文件，避免与 rollout_results.md 混在一起
        log_path = os.path.join("training_logs", "token_weights.md")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    # Header
    header = f"=== Rollout Step {step} ==="
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 数据行组装
    rows = []
    for idx, (prompt, completion, solution) in enumerate(zip(prompts_text, completions_text, solutions)):
        # 预览文本
        preview_p = prompt[:prompt_preview_chars] + "..." if len(prompt) > prompt_preview_chars else prompt
        preview_c = completion[:completion_preview_chars] + "..." if len(completion) > completion_preview_chars else completion
        
        # 格式化 solution：如果是列表（10 个答案），显示所有非空答案
        if isinstance(solution, (list, tuple)):
            non_empty = [s for s in solution if s and str(s).strip()]
            solution_str = " | ".join(non_empty[:10]) if non_empty else ""
        else:
            solution_str = str(solution) if solution else ""
        
        # 奖励值
        acc = 0.0
        fmt = 0.0
        tag = 0.0
        length_val = 0.0
        vgr_val = 0.0
        
        if rewards_per_func_local.numel() > 0:
            # 名称到索引映射（兼容不同命名）
            name_to_idx = {name: i for i, name in enumerate(reward_names)}

            def any_index(*candidates):
                for key in candidates:
                    if key in name_to_idx:
                        return name_to_idx[key]
                return None

            acc_idx = any_index("accuracy_reward", "mc_idx_reward")
            if acc_idx is not None and idx < rewards_per_func_local.shape[0]:
                acc = float(rewards_per_func_local[idx, acc_idx].item())

            fmt_idx = any_index("format_reward", "think_format_reward")
            if fmt_idx is not None and idx < rewards_per_func_local.shape[0]:
                fmt = float(rewards_per_func_local[idx, fmt_idx].item())

            tag_idx = any_index("tag_reward", "tag_count_reward")
            if tag_idx is not None and idx < rewards_per_func_local.shape[0]:
                tag = float(rewards_per_func_local[idx, tag_idx].item())

            length_idx = any_index("length_reward")
            if length_idx is not None and idx < rewards_per_func_local.shape[0]:
                length_val = float(rewards_per_func_local[idx, length_idx].item())

            vgr_idx = any_index("vgr_hard_negative", "vgr_reward", "vgr_reward_as_additive")
            if vgr_idx is not None and idx < rewards_per_func_local.shape[0]:
                vgr_val = float(rewards_per_func_local[idx, vgr_idx].item())
        
        tot = float(total_rewards_local[idx].item()) if total_rewards_local.numel() > 0 else 0.0
        adv_val = None
        if advantages_local is not None and idx < len(advantages_local):
            try:
                adv_val = float(advantages_local[idx])
            except Exception:
                adv_val = None
        is_resampled = False
        if resampled_flags is not None and idx < len(resampled_flags):
            try:
                is_resampled = bool(resampled_flags[idx])
            except Exception:
                is_resampled = False

        rows.append(
            {
                "idx": idx + 1,
                "prompt": preview_p,
                "completion": preview_c,
                "solution": solution_str,
                "accuracy": acc,
                "vgr": vgr_val,
                "format": fmt,
                "tag": tag,
                "length": length_val,
                "total": tot,
                "advantage": adv_val,
                "resampled": is_resampled,
            }
        )
    
    # Write to log file
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n{header}\n")
            f.write(f"Time: {ts}\n")
            f.write(f"Epoch: {epoch:.2f}\n\n")
            
            adv_desc = advantage_desc or "token-level weighted" if advantages_local else "N/A"
            
            for row in rows:
                f.write(f"### Sample {row['idx']}\n\n")
                f.write(f"**Prompt:**\n```\n{row['prompt']}\n```\n\n")
                f.write(f"**Completion:**\n```\n{row['completion']}\n```\n\n")
                if row['solution']:
                    f.write(f"**Solution:** {row['solution']}\n\n")
                
                f.write(f"**Rewards:**\n")
                f.write(f"- Accuracy: {row['accuracy']:.3f}\n")
                f.write(f"- VGR: {row['vgr']:.3f}\n")
                f.write(f"- Format: {row['format']:.3f}\n")
                f.write(f"- Tag: {row['tag']:.3f}\n")
                f.write(f"- Length: {row['length']:.3f}\n")
                f.write(f"- **Total**: {row['total']:.3f}\n\n")
                
                if row["advantage"] is not None:
                    f.write(f"**Advantage ({adv_desc}):** {float(row['advantage']):.3f}\n\n")
                
                if row.get("resampled", False):
                    f.write("*(Resampled)*\n\n")
                
                f.write("---\n\n")
    except Exception as e:
        pass


def emit_eval_logs(
    eval_samples: List[Dict[str, Any]],
    log_path: Optional[str] = None,
    step: int = 0,
    epoch: float = 0.0,
) -> None:
    """Write evaluation results to markdown log."""
    if not eval_samples:
        return
    
    if not log_path:
        log_path = os.path.join("training_logs", "eval_results.md")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    try:
        header = f"=== Evaluation Step {step} ==="
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n{header}\n")
            f.write(f"Time: {ts}\n")
            f.write(f"Epoch: {epoch:.2f}\n\n")
            
            for idx, sample in enumerate(eval_samples, 1):
                f.write(f"### Eval Sample {idx}\n\n")
                if "prompt" in sample:
                    f.write(f"**Prompt:**\n```\n{sample['prompt'][:500]}\n```\n\n")
                if "completion" in sample:
                    f.write(f"**Completion:**\n```\n{sample['completion'][:500]}\n```\n\n")
                if "solution" in sample:
                    f.write(f"**Solution:** {sample['solution']}\n\n")
                if "accuracy" in sample:
                    f.write(f"**Accuracy:** {sample['accuracy']:.3f}\n\n")
                f.write("---\n\n")
    except Exception:
        pass


def emit_token_weights_logs(
    token_weights: torch.Tensor,
    log_path: Optional[str] = None,
    step: int = 0,
) -> None:
    """Write token weights to log file."""
    if token_weights is None or token_weights.numel() == 0:
        return
    
    if not log_path:
        log_path = os.path.join("training_logs", "token_weights.txt")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    try:
        tw = token_weights.detach().cpu().numpy()
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n=== Step {step} ===\n")
            if tw.ndim == 2:
                for i, row in enumerate(tw[:8]):
                    f.write(f"Sample {i}: {row[:20]}\n")
            else:
                f.write(f"Shape: {tw.shape}, First 50: {tw.flatten()[:50]}\n")
    except Exception:
        pass


def emit_tokenwise_weights(
    tokenwise_weights_list: List[np.ndarray],
    log_path: Optional[str] = None,
    step: int = 0,
) -> None:
    """Write tokenwise weights to log file."""
    if not tokenwise_weights_list:
        return
    
    if not log_path:
        log_path = os.path.join("training_logs", "tokenwise_weights.txt")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n=== Step {step} ===\n")
            for i, tw in enumerate(tokenwise_weights_list[:8]):
                if tw is not None and len(tw) > 0:
                    f.write(f"Sample {i}: shape={tw.shape}, first_10={tw[:10]}\n")
    except Exception:
        pass


def perform_realtime_rollout_logging(
    prompts_text: List[str],
    completions_text: List[str],
    solutions: List[str],
    rewards_per_func: torch.Tensor,
    total_rewards: torch.Tensor,
    reward_names: List[str],
    vgr_info: List[Dict[str, Any]],
    mode: str,
    step: int,
    epoch: float,
    accelerator,
    metrics_store: Dict[str, Any],
    advantages: Optional[torch.Tensor] = None,
    token_weights: Optional[torch.Tensor] = None,
    tokenwise_weights_list: Optional[List[np.ndarray]] = None,
    advantage_desc: Optional[str] = None,
    images: Optional[List[Any]] = None,
    disable_realtime_logging: bool = False,
    vgr_as_coefficient: int = 0,
    resampled_flags: Optional[List[bool]] = None,
) -> None:
    """Perform realtime logging for rollout data."""
    if disable_realtime_logging or mode != "train":
        return
    
    try:
        if accel_gather is not None:
            try:
                prompts_text = accel_gather_object(prompts_text)
                completions_text = accel_gather_object(completions_text)
                solutions = accel_gather_object(solutions)
                vgr_info = accel_gather_object(vgr_info) if vgr_info else []
                
                rewards_per_func = accel_gather(rewards_per_func)
                total_rewards = accel_gather(total_rewards)
                
                if advantages is not None:
                    advantages = accel_gather(advantages)
                    advantages_list = advantages.cpu().tolist() if advantages.numel() > 0 else None
                else:
                    advantages_list = None
                
                if resampled_flags is not None:
                    resampled_flags = accel_gather_object(resampled_flags)
            except Exception:
                pass
        
        if not accelerator.is_main_process:
            return
        
        if not prompts_text or not completions_text:
            return
        
        log_dir = os.path.join("training_logs", datetime.now().strftime("%Y%m%d_%H%M%S"))
        os.makedirs(log_dir, exist_ok=True)
        
        rollout_log_path = os.path.join(log_dir, "rollout_results.md")
        
        emit_rollout_logs(
            prompts_text=prompts_text,
            completions_text=completions_text,
            solutions=solutions,
            rewards_per_func_local=rewards_per_func,
            total_rewards_local=total_rewards,
            reward_names=reward_names,
            vgr_info=vgr_info,
            log_path=rollout_log_path,
            step=step,
            epoch=epoch,
            advantages_local=advantages_list,
            advantage_desc=advantage_desc,
            vgr_as_coefficient=vgr_as_coefficient,
            resampled_flags=resampled_flags,
        )
        
        if token_weights is not None:
            emit_token_weights_logs(token_weights, log_path=os.path.join(log_dir, "token_weights.txt"), step=step)
        
        if tokenwise_weights_list:
            emit_tokenwise_weights(tokenwise_weights_list, log_path=os.path.join(log_dir, "tokenwise_weights.txt"), step=step)
        
        if vgr_info:
            record_vgr_raw_stats(vgr_info, metrics_store, mode, accelerator)
    except Exception:
        pass
