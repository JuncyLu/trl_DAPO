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

import re

# 软格式奖励的辅助正则表达式
ALLOWED_NOISE = re.compile(r'^[\s:.,;!?\"\'\-\(\)\[\]_]*$')
BAD_PATTERNS = [
    re.compile(r'</think>{2,}', re.I),   # 多重关闭
    re.compile(r'[-_=]{4,}'),            # 连续符号风暴
]

FORMAT_FULL = re.compile(
    r'(?s)^\s*<think>(?P<thought>.*?)</think>\s*Answer\s*:\s*(?P<ans>[A-J])\s*$'
)


def think_format_reward(completions: list[list[dict[str, str]]], **kwargs) -> list[float]:
    r"""
    Reward function that checks if the reasoning process is enclosed within exactly one pair of `<think>` and `</think>` tags.
    The function returns a reward of 1.0 if the format is correct, otherwise 0.0.
    
    Strict constraints:
    - Must contain exactly one pair of <think></think> tags
    - No other XML-like tags allowed (e.g., <html>, <answer>, etc.)
    - No nested or multiple <think> tags allowed

    Args:
        completions (`list[list[dict[str, str]]]`):
            List of completions to be evaluated. Each completion must be a list of one message, i.e. a dictionary
            containing the key `"content"` with the value being the text of the completion.
        **kwargs:
            Additional keyword arguments. This function does not use them, but they are required in the function
            signature to ensure compatibility with trainers like [`GRPOTrainer`].

    Returns:
        `list[float]`:
            A list of rewards, where each reward is 1.0 if the completion matches the expected format, otherwise 0.0.

    Example:
    ```python
    >>> from trl.rewards import think_format_reward

    >>> completions = [
    ...     [{"content": "<think>\nThis is my reasoning.\n</think>\nThis is my answer."}],
    ...     [{"content": "<think>\nThis is my reasoning.\nThis is my answer."}],
    ...     [{"content": "<think><think>nested</think></think>"}],
    ...     [{"content": "<html><think>reasoning</think></html>"}],
    ... ]
    >>> think_format_reward(completions)
    [1.0, 0.0, 0.0, 0.0]
    ```
    """
    def check_format(content: str) -> bool:
        # Check for exactly one pair of <think></think> tags
        think_open_count = content.count('<think>')
        think_close_count = content.count('</think>')
        
        if think_open_count != 1 or think_close_count != 1:
            return False
        
        # Check for other XML-like tags (case insensitive)
        # Find all XML tags and check if any are not the allowed ones
        all_tags = re.findall(r'<[^>]+>', content)
        allowed_tags = ['<think>', '</think>']
        for tag in all_tags:
            if tag.lower() not in [t.lower() for t in allowed_tags]:
                return False
        
        # Check for proper nesting - no nested <think> tags
        pattern = r'^<think>(?!.*<think>)(.*?)</think>.*$'
        return bool(re.match(pattern, content, re.DOTALL | re.MULTILINE))
    
    completion_contents = [completion[0]["content"] for completion in completions]
    return [1.0 if check_format(content) else 0.0 for content in completion_contents]


def soft_think_format_reward(text: str) -> float:
    """
    可塑 + 反作弊的格式奖励函数
    
    Args:
        text: 要评估的文本内容
        
    Returns:
        float: 0.0-1.0之间的格式奖励分数
    """
    text = (text or "").strip()
    score = 0.0

    # 反作弊先扣分
    penalty = 0.0
    for pat in BAD_PATTERNS:
        if pat.search(text):
            penalty -= 0.25   # 可调，最多叠到 -0.75

    # 完整匹配直接高分
    m = FORMAT_FULL.match(text)
    if m:
        thought = (m.group("thought") or "").strip()
        score = 0.9 + min(len(thought) / 80.0, 0.1)  # 0.9~1.0
    else:
        # 组件式部分得分
        has_open  = "<think>" in text
        has_close = "</think>" in text
        if has_open:  score += 0.3
        if has_close: score += 0.3
        if re.search(r"Answer\s*:\s*[A-J]\b", text): score += 0.3

        # 思考段长度给予最多 0.1
        mm = re.search(r"<think>(?P<t>.*?)</think>", text, re.S)
        if mm:
            t = (mm.group("t") or "").strip()
            if t and not ALLOWED_NOISE.fullmatch(t):
                score += min(len(t) / 80.0, 0.1)

        # 顺序错误扣分（Answer 出现在 think 之前）
        pos_think = text.find("<think>")
        pos_ans   = re.search(r"Answer\s*:", text)
        if pos_think >= 0 and pos_ans and pos_think > pos_ans.start():
            penalty -= 0.2

    score = max(0.0, min(1.0, score + penalty))
    return float(score)


def soft_think_format_reward_batch(completions: list[list[dict[str, str]]], **kwargs) -> list[float]:
    """
    批量处理软格式奖励函数，兼容TRL训练器接口
    
    Args:
        completions: 完成文本列表，每个元素是包含"content"键的字典列表
        **kwargs: 其他参数（保持兼容性）
        
    Returns:
        list[float]: 每个完成文本的格式奖励分数
    """
    completion_contents = [completion[0]["content"] for completion in completions]
    return [soft_think_format_reward(content) for content in completion_contents]