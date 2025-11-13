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
    """Reward function that checks if the reasoning process is enclosed within <think> and </think> tags, while the final answer is enclosed within <answer> and </answer> tags."""
    pattern = re.compile(
        r"^<think>\n.*?\n</think>\n<answer>\n.*?\n</answer>$",
        re.DOTALL | re.MULTILINE,
    )

    rewards: list[float] = []
    for completion in completions:
        parts = _collect_text(completion)
        content = "\n".join(parts).strip()

        if not content:
            rewards.append(0.0)
            continue

        rewards.append(1.0 if pattern.match(content) else 0.0)

    return rewards


def tag_count_reward(completions, **kwargs) -> list[float]:
    def count_tags(text: str) -> float:
        illegal = re.findall(r'</?\s*([a-zA-Z0-9_]+)', text)
        if any(tag not in {"think", "/think", "answer", "/answer"} for tag in illegal):
            return 0.0
        count = 0.0
        if text.count("<think>\n") == 1:
            count += 0.25
        if text.count("\n</think>\n") == 1:
            count += 0.25
        if text.count("\n<answer>\n") == 1:
            count += 0.25
        if text.count("\n</answer>") == 1:
            count += 0.25
        return count

    contents = [completion[0]["content"] for completion in completions]
    return [count_tags(c) for c in contents]
