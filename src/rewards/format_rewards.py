import re
from typing import Any


def _collect_text(node: Any) -> list[str]:
    """Recursively collect textual content from a completion node."""
    if node is None:
        return []
    if isinstance(node, str):
        return [node]
    if isinstance(node, dict):
        texts = []
        # Prioritize explicit text fields if present
        if "text" in node:
            texts.extend(_collect_text(node["text"]))
        if "content" in node:
            texts.extend(_collect_text(node["content"]))
        if "value" in node:
            texts.extend(_collect_text(node["value"]))
        return texts
    if isinstance(node, list):
        texts = []
        for item in node:
            texts.extend(_collect_text(item))
        return texts
    return [str(node)]


def think_format_reward(completions: list[Any], **kwargs) -> list[float]:
    """
    格式奖励函数：要求思考内容位于首个 <think>...</think> 块中，答案位于后续
    <answer>...</answer> 块中，且每种标签恰好出现一次；<answer> 中必须是单个选项（A/B/C/D）。
    只要存在额外标签或不满足上述条件，则奖励为 0.0。
    
    Args:
        completions: 待评估的完成列表
        **kwargs: 兼容性参数
    
    Returns:
        格式匹配奖励列表 (1.0 或 0.0)
    """
    think_pattern = re.compile(r"<think>(.*?)</think>", re.DOTALL)
    answer_pattern = re.compile(r"<answer>(.*?)</answer>", re.DOTALL)
    all_tags_pattern = re.compile(r"</?[^>]+>")
    allowed_tags = {"<think>", "</think>", "<answer>", "</answer>"}
    
    rewards: list[float] = []
    for completion in completions:
        parts = _collect_text(completion)
        content = "\n".join(parts).strip()
        if not content:
            rewards.append(0.0)
            continue
        
        stripped = content.lstrip()
        if not stripped.startswith("<think>"):
            rewards.append(0.0)
            continue
        
        think_matches = list(think_pattern.finditer(content))
        answer_matches = list(answer_pattern.finditer(content))
        if len(think_matches) != 1 or len(answer_matches) != 1:
            rewards.append(0.0)
            continue
        
        think_span = think_matches[0].span()
        answer_span = answer_matches[0].span()
        if think_span[0] > answer_span[0] or think_span[1] > answer_span[0]:
            rewards.append(0.0)
            continue

        # Any non-whitespace text outside the two allowed blocks invalidates the answer
        outside_segments = [
            content[:think_span[0]],
            content[think_span[1]:answer_span[0]],
            content[answer_span[1]:],
        ]
        if any(segment.strip() for segment in outside_segments):
            rewards.append(0.0)
            continue

        think_content = think_matches[0].group(1).strip()
        if not think_content:
            rewards.append(0.0)
            continue
        
        answer_content = answer_matches[0].group(1).strip().upper()
        if answer_content in {"A", "B", "C", "D"}:
            valid_answer = True
        elif answer_content in {"[A]", "[B]", "[C]", "[D]"}:
            valid_answer = True
        else:
            valid_answer = False
        if not valid_answer or not answer_content:
            rewards.append(0.0)
            continue
        
        all_tags = all_tags_pattern.findall(content)
        has_other_tags = any(tag not in allowed_tags for tag in all_tags)
        rewards.append(0.0 if has_other_tags else 1.0)
    
    return rewards
