"""DAPO 日志：rollout、evaluation 与注意力诊断输出。"""

import json
import math
import os
from datetime import datetime
from typing import Any, Dict, List, Optional

import numpy as np
import torch



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

            length_idx = any_index("length_reward", "soft_overlong_punishment_reward")
            if length_idx is not None and idx < rewards_per_func_local.shape[0]:
                length_val = float(rewards_per_func_local[idx, length_idx].item())

            vgr_idx = any_index("vgr_reward", "vgr_reward_as_additive")
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
                    vgr_scores = [r[7] for r in rows]
                    total_scores = [r[8] for r in rows]
                    adv_scores = [r[9] for r in rows if r[9] is not None]
                    
                    f.write(f"| Accuracy Mean | {np.mean(accuracy_scores):.3f} ± {np.std(accuracy_scores):.3f} |\n")
                    f.write(f"| Format Mean | {np.mean(format_scores):.3f} ± {np.std(format_scores):.3f} |\n")
                    f.write(f"| Length Mean | {np.mean(length_scores):.3f} ± {np.std(length_scores):.3f} |\n")
                    f.write(f"| VGR Mean | {np.mean(vgr_scores):.3f} ± {np.std(vgr_scores):.3f} |\n")
                    f.write(f"| Total Reward Mean | {np.mean(total_scores):.3f} ± {np.std(total_scores):.3f} |\n")
                    f.write(f"| Accuracy Rate | {np.mean([1 if s > 0 else 0 for s in accuracy_scores]):.3f} |\n")
                    f.write(f"| Format Rate | {np.mean([1 if s > 0 else 0 for s in format_scores]):.3f} |\n")
                    f.write(f"| Success Rate | {np.mean([1 if s > 0 else 0 for s in total_scores]):.3f} |\n\n")
                    if adv_scores:
                        f.write(f"| Advantage ({adv_desc}) Mean | {np.mean(adv_scores):.3f} ± {np.std(adv_scores):.3f} |\n")
                        f.write("\n")
                    
                    # 分段 VGR 统计
                    if vgr_info:
                        f.write("### VGR Statistics\n\n")
                        f.write("| Stage | VGR Mean | VGR Std | AEI Text | AEI Vision |\n")
                        f.write("|-------|----------|---------|----------|------------|\n")
                        
                        early_vgr = [info.get("early_vgr", 0) for info in vgr_info if info.get("early_vgr") is not None]
                        middle_vgr = [info.get("middle_vgr", 0) for info in vgr_info if info.get("middle_vgr") is not None]
                        late_vgr = [info.get("late_vgr", 0) for info in vgr_info if info.get("late_vgr") is not None]
                        all_vgr = [info.get("all_vgr", 0) for info in vgr_info if info.get("all_vgr") is not None]
                        
                        early_aei_text = [info.get("early_aei_text", 0) for info in vgr_info]
                        early_aei_vision = [info.get("early_aei_vision", 0) for info in vgr_info]
                        middle_aei_text = [info.get("middle_aei_text", 0) for info in vgr_info]
                        middle_aei_vision = [info.get("middle_aei_vision", 0) for info in vgr_info]
                        late_aei_text = [info.get("late_aei_text", 0) for info in vgr_info]
                        late_aei_vision = [info.get("late_aei_vision", 0) for info in vgr_info]
                        all_aei_text = [info.get("all_aei_text", 0) for info in vgr_info]
                        all_aei_vision = [info.get("all_aei_vision", 0) for info in vgr_info]
                        
                        f.write(f"| Early | {np.mean(early_vgr):.3f} | {np.std(early_vgr):.3f} | {np.mean(early_aei_text):.3f} | {np.mean(early_aei_vision):.3f} |\n")
                        f.write(f"| Middle | {np.mean(middle_vgr):.3f} | {np.std(middle_vgr):.3f} | {np.mean(middle_aei_text):.3f} | {np.mean(middle_aei_vision):.3f} |\n")
                        f.write(f"| Late | {np.mean(late_vgr):.3f} | {np.std(late_vgr):.3f} | {np.mean(late_aei_text):.3f} | {np.mean(late_aei_vision):.3f} |\n")
                        f.write(f"| All | {np.mean(all_vgr):.3f} | {np.std(all_vgr):.3f} | {np.mean(all_aei_text):.3f} | {np.mean(all_aei_vision):.3f} |\n\n")
                
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
                    
                    # 详细 metrics
                    if info:
                        f.write("**Detailed Metrics:**\n\n")
                        f.write("```json\n")
                        detailed_metrics = {
                            "rewards": {
                                "accuracy": float(r[4]),
                                "format": float(r[5]),
                                "length": float(r[6]),
                                "vgr": float(r[7]),
                                "total": float(r[8])
                            },
                            "advantage": float(r[9]) if r[9] is not None else None,
                            "attention_metrics": {
                                "early": {
                                    "vgr": info.get("early_vgr"),
                                    "aei_text": info.get("early_aei_text"),
                                    "aei_vision": info.get("early_aei_vision"),
                                    "text_ratio": info.get("early_text_ratio"),
                                    "vision_ratio": info.get("early_vision_ratio")
                                },
                                "middle": {
                                    "vgr": info.get("middle_vgr"),
                                    "aei_text": info.get("middle_aei_text"),
                                    "aei_vision": info.get("middle_aei_vision"),
                                    "text_ratio": info.get("middle_text_ratio"),
                                    "vision_ratio": info.get("middle_vision_ratio")
                                },
                                "late": {
                                    "vgr": info.get("late_vgr"),
                                    "aei_text": info.get("late_aei_text"),
                                    "aei_vision": info.get("late_aei_vision"),
                                    "text_ratio": info.get("late_text_ratio"),
                                    "vision_ratio": info.get("late_vision_ratio")
                                },
                                "all": {
                                    "vgr": info.get("all_vgr"),
                                    "aei_text": info.get("all_aei_text"),
                                    "aei_vision": info.get("all_aei_vision"),
                                    "text_ratio": info.get("all_text_ratio"),
                                    "vision_ratio": info.get("all_vision_ratio")
                                }
                            },
                            "token_counts": {
                                "vision_tokens": float(info.get("num_vision_tokens", 0) or 0),
                                "text_tokens": float(info.get("num_text_tokens", 0) or 0),
                                "total_tokens": float((info.get("num_vision_tokens", 0) or 0) + (info.get("num_text_tokens", 0) or 0)),
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
            
            # 注意力指标
            attention_metrics = {
                "eval_attention/early/vgr": logs.get("eval_attention/early/vgr"),
                "eval_attention/middle/vgr": logs.get("eval_attention/middle/vgr"),
                "eval_attention/late/vgr": logs.get("eval_attention/late/vgr"),
                "eval_attention/all/vgr": logs.get("eval_attention/all/vgr"),
            }
            
            if any(v is not None for v in attention_metrics.values()):
                f.write("\n### Attention Statistics\n\n")
                f.write("| Stage | VGR | AEI Text | AEI Vision |\n")
                f.write("|-------|-----|----------|------------|\n")
                
                stages = ["early", "middle", "late", "all"]
                for stage in stages:
                    vgr_key = f"eval_attention/{stage}/vgr"
                    aei_text_key = f"eval_attention/{stage}/aei_text"
                    aei_vision_key = f"eval_attention/{stage}/aei_vision"
                    
                    vgr_val = logs.get(vgr_key, 0.0)
                    aei_text_val = logs.get(aei_text_key, 0.0)
                    aei_vision_val = logs.get(aei_vision_key, 0.0)
                    
                    f.write(f"| {stage.title()} | {vgr_val:.3f} | {aei_text_val:.3f} | {aei_vision_val:.3f} |\n")
            
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
    """
    计算真实的 VGR 指标用于日志记录
    
    Args:
        sample_results: 注意力样本结果列表
        skip_reasons: 跳过原因列表
        
    Returns:
        VGR 指标字典列表
    """
    results = []
    if skip_reasons is None:
        skip_reasons = [None] * len(sample_results)

    for idx, res in enumerate(sample_results):
        if res is None:
            reason = skip_reasons[idx] if idx < len(skip_reasons) else None
            default_result = {
                "vgr": 1.0,
                "text_ratio": 0.5,
                "vision_ratio": 0.5,
                "attention_distribution": [0.5, 0.5],
                "num_vision_tokens": 0,
                "num_text_tokens": 0,
                "attention_text": 0.0,
                "attention_vision": 0.0,
                "early_vgr": 1.0,
                "middle_vgr": 1.0,
                "late_vgr": 1.0,
                "all_vgr": 1.0,
                "early_aei_text": 0.0,
                "early_aei_vision": 0.0,
                "middle_aei_text": 0.0,
                "middle_aei_vision": 0.0,
                "late_aei_text": 0.0,
                "late_aei_vision": 0.0,
                "all_aei_text": 0.0,
                "all_aei_vision": 0.0,
                "early_text_ratio": 0.5,
                "early_vision_ratio": 0.5,
                "middle_text_ratio": 0.5,
                "middle_vision_ratio": 0.5,
                "late_text_ratio": 0.5,
                "late_vision_ratio": 0.5,
                "all_text_ratio": 0.5,
                "all_vision_ratio": 0.5,
                "aei_text": 0.0,
                "aei_vision": 0.0,
                "skip_reason": reason,
            }
            results.append(default_result)
            continue

        segments = getattr(res, "segments", {}) if res is not None else {}
        # Align with attention_metrics.AttentionSampleResult fields:
        # text tokens are stored as `num_instruction_tokens` in the result.
        num_vision_tokens = getattr(res, "num_vision_tokens", 0)
        num_text_tokens = getattr(res, "num_instruction_tokens", getattr(res, "num_text_tokens", 0))

        def process_segment(segment_name):
            segment = segments.get(segment_name)
            if segment is None or not hasattr(segment, "vgr") or segment.vgr is None:
                return {
                    "vgr": 1.0,
                    "aei_text": 0.0,
                    "aei_vision": 0.0,
                    "attention_text": 0.0,
                    "attention_vision": 0.0,
                    "text_ratio": 0.5,
                    "vision_ratio": 0.5,
                }

            vgr = float(segment.vgr)
            if not (vgr > 0) or not math.isfinite(vgr):
                return {
                    "vgr": 1.0,
                    "aei_text": 0.0,
                    "aei_vision": 0.0,
                    "attention_text": 0.0,
                    "attention_vision": 0.0,
                    "text_ratio": 0.5,
                    "vision_ratio": 0.5,
                }

            aei_text = float(getattr(segment, "aei_text", 0.0))
            aei_vision = float(getattr(segment, "aei_vision", 0.0))
            attention_text = float(getattr(segment, "attention_text", 0.0))
            attention_vision = float(getattr(segment, "attention_vision", 0.0))
            text_ratio = vgr / (1.0 + vgr)
            vision_ratio = 1.0 / (1.0 + vgr)

            return {
                "vgr": round(float(vgr), 6),
                "aei_text": round(float(aei_text), 6),
                "aei_vision": round(float(aei_vision), 6),
                "attention_text": round(float(attention_text), 6),
                "attention_vision": round(float(attention_vision), 6),
                "text_ratio": round(float(text_ratio), 6),
                "vision_ratio": round(float(vision_ratio), 6),
            }

        early_data = process_segment("early")
        middle_data = process_segment("middle")
        late_data = process_segment("late")
        all_data = process_segment("all")

        # 修复VGR选择逻辑：优先使用late段，如果无效则使用all段
        if late_data["vgr"] != 1.0:
            main_segment = late_data
        else:
            main_segment = all_data
        vgr = main_segment["vgr"]

        text_ratio = vgr / (1.0 + vgr)
        vision_ratio = 1.0 / (1.0 + vgr)

        result = {
            "vgr": round(float(vgr), 6),
            "text_ratio": round(float(text_ratio), 6),
            "vision_ratio": round(float(vision_ratio), 6),
            "attention_distribution": [text_ratio, vision_ratio],
            "num_vision_tokens": int(num_vision_tokens),
            "num_text_tokens": int(num_text_tokens),
            # Use late segment's attention values, fallback to all segment
            "attention_text": main_segment["attention_text"],
            "attention_vision": main_segment["attention_vision"],
            "early_vgr": early_data["vgr"],
            "middle_vgr": middle_data["vgr"],
            "late_vgr": late_data["vgr"],
            "all_vgr": all_data["vgr"],
            "early_aei_text": early_data["aei_text"],
            "early_aei_vision": early_data["aei_vision"],
            "middle_aei_text": middle_data["aei_text"],
            "middle_aei_vision": middle_data["aei_vision"],
            "late_aei_text": late_data["aei_text"],
            "late_aei_vision": late_data["aei_vision"],
            "all_aei_text": all_data["aei_text"],
            "all_aei_vision": all_data["aei_vision"],
            "early_text_ratio": early_data["text_ratio"],
            "early_vision_ratio": early_data["vision_ratio"],
            "middle_text_ratio": middle_data["text_ratio"],
            "middle_vision_ratio": middle_data["vision_ratio"],
            "late_text_ratio": late_data["text_ratio"],
            "late_vision_ratio": late_data["vision_ratio"],
            "all_text_ratio": all_data["text_ratio"],
            "all_vision_ratio": all_data["vision_ratio"],
            "aei_text": all_data["aei_text"],
            "aei_vision": all_data["aei_vision"],
            "skip_reason": None,
        }
        results.append(result)

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
