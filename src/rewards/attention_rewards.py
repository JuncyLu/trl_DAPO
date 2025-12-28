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


def vgr_reward(completions: List[List[dict]], **kwargs) -> List[float]:
    """
    基于组内MAD标准化的 VGR (Vision-Text Gain Ratio) 奖励函数。
    - VGR 越小表示注意力越平衡，映射到更高的奖励
    - 在同一 prompt 的多次采样内使用 MAD (Median Absolute Deviation) 标准化
    - 使用 tanh 函数映射到 [-0.5, 0.5] 范围
    - MAD 不足时返回中性奖励 0.0
    
    需要 kwargs:
      - attention_text: List[float]   # A_T（按层与生成长度归一后的：每个输出 token 对文本 token 的平均注意力）
      - attention_vision: List[float] # A_O（按层与生成长度归一后的：每个输出 token 对非文本 token 的平均注意力）
      - num_text_tokens: List[int]    # |T|
      - num_vision_tokens: List[int]  # |O|
      - num_generations: int          # 每个 prompt 的采样数
      - vgr_sigma: float              # tanh 的缩放因子，默认 1.0
    """
    import numpy as np
    
    n = len(completions)
    if n == 0:
        return []
    
    # 从 kwargs 获取注意力数据和分组信息
    A_T = kwargs.get("attention_text", [])
    A_O = kwargs.get("attention_vision", [])
    N_T = kwargs.get("num_text_tokens", [])
    N_O = kwargs.get("num_vision_tokens", [])
    num_generations = kwargs.get("num_generations", 1)
    sigma = kwargs.get("vgr_sigma", 1.0)  # 默认 sigma=1.0
    
    # 数据验证
    if not all([isinstance(x, list) for x in [A_T, A_O, N_T, N_O]]):
        return [0.0] * n
    
    m = min(len(A_T), len(A_O), len(N_T), len(N_O), n)
    if m == 0:
        return [0.0] * n
    
    # 计算每个样本的 VGR 值
    eps = 1e-8
    vgr_values = []
    for i in range(m):
        try:
            a_t, a_o = float(A_T[i]), float(A_O[i])
            t, o = int(N_T[i]), int(N_O[i])
            
            if t <= 0 or o <= 0:
                vgr_values.append(None)
                continue
            
            text_density = a_t / t
            vision_density = a_o / o
            
            if vision_density <= eps:
                vgr_values.append(None)
                continue
            
            vgr = text_density / vision_density
            vgr_values.append(vgr)
        except Exception:
            vgr_values.append(None)
    
    # 按 num_generations 分组
    if num_generations <= 1:
        # 单采样，直接返回 0.0
        return [0.0] * n
    
    num_groups = m // num_generations
    rewards = []
    
    for group_idx in range(num_groups):
        start_idx = group_idx * num_generations
        end_idx = start_idx + num_generations
        group_vgrs = vgr_values[start_idx:end_idx]
        
        # 过滤掉 None 值
        valid_vgrs = [x for x in group_vgrs if x is not None]
        group_size = len(valid_vgrs)
        
        # 样本太少，无法稳定估计
        if group_size < 2:
            rewards.extend([0.0] * len(group_vgrs))
            continue
        
        # 计算 Median 和 MAD
        valid_vgrs_array = np.array(valid_vgrs)
        median_v = np.median(valid_vgrs_array)
        mad = np.median(np.abs(valid_vgrs_array - median_v))
        
        # MAD 过小，说明组内变异不足
        if mad < eps:
            rewards.extend([0.0] * len(group_vgrs))
            continue
        
        # 使用 MAD 标准化 + tanh 映射
        # z = (median - vgr) / (1.4826 * MAD)  # VGR 越小 -> z 越大 -> reward 越高
        # reward = 0.5 * tanh(z / sigma)  # 映射到 [-0.5, 0.5]
        for vgr in group_vgrs:
            if vgr is None:
                rewards.append(0.0)
            else:
                z = (median_v - vgr) / (1.4826 * mad + eps)
                reward = 0.5 * np.tanh(z / sigma)
                # clip 到 [-0.5, 0.5]
                reward = float(np.clip(reward, -0.5, 0.5))
                rewards.append(reward)
    
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


def vgr_hard_negative(completions: List[List[dict]], **kwargs) -> List[float]:
    """
    基于组内MAD标准化的 VGR 奖惩（Hard Negative版本）：
    - 组内 MAD 映射基于「所有样本」的 VGR（与 vgr_reward 一致）
    - 但最终只对 acc=1 的样本应用该映射，acc=0 的样本返回 0（中性）
    - 使用 tanh 函数映射到 [-0.5, 0.5] 范围作为奖惩值
    - 如果组内只有一个正确样本，返回 0（中性）

    需要 kwargs:
      - attention_text: List[float]
      - attention_vision: List[float]
      - num_text_tokens: List[int]
      - num_vision_tokens: List[int]
      - num_generations: int
      - accuracies: List[float]  # 每个样本的准确率（0.0 或 1.0），与 completions 对齐
      - vgr_sigma: float         # tanh 的缩放因子，默认 1.0
    """
    import numpy as np
    
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
    sigma = kwargs.get("vgr_sigma", 1.0)  # 默认 sigma=1.0

    # 数据验证
    if not all([isinstance(x, list) for x in [A_T, A_O, N_T, N_O]]):
        return [0.0] * n
    if accuracies is None or not isinstance(accuracies, list) or len(accuracies) < n:
        # 缺少准确率信息则无法区分奖惩对象，统一返回中性 0
        return [0.0] * n

    m = min(len(A_T), len(A_O), len(N_T), len(N_O), n)
    if m == 0:
        return [0.0] * n

    # 计算每个样本的 VGR 值
    eps = 1e-8
    vgr_values: List[float] = []
    for i in range(m):
        try:
            a_t, a_o = float(A_T[i]), float(A_O[i])
            t, o = int(N_T[i]), int(N_O[i])

            if t <= 0 or o <= 0:
                vgr_values.append(None)  # type: ignore
                continue

            text_density = a_t / t
            vision_density = a_o / o

            if vision_density <= eps:
                vgr_values.append(None)  # type: ignore
                continue

            vgr = text_density / vision_density
            vgr_values.append(vgr)
        except Exception:
            vgr_values.append(None)  # type: ignore

    # 按 num_generations 分组
    if num_generations <= 1:
        # 单采样无法进行稳定的组内归一化，全部返回中性 0
        return [0.0] * n

    num_groups = m // num_generations
    rewards: List[float] = []

    for group_idx in range(num_groups):
        start_idx = group_idx * num_generations
        end_idx = start_idx + num_generations
        group_vgrs = vgr_values[start_idx:end_idx]
        group_accs = accuracies[start_idx:end_idx]

        # 先基于「所有样本的有效 VGR」做统计
        valid_vgrs_all = [x for x in group_vgrs if x is not None]
        group_size_all = len(valid_vgrs_all)

        group_rewards = [0.0] * len(group_vgrs)  # 默认中性 0

        # 样本太少，无法稳定估计
        if group_size_all < 2:
            rewards.extend(group_rewards)
            continue

        # 计算 Median 和 MAD
        valid_vgrs_array = np.array(valid_vgrs_all)
        median_v = np.median(valid_vgrs_array)
        mad = np.median(np.abs(valid_vgrs_array - median_v))

        # MAD 过小，说明组内变异不足
        if mad < eps:
            rewards.extend(group_rewards)
            continue

        # 统计组内正确样本数量
        acc1_count = sum(1 for x in group_accs if float(x) == 1.0)
        
        # 如果组内只有一个或没有正确样本，全部返回 0
        if acc1_count < 2:
            rewards.extend(group_rewards)
            continue

        # 使用 MAD 标准化 + tanh 映射（与 vgr_reward 一致的逻辑）
        # z = (median - vgr) / (1.4826 * MAD)  # VGR 越小 -> z 越大 -> reward 越高
        # reward = 0.5 * tanh(z / sigma)  # 映射到 [-0.5, 0.5]
        # 但只对 acc=1 的样本应用，acc=0 的样本保持 0
        for j, (vgr, acc) in enumerate(zip(group_vgrs, group_accs)):
            if float(acc) == 1.0:
                if vgr is None:
                    group_rewards[j] = 0.0
                else:
                    z = (median_v - vgr) / (1.4826 * mad + eps)
                    reward = 0.5 * np.tanh(z / sigma)
                    # clip 到 [-0.5, 0.5]
                    reward = float(np.clip(reward, -0.5, 0.5))
                    group_rewards[j] = reward
            else:
                # acc=0 的样本保持 0
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
