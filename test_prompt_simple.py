"""
简化版系统提示词测试 - 单卡快速测试
"""
import os
import torch
from datetime import datetime
from pathlib import Path
from datasets import load_dataset
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from tqdm import tqdm
import re

# 系统提示词
SYSTEM_PROMPT = (
    "A conversation between user and assistant. The user asks an open-ended question about an image, and the assistant solves it.\n"
    "The assistant first thinks about the reasoning process in the mind and then provides the user with the answer.\n"
    "Inside the <think> ... </think> block, follow this flow:\n"
    "Describe the overall scene—lighting, setting, and main activity.\n"
    "List the primary objects and their key attributes such as colour, quantity, and positions.\n"
    "Point out the visual evidence that directly supports the answer.\n"
    "Conclude with the short, precise answer in natural language (typically one or a few words).\n"
    "The final answer must be enclosed within <answer></answer> tags.\n"
    "The answer should be concise and in natural language—use simple words without articles (a, an, the) when possible.\n"
    "Prefer digits over spelled-out numbers (e.g., '2' instead of 'two').\n"
    "Avoid punctuation and capitalization in the answer unless necessary.\n"
    "The response must end immediately after the closing </answer> tag.\n"
    "For example:\n<think>\nThis is my reasoning.\n</think>\n<answer>\n2 red apples\n</answer>"
)

NUM_SAMPLES = 50
MODEL_NAME = "Qwen/Qwen2.5-VL-7B-Instruct"

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = Path(f"prompt_test_logs/{timestamp}")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_file = log_dir / "test_results.md"
    
    print("=" * 80)
    print(f"系统提示词测试 - {timestamp}")
    print("=" * 80)
    print(f"Model: {MODEL_NAME}")
    print(f"Samples: {NUM_SAMPLES}")
    print("=" * 80)
    
    # 加载模型
    print("\n加载模型...")
    processor = AutoProcessor.from_pretrained(MODEL_NAME, trust_remote_code=True)
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True
    )
    model.eval()
    
    # 加载数据
    print(f"\n加载 A-OKVQA 数据集 ({NUM_SAMPLES} 样本)...")
    dataset = load_dataset("HuggingFaceM4/A-OKVQA", split="validation", streaming=False)
    samples = list(dataset.select(range(NUM_SAMPLES)))
    
    # 统计
    stats = {"total": NUM_SAMPLES, "has_think": 0, "has_answer": 0, "valid": 0}
    
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"# 系统提示词测试结果 - {timestamp}\n\n")
        f.write(f"**模型**: {MODEL_NAME}\n\n")
        f.write(f"**样本数**: {NUM_SAMPLES}\n\n")
        f.write("---\n\n")
        
        print("\n开始推理...\n")
        for idx, sample in enumerate(tqdm(samples, desc="测试进度")):
            try:
                question = sample["question"]
                image = sample["image"]
                refs = sample.get("direct_answers", [])
                
                # 构建消息
                messages = [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": [
                        {"type": "image", "image": image},
                        {"type": "text", "text": question}
                    ]}
                ]
                
                text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
                inputs = processor(text=[text], images=[image], return_tensors="pt", padding=True).to(model.device)
                
                # 生成
                with torch.no_grad():
                    output_ids = model.generate(
                        **inputs,
                        max_new_tokens=512,
                        temperature=0.7,
                        do_sample=True,
                        pad_token_id=processor.tokenizer.pad_token_id,
                    )
                
                generated_ids = output_ids[0][inputs.input_ids.shape[1]:]
                completion = processor.decode(generated_ids, skip_special_tokens=True)
                
                # 检查格式
                has_think = bool(re.search(r'<think>.*?</think>', completion, re.DOTALL | re.IGNORECASE))
                has_answer = bool(re.search(r'<answer>.*?</answer>', completion, re.DOTALL | re.IGNORECASE))
                
                if has_think:
                    stats["has_think"] += 1
                if has_answer:
                    stats["has_answer"] += 1
                if has_think and has_answer:
                    stats["valid"] += 1
                
                # 提取内容
                think_match = re.search(r'<think>(.*?)</think>', completion, re.DOTALL | re.IGNORECASE)
                answer_match = re.search(r'<answer>(.*?)</answer>', completion, re.DOTALL | re.IGNORECASE)
                
                thinking = think_match.group(1).strip() if think_match else "❌ 无"
                answer = answer_match.group(1).strip() if answer_match else "❌ 无"
                
                # 写入日志
                f.write(f"### [{idx+1}/{NUM_SAMPLES}] {sample.get('question_id', f'q_{idx}')}\n\n")
                f.write(f"**问题**: {question}\n\n")
                f.write(f"**参考答案**: {', '.join(refs[:5])}\n\n")
                f.write(f"**推理过程**: {thinking[:150]}{'...' if len(thinking) > 150 else ''}\n\n")
                f.write(f"**提取答案**: `{answer}`\n\n")
                f.write(f"**格式**: {'✅ 完整' if (has_think and has_answer) else '❌ 不完整'}\n\n")
                f.write(f"<details><summary>完整输出</summary>\n\n```\n{completion}\n```\n\n</details>\n\n")
                f.write("---\n\n")
                f.flush()
                
            except Exception as e:
                f.write(f"### [{idx+1}/{NUM_SAMPLES}] Error\n\n")
                f.write(f"**错误**: {str(e)}\n\n")
                f.write("---\n\n")
                continue
    
    # 输出统计
    print("\n" + "=" * 80)
    print("测试完成！")
    print("=" * 80)
    print(f"总样本: {stats['total']}")
    print(f"格式完整: {stats['valid']} ({stats['valid']/stats['total']*100:.1f}%)")
    print(f"包含 <think>: {stats['has_think']} ({stats['has_think']/stats['total']*100:.1f}%)")
    print(f"包含 <answer>: {stats['has_answer']} ({stats['has_answer']/stats['total']*100:.1f}%)")
    print("=" * 80)
    print(f"\n详细结果: {log_file}")
    print(f"建议: 格式完整率应 > 95%")

if __name__ == "__main__":
    main()

