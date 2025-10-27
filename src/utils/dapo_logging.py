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
    mdi_info: List[Dict[str, Any]],
    log_path: Optional[str] = None,
    prompt_preview_chars: int = 2000,
    completion_preview_chars: int = 2000,
    mdi_as_coefficient: int = 0,
    step: int = 0,
    epoch: float = 0.0,
) -> None:
    """将 rollout 信息写入 markdown。

    仅保留必要字段说明：rewards_per_func_local 与 reward_names 一一对应；mdi_info
    为 compute_real_mdi_metrics 输出，用于展示分段与汇总 MDI。
    """
    # If caller provides a path, respect it; else fallback to default
    if not log_path:
        log_path = os.path.join("training_logs", "rollout_results.md")
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
        mdi_val = 0.0
        
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

            mdi_idx = any_index("mdi_reward", "mdi_reward_as_additive")
            if mdi_idx is not None and idx < rewards_per_func_local.shape[0]:
                mdi_val = float(rewards_per_func_local[idx, mdi_idx].item())
        
        tot = float(total_rewards_local[idx].item()) if total_rewards_local.numel() > 0 else 0.0
        rows.append((idx + 1, preview_p, preview_c, solution or "", acc, fmt, length_val, mdi_val, tot))
    
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
                    mdi_scores = [r[7] for r in rows]
                    total_scores = [r[8] for r in rows]
                    
                    f.write(f"| Accuracy Mean | {np.mean(accuracy_scores):.3f} ± {np.std(accuracy_scores):.3f} |\n")
                    f.write(f"| Format Mean | {np.mean(format_scores):.3f} ± {np.std(format_scores):.3f} |\n")
                    f.write(f"| Length Mean | {np.mean(length_scores):.3f} ± {np.std(length_scores):.3f} |\n")
                    f.write(f"| MDI Mean | {np.mean(mdi_scores):.3f} ± {np.std(mdi_scores):.3f} |\n")
                    f.write(f"| Total Reward Mean | {np.mean(total_scores):.3f} ± {np.std(total_scores):.3f} |\n")
                    f.write(f"| Accuracy Rate | {np.mean([1 if s > 0 else 0 for s in accuracy_scores]):.3f} |\n")
                    f.write(f"| Format Rate | {np.mean([1 if s > 0 else 0 for s in format_scores]):.3f} |\n")
                    f.write(f"| Success Rate | {np.mean([1 if s > 0 else 0 for s in total_scores]):.3f} |\n\n")
                    
                    # 分段 MDI 统计
                    if mdi_info:
                        f.write("### MDI Statistics\n\n")
                        f.write("| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |\n")
                        f.write("|-------|----------|---------|----------|------------|\n")
                        
                        early_mdi = [info.get("early_mdi", 0) for info in mdi_info if info.get("early_mdi") is not None]
                        middle_mdi = [info.get("middle_mdi", 0) for info in mdi_info if info.get("middle_mdi") is not None]
                        late_mdi = [info.get("late_mdi", 0) for info in mdi_info if info.get("late_mdi") is not None]
                        all_mdi = [info.get("all_mdi", 0) for info in mdi_info if info.get("all_mdi") is not None]
                        
                        early_aei_text = [info.get("early_aei_text", 0) for info in mdi_info]
                        early_aei_vision = [info.get("early_aei_vision", 0) for info in mdi_info]
                        middle_aei_text = [info.get("middle_aei_text", 0) for info in mdi_info]
                        middle_aei_vision = [info.get("middle_aei_vision", 0) for info in mdi_info]
                        late_aei_text = [info.get("late_aei_text", 0) for info in mdi_info]
                        late_aei_vision = [info.get("late_aei_vision", 0) for info in mdi_info]
                        all_aei_text = [info.get("all_aei_text", 0) for info in mdi_info]
                        all_aei_vision = [info.get("all_aei_vision", 0) for info in mdi_info]
                        
                        f.write(f"| Early | {np.mean(early_mdi):.3f} | {np.std(early_mdi):.3f} | {np.mean(early_aei_text):.3f} | {np.mean(early_aei_vision):.3f} |\n")
                        f.write(f"| Middle | {np.mean(middle_mdi):.3f} | {np.std(middle_mdi):.3f} | {np.mean(middle_aei_text):.3f} | {np.mean(middle_aei_vision):.3f} |\n")
                        f.write(f"| Late | {np.mean(late_mdi):.3f} | {np.std(late_mdi):.3f} | {np.mean(late_aei_text):.3f} | {np.mean(late_aei_vision):.3f} |\n")
                        f.write(f"| All | {np.mean(all_mdi):.3f} | {np.std(all_mdi):.3f} | {np.mean(all_aei_text):.3f} | {np.mean(all_aei_vision):.3f} |\n\n")
                
                # 样本明细
                for i, (r, info) in enumerate(zip(rows, mdi_info), start=1):
                    f.write(f"### Sample {i}\n\n")
                    f.write(f"**Prompt:** {r[1]}\n\n")
                    f.write(f"**Completion:** {r[2]}\n\n")
                    f.write(f"**Solution:** {r[3]}\n\n")
                    
                    # 按 MDI 使用方式显示标签
                    true_mdi = info.get("mdi", 0.0) if info else 0.0
                    
                    if mdi_as_coefficient == 1:
                        # MDI作为系数
                        f.write(f"**Rewards:** accuracy={r[4]:.3f}, format={r[5]:.3f}, length={r[6]:.3f}, mdi_coe={r[7]:.3f}, mdi={true_mdi:.3f}, total={r[8]:.3f}\n\n")
                    else:
                        # MDI作为加法项
                        f.write(f"**Rewards:** accuracy={r[4]:.3f}, format={r[5]:.3f}, length={r[6]:.3f}, mdi_add={r[7]:.3f}, mdi={true_mdi:.3f}, total={r[8]:.3f}\n\n")
                    
                    # 详细 metrics
                    if info:
                        f.write("**Detailed Metrics:**\n\n")
                        f.write("```json\n")
                        detailed_metrics = {
                            "rewards": {
                                "accuracy": float(r[4]),
                                "format": float(r[5]),
                                "length": float(r[6]),
                                "mdi": float(r[7]),
                                "total": float(r[8])
                            },
                            "attention_metrics": {
                                "early": {
                                    "mdi": info.get("early_mdi"),
                                    "aei_text": info.get("early_aei_text"),
                                    "aei_vision": info.get("early_aei_vision"),
                                    "text_ratio": info.get("early_text_ratio"),
                                    "vision_ratio": info.get("early_vision_ratio")
                                },
                                "middle": {
                                    "mdi": info.get("middle_mdi"),
                                    "aei_text": info.get("middle_aei_text"),
                                    "aei_vision": info.get("middle_aei_vision"),
                                    "text_ratio": info.get("middle_text_ratio"),
                                    "vision_ratio": info.get("middle_vision_ratio")
                                },
                                "late": {
                                    "mdi": info.get("late_mdi"),
                                    "aei_text": info.get("late_aei_text"),
                                    "aei_vision": info.get("late_aei_vision"),
                                    "text_ratio": info.get("late_text_ratio"),
                                    "vision_ratio": info.get("late_vision_ratio")
                                },
                                "all": {
                                    "mdi": info.get("all_mdi"),
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
                "eval_mdi": metrics.get("eval_mdi", 0.0),
            }
            
            for key, value in core_metrics.items():
                if value is not None:
                    f.write(f"| {key} | {value:.4f} |\n")
            
            # 注意力指标
            attention_metrics = {
                "eval_attention/early/mdi": logs.get("eval_attention/early/mdi"),
                "eval_attention/middle/mdi": logs.get("eval_attention/middle/mdi"),
                "eval_attention/late/mdi": logs.get("eval_attention/late/mdi"),
                "eval_attention/all/mdi": logs.get("eval_attention/all/mdi"),
            }
            
            if any(v is not None for v in attention_metrics.values()):
                f.write("\n### Attention Statistics\n\n")
                f.write("| Stage | MDI | AEI Text | AEI Vision |\n")
                f.write("|-------|-----|----------|------------|\n")
                
                stages = ["early", "middle", "late", "all"]
                for stage in stages:
                    mdi_key = f"eval_attention/{stage}/mdi"
                    aei_text_key = f"eval_attention/{stage}/aei_text"
                    aei_vision_key = f"eval_attention/{stage}/aei_vision"
                    
                    mdi_val = logs.get(mdi_key, 0.0)
                    aei_text_val = logs.get(aei_text_key, 0.0)
                    aei_vision_val = logs.get(aei_vision_key, 0.0)
                    
                    f.write(f"| {stage.title()} | {mdi_val:.3f} | {aei_text_val:.3f} | {aei_vision_val:.3f} |\n")
            
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


def compute_real_mdi_metrics(
    sample_results: List[Any],
    skip_reasons: Optional[List[Optional[str]]] = None,
) -> List[Dict[str, Any]]:
    """
    计算真实的 MDI 指标用于日志记录
    
    Args:
        sample_results: 注意力样本结果列表
        skip_reasons: 跳过原因列表
        
    Returns:
        MDI 指标字典列表
    """
    results = []
    if skip_reasons is None:
        skip_reasons = [None] * len(sample_results)

    for idx, res in enumerate(sample_results):
        if res is None:
            reason = skip_reasons[idx] if idx < len(skip_reasons) else None
            default_result = {
                "mdi": 1.0,
                "text_ratio": 0.5,
                "vision_ratio": 0.5,
                "attention_distribution": [0.5, 0.5],
                "num_vision_tokens": 0,
                "num_text_tokens": 0,
                "attention_text": 0.0,
                "attention_vision": 0.0,
                "early_mdi": 1.0,
                "middle_mdi": 1.0,
                "late_mdi": 1.0,
                "all_mdi": 1.0,
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
            if segment is None or not hasattr(segment, "mdi") or segment.mdi is None:
                return {
                    "mdi": 1.0,
                    "aei_text": 0.0,
                    "aei_vision": 0.0,
                    "attention_text": 0.0,
                    "attention_vision": 0.0,
                    "text_ratio": 0.5,
                    "vision_ratio": 0.5,
                }

            mdi = float(segment.mdi)
            if not (mdi > 0) or not math.isfinite(mdi):
                return {
                    "mdi": 1.0,
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
            text_ratio = mdi / (1.0 + mdi)
            vision_ratio = 1.0 / (1.0 + mdi)

            return {
                "mdi": round(float(mdi), 6),
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

        # 修复MDI选择逻辑：优先使用late段，如果无效则使用all段
        if late_data["mdi"] != 1.0:
            main_segment = late_data
        else:
            main_segment = all_data
        mdi = main_segment["mdi"]

        text_ratio = mdi / (1.0 + mdi)
        vision_ratio = 1.0 / (1.0 + mdi)

        result = {
            "mdi": round(float(mdi), 6),
            "text_ratio": round(float(text_ratio), 6),
            "vision_ratio": round(float(vision_ratio), 6),
            "attention_distribution": [text_ratio, vision_ratio],
            "num_vision_tokens": int(num_vision_tokens),
            "num_text_tokens": int(num_text_tokens),
            # Use late segment's attention values, fallback to all segment
            "attention_text": main_segment["attention_text"],
            "attention_vision": main_segment["attention_vision"],
            "early_mdi": early_data["mdi"],
            "middle_mdi": middle_data["mdi"],
            "late_mdi": late_data["mdi"],
            "all_mdi": all_data["mdi"],
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
