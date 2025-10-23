# Copyright 2020-2025 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import math
from typing import List, Optional


def mdi_reward_legacy(completions: List[List[dict]], **kwargs) -> List[float]:
    """
    MDI 系数版（与 accuracy 相乘）- 旧版本备份：
      - 仅使用原始注意力参数：A_T, A_O, |T|, |O|
      - MDI 公式保持不变：MDI = (A_T/|T|) / (A_O/|O|)
      - 将 MDI 映射为分段线性系数 c ∈ [0.40, 1.00]（区间内线性插值，避免突变）
      - 返回系数列表，与 completions 等长
    需要 kwargs:
      - attention_text: List[float]   # A_T（所有输出 token 对文本 token 的总注意力）
      - attention_vision: List[float] # A_O（所有输出 token 对非文本 token 的总注意力）
      - num_text_tokens: List[int]    # |T|
      - num_vision_tokens: List[int]  # |O|
    外层聚合建议：
      R_i = (4.0 * acc[i]) * c[i] + 1.0 * format[i]
    """
    n = len(completions) if isinstance(completions, list) else 0
    if n == 0:
        return []

    A_T = kwargs.get("attention_text", [])
    A_O = kwargs.get("attention_vision", [])
    N_T = kwargs.get("num_text_tokens", [])
    N_O = kwargs.get("num_vision_tokens", [])

    # 基本校验
    if not (isinstance(A_T, list) and isinstance(A_O, list) and isinstance(N_T, list) and isinstance(N_O, list)):
        return [0.40] * n

    m = min(len(A_T), len(A_O), len(N_T), len(N_O), n)
    if m == 0:
        return [0.40] * n

    eps = 1e-6
    coefs: List[float] = []

    # 分段线性映射（根据 rollout 中的 MDI 分布定标）：
    #   区间        -> 系数范围（线性插值）
    #   MDI <= 5    -> 1.00
    #   5–10        -> 1.00 -> 0.95
    #   10–20       -> 0.95 -> 0.80
    #   20–30       -> 0.80 -> 0.70
    #   30–40       -> 0.70 -> 0.55
    #   40–60       -> 0.55 -> 0.40
    #   > 60        -> 0.40
    def map_mdi_to_coef(x: float) -> float:
        if x <= 5.0:
            return 1.00
        elif x <= 10.0:
            # [5,10] -> [1.00,0.95]
            return 1.00 - (x - 5.0) * (1.00 - 0.95) / 5.0
        elif x <= 20.0:
            # [10,20] -> [0.95,0.80]
            return 0.95 - (x - 10.0) * (0.95 - 0.80) / 10.0
        elif x <= 30.0:
            # [20,30] -> [0.80,0.70]
            return 0.80 - (x - 20.0) * (0.80 - 0.70) / 10.0
        elif x <= 40.0:
            # [30,40] -> [0.70,0.55]
            return 0.70 - (x - 30.0) * (0.70 - 0.55) / 10.0
        elif x <= 60.0:
            # [40,60] -> [0.55,0.40]
            return 0.55 - (x - 40.0) * (0.55 - 0.40) / 20.0
        else:
            return 0.40

    for i in range(m):
        try:
            a_t = float(A_T[i]); a_o = float(A_O[i])
            t   = int(N_T[i]);   o   = int(N_O[i])

            # 计算 MDI（保持原公式；加极小值防 0）
            text_density   = a_t / max(1, t)
            vision_density = a_o / max(1, o)
            mdi = text_density / max(vision_density, eps)

            # 分段线性映射到系数
            c = map_mdi_to_coef(mdi)

            # 安全裁剪
            if c < 0.40: c = 0.40
            if c > 1.00: c = 1.00
            coefs.append(float(c))
        except Exception:
            coefs.append(0.40)

    # 对齐长度
    if len(coefs) < n:
        coefs.extend([0.40] * (n - len(coefs)))
    elif len(coefs) > n:
        coefs = coefs[:n]

    return coefs


def aei_reward(completions: List[List[dict]], modality: str = "text", **kwargs) -> List[float]:
    """
    基于AEI (Attention Efficiency Index) 计算奖励。
    
    Args:
        completions (`List[List[dict]]`):
            List of completions to be evaluated.
        modality (`str`):
            Modality to compute AEI for. Must be "text" or "vision".
        **kwargs:
            Additional keyword arguments. Must include 'trainer' key for AEI scores.
            
    Returns:
        `List[float]`:
            A list of rewards based on AEI scores.
    """
    if modality not in {"text", "vision"}:
        raise ValueError("modality must be 'text' or 'vision'")
    
    trainer = kwargs.get("trainer")
    if trainer is None:
        return [0.0] * len(completions)
    
    # Get AEI scores from trainer metrics
    aei_scores = getattr(trainer, f"_aei_{modality}_scores_current_batch", None)
    if not aei_scores:
        return [0.0] * len(completions)
    
    try:
        aei_scores = list(aei_scores)
    except TypeError:
        aei_scores = [aei_scores]
    
    if len(aei_scores) < len(completions):
        repeats = (len(completions) + len(aei_scores) - 1) // len(aei_scores)
        aei_scores = (aei_scores * repeats)[: len(completions)]
    elif len(aei_scores) > len(completions):
        aei_scores = aei_scores[: len(completions)]
    
    # Simple reward: normalize AEI score to [0, 1] range
    rewards = []
    for score in aei_scores:
        try:
            # Normalize AEI score (assuming typical range 0-2, normalize to 0-1)
            normalized = min(1.0, max(0.0, float(score) / 2.0))
            rewards.append(normalized)
        except Exception:
            rewards.append(0.0)
    
    return rewards


def mdi_reward(completions: List[List[dict]], **kwargs) -> List[float]:
    """
    新版MDI奖励函数，使用新公式和系数表：
      - 新MDI公式：MDI = exp(-|log(A_T/|T| / A_O/|O|) + ε|)
      - 其中 ε = ln(2) ≈ 0.693
      - 使用新的系数表映射MDI值到奖励系数
    需要 kwargs:
      - attention_text: List[float]   # A_T（所有输出 token 对文本 token 的总注意力）
      - attention_vision: List[float] # A_O（所有输出 token 对非文本 token 的总注意力）
      - num_text_tokens: List[int]    # |T|
      - num_vision_tokens: List[int]  # |O|
    """
    n = len(completions) if isinstance(completions, list) else 0
    if n == 0:
        return []

    A_T = kwargs.get("attention_text", [])
    A_O = kwargs.get("attention_vision", [])
    N_T = kwargs.get("num_text_tokens", [])
    N_O = kwargs.get("num_vision_tokens", [])

    # 基本校验
    if not (isinstance(A_T, list) and isinstance(A_O, list) and isinstance(N_T, list) and isinstance(N_O, list)):
        return [0.40] * n

    m = min(len(A_T), len(A_O), len(N_T), len(N_O), n)
    if m == 0:
        return [0.40] * n

    eps = 1e-6
    epsilon = math.log(0.5)  # ln(0.5) ≈ -0.693
    coefs: List[float] = []

    # 新系数表映射函数
    def map_mdi_to_coef(mdi_value: float) -> float:
        """
        根据新的系数表映射MDI值到系数：
        MDI 范围        系数    说明
        ≥ 0.95         1.00    最佳平衡
        0.90 – 0.95    0.97    轻微惩罚
        0.80 – 0.90    0.90    中等偏轻
        0.70 – 0.80    0.80    中等惩罚
        0.60 – 0.70    0.70    较强惩罚
        0.45 – 0.60    0.55    强惩罚
        < 0.45         0.40    最强惩罚（下限）
        """
        if mdi_value >= 0.95:
            return 1.00
        elif mdi_value >= 0.90:
            # [0.90, 0.95] -> [0.97, 1.00]
            return 0.97 + (mdi_value - 0.90) * (1.00 - 0.97) / (0.95 - 0.90)
        elif mdi_value >= 0.80:
            # [0.80, 0.90] -> [0.90, 0.97]
            return 0.90 + (mdi_value - 0.80) * (0.97 - 0.90) / (0.90 - 0.80)
        elif mdi_value >= 0.70:
            # [0.70, 0.80] -> [0.80, 0.90]
            return 0.80 + (mdi_value - 0.70) * (0.90 - 0.80) / (0.80 - 0.70)
        elif mdi_value >= 0.60:
            # [0.60, 0.70] -> [0.70, 0.80]
            return 0.70 + (mdi_value - 0.60) * (0.80 - 0.70) / (0.70 - 0.60)
        elif mdi_value >= 0.45:
            # [0.45, 0.60] -> [0.55, 0.70]
            return 0.55 + (mdi_value - 0.45) * (0.70 - 0.55) / (0.60 - 0.45)
        else:
            return 0.40

    for i in range(m):
        try:
            a_t = float(A_T[i])
            a_o = float(A_O[i])
            t = int(N_T[i])
            o = int(N_O[i])

            # 计算新的MDI公式：MDI = exp(-|log(A_T/|T| / A_O/|O|) + ε|)
            if t <= 0 or o <= 0:
                coefs.append(0.40)
                continue
                
            text_density = a_t / t
            vision_density = a_o / o
            
            if vision_density <= eps:
                coefs.append(0.40)
                continue
                
            # 计算 log(A_T/|T| / A_O/|O|) + ε
            log_ratio = math.log(text_density / vision_density)
            mdi = math.exp(-abs(log_ratio + epsilon))

            # 映射到系数
            c = map_mdi_to_coef(mdi)

            # 安全裁剪
            c = max(0.40, min(1.00, c))
            coefs.append(float(c))
            
        except Exception:
            coefs.append(0.40)

    # 对齐长度
    if len(coefs) < n:
        coefs.extend([0.40] * (n - len(coefs)))
    elif len(coefs) > n:
        coefs = coefs[:n]

    return coefs
