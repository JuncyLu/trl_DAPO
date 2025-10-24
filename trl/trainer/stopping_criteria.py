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
from transformers import StoppingCriteria, StoppingCriteriaList


class AnswerStop(StoppingCriteria):
    """
    停止条件：当生成文本包含 "Answer: X" 格式时停止生成
    用于防止模型生成过长的文本和避免格式错误
    """
    
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.answer_pattern = re.compile(r"Answer\s*:\s*[A-J]\b")
    
    def __call__(self, input_ids, scores, **kwargs) -> bool:
        """
        检查是否应该停止生成
        
        Args:
            input_ids: 输入token IDs
            scores: 模型输出分数
            **kwargs: 其他参数
            
        Returns:
            bool: True表示应该停止生成
        """
        try:
            # 解码当前生成的文本
            text = self.tokenizer.decode(input_ids[0], skip_special_tokens=True)
            # 检查是否包含答案格式
            return bool(self.answer_pattern.search(text))
        except Exception:
            # 如果解码失败，不停止生成
            return False


class ThinkFormatStop(StoppingCriteria):
    """
    停止条件：当生成文本包含完整的思考格式时停止生成
    用于确保模型生成正确的思考格式
    """
    
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.think_pattern = re.compile(r"<think>.*?</think>\s*Answer\s*:\s*[A-J]\b", re.DOTALL)
    
    def __call__(self, input_ids, scores, **kwargs) -> bool:
        """
        检查是否应该停止生成
        
        Args:
            input_ids: 输入token IDs
            scores: 模型输出分数
            **kwargs: 其他参数
            
        Returns:
            bool: True表示应该停止生成
        """
        try:
            # 解码当前生成的文本
            text = self.tokenizer.decode(input_ids[0], skip_special_tokens=True)
            # 检查是否包含完整的思考格式
            return bool(self.think_pattern.search(text))
        except Exception:
            # 如果解码失败，不停止生成
            return False


def create_stopping_criteria(tokenizer, stop_type="answer"):
    """
    创建停止条件列表
    
    Args:
        tokenizer: 分词器
        stop_type: 停止类型 ("answer" 或 "think_format")
        
    Returns:
        StoppingCriteriaList: 停止条件列表
    """
    if stop_type == "answer":
        return StoppingCriteriaList([AnswerStop(tokenizer)])
    elif stop_type == "think_format":
        return StoppingCriteriaList([ThinkFormatStop(tokenizer)])
    else:
        # 默认使用答案停止条件
        return StoppingCriteriaList([AnswerStop(tokenizer)])
