"""DAPO 日志：rollout、evaluation 与注意力诊断输出。"""

import json
import math
import os
from datetime import datetime
from typing import Any, Dict, List, Optional

import numpy as np
import torch
from trl.data_utils import is_conversational, apply_chat_template



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
        
        # 奖励值
        acc = 0.0
        fmt = 0.0
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
        rows.append((idx + 1, preview_p, preview_c, solution or "", acc, fmt, length_val, vgr_val, tot, adv_val))
    
    # 写入 rollout 日志
    if log_path:
        try:
            os.makedirs(os.path.dirname(log_path), exist_ok=True)
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(f"\n## {header} | {ts}\n\n")
                
                # 总体统计
                if rows:
                    f.write("### Overall Statistics\n\n")
                    f.write("| Metric | Value |\n")
                    f.write("|--------|-------|\n")
                    
                    # 计算统计
                    accuracy_scores = [r[4] for r in rows]
                    format_scores = [r[5] for r in rows]
                    length_scores = [r[6] for r in rows]
                    total_scores = [r[8] for r in rows]
                    adv_scores = [r[9] for r in rows if r[9] is not None]
                    # 来自 attention 的 VGR 原始指标（若可用）
                    vgr_raw_list = []
                    if vgr_info:
                        for info in vgr_info:
                            try:
                                vgr_raw_list.append(float(info.get("vgr", float("nan"))))
                            except Exception:
                                pass
                    
                    f.write(f"| Accuracy Mean | {np.mean(accuracy_scores):.3f} ± {np.std(accuracy_scores):.3f} |\n")
                    f.write(f"| Format Mean | {np.mean(format_scores):.3f} ± {np.std(format_scores):.3f} |\n")
                    f.write(f"| Length Mean | {np.mean(length_scores):.3f} ± {np.std(length_scores):.3f} |\n")
                    f.write(f"| Total Reward Mean | {np.mean(total_scores):.3f} ± {np.std(total_scores):.3f} |\n")
                    f.write(f"| Accuracy Rate | {np.mean([1 if s > 0 else 0 for s in accuracy_scores]):.3f} |\n")
                    f.write(f"| Format Rate | {np.mean([1 if s > 0 else 0 for s in format_scores]):.3f} |\n")
                    f.write(f"| Success Rate | {np.mean([1 if s > 0 else 0 for s in total_scores]):.3f} |\n\n")
                    if adv_scores:
                        f.write(f"| Advantage ({adv_desc}) Mean | {np.mean(adv_scores):.3f} ± {np.std(adv_scores):.3f} |\n")
                        f.write("\n")
                    # 汇总 VGR 原始指标
                    if vgr_raw_list:
                        try:
                            vgr_mean = float(np.nanmean(vgr_raw_list))
                            vgr_std = float(np.nanstd(vgr_raw_list))
                            f.write(f"| VGR (raw) Mean | {vgr_mean:.3f} ± {vgr_std:.3f} |\n\n")
                        except Exception:
                            pass
                    
                    # Attention statistics removed (AEI unused)
                
                # 样本明细
                for i, (r, info) in enumerate(zip(rows, vgr_info), start=1):
                    f.write(f"### Sample {i}\n\n")
                    f.write(f"**Prompt:** {r[1]}\n\n")
                    f.write(f"**Completion:** {r[2]}\n\n")
                    f.write(f"**Solution:** {r[3]}\n\n")
                    
                    # 按 VGR 使用方式显示标签
                    true_vgr = info.get("vgr", 0.0) if info else 0.0
                    
                    if vgr_as_coefficient == 1:
                        # VGR作为系数
                        f.write(f"**Rewards:** accuracy={r[4]:.3f}, format={r[5]:.3f}, length={r[6]:.3f}, vgr_coe={r[7]:.3f}, vgr={true_vgr:.3f}, total={r[8]:.3f}\n\n")
                    else:
                        # VGR作为加法项
                        f.write(f"**Rewards:** accuracy={r[4]:.3f}, format={r[5]:.3f}, length={r[6]:.3f}, vgr_add={r[7]:.3f}, vgr={true_vgr:.3f}, total={r[8]:.3f}\n\n")

                    # Advantage（若提供则展示；若为 token_weights 实验，建议传入加权后的优势）
                    if r[9] is not None:
                        f.write(f"**Advantage ({adv_desc}):** {float(r[9]):.4f}\n\n")
                    
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
                                "accuracy": float(r[4]),
                                "format": float(r[5]),
                                "length": float(r[6]),
                                "vgr": float(r[7]),
                                "total": float(r[8])
                            },
                            "advantage": float(r[9]) if r[9] is not None else None,
                            "token_counts": {
                                "vision_tokens": float(info.get("num_vision_tokens", 0) or 0),
                                "text_tokens": float(info.get("num_text_tokens", 0) or 0),
                                "total_tokens": float((info.get("num_vision_tokens", 0) or 0) + (info.get("num_text_tokens", 0) or 0)),
                            },
                            "vgr_metrics": {
                                "vgr_raw": float(info.get("vgr", 0.0) or 0.0),
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
        except Exception as e:
            print(f"⚠️  Warning: Failed to write to rollout log file: {e}")


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
    # If caller provides a path, respect it; else fallback to default
    if not log_path:
        log_path = os.path.join("training_logs", "eval_results.md")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    try:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"=== Evaluation Step {step} ==="
        
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n## {header} | {ts}\n\n")
            
            # 添加总体统计信息
            f.write("### Overall Statistics\n\n")
            f.write("| Metric | Value |\n")
            f.write("|--------|-------|\n")
            
            # 核心指标
            core_metrics = {
                "eval_loss": logs.get("eval_loss", 0.0),
                "eval_reward": metrics.get("eval_reward", 0.0),
                "eval_accuracy": metrics.get("eval_accuracy", 0.0),
                "eval_format": metrics.get("eval_format", 0.0),
                "eval_length": metrics.get("eval_length", 0.0),
                "eval_vgr": metrics.get("eval_vgr", 0.0),
            }
            
            for key, value in core_metrics.items():
                if value is not None:
                    f.write(f"| {key} | {value:.4f} |\n")

            # 若样本包含 vgr 原始指标，则补充聚合值
            try:
                vgr_vals = []
                for sample in (eval_samples or []):
                    dm = sample.get("detailed_metrics", {}) if isinstance(sample, dict) else {}
                    vm = dm.get("vgr_metrics", {}) if isinstance(dm, dict) else {}
                    v = vm.get("vgr_raw", None)
                    if isinstance(v, (int, float)):
                        vgr_vals.append(float(v))
                if vgr_vals:
                    vgr_mean = float(np.nanmean(vgr_vals))
                    vgr_std = float(np.nanstd(vgr_vals))
                    f.write(f"| eval_vgr_raw | {vgr_mean:.4f} ± {vgr_std:.4f} |\n")
            except Exception:
                pass
            
            # 注意力指标（AEI 移除）
            
            # 样本数据
            if eval_samples:
                f.write(f"\n### Evaluation Samples ({len(eval_samples)} samples)\n\n")
                
                for i, sample in enumerate(eval_samples, 1):
                    f.write(f"### Sample {i}\n\n")
                    
                    # 显示prompt
                    f.write(f"**Prompt:** {sample.get('prompt', 'N/A')}\n\n")
                    
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
                    f.write(", ".join(reward_parts))
                    f.write(f", total={sample.get('total_reward', 0.0):.3f}\n\n")
                    
                    # 显示详细指标（如果有）
                    if 'detailed_metrics' in sample:
                        f.write("**Detailed Metrics:**\n\n")
                        f.write("```json\n")
                        f.write(json.dumps(sample['detailed_metrics'], ensure_ascii=False, indent=2))
                        f.write("\n```\n\n")
                    
                    f.write("---\n\n")
    except Exception as e:
        print(f"⚠️  Warning: Failed to write to eval log file: {e}")


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
        if token_weights is None:
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
    except Exception as e:
        print(f"⚠️  Warning: Failed to write token weights log: {e}")


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
        if not token_strings or not token_weights:
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
    token_weights_tensor: Optional[torch.Tensor],
    completion_ids: torch.Tensor,
    completion_mask: torch.Tensor,
    process_slice: slice,
) -> None:
    """Unified realtime rollout logging pipeline moved out of the trainer."""
    try:
        if not is_main_process:
            return
        if not getattr(args, "realtime_rollout_logging", False):
            return
        if mode != "train":
            return

        # Build VGR info for logging (no AEI usage downstream)
        vgr_info: List[Dict[str, Any]] = []
        if compute_attention_metrics and attention_logs is not None:
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
                    vgr_info = _compute_real_vgr_metrics(sample_results, skip_slice)
            except Exception:
                vgr_info = []

        # Solutions (if present)
        solutions = [inp.get("solution", "") for inp in inputs]

        # Compose prompts text with chat template if needed
        if is_conversational(inputs[0]):
            log_prompts_text = [apply_chat_template({"prompt": p}, processing_class)["prompt"] for p in prompts]
        else:
            log_prompts_text = prompts_text

        # Prepare advantage values for table
        advantages_for_log = None
        try:
            # `advantages` is not passed; instead consume per-row from total_rewards? keep None for simplicity
            if getattr(args, "token_weights", False) and token_weights_tensor is not None:
                tw_local = token_weights_tensor[process_slice]
                cm_local = completion_mask[process_slice].float()
                valid = cm_local.sum(dim=1).clamp(min=1.0)
                mean_w = (tw_local * cm_local).sum(dim=1) / valid
                advantages_for_log = mean_w.detach().cpu().tolist()
        except Exception:
            advantages_for_log = None

        # Emit markdown rollout log
        emit_rollout_logs(
            prompts_text=log_prompts_text,
            completions_text=completions_text,
            solutions=solutions,
            rewards_per_func_local=rewards_per_func_local,
            total_rewards_local=total_rewards_local,
            reward_names=reward_names,
            vgr_info=vgr_info,
            log_path=getattr(args, "rollout_log_path", None),
            prompt_preview_chars=getattr(args, "prompt_preview_chars", 2000),
            completion_preview_chars=getattr(args, "completion_preview_chars", 2000),
            vgr_as_coefficient=getattr(args, "vgr_as_coefficient", 0),
            step=state_step,
            epoch=state_epoch,
            advantages_local=advantages_for_log,
        )

        # Token weight logs (coarse stats)
        if getattr(args, "token_weights", False) and token_weights_tensor is not None:
            emit_token_weights_logs(
                token_weights=token_weights_tensor,
                log_path=getattr(args, "rollout_log_path", None),
                step=state_step,
                epoch=state_epoch,
            )

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
    except Exception as e:
        print(f"⚠️  Warning: realtime rollout logging failed: {e}")


def print_compact_logs(logs: Dict[str, float], mode: str, use_hard_negative: bool = False) -> None:
    """Pretty-print compact grouped logs to terminal (moved out of trainer)."""
    try:
        # Rewards line
        r_acc = logs.get("rewards/accuracy_reward/mean", logs.get("eval_rewards/accuracy_reward/mean"))
        r_fmt = logs.get("rewards/think_format_reward/mean", logs.get("eval_rewards/think_format_reward/mean"))
        # Prefer new VGR reward key; fall back to legacy additive key if present
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
        if r_fmt is not None: rewards_line.append(f"fmt={r_fmt:.3f}")
        if r_vgr is not None: rewards_line.append(f"vgr={r_vgr:.3f}")
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
        eval_samples: List[Dict[str, Any]] = []
        for i in range(sample_count):
            rewards_map: Dict[str, float] = {}
            for name in reward_names:
                vals = reward_lists.get(name, [])
                if i < len(vals):
                    try:
                        rewards_map[name] = float(vals[i])
                    except Exception:
                        pass
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
            # 注入详细 VGR 原始指标（若可用）
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
