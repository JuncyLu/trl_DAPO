"""DAPO 日志：rollout、evaluation 与注意力诊断输出。"""

import json
import math
import os
from datetime import datetime
from typing import Any, Dict, List, Optional

import numpy as np
import torch
from trl.data_utils import is_conversational, apply_chat_template


def _debug_log(message: str, **kwargs: Any) -> None:
    """
    简单的调试输出，便于定位在日志写入流程中的阻塞点。
    """
    pass  # 调试日志已禁用

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
    _debug_log(
        "emit_rollout_logs:start",
        step=step,
        epoch=epoch,
        prompt_cnt=len(prompts_text),
        completion_cnt=len(completions_text),
    )
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
            
            repetition_val = 0.0
            repetition_idx = any_index("repetition_reward")
            if repetition_idx is not None and idx < rewards_per_func_local.shape[0]:
                repetition_val = float(rewards_per_func_local[idx, repetition_idx].item())
        
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
                "repetition": repetition_val,
                "total": tot,
                "advantage": adv_val,
                "resampled": is_resampled,
            }
        )
    _debug_log("emit_rollout_logs:rows_ready", rows=len(rows), log_path=log_path)
    
    # 写入 rollout 日志
    if log_path:
        try:
            _debug_log("emit_rollout_logs:open_file", log_path=log_path)
            os.makedirs(os.path.dirname(log_path), exist_ok=True)
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(f"\n## {header} | {ts}\n\n")
                
                # 总体统计
                if rows:
                    f.write("### Overall Statistics\n\n")
                    f.write("| Metric | Value |\n")
                    f.write("|--------|-------|\n")
                    
                    # 计算统计
                    accuracy_scores = [r["accuracy"] for r in rows]
                    vgr_scores = [r["vgr"] for r in rows]
                    format_scores = [r["format"] for r in rows]
                    tag_scores = [r["tag"] for r in rows]
                    length_scores = [r["length"] for r in rows]
                    repetition_scores = [r["repetition"] for r in rows]
                    total_scores = [r["total"] for r in rows]
                    adv_scores = [r["advantage"] for r in rows if r["advantage"] is not None]
                    # 来自 attention 的 VGR 原始指标（若可用）
                    vgr_raw_list = []
                    if vgr_info:
                        for info in vgr_info:
                            try:
                                vgr_raw_list.append(float(info.get("vgr", float("nan"))))
                            except Exception:
                                pass
                    
                    if accuracy_scores:
                        f.write(f"| Accuracy Mean | {np.mean(accuracy_scores):.3f} ± {np.std(accuracy_scores):.3f} |\n")
                        f.write(f"| Accuracy Rate | {np.mean([1 if s > 0 else 0 for s in accuracy_scores]):.3f} |\n")
                    if vgr_scores:
                        f.write(f"| VGR Mean | {np.mean(vgr_scores):.3f} ± {np.std(vgr_scores):.3f} |\n")
                    if format_scores:
                        f.write(f"| Format Mean | {np.mean(format_scores):.3f} ± {np.std(format_scores):.3f} |\n")
                        f.write(f"| Format Rate | {np.mean([1 if s > 0 else 0 for s in format_scores]):.3f} |\n")
                    if tag_scores:
                        f.write(f"| Tag Mean | {np.mean(tag_scores):.3f} ± {np.std(tag_scores):.3f} |\n")
                        f.write(f"| Tag Rate | {np.mean([1 if s > 0 else 0 for s in tag_scores]):.3f} |\n")
                    if length_scores:
                        f.write(f"| Length Mean | {np.mean(length_scores):.3f} ± {np.std(length_scores):.3f} |\n")
                    if total_scores:
                        f.write(f"| Total Reward Mean | {np.mean(total_scores):.3f} ± {np.std(total_scores):.3f} |\n")
                        f.write(f"| Success Rate | {np.mean([1 if s > 0 else 0 for s in total_scores]):.3f} |\n\n")
                    if adv_scores:
                        f.write(f"| Advantage ({adv_desc}) Mean | {np.mean(adv_scores):.3f} ± {np.std(adv_scores):.3f} |\n")
                    resampled_count = sum(1 for r in rows if r.get("resampled"))
                    if resampled_count:
                        f.write(f"| Resampled Samples | {resampled_count} |\n")
                    if adv_scores or resampled_count:
                        f.write("\n")
                    # 汇总 vgr_raw（原始VGR）
                    if vgr_raw_list:
                        try:
                            vgr_mean = float(np.nanmean(vgr_raw_list))
                            vgr_std = float(np.nanstd(vgr_raw_list))
                            f.write(f"| vgr_raw Mean | {vgr_mean:.3f} ± {vgr_std:.3f} |\n\n")
                        except Exception:
                            pass
                    
                # 样本明细 - 确保 vgr_info 与 rows 长度一致
                # 如果 vgr_info 长度不足，用空字典填充
                vgr_info_padded = list(vgr_info) + [{}] * max(0, len(rows) - len(vgr_info))
                for i, (row, info) in enumerate(zip(rows, vgr_info_padded), start=1):
                    labels = []
                    if row.get("resampled"):
                        labels.append("Resampled")
                    label = f" ({', '.join(labels)})" if labels else ""
                    f.write(f"### Sample {i}{label}\n\n")
                    f.write(f"**Prompt:** {row['prompt']}\n\n")
                    f.write(f"**Completion:** {row['completion']}\n\n")
                    f.write(f"**Solution:** {row['solution']}\n\n")
                    
                    # 按 VGR 使用方式显示标签
                    true_vgr = info.get("vgr", 0.0) if info else 0.0
                    
                    # 统一命名：奖励一律用 vgr，原始值用 vgr_raw
                    f.write(
                        "**Rewards:** accuracy={:.3f}, vgr={:.3f}, format={:.3f}, tag={:.3f}, length={:.3f}, "
                        "vgr_raw={:.3f}, total={:.3f}\n\n".format(
                            row["accuracy"],
                            row["vgr"],
                            row["format"],
                            row["tag"],
                            row["length"],
                            float(true_vgr),
                            row["total"],
                        )
                    )

                    # Advantage（若提供则展示；若为 token_weights 实验，建议传入加权后的优势）
                    if row["advantage"] is not None:
                        f.write(f"**Advantage ({adv_desc}):** {float(row['advantage']):.4f}\n\n")
                    
                    # 详细 metrics：补充 VGR 原始指标
                    if info:
                        f.write("**Detailed Metrics:**\n\n")
                        f.write("```json\n")
                        # 计算更直观的密度/比例
                        try:
                            _attn_text = float(info.get("attention_text", 0.0) or 0.0)
                            _attn_vision = float(info.get("attention_vision", 0.0) or 0.0)
                            _t = int(info.get("num_text_tokens", 0) or 0)
                            _o = int(info.get("num_vision_tokens", 0) or 0)
                        except Exception:
                            _attn_text, _attn_vision, _t, _o = 0.0, 0.0, 0, 0
                        density_text = (_attn_text / _t) if _t > 0 else None
                        density_vision = (_attn_vision / _o) if _o > 0 else None
                        text_ratio = None
                        vision_ratio = None
                        try:
                            # 与 compute_real_vgr_metrics 一致的分配比例
                            _vgr_val = float(info.get("vgr", 1.0))
                            text_ratio = _vgr_val / (1.0 + _vgr_val)
                            vision_ratio = 1.0 / (1.0 + _vgr_val)
                        except Exception:
                            pass

                        detailed_metrics = {
                            "rewards": {
                                "accuracy": float(row["accuracy"]),
                                "vgr": float(row["vgr"]),
                                "format": float(row["format"]),
                                "tag": float(row["tag"]),
                                "length": float(row["length"]),
                                "total": float(row["total"]),
                            },
                            "advantage": float(row["advantage"]) if row["advantage"] is not None else None,
                            "resampled": bool(row.get("resampled", False)),
                            "token_counts": {
                                "vision_tokens": float(info.get("num_vision_tokens", 0) or 0),
                                "text_tokens": float(info.get("num_text_tokens", 0) or 0),
                                "total_tokens": float((info.get("num_vision_tokens", 0) or 0) + (info.get("num_text_tokens", 0) or 0)),
                            },
                            "vgr_metrics": {
                                "vgr_raw": float(_vgr_val) if isinstance(_vgr_val, (int, float)) else None,
                                "attention_text": _attn_text,
                                "attention_vision": _attn_vision,
                                "density_text": density_text,
                                "density_vision": density_vision,
                                "text_ratio": text_ratio,
                                "vision_ratio": vision_ratio,
                            },
                            "overall": {
                                "attention_distribution": info.get("attention_distribution"),
                                "skip_reason": info.get("skip_reason"),
                            },
                        }
                        f.write(json.dumps(detailed_metrics, ensure_ascii=False, indent=2))
                        f.write("\n```\n\n")
                    
                    f.write("---\n\n")
            _debug_log("emit_rollout_logs:write_done", log_path=log_path, rows=len(rows))
        except Exception as e:
            print(f"⚠️  Warning: Failed to write to rollout log file: {e}")
            _debug_log("emit_rollout_logs:error", error=str(e))


def emit_eval_logs(
    metrics: Dict[str, float],
    logs: Dict[str, float],
    eval_samples: List[Dict[str, Any]],
    log_path: str,
    step: int = 0,
    epoch: float = 0.0,
) -> None:
    """
    记录 evaluation 日志到 markdown 文件
    
    Args:
        metrics: 计算得到的指标字典
        logs: 原始日志字典
        eval_samples: evaluation 样本数据
        log_path: evaluation 日志文件路径
        step: 当前步数
        epoch: 当前轮次
    """
    _debug_log(
        "emit_eval_logs:start",
        step=step,
        epoch=epoch,
        sample_cnt=len(eval_samples),
        log_path=log_path,
    )
    # If caller provides a path, respect it; else fallback to default
    if not log_path:
        log_path = os.path.join("training_logs", "eval_results.md")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    try:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"=== Evaluation Step {step} ==="
        
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        
        def _strip_system_from_chatml(text: str) -> str:
            try:
                marker_start = "<|im_start|>system"
                marker_end = "<|im_end|>"
                out = str(text)
                while True:
                    s = out.find(marker_start)
                    if s == -1:
                        break
                    e = out.find(marker_end, s)
                    if e == -1:
                        break
                    out = out[:s] + out[e + len(marker_end):]
                return out.strip()
            except Exception:
                return text

        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n## {header} | {ts}\n\n")
            
            # 添加总体统计信息
            f.write("### Overall Statistics\n\n")
            f.write("| Metric | Value |\n")
            f.write("|--------|-------|\n")
            
            # 从样本数据中计算分项奖励的平均值
            reward_keys = ["accuracy", "vgr", "format", "tag", "length"]
            computed_means = {}
            if eval_samples:
                for key in reward_keys:
                    values = []
                    for sample in eval_samples:
                        rewards = sample.get("rewards", {})
                        if key in rewards:
                            try:
                                values.append(float(rewards[key]))
                            except Exception:
                                pass
                    if values:
                        computed_means[key] = sum(values) / len(values)
                    else:
                        computed_means[key] = 0.0
                
                # 计算总奖励的平均值
                total_values = []
                for sample in eval_samples:
                    try:
                        total_values.append(float(sample.get("total_reward", 0.0)))
                    except Exception:
                        pass
                if total_values:
                    computed_means["reward"] = sum(total_values) / len(total_values)
                else:
                    computed_means["reward"] = 0.0
            
            # 核心指标
            core_metrics = {
                "eval_loss": logs.get("eval_loss", 0.0),
                "eval_reward": computed_means.get("reward", metrics.get("eval_reward", 0.0)),
                "eval_accuracy": computed_means.get("accuracy", 0.0),
                "eval_vgr": computed_means.get("vgr", 0.0),
                "eval_format": computed_means.get("format", 0.0),
                "eval_tag": computed_means.get("tag", 0.0),
                "eval_length": computed_means.get("length", 0.0),
            }
            
            for key, value in core_metrics.items():
                if value is not None:
                    f.write(f"| {key} | {value:.4f} |\n")

            # 样本数据
            if eval_samples:
                f.write(f"\n### Evaluation Samples ({len(eval_samples)} samples)\n\n")
                
                for i, sample in enumerate(eval_samples, 1):
                    f.write(f"### Sample {i}\n\n")
                    
                    # 显示prompt
                    if 'problem' in sample and isinstance(sample['problem'], str) and sample['problem']:
                        _prompt_str = sample['problem']
                    else:
                        _raw_prompt = sample.get('prompt', 'N/A')
                        _prompt_str = _strip_system_from_chatml(_raw_prompt) if isinstance(_raw_prompt, str) else _raw_prompt
                    f.write(f"**Prompt:** {_prompt_str}\n\n")
                    
                    # 显示completion
                    f.write(f"**Completion:** {sample.get('completion', 'N/A')}\n\n")
                    
                    # 显示solution（如果有）
                    if 'solution' in sample:
                        f.write(f"**Solution:** {sample['solution']}\n\n")
                    
                    # 显示rewards
                    rewards = sample.get('rewards', {})
                    f.write(f"**Rewards:** ")
                    reward_parts = []
                    for key, value in rewards.items():
                        reward_parts.append(f"{key}={value:.3f}")
                    if reward_parts:
                        f.write(", ".join(reward_parts))
                        f.write(f", total={sample.get('total_reward', 0.0):.3f}\n\n")
                    else:
                        # 如果rewards为空，至少显示total
                        f.write(f"total={sample.get('total_reward', 0.0):.3f}\n\n")
                    
                    # 显示详细指标（如果有）
                    if 'detailed_metrics' in sample:
                        f.write("**Detailed Metrics:**\n\n")
                        f.write("```json\n")
                        f.write(json.dumps(sample['detailed_metrics'], ensure_ascii=False, indent=2))
                        f.write("\n```\n\n")
                    
                    f.write("---\n\n")
        _debug_log("emit_eval_logs:write_done", log_path=log_path, sample_cnt=len(eval_samples))
    except Exception as e:
        print(f"⚠️  Warning: Failed to write to eval log file: {e}")
        _debug_log("emit_eval_logs:error", error=str(e))


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
        # Compute VGR safely
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


def emit_token_weights_logs(
    token_weights: Any,
    log_path: Optional[str] = None,
    step: int = 0,
    epoch: float = 0.0,
    max_preview_tokens: int = 16,
) -> None:
    """
    将 token-level 权重的统计信息附加写入与 rollout 相同的 Markdown 文件。

    Args:
        token_weights: (B, T) 的张量，或可转换为 ndarray 的对象。
        log_path: 同 emit_rollout_logs 的路径；如为空则落到 training_logs/rollout_results.md。
        step, epoch: 训练步与 epoch，仅用于标题说明。
        max_preview_tokens: 每个样本预览的前若干 token 权重。
    """
    try:
        _debug_log(
            "emit_token_weights_logs:start",
            step=step,
            epoch=epoch,
            log_path=log_path,
        )
        if token_weights is None:
            _debug_log("emit_token_weights_logs:skip_no_weights")
            return
        if not log_path:
            log_path = os.path.join("training_logs", "token_weights.md")
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        if isinstance(token_weights, torch.Tensor):
            tw = token_weights.detach().float().cpu().numpy()
        else:
            tw = np.asarray(token_weights, dtype=float)

        # 统计信息
        flat = tw.reshape(-1)
        mean = float(np.mean(flat)) if flat.size else 1.0
        std = float(np.std(flat)) if flat.size else 0.0
        w_min = float(np.min(flat)) if flat.size else 1.0
        w_max = float(np.max(flat)) if flat.size else 1.0
        above1 = float(np.mean(flat > 1.0)) if flat.size else 0.0
        below1 = float(np.mean(flat < 1.0)) if flat.size else 0.0

        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n### Token Weights — Step {step}, Epoch {epoch:.2f}\n\n")
            f.write("| Stat | Value |\n")
            f.write("|------|-------|\n")
            f.write(f"| mean | {mean:.4f} |\n")
            f.write(f"| std | {std:.4f} |\n")
            f.write(f"| min | {w_min:.4f} |\n")
            f.write(f"| max | {w_max:.4f} |\n")
            f.write(f"| frac(>1) | {above1:.3f} |\n")
            f.write(f"| frac(<1) | {below1:.3f} |\n\n")

            # 样本预览
            try:
                B = tw.shape[0]
                T = tw.shape[1] if tw.ndim >= 2 else 0
                preview = min(B, 8)
                f.write(f"预览前 {preview} 个样本，每个样本前 {max_preview_tokens} 个 token 权重：\n\n")
                for i in range(preview):
                    row = tw[i] if T > 0 else np.array([])
                    row_mean = float(np.mean(row)) if row.size else 1.0
                    row_std = float(np.std(row)) if row.size else 0.0
                    head = ", ".join([f"{x:.3f}" for x in row[:max_preview_tokens]]) if row.size else ""
                    f.write(f"- Sample {i+1}: mean={row_mean:.4f}, std={row_std:.4f}, head=[{head}]\n")
                f.write("\n")
            except Exception:
                pass
        _debug_log("emit_token_weights_logs:write_done", log_path=log_path, preview=min(tw.shape[0], 8) if tw.ndim >= 1 else 0)
    except Exception as e:
        print(f"⚠️  Warning: Failed to write token weights log: {e}")
        _debug_log("emit_token_weights_logs:error", error=str(e))


def emit_tokenwise_weights(
    token_strings: List[List[str]],
    token_weights: List[List[float]],
    log_path: Optional[str] = None,
    step: int = 0,
    epoch: float = 0.0,
    max_preview_tokens: int = 384,
) -> None:
    """
    将“逐 token”的权重与对应 token 串联输出到与 rollout 相同的日志文件中。
    - 不做星号或其他可视化包裹，仅以 (token, weight) 对列表形式展示，避免歧义。
    - 仅预览前 max_preview_tokens 个 token，避免日志过长。

    Args:
        token_strings: List[per-sample tokens]，每个元素是该样本 completion 的逐 token 字符串列表。
        token_weights: List[per-sample weights]，每个元素是与 token_strings 对齐的权重列表。
        log_path: 同 rollout 日志路径；若为空，落到 training_logs/rollout_results.md。
        step/epoch: 仅用于标题说明。
        max_preview_tokens: 每个样本最多展示多少个 token。
    """
    try:
        _debug_log(
            "emit_tokenwise_weights:start",
            step=step,
            epoch=epoch,
            log_path=log_path,
            sample_cnt=len(token_strings),
        )
        if not token_strings or not token_weights:
            _debug_log("emit_tokenwise_weights:skip_empty")
            return
        if not log_path:
            log_path = os.path.join("training_logs", "rollout_results.md")
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n### Tokenwise Weights — Step {step}, Epoch {epoch:.2f}\n")
            preview = min(len(token_strings), 8)
            for i in range(preview):
                ts = token_strings[i] or []
                ws = token_weights[i] or []
                n = min(len(ts), len(ws), max_preview_tokens)
                if n == 0:
                    continue
                # 构造单行文本：保持 token 自带空格，词后加 (weight)
                def _norm(s: str) -> str:
                    return s.replace("▁", " ").replace("Ġ", " ")
                parts = []
                for j in range(n):
                    tok = _norm((ts[j] or "").replace("`", "\u0060"))
                    w = float(ws[j]) if isinstance(ws[j], (int, float)) else 1.0
                    parts.append(f"{tok}({w:.3f})")
                line = "".join(parts)
                f.write(f"Sample {i+1}: {line}\n")
    except Exception as e:
        print(f"⚠️  Warning: Failed to write tokenwise weights: {e}")
        _debug_log("emit_tokenwise_weights:error", error=str(e))


def perform_realtime_rollout_logging(
    *,
    is_main_process: bool,
    mode: str,
    args: Any,
    state_step: int,
    state_epoch: float,
    compute_attention_metrics: bool,
    attention_logs: Any,
    attention_skip_reasons: Any,
    processing_class: Any,
    prompts: List[Any],
    inputs: List[Dict[str, Any]],
    prompts_text: List[str],
    completions_text: List[str],
    rewards_per_func_local: torch.Tensor,
    total_rewards_local: torch.Tensor,
    reward_names: List[str],
    advantages_tensor: Optional[torch.Tensor],
    token_weights_tensor: Optional[torch.Tensor],
    completion_ids: torch.Tensor,
    completion_mask: torch.Tensor,
    process_slice: slice,
) -> None:
    """Unified realtime rollout logging pipeline moved out of the trainer."""
    try:
        _debug_log(
            "perform_realtime_rollout_logging:start",
            mode=mode,
            step=state_step,
            epoch=state_epoch,
            is_main=is_main_process,
            prompts=len(prompts),
        )
        if not getattr(args, "realtime_rollout_logging", False):
            _debug_log("perform_realtime_rollout_logging:disable_flag")
            return
        if mode != "train":
            _debug_log("perform_realtime_rollout_logging:non_train_mode", mode=mode)
            return

        # Check for empty batch but don't return early since gather is collective
        has_data = len(prompts) > 0 and rewards_per_func_local.numel() > 0 and total_rewards_local.numel() > 0
        if not has_data:
            _debug_log(
                "perform_realtime_rollout_logging:empty_batch_will_participate_in_gather",
                prompts=len(prompts),
                rewards_numel=rewards_per_func_local.numel(),
                total_numel=total_rewards_local.numel(),
            )
        vgr_info: List[Dict[str, Any]] = [{}] * len(prompts)
        solutions: List[str] = [""] * len(prompts)
        log_prompts_text: List[str] = [""] * len(prompts)
        advantages_for_log: Optional[List[float]] = None
        resampled_flags_local: Optional[List[bool]] = None
        
        if has_data:
            if compute_attention_metrics:
                # Priority 1: Use vgr_metrics already attached to inputs (guarantees alignment even with dynamic sampling)
                vgr_info_from_inputs = [inp.get("vgr_metrics") for inp in inputs]
                if any(m is not None for m in vgr_info_from_inputs):
                    vgr_info = [m if m is not None else {} for m in vgr_info_from_inputs]
                # Priority 2: Fallback to slicing the global attention_logs deque (prone to alignment issues)
                elif attention_logs is not None:
                    try:
                        att_list = list(attention_logs)
                        if att_list:
                            from .dapo_logging import compute_real_vgr_metrics as _compute_real_vgr_metrics
                            sample_results = att_list[-len(prompts):]
                            if attention_skip_reasons is not None:
                                skips = list(attention_skip_reasons)
                                skip_slice = skips[-len(sample_results):] if len(skips) >= len(sample_results) else [None] * len(sample_results)
                            else:
                                skip_slice = [None] * len(sample_results)
                            vgr_info_computed = _compute_real_vgr_metrics(sample_results, skip_slice)
                            if vgr_info_computed:
                                vgr_info = vgr_info_computed
                    except Exception:
                        pass

            # Solutions (if present)
            solutions = [inp.get("solution", "") for inp in inputs]

            # Compose prompts text for logs: prefer 'problem' if available; otherwise render user-only chat without system
            problems: List[Optional[str]] = []
            try:
                problems = [inp.get("problem", None) for inp in inputs]
            except Exception:
                problems = [None] * len(prompts)

            if is_conversational(inputs[0]):
                prompts_user_only: List[List[Dict[str, Any]]] = []
                for p in prompts:
                    try:
                        p2 = [m for m in p if isinstance(m, dict) and m.get("role") == "user"]
                        if not p2:
                            p2 = [m for m in p if isinstance(m, dict) and m.get("role") != "system"] or p
                    except Exception:
                        p2 = p
                    prompts_user_only.append(p2)
                rendered = [apply_chat_template({"prompt": p2}, processing_class)["prompt"] for p2 in prompts_user_only]
            else:
                rendered = prompts_text

            log_prompts_text = []
            for i in range(len(rendered)):
                val = problems[i] if i < len(problems) and isinstance(problems[i], str) and problems[i] else rendered[i]
                log_prompts_text.append(val)

            # Prepare advantage values for table: always log group (reward-based) advantages
            try:
                if advantages_tensor is not None:
                    advantages_for_log = advantages_tensor.detach().cpu().tolist()
            except Exception:
                advantages_for_log = None

            # Resampled flags: mark which samples came from dynamic resampling
            try:
                resampled_flags_local = [bool(inp.get("resampled", False)) for inp in inputs]
            except Exception:
                resampled_flags_local = None

        # Optionally gather data across all ranks so that rollout logs include
        # prompt groups from every device, similar to Ray DAPO. We perform the
        # collectives on all ranks, but only the main process writes to disk.
        log_prompts_all = log_prompts_text
        completions_all = completions_text
        solutions_all = solutions
        vgr_info_all = vgr_info
        rewards_per_func_all = rewards_per_func_local
        total_rewards_all = total_rewards_local
        advantages_all = advantages_for_log
        resampled_flags_all = resampled_flags_local

        if accel_gather_object is not None and accel_gather is not None:
            _debug_log(
                "perform_realtime_rollout_logging:gather_start",
                prompts=len(log_prompts_text),
                completions=len(completions_text),
                rewards_shape=tuple(rewards_per_func_local.shape),
                total_shape=tuple(total_rewards_local.shape),
            )
            try:
                # Lists / Python objects
                log_prompts_all = accel_gather_object(log_prompts_text)
                completions_all = accel_gather_object(completions_text)
                solutions_all = accel_gather_object(solutions)
                if resampled_flags_local is not None:
                    resampled_flags_all = accel_gather_object(resampled_flags_local)
                else:
                    resampled_flags_all = None
                # Gather vgr_info as well to match completions_all length
                vgr_info_all = accel_gather_object(vgr_info)

                # Rewards/advantages: these are already sliced per-rank by the trainer
                # We need to gather them to get the full batch view
                # Convert to list format first to handle variable-length per-rank data
                rewards_list = rewards_per_func_local.detach().cpu().tolist() if rewards_per_func_local.numel() > 0 else []
                total_list = total_rewards_local.detach().cpu().tolist() if total_rewards_local.numel() > 0 else []
                
                # Gather lists
                rewards_all_lists = accel_gather_object(rewards_list)
                total_all_lists = accel_gather_object(total_list)
                
                # Convert back to tensors on main process
                if len(rewards_all_lists) > 0 and isinstance(rewards_all_lists[0], list):
                    # rewards_all_lists is now a flat list from all ranks
                    rewards_per_func_all = torch.tensor(rewards_all_lists, dtype=torch.float32, device=rewards_per_func_local.device)
                else:
                    rewards_per_func_all = rewards_per_func_local
                    
                if len(total_all_lists) > 0:
                    total_rewards_all = torch.tensor(total_all_lists, dtype=torch.float32, device=total_rewards_local.device)
                else:
                    total_rewards_all = total_rewards_local

                # Gather advantages similarly
                if advantages_for_log is not None:
                    advantages_all = accel_gather_object(advantages_for_log)
                else:
                    advantages_all = None
            except Exception as e:
                # Fall back to local-only logging on failure
                _debug_log("perform_realtime_rollout_logging:gather_error", error=str(e))
                log_prompts_all = log_prompts_text
                completions_all = completions_text
                solutions_all = solutions
                vgr_info_all = vgr_info
                rewards_per_func_all = rewards_per_func_local
                total_rewards_all = total_rewards_local
                advantages_all = advantages_for_log
                resampled_flags_all = resampled_flags_local
            else:
                _debug_log(
                    "perform_realtime_rollout_logging:gather_done",
                    prompts=len(log_prompts_all),
                    completions=len(completions_all),
                    solutions=len(solutions_all),
                    vgr_info=len(vgr_info_all),
                    rewards_shape=tuple(rewards_per_func_all.shape) if torch.is_tensor(rewards_per_func_all) else f"list_{len(rewards_per_func_all) if isinstance(rewards_per_func_all, list) else 'unknown'}",
                    total_shape=tuple(total_rewards_all.shape) if torch.is_tensor(total_rewards_all) else f"list_{len(total_rewards_all) if isinstance(total_rewards_all, list) else 'unknown'}",
                )

        _debug_log(
            "perform_realtime_rollout_logging:prepared_data",
            prompts=len(log_prompts_all),
            completions=len(completions_all),
        )
        # Only the main process writes logs to disk.
        if not is_main_process:
            _debug_log("perform_realtime_rollout_logging:non_main_exit")
            return
        
        # Skip writing if we have no data (can happen after gather on main process with empty ranks)
        if len(log_prompts_all) == 0 or rewards_per_func_all.numel() == 0:
            _debug_log("perform_realtime_rollout_logging:main_skip_no_data_after_gather")
            return

        adv_label = "group-normalized"
        _debug_log(
            "perform_realtime_rollout_logging:emit_rollout_logs_enter",
            prompts=len(log_prompts_all),
            completions=len(completions_all),
            rewards_shape=tuple(rewards_per_func_all.shape),
            total_rewards_shape=tuple(total_rewards_all.shape),
        )
        emit_rollout_logs(
            prompts_text=log_prompts_all,
            completions_text=completions_all,
            solutions=solutions_all,
            rewards_per_func_local=rewards_per_func_all,
            total_rewards_local=total_rewards_all,
            reward_names=reward_names,
            vgr_info=vgr_info_all,
            log_path=getattr(args, "rollout_log_path", None),
            prompt_preview_chars=getattr(args, "prompt_preview_chars", 2000),
            completion_preview_chars=getattr(args, "completion_preview_chars", 2000),
            vgr_as_coefficient=getattr(args, "vgr_as_coefficient", 0),
            step=state_step,
            epoch=state_epoch,
            advantages_local=advantages_all,
            adv_desc=adv_label,
            resampled_flags=resampled_flags_all,
        )
        _debug_log("perform_realtime_rollout_logging:emit_rollout_logs_exit")

        # Token weight logs (coarse stats)
        if getattr(args, "token_weights", False) and token_weights_tensor is not None:
            _debug_log("perform_realtime_rollout_logging:emit_token_weights_enter")
            emit_token_weights_logs(
                token_weights=token_weights_tensor,
                log_path=getattr(args, "rollout_log_path", None),
                step=state_step,
                epoch=state_epoch,
            )
            _debug_log("perform_realtime_rollout_logging:emit_token_weights_exit")

            # Tokenwise preview with decoded tokens
            try:
                tokenizer = getattr(processing_class, "tokenizer", None)
                if tokenizer is not None:
                    token_strs: list[list[str]] = []
                    token_wts: list[list[float]] = []
                    local_ids = completion_ids
                    local_mask = completion_mask
                    local_w = token_weights_tensor
                    for i in range(local_ids.size(0)):
                        valid_len = int(local_mask[i].sum().item())
                        if valid_len <= 0:
                            token_strs.append([])
                            token_wts.append([])
                            continue
                        ids_i = local_ids[i, :valid_len].detach().cpu().tolist()
                        toks = tokenizer.convert_ids_to_tokens(ids_i, skip_special_tokens=False)
                        token_strs.append([str(t) for t in toks])
                        token_wts.append(local_w[i, :valid_len].detach().cpu().tolist())
                    import os as _os
                    rollout_path = getattr(args, "rollout_log_path", None)
                    token_log_path = _os.path.join(_os.path.dirname(rollout_path), "token_weights.md") if rollout_path else None
                    emit_tokenwise_weights(
                        token_strings=token_strs,
                        token_weights=token_wts,
                        log_path=token_log_path,
                        step=state_step,
                        epoch=state_epoch,
                    )
            except Exception:
                pass
        _debug_log("perform_realtime_rollout_logging:done")
    except Exception as e:
        print(f"⚠️  Warning: realtime rollout logging failed: {e}")
        _debug_log("perform_realtime_rollout_logging:error", error=str(e))


def print_compact_logs(logs: Dict[str, float], mode: str, use_hard_negative: bool = False) -> None:
    """Pretty-print compact grouped logs to terminal (moved out of trainer)."""
    try:
        # Rewards line
        r_acc = logs.get("rewards/accuracy_reward/mean", logs.get("eval_rewards/accuracy_reward/mean"))
        r_fmt = logs.get("rewards/think_format_reward/mean", logs.get("eval_rewards/think_format_reward/mean"))
        r_tag = logs.get("rewards/tag_count_reward/mean", logs.get("eval_rewards/tag_count_reward/mean"))
        # 统一优先读取 rewards/vgr/mean；兼容旧键名
        r_vgr = logs.get("rewards/vgr/mean", logs.get("eval_rewards/vgr/mean"))
        if r_vgr is None:
            if use_hard_negative:
                r_vgr = logs.get("rewards/vgr_hard_negative/mean", logs.get("eval_rewards/vgr_hard_negative/mean"))
            else:
                r_vgr = logs.get("rewards/vgr_reward/mean", logs.get("eval_rewards/vgr_reward/mean"))
                if r_vgr is None:
                    r_vgr = logs.get("rewards/vgr_reward_as_additive/mean", logs.get("eval_rewards/vgr_reward_as_additive/mean"))
        r_len = logs.get("rewards/length_reward/mean", logs.get("eval_rewards/length_reward/mean"))
        r_total = logs.get("reward", logs.get("eval_reward"))
        rewards_line = []
        if r_acc is not None: rewards_line.append(f"acc={r_acc:.3f}")
        if r_vgr is not None: rewards_line.append(f"vgr={r_vgr:.3f}")
        if r_fmt is not None: rewards_line.append(f"fmt={r_fmt:.3f}")
        if r_tag is not None: rewards_line.append(f"tag={r_tag:.3f}")
        if r_len is not None: rewards_line.append(f"len={r_len:.3f}")
        if r_total is not None: rewards_line.append(f"total={r_total:.3f}")
        if rewards_line:
            print("Rewards: " + ", ".join(rewards_line))

        # Loss/optim line
        loss = logs.get("loss", logs.get("eval_loss"))
        ent = logs.get("entropy", logs.get("eval_entropy"))
        lr = logs.get("learning_rate")
        grad = logs.get("grad_norm", logs.get("eval_grad_norm"))
        clip_low = logs.get("clip_ratio/low_mean", logs.get("eval_clip_ratio/low_mean"))
        clip_high = logs.get("clip_ratio/high_mean", logs.get("eval_clip_ratio/high_mean"))
        loss_line = []
        if loss is not None: loss_line.append(f"loss={loss:.4f}")
        if ent is not None: loss_line.append(f"entropy={ent:.4f}")
        if lr is not None: loss_line.append(f"lr={lr:.2e}")
        if grad is not None: loss_line.append(f"grad={grad:.3f}")
        if clip_low is not None: loss_line.append(f"clip_low={clip_low:.3f}")
        if clip_high is not None: loss_line.append(f"clip_high={clip_high:.3f}")
        if loss_line:
            print("Optim:   " + ", ".join(loss_line))
    except Exception:
        pass


def perform_eval_logging(
    *,
    is_main_process: bool,
    mode: str,
    args: Any,
    state_step: int,
    state_epoch: float,
    metrics: Dict[str, float],
    logs: Dict[str, float],
    internal_logs: Dict[str, Any],
    reward_names: List[str],
) -> None:
    """Assemble and emit evaluation logs to markdown (moved out of trainer)."""
    if not is_main_process or mode != "eval":
        return
    try:
        prompts_cm = list(internal_logs.get("prompt_chatml", []))
        completions_cm = list(internal_logs.get("completion", []))
        rewards_log = internal_logs.get("rewards", {}) if isinstance(internal_logs, dict) else {}
        total_rewards = list(rewards_log.get("total", [])) if isinstance(rewards_log, dict) else []
        reward_lists = {name: list(rewards_log.get(name, [])) for name in reward_names}

        # 准备 VGR 原始指标（若 attention 可用）
        vgr_info: List[Dict[str, Any]] = []
        try:
            att_list = list(internal_logs.get("attention", [])) if isinstance(internal_logs, dict) else []
            if att_list:
                sample_results = att_list[-len(prompts_cm):]
                skip_slice = [None] * len(sample_results)
                vgr_info = compute_real_vgr_metrics(sample_results, skip_slice)
        except Exception:
            vgr_info = []

        sample_count = min(len(prompts_cm), len(completions_cm))
        # 对齐 vgr_info 长度
        if vgr_info:
            vgr_info = vgr_info[:sample_count]
        
        # 检查奖励数据长度，如果发现不一致则打印警告
        if reward_names and sample_count > 0:
            for name in reward_names:
                vals = reward_lists.get(name, [])
                if len(vals) < sample_count:
                    print(f"⚠️  Warning: reward '{name}' has only {len(vals)} values but {sample_count} samples expected")
        
        eval_samples: List[Dict[str, Any]] = []
        for i in range(sample_count):
            rewards_map: Dict[str, float] = {}
            # 统一命名映射：accuracy、vgr、format、tag、length
            name_map = {
                "accuracy_reward": "accuracy",
                "vgr_reward": "vgr",
                "vgr_reward_as_additive": "vgr",
                "vgr_hard_negative": "vgr",
                "think_format_reward": "format",
                "tag_count_reward": "tag",
                "length_reward": "length",
            }
            for name in reward_names:
                vals = reward_lists.get(name, [])
                disp = name_map.get(name, name)
                if i < len(vals):
                    try:
                        rewards_map[disp] = float(vals[i])
                    except Exception:
                        # 如果转换失败，使用默认值0.0
                        if disp not in rewards_map:
                            rewards_map[disp] = 0.0
                else:
                    # 如果数据缺失，使用默认值0.0，确保所有样本都有完整的奖励信息
                    if disp not in rewards_map:
                        rewards_map[disp] = 0.0
            total_val = 0.0
            if i < len(total_rewards):
                try:
                    total_val = float(total_rewards[i])
                except Exception:
                    total_val = 0.0

            sample_obj: Dict[str, Any] = {
                "prompt": prompts_cm[i],
                "completion": completions_cm[i],
                "rewards": rewards_map,
                "total_reward": total_val,
            }
            # 注入详细 VGR 原始指标（若可用），并在 rewards 中加入 vgr_raw
            if vgr_info and i < len(vgr_info) and vgr_info[i]:
                info = vgr_info[i]
                try:
                    attn_text = float(info.get("attention_text", 0.0) or 0.0)
                    attn_vision = float(info.get("attention_vision", 0.0) or 0.0)
                    t = int(info.get("num_text_tokens", 0) or 0)
                    o = int(info.get("num_vision_tokens", 0) or 0)
                except Exception:
                    attn_text, attn_vision, t, o = 0.0, 0.0, 0, 0
                density_text = (attn_text / t) if t > 0 else None
                density_vision = (attn_vision / o) if o > 0 else None
                vgr_raw = float(info.get("vgr", 0.0) or 0.0)
                text_ratio = None
                vision_ratio = None
                try:
                    text_ratio = vgr_raw / (1.0 + vgr_raw)
                    vision_ratio = 1.0 / (1.0 + vgr_raw)
                except Exception:
                    pass

                # 将 vgr_raw 作为奖励行中的一个显示项（统一命名）
                try:
                    rewards_map["vgr_raw"] = float(vgr_raw)
                except Exception:
                    pass

                sample_obj["detailed_metrics"] = {
                    "vgr_metrics": {
                        "vgr_raw": vgr_raw,
                        "attention_text": attn_text,
                        "attention_vision": attn_vision,
                        "density_text": density_text,
                        "density_vision": density_vision,
                        "text_ratio": text_ratio,
                        "vision_ratio": vision_ratio,
                    },
                    "token_counts": {
                        "vision_tokens": float(o),
                        "text_tokens": float(t),
                        "total_tokens": float(t + o),
                    },
                    "overall": {
                        "attention_distribution": info.get("attention_distribution"),
                        "skip_reason": info.get("skip_reason"),
                    },
                }
            eval_samples.append(sample_obj)

        emit_eval_logs(
            metrics=metrics,
            logs=logs,
            eval_samples=eval_samples,
            log_path=getattr(args, "eval_log_path", None),
            step=state_step,
            epoch=state_epoch,
        )
    except Exception as e:
        print(f"⚠️  Warning: Failed to emit eval logs: {e}")
