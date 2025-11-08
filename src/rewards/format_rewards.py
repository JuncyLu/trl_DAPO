import re


def think_format_reward(completions: list[list[dict[str, str]]], **kwargs) -> list[float]:
    """
    格式奖励函数：检查推理过程是否包含在 <think> 标签中，
    答案是否包含在 <answer> 标签中。两个标签都存在时返回 1.0，否则 0.0。
    如果包含除了这两个标签之外的其他标签，返回 0.0。
    
    Args:
        completions: 待评估的完成列表，每个完成包含 content 键
        **kwargs: 兼容性参数
    
    Returns:
        格式匹配奖励列表 (1.0 或 0.0)
    """
    # 正则模式：推理标签（开头且不重复）和答案标签
    think_pattern = r"^<think>(?!.*<think>)(.*?)</think>.*$"
    answer_pattern = r"<answer>(.*?)</answer>"
    # 匹配所有标签（包括开标签和闭标签）
    all_tags_pattern = r"</?[^>]+>"
    # 允许的标签集合
    allowed_tags = {"<think>", "</think>", "<answer>", "</answer>"}
    
    rewards = []
    for completion in completions:
        content = completion[0]["content"]
        
        # 检查两个标签是否都存在
        think_match = re.match(think_pattern, content, re.DOTALL | re.MULTILINE)
        answer_match = re.search(answer_pattern, content, re.DOTALL)
        
        # 如果基本格式不匹配，直接返回 0.0
        if not (think_match and answer_match):
            rewards.append(0.0)
            continue
        
        # 检查是否包含其他标签
        all_tags = re.findall(all_tags_pattern, content)
        has_other_tags = any(tag not in allowed_tags for tag in all_tags)
        
        # 如果包含其他标签，返回 0.0
        rewards.append(0.0 if has_other_tags else 1.0)
    
    return rewards
