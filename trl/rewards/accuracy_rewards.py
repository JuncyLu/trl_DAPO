import re
from typing import Optional

from trl.import_utils import is_math_verify_available


if is_math_verify_available():
    from latex2sympy2_extended import NormalizationConfig
    from math_verify import LatexExtractionConfig, parse, verify


def accuracy_reward(completions: list[list[dict[str, str]]], solution: list[str], problems: list[str] = None, **kwargs) -> list[Optional[float]]:
    """
    多选题奖励函数：匹配预测字母与正确选项。
    优先从 <answer> 标签提取，否则通过显式模式或最后出现的字母匹配。
    
    Args:
        completions: 待评估的完成列表，每个完成包含 content 键
        solution: 正确答案文本列表
        problems: 可选的问题文本列表，用于选项匹配
        **kwargs: 兼容性参数
    
    Returns:
        每个完成的准确度分数列表 (1.0 或 0.0)
    """
    # 全角字符映射和正则模式（按优先级排序）
    fullwidth_map = {"Ａ": "A", "Ｂ": "B", "Ｃ": "C", "Ｄ": "D", "Ｅ": "E", "Ｆ": "F", "Ｇ": "G", "Ｈ": "H", "Ｉ": "I", "Ｊ": "J"}
    answer_patterns = [
        re.compile(r"(?i)(?:final\s*answer|answer|答案)\s*(?:is|为|是)?\s*[:：\-]?\s*(?:option|choice|选项)?\s*[\(\[\s]*([A-JＡ-Ｊ])"),
        re.compile(r"(?i)(?:option|choice|选项)\s*(?:is|为|是)?\s*[:：\-]?\s*[\(\[\s]*([A-JＡ-Ｊ])"),
        re.compile(r"(?i)[（(]?([A-JＡ-Ｊ])[)）]?$"),
    ]
    
    scores = []
    for i, (comp, sol) in enumerate(zip(completions, solution)):
        try:
            # 收集文本内容
            def _collect_text(node) -> list[str]:
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
                    texts = []
                    for item in node:
                        texts.extend(_collect_text(item))
                    return texts
                return []
            
            pieces = _collect_text(comp)
            text = "\n".join(pieces) if pieces else str(comp)
            
            # 优先从 <answer> 标签提取
            answer_match = re.search(r"<answer>(.*?)</answer>", text, re.DOTALL)
            pred = answer_match.group(1).strip() if answer_match else None
            
            # 否则使用显式模式匹配
            if pred is None:
                # 清理 redacted_reasoning 标签
                text = re.sub(r"<think>.*?</think>", " ", text, flags=re.IGNORECASE | re.DOTALL)
                
                # 从后往前搜索包含关键词的行
                lines = [line.strip() for line in text.splitlines() if line.strip()]
                keywords = ("answer", "答案", "选项", "choice", "option")
                
                for line in reversed(lines):
                    if not any(k in line.lower() for k in keywords):
                        continue
                    for pattern in answer_patterns:
                        match = pattern.search(line)
                        if match:
                            pred = match.group(1)
                            break
                    if pred:
                        break
                
                # 最后尝试提取所有字母，取最后一个
                if pred is None:
                    cands = re.findall(r"\b([A-JＡ-Ｊ])\b", text)
                    pred = cands[-1] if cands else None
                
                # 标准化全角字符
                if pred:
                    pred = fullwidth_map.get(pred, pred).upper()
            
            # 直接比较预测字母和正确答案字母
            if pred and sol and pred.strip().upper() == sol.strip().upper():
                scores.append(1.0)
            else:
                scores.append(0.0)
                    
        except Exception:
            scores.append(0.0)
    
    return scores
