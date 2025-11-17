"""
系统提示词测试脚本 - 模拟 rollout 过程
测试 50 个问题，记录推理日志，验证系统提示词效果
accelerate launch \
  --num_processes=4 \
  --num_machines=1 \
  --mixed_precision=bf16 \
  --multi_gpu \
  src/test/test_system_prompt.py
"""
import os
import sys
import json
import torch
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from datasets import load_dataset
from transformers import AutoModelForVision2Seq, AutoProcessor
from accelerate import Accelerator
from tqdm import tqdm

# 系统提示词（可修改测试）
# SYSTEM_PROMPT = (
    # "A conversation between user and assistant. The user asks an open-ended question about an image, and the assistant solves it.\n"
    # "The assistant first thinks about the reasoning process in the mind and then provides the user with the answer.\n"
    # "Inside the <think> ... </think> block, follow this flow:\n"
    # "Describe the overall scene—lighting, setting, and main activity.\n"
    # "List the primary objects and their key attributes such as colour, quantity, and positions.\n"
    # "Point out the visual evidence that directly supports the answer.\n"
    # "Conclude with the short, precise answer in natural language (typically one or a few words).\n"
    # "The final answer must be enclosed within <answer></answer> tags.\n"
    # "The answer should be concise and in natural language—use simple words without articles (a, an, the) when possible.\n"
    # "Prefer digits over spelled-out numbers (e.g., '2' instead of 'two').\n"
    # "Avoid punctuation and capitalization in the answer unless necessary.\n"
    # "The response must end immediately after the closing </answer> tag.\n"
    # "For example:\n<think>\nThis is my reasoning.\n</think>\n<answer>\n2 red apples\n</answer>"
# )
SYSTEM_PROMPT = """You MUST respond in this EXACT format:

<think>
[reasoning - be thorough and detailed]
</think>
<answer>
[brief answer - 1-5 words]
</answer>

FORMAT RULES:
• Start with <think>, end with </answer>
• NO text outside these tags

THINKING GUIDELINES (write 3-4+ sentences):
1. Describe the scene: setting, lighting, main subjects
2. Identify key objects: colors, quantities, positions, states
3. Analyze visual evidence that supports your answer
4. Reason step-by-step to reach the conclusion

ANSWER GUIDELINES:
• Keep it short: 1-5 words preferred

EXAMPLES:

Question: What is the man holding?
<think>
The image shows a man standing outdoors in daylight. He is wearing casual clothing and appears to be in a park setting. In his right hand, he is holding a red disc-shaped object. The object has the characteristic flat, circular shape of a frisbee, commonly used for outdoor recreational activities. The bright red color makes it stand out against the background.
</think>
<answer>
frisbee
</answer>

Question: How many birds are visible?
<think>
Looking at the image carefully, I can see several birds perched on a wire or branch. Let me count them one by one from left to right. I can identify the first bird on the far left, then three more birds spaced along the middle section, and finally one bird on the right end. In total, there are five distinct birds visible in the frame.
</think>
<answer>
5
</answer>

Think thoroughly and support your answer with visual evidence"""

@dataclass
class TestConfig:
    model_name: str = "Qwen/Qwen2.5-VL-7B-Instruct"
    dataset_name: str = "HuggingFaceM4/A-OKVQA"
    num_samples: int = 50
    max_new_tokens: int = 512
    temperature: float = 0.3  # 更低温度以确保格式遵循
    log_dir: str = "prompt_test_logs"
    
def format_prompt(question: str, system_prompt: str) -> str:
    """格式化提示词"""
    return f"{system_prompt}\n\nUser: {question}\nAssistant:"

def extract_answer(text: str) -> Optional[str]:
    """从输出中提取 <answer> 标签内容"""
    import re
    match = re.search(r'<answer>(.*?)</answer>', text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def extract_thinking(text: str) -> Optional[str]:
    """从输出中提取 <think> 标签内容"""
    import re
    match = re.search(r'<think>(.*?)</think>', text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def load_aokvqa_samples(num_samples: int = 50):
    """加载 A-OKVQA 数据集样本"""
    print(f"Loading {num_samples} samples from A-OKVQA dataset...")
    dataset = load_dataset("HuggingFaceM4/A-OKVQA", split="validation", streaming=False)
    
    samples = []
    for i, item in enumerate(dataset):
        if i >= num_samples:
            break
        # 解析 direct_answers（可能是字符串格式的列表）
        direct_answers = item.get("direct_answers", [])
        if isinstance(direct_answers, str):
            try:
                direct_answers = json.loads(direct_answers)
            except:
                direct_answers = [direct_answers] if direct_answers else []
        
        samples.append({
            "question_id": item.get("question_id", f"q_{i}"),
            "question": item["question"],
            "image": item["image"],
            "direct_answers": direct_answers if isinstance(direct_answers, list) else [],
            "choices": item.get("choices", []),
            "correct_choice_idx": item.get("correct_choice_idx", None),
        })
    
    print(f"Loaded {len(samples)} samples")
    return samples

def main():
    config = TestConfig()
    
    # 创建日志目录
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = Path(config.log_dir) / timestamp
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_file = log_dir / "test_results.md"
    stats_file = log_dir / "statistics.json"
    
    print("=" * 80)
    print("系统提示词测试")
    print("=" * 80)
    print(f"Model: {config.model_name}")
    print(f"Samples: {config.num_samples}")
    print(f"Log dir: {log_dir}")
    print("=" * 80)
    
    # 初始化 Accelerator
    accelerator = Accelerator()
    device = accelerator.device
    
    # 加载模型和处理器
    print("\nLoading model and processor...")
    processor = AutoProcessor.from_pretrained(
        config.model_name,
        trust_remote_code=True
    )
    model = AutoModelForVision2Seq.from_pretrained(
        config.model_name,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True
    )
    model.eval()
    
    # 使用 Accelerator 准备模型
    model = accelerator.prepare(model)
    
    # 加载数据（只在主进程加载）
    if accelerator.is_main_process:
        samples = load_aokvqa_samples(config.num_samples)
    else:
        samples = []
    
    # 统计信息
    stats = {
        "total_samples": len(samples),
        "successful_generations": 0,
        "has_think_tag": 0,
        "has_answer_tag": 0,
        "valid_format": 0,
        "avg_answer_length": 0,
        "avg_thinking_length": 0,
    }
    
    # 开始测试（只在主进程运行）
    if not accelerator.is_main_process:
        accelerator.wait_for_everyone()
        return
    
    print("\n" + "=" * 80)
    print("开始推理...")
    print("=" * 80)
    
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"# 系统提示词测试结果\n\n")
        f.write(f"**测试时间**: {timestamp}\n\n")
        f.write(f"**模型**: {config.model_name}\n\n")
        f.write(f"**样本数**: {config.num_samples}\n\n")
        f.write("---\n\n")
        f.write("## 系统提示词\n\n")
        f.write(f"```\n{SYSTEM_PROMPT}\n```\n\n")
        f.write("---\n\n")
        f.write("## 推理结果\n\n")
        
        answer_lengths = []
        thinking_lengths = []
        
        for idx, sample in enumerate(tqdm(samples, desc="Processing")):
            question_id = sample["question_id"]
            question = sample["question"]
            image = sample["image"]
            direct_answers = sample["direct_answers"]
            
            try:
                # 验证图片
                if image is None:
                    print(f"Warning: Sample {idx + 1} has no image!")
                    continue
                
                # 构建输入
                messages = [
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": [
                            {"type": "image", "image": image},
                            {"type": "text", "text": question}
                        ]
                    }
                ]
                
                text = processor.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=True
                )
                
                inputs = processor(
                    text=[text],
                    images=[image],
                    return_tensors="pt",
                    padding=True
                ).to(device)
                
                # 生成（使用 unwrap_model 访问底层模型）
                with torch.no_grad():
                    unwrapped_model = accelerator.unwrap_model(model)
                    output_ids = unwrapped_model.generate(
                        **inputs,
                        max_new_tokens=config.max_new_tokens,
                        temperature=config.temperature,
                        do_sample=True if config.temperature > 0 else False,
                        top_p=0.9,  # nucleus sampling
                        top_k=50,   # top-k sampling
                        repetition_penalty=1.1,  # 避免重复
                        pad_token_id=processor.tokenizer.pad_token_id,
                        eos_token_id=processor.tokenizer.eos_token_id,
                    )
                
                # 解码
                generated_ids = output_ids[0][inputs.input_ids.shape[1]:]
                completion = processor.decode(
                    generated_ids,
                    skip_special_tokens=True,
                    clean_up_tokenization_spaces=True
                )
                
                stats["successful_generations"] += 1
                
                # 提取内容
                thinking = extract_thinking(completion)
                answer = extract_answer(completion)
                
                if thinking:
                    stats["has_think_tag"] += 1
                    thinking_lengths.append(len(thinking.split()))
                    
                if answer:
                    stats["has_answer_tag"] += 1
                    answer_lengths.append(len(answer.split()))
                    
                if thinking and answer:
                    stats["valid_format"] += 1
                
                # 写入日志
                f.write(f"### 样本 {idx + 1}/{config.num_samples}\n\n")
                f.write(f"**Question ID**: `{question_id}`\n\n")
                f.write(f"**Question**: {question}\n\n")
                # 安全地显示参考答案
                ref_answers_str = ', '.join(str(ans) for ans in (direct_answers[:5] if isinstance(direct_answers, list) else []))
                f.write(f"**Reference Answers**: {ref_answers_str if ref_answers_str else 'N/A'}\n\n")
                f.write(f"**Generated Completion**:\n```\n{completion}\n```\n\n")
                
                if thinking:
                    f.write(f"**Extracted Thinking**: {thinking[:200]}{'...' if len(thinking) > 200 else ''}\n\n")
                else:
                    f.write(f"**Extracted Thinking**: ❌ None\n\n")
                    
                if answer:
                    f.write(f"**Extracted Answer**: `{answer}`\n\n")
                else:
                    f.write(f"**Extracted Answer**: ❌ None\n\n")
                
                f.write(f"**Format Valid**: {'✅ Yes' if (thinking and answer) else '❌ No'}\n\n")
                f.write("---\n\n")
                f.flush()
                
            except Exception as e:
                f.write(f"### 样本 {idx + 1}/{config.num_samples}\n\n")
                f.write(f"**Question ID**: `{question_id}`\n\n")
                f.write(f"**Question**: {question}\n\n")
                f.write(f"**Error**: {str(e)}\n\n")
                f.write("---\n\n")
                f.flush()
                print(f"Error processing sample {idx + 1}: {e}")
                continue
    
    # 计算统计信息
    if answer_lengths:
        stats["avg_answer_length"] = sum(answer_lengths) / len(answer_lengths)
    if thinking_lengths:
        stats["avg_thinking_length"] = sum(thinking_lengths) / len(thinking_lengths)
    
    stats["format_compliance_rate"] = stats["valid_format"] / stats["total_samples"] * 100
    stats["think_tag_rate"] = stats["has_think_tag"] / stats["total_samples"] * 100
    stats["answer_tag_rate"] = stats["has_answer_tag"] / stats["total_samples"] * 100
    
    # 保存统计信息
    with open(stats_file, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    # 输出总结
    print("\n" + "=" * 80)
    print("测试完成！")
    print("=" * 80)
    print(f"总样本数: {stats['total_samples']}")
    print(f"成功生成: {stats['successful_generations']}")
    print(f"格式完整率: {stats['format_compliance_rate']:.1f}% ({stats['valid_format']}/{stats['total_samples']})")
    print(f"包含 <think> 标签: {stats['think_tag_rate']:.1f}% ({stats['has_think_tag']}/{stats['total_samples']})")
    print(f"包含 <answer> 标签: {stats['answer_tag_rate']:.1f}% ({stats['has_answer_tag']}/{stats['total_samples']})")
    print(f"平均答案长度: {stats['avg_answer_length']:.1f} 词")
    print(f"平均推理长度: {stats['avg_thinking_length']:.1f} 词")
    print("=" * 80)
    print(f"\n详细日志: {log_file}")
    print(f"统计信息: {stats_file}")

if __name__ == "__main__":
    main()

