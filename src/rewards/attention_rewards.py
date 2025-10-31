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

from typing import List


def mdi_reward(completions: List[List[dict]], **kwargs) -> List[float]:
    """
    基于组内分位数归一化的 MDI 奖励函数。
    - MDI 越小表示注意力越平衡，映射到更高的奖励
    - 在同一 prompt 的多次采样内进行分位数归一化
    - 分位差不足时返回中性奖励 0.5
    
    需要 kwargs:
      - attention_text: List[float]   # A_T（所有输出 token 对文本 token 的总注意力）
      - attention_vision: List[float] # A_O（所有输出 token 对非文本 token 的总注意力）
      - num_text_tokens: List[int]    # |T|
      - num_vision_tokens: List[int]  # |O|
      - num_generations: int          # 每个 prompt 的采样数
    """
    n = len(completions)
    if n == 0:
        return []
    
    # 从 kwargs 获取注意力数据和分组信息
    A_T = kwargs.get("attention_text", [])
    A_O = kwargs.get("attention_vision", [])
    N_T = kwargs.get("num_text_tokens", [])
    N_O = kwargs.get("num_vision_tokens", [])
    num_generations = kwargs.get("num_generations", 1)
    
    # 数据验证
    if not all([isinstance(x, list) for x in [A_T, A_O, N_T, N_O]]):
        return [0.5] * n
    
    m = min(len(A_T), len(A_O), len(N_T), len(N_O), n)
    if m == 0:
        return [0.5] * n
    
    # 计算每个样本的 MDI 值
    eps = 1e-6
    mdi_values = []
    for i in range(m):
        try:
            a_t, a_o = float(A_T[i]), float(A_O[i])
            t, o = int(N_T[i]), int(N_O[i])
            
            if t <= 0 or o <= 0:
                mdi_values.append(None)
                continue
            
            text_density = a_t / t
            vision_density = a_o / o
            
            if vision_density <= eps:
                mdi_values.append(None)
                continue
            
            mdi = text_density / vision_density
            mdi_values.append(mdi)
        except Exception:
            mdi_values.append(None)
    
    # 按 num_generations 分组
    if num_generations <= 1:
        # 单采样，直接返回 0.5
        return [0.5] * n
    
    num_groups = m // num_generations
    rewards = []
    
    alpha_abs = 5.0  # 绝对阈值
    beta_rel = 0.10  # 相对阈值 10%
    
    for group_idx in range(num_groups):
        start_idx = group_idx * num_generations
        end_idx = start_idx + num_generations
        group_mdis = mdi_values[start_idx:end_idx]
        
        # 过滤掉 None 值
        valid_mdis = [x for x in group_mdis if x is not None]
        group_size = len(valid_mdis)
        
        # 判断分位差是否充足
        if group_size < 3:
            # 样本太少，返回 0.5
            rewards.extend([0.5] * len(group_mdis))
            continue
        
        # 计算 IQR 和中位数，确定分位数位置
        sorted_mdis = sorted(valid_mdis)
        
        if group_size < 10:
            # 样本少，用 Q75-Q25
            q_lo_idx = int(group_size * 0.25)
            q_hi_idx = int(group_size * 0.75)
        else:
            # 样本多，用 Q90-Q10
            q_lo_idx = int(group_size * 0.10)
            q_hi_idx = int(group_size * 0.90)
        
        q_lo = sorted_mdis[q_lo_idx]
        q_hi = sorted_mdis[q_hi_idx]
        iqr = q_hi - q_lo
        median = sorted_mdis[group_size // 2]
        
        # 判断分位差是否充足
        threshold = max(alpha_abs, beta_rel * median)
        if iqr < threshold:
            # 分位差不足
            rewards.extend([0.5] * len(group_mdis))
            continue
        
        # 分位差充足，使用分位数进行归一化
        # 检查分母是否过小（兜底保护）
        if iqr <= eps:
            # 即使通过了阈值判定，分母仍可能为0，统一返回0.5
            rewards.extend([0.5] * len(group_mdis))
            continue
        
        # 使用分位数映射：s = clip((Q_hi - MDI) / (Q_hi - Q_lo), 0, 1)
        # MDI 越小 -> (Q_hi - MDI) 越大 -> s 越大（奖励越高）
        for mdi in group_mdis:
            if mdi is None:
                rewards.append(0.5)
            else:
                normalized = (q_hi - mdi) / iqr
                # clip 到 [0, 1]
                normalized = max(0.0, min(1.0, normalized))
                rewards.append(float(normalized))
    
    # 处理剩余样本（不足一组的）
    remaining = m % num_generations
    if remaining > 0:
        rewards.extend([0.5] * remaining)
    
    # 对齐长度
    if len(rewards) < n:
        rewards.extend([0.5] * (n - len(rewards)))
    elif len(rewards) > n:
        rewards = rewards[:n]
    
    return rewards


def mdi_hard_negative(completions: List[List[dict]], **kwargs) -> List[float]:
    """
    基于组内分位数归一化的 MDI 奖惩（第二版）：
    - 组内分位数映射仍基于「所有样本」的 MDI（与 mdi_reward 一致）
    - 但最终只对 acc=1 的样本应用该映射，acc=0 的样本返回 0（中性）
    - 将 [0, 1] 线性平移为 [-0.5, 0.5] 作为奖惩值

    需要 kwargs:
      - attention_text: List[float]
      - attention_vision: List[float]
      - num_text_tokens: List[int]
      - num_vision_tokens: List[int]
      - num_generations: int
      - accuracies: List[float]  # 每个样本的准确率（0.0 或 1.0），与 completions 对齐
    """
    n = len(completions)
    if n == 0:
        return []

    # 从 kwargs 获取注意力数据和分组信息
    A_T = kwargs.get("attention_text", [])
    A_O = kwargs.get("attention_vision", [])
    N_T = kwargs.get("num_text_tokens", [])
    N_O = kwargs.get("num_vision_tokens", [])
    num_generations = kwargs.get("num_generations", 1)
    accuracies = kwargs.get("accuracies", None)

    # 数据验证
    if not all([isinstance(x, list) for x in [A_T, A_O, N_T, N_O]]):
        return [0.0] * n
    if accuracies is None or not isinstance(accuracies, list) or len(accuracies) < n:
        # 缺少准确率信息则无法区分奖惩对象，统一返回中性 0
        return [0.0] * n

    m = min(len(A_T), len(A_O), len(N_T), len(N_O), n)
    if m == 0:
        return [0.0] * n

    # 计算每个样本的 MDI 值
    eps = 1e-6
    mdi_values: List[float] = []
    for i in range(m):
        try:
            a_t, a_o = float(A_T[i]), float(A_O[i])
            t, o = int(N_T[i]), int(N_O[i])

            if t <= 0 or o <= 0:
                mdi_values.append(None)  # type: ignore
                continue

            text_density = a_t / t
            vision_density = a_o / o

            if vision_density <= eps:
                mdi_values.append(None)  # type: ignore
                continue

            mdi = text_density / vision_density
            mdi_values.append(mdi)
        except Exception:
            mdi_values.append(None)  # type: ignore

    # 按 num_generations 分组
    if num_generations <= 1:
        # 单采样无法进行稳定的组内归一化，全部返回中性 0
        return [0.0] * n

    num_groups = m // num_generations
    rewards: List[float] = []

    alpha_abs = 5.0  # 绝对阈值
    beta_rel = 0.10  # 相对阈值 10%

    for group_idx in range(num_groups):
        start_idx = group_idx * num_generations
        end_idx = start_idx + num_generations
        group_mdis = mdi_values[start_idx:end_idx]
        group_accs = accuracies[start_idx:end_idx]

        # 先基于「所有样本的有效 MDI」做分位统计
        valid_mdis_all = [x for x in group_mdis if x is not None]
        group_size_all = len(valid_mdis_all)

        group_rewards = [0.0] * len(group_mdis)  # 默认中性 0

        if group_size_all < 3:
            # 样本太少，无法稳定分位归一化：acc=1 也返回 0；acc=0 本就为 0
            rewards.extend(group_rewards)
            continue

        sorted_mdis = sorted(valid_mdis_all)
        if group_size_all < 10:
            q_lo_idx = int(group_size_all * 0.25)
            q_hi_idx = int(group_size_all * 0.75)
        else:
            q_lo_idx = int(group_size_all * 0.10)
            q_hi_idx = int(group_size_all * 0.90)

        q_lo = sorted_mdis[q_lo_idx]
        q_hi = sorted_mdis[q_hi_idx]
        iqr = q_hi - q_lo
        median = sorted_mdis[group_size_all // 2]

        threshold = max(alpha_abs, beta_rel * median)
        if iqr < threshold or iqr <= eps:
            # 分位差不足或分母过小：acc=1 返回 0；acc=0 仍为 0
            rewards.extend(group_rewards)
            continue

        # 组内对所有样本先计算映射值（基于所有样本的 MDI），但只赋给 acc=1
        mapped_values = []
        for mdi in group_mdis:
            if mdi is None:
                mapped_values.append(None)
            else:
                normalized = (q_hi - mdi) / iqr  # 映射到 [0, 1]
                normalized = max(0.0, min(1.0, float(normalized)))
                mapped = normalized - 0.5  # 平移到 [-0.5, 0.5]
                # clip 到 [-0.5, 0.5]
                mapped_values.append(max(-0.5, min(0.5, mapped)))

        # 如果组内仅有一个 acc=1，按约定该样本返回 0（中性）
        acc1_count = sum(1 for x in group_accs if float(x) == 1.0)

        for j, (acc, mapped) in enumerate(zip(group_accs, mapped_values)):
            if float(acc) == 1.0:
                if acc1_count >= 2 and mapped is not None:
                    group_rewards[j] = float(mapped)
                else:
                    group_rewards[j] = 0.0
            else:
                group_rewards[j] = 0.0

        rewards.extend(group_rewards)

    # 处理剩余样本（不足一组的）
    remaining = m % num_generations
    if remaining > 0:
        rewards.extend([0.0] * remaining)

    # 对齐长度
    if len(rewards) < n:
        rewards.extend([0.0] * (n - len(rewards)))
    elif len(rewards) > n:
        rewards = rewards[:n]

    return rewards
