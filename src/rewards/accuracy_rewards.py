import re
from typing import Optional

def accuracy_reward(completions: list[list[dict[str, str]]], solution: list[str], **kwargs) -> list[Optional[float]]:
    """多选题奖励：匹配预测字母与正确选项"""
    fullwidth_map = {"Ａ": "A", "Ｂ": "B", "Ｃ": "C", "Ｄ": "D", "Ｅ": "E", "Ｆ": "F", "Ｇ": "G", "Ｈ": "H", "Ｉ": "I", "Ｊ": "J"}
    answer_patterns = [
        re.compile(r"(?i)(?:final\s*answer|answer|答案)\s*(?:is|为|是)?\s*[:：\-]?\s*(?:option|choice|选项)?\s*[\(\[\s]*([A-JＡ-Ｊ])"),
        re.compile(r"(?i)(?:option|choice|选项)\s*(?:is|为|是)?\s*[:：\-]?\s*[\(\[\s]*([A-JＡ-Ｊ])"),
        re.compile(r"(?i)[（(]?([A-JＡ-Ｊ])[)）]?$"),
    ]
    
    scores = []
    for comp, sol in zip(completions, solution):
        try:
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
                    return sum([_collect_text(item) for item in node], [])
                return []
            
            text = "\n".join(_collect_text(comp)) or str(comp)
            
            answer_match = re.search(r"<answer>(.*?)</answer>", text, re.DOTALL)
            pred = answer_match.group(1).strip() if answer_match else None
            
            if pred is None:
                text = re.sub(r"<think>.*?</think>", " ", text, flags=re.IGNORECASE | re.DOTALL)
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
                
                if pred is None:
                    cands = re.findall(r"\b([A-JＡ-Ｊ])\b", text)
                    pred = cands[-1] if cands else None
                
                if pred:
                    pred = fullwidth_map.get(pred, pred).upper()
            
            scores.append(1.0 if pred and sol and pred.strip().upper() == sol.strip().upper() else 0.0)
                    
        except Exception:
            scores.append(0.0)
    
    return scores
