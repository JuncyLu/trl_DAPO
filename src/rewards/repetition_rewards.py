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

from typing import Any, List


def _collect_text(node: Any) -> list[str]:
    """递归收集文本内容"""
    if isinstance(node, str):
        return [node]
    if isinstance(node, dict):
        texts = []
        if "text" in node and isinstance(node["text"], str):
            texts.append(node["text"])
        if "content" in node:
            texts.extend(_collect_text(node["content"]))
        return texts
    if isinstance(node, list):
        return sum([_collect_text(item) for item in node], [])
    return [str(node)]


def _zipngram(text: str, ngram_size: int):
    """提取 n-gram"""
    words = text.lower().split()
    if len(words) < ngram_size:
        return []
    return list(zip(*[words[i:] for i in range(ngram_size)]))


def repetition_reward(
    completions: List[Any], 
    repetition_n_grams: int = 3, 
    repetition_max_penalty: float = -1.0,
    **kwargs
) -> List[float]:
    """
    惩罚模型生成文本中的重复内容。
    参考：https://arxiv.org/abs/2502.03373
    
    通过检测生成文本中的重复 n-gram 模式来评估重复程度，并给予相应的惩罚。
    
    Args:
        completions: List of model completions
        repetition_n_grams: n-gram 大小，默认为 3
        repetition_max_penalty: 最大惩罚值，默认为 -1.0
        
    Returns:
        List[float]: 奖励值列表，范围 [repetition_max_penalty, 0.0]
    """
    rewards = []
    
    # 从 kwargs 中获取参数（如果有的话）
    n_grams = kwargs.get("repetition_n_grams", repetition_n_grams)
    max_penalty = kwargs.get("repetition_max_penalty", repetition_max_penalty)
    
    for completion in completions:
        # 提取文本内容
        parts = _collect_text(completion)
        content = " ".join(parts).strip()
        
        # 空文本或过短文本不惩罚
        if not content or len(content.split()) < n_grams:
            rewards.append(0.0)
            continue
        
        try:
            # 提取 n-grams
            ngrams_list = _zipngram(content, n_grams)
            
            if not ngrams_list:
                rewards.append(0.0)
                continue
            
            # 计算唯一 n-gram 比例
            ngrams_set = set(ngrams_list)
            total = len(ngrams_list)
            unique = len(ngrams_set)
            
            # 重复率：1 - (唯一数 / 总数)
            # 完全不重复时 scaling = 0，完全重复时 scaling = 1
            scaling = 1 - unique / total
            
            # 计算惩罚：scaling 越大（重复越多），惩罚越大（reward 越负）
            reward = scaling * max_penalty
            rewards.append(float(reward))
            
        except Exception:
            # 异常情况返回 0
            rewards.append(0.0)
    
    return rewards

