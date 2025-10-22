#!/usr/bin/env python3
"""
A-OKVQA 数据预处理脚本 - 为 TRL/GRPO 训练准备数据（测试版本）

将 HuggingFaceM4/A-OKVQA 数据集转换为 TRL 训练所需的格式，
根据 question_id 文件进行数据分割：前5000个用于训练，500个用于评估。

用法:
    python prepare_aokvqa_for_trl_test.py \
        --dataset_path HuggingFaceM4/A-OKVQA \
        --out_dir ./aokvqa_trl_test_data \
        --question_id_file ./A-OKVQA_question_id.txt
"""

import argparse
import hashlib
import json
import logging
import os
import random
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from datasets import load_dataset
from PIL import Image
from tqdm import tqdm

# 设置随机种子
os.environ["PYTHONHASHSEED"] = "0"
random.seed(0)
np.random.seed(0)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("prepare_aokvqa_test.log", mode="w", encoding="utf-8")
    ]
)
logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description="将 A-OKVQA 数据集转换为 TRL 训练格式（测试版本）",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "--dataset_path",
        type=str,
        default="HuggingFaceM4/A-OKVQA",
        help="数据集路径（HuggingFace Hub 名称或本地路径）"
    )
    
    parser.add_argument(
        "--out_dir",
        type=str,
        required=True,
        help="输出目录路径"
    )
    
    parser.add_argument(
        "--question_id_file",
        type=str,
        required=True,
        help="question_id 过滤文件路径"
    )
    
    parser.add_argument(
        "--train_size",
        type=int,
        default=5000,
        help="训练集样本数量"
    )
    
    parser.add_argument(
        "--eval_size",
        type=int,
        default=500,
        help="评估集样本数量"
    )
    
    parser.add_argument(
        "--use_chat_template",
        action="store_true",
        help="使用 HuggingFace chat template 格式（预留功能）"
    )
    
    return parser.parse_args()


def load_question_ids(question_id_file: str) -> List[str]:
    """加载 question_id 过滤列表，保持原始顺序"""
    logger.info(f"加载 question_id 文件: {question_id_file}")
    
    question_ids = []
    with open(question_id_file, 'r', encoding='utf-8') as f:
        for line in f:
            question_id = line.strip()
            if question_id:
                question_ids.append(question_id)
    
    logger.info(f"加载了 {len(question_ids)} 个 question_id")
    return question_ids


def split_question_ids(question_ids: List[str], train_size: int, eval_size: int) -> Tuple[List[str], List[str]]:
    """将 question_id 列表分割为训练集和评估集"""
    total_needed = train_size + eval_size
    if len(question_ids) < total_needed:
        logger.warning(f"question_id 数量 ({len(question_ids)}) 少于所需数量 ({total_needed})")
        logger.warning(f"将使用全部 {len(question_ids)} 个 question_id")
        # 按比例分配
        actual_train_size = int(len(question_ids) * train_size / total_needed)
        actual_eval_size = len(question_ids) - actual_train_size
        train_ids = question_ids[:actual_train_size]
        eval_ids = question_ids[actual_train_size:]
    else:
        # 训练集：前train_size个
        train_ids = question_ids[:train_size]
        # 评估集：最后eval_size个
        eval_ids = question_ids[-eval_size:]
    
    logger.info(f"数据分割: 训练集 {len(train_ids)} 个（前{train_size}个），评估集 {len(eval_ids)} 个（最后{eval_size}个）")
    return train_ids, eval_ids


def compute_image_hash(image: Image.Image) -> str:
    """计算图片内容哈希（MD5前8位）"""
    import io
    buffer = io.BytesIO()
    # 确保图片为RGB格式
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image.save(buffer, format='JPEG', quality=95)
    image_bytes = buffer.getvalue()
    
    # 计算MD5哈希
    md5_hash = hashlib.md5(image_bytes).hexdigest()
    return md5_hash[:8]


def save_image(image: Image.Image, question_id: str, image_hash: str, images_dir: Path) -> str:
    """保存图片到指定目录，返回相对路径"""
    # 确保图片为RGB格式
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # 生成文件名
    filename = f"{question_id}_{image_hash}.jpg"
    filepath = images_dir / filename
    
    # 如果文件已存在，直接返回路径
    if filepath.exists():
        return f"images/{filename}"
    
    # 保存图片
    image.save(filepath, 'JPEG', quality=95, optimize=True)
    
    # 返回相对路径（POSIX格式）
    return f"images/{filename}"


def build_prompt(question: str, choices: List[str], use_chat_template: bool = False) -> Union[str, Dict]:
    """构建 prompt 文本"""
    if not choices:
        return ""
    
    # 构建选项文本
    choices_text = "Choices:\n"
    for i, choice in enumerate(choices):
        letter = chr(ord('A') + i)
        choices_text += f"{letter}. {choice}\n"
    
    # 构建完整 prompt
    prompt_text = f"Question: {question}\n{choices_text}Please select the correct answer ({'/'.join([chr(ord('A') + i) for i in range(len(choices))])})."
    
    if use_chat_template:
        # 预留：使用 chat template 格式
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image"},
                    {"type": "text", "text": prompt_text}
                ]
            }
        ]
        return json.dumps(messages, ensure_ascii=False)
    
    return prompt_text


def process_split(
    dataset,
    question_ids: List[str],
    images_dir: Path,
    use_chat_template: bool = False,
    split_name: str = "unknown"
) -> Tuple[List[Dict], Dict[str, int]]:
    """处理单个 split 的数据"""
    logger.info(f"处理 {split_name}，原始样本数: {len(dataset)}")
    
    processed_data = []
    image_hash_map = {}  # 用于去重
    stats = {
        "total": 0,
        "filtered_by_id": 0,
        "invalid_data": 0,
        "duplicate_images": 0,
        "saved_images": 0
    }
    
    # 将 question_ids 转换为 set 以提高查找效率
    question_id_set = set(question_ids)
    
    for example in tqdm(dataset, desc=f"处理 {split_name}"):
        stats["total"] += 1
        
        # 检查 question_id 是否在过滤列表中
        question_id = example.get("question_id", "")
        if question_id not in question_id_set:
            stats["filtered_by_id"] += 1
            continue
        
        # 验证数据完整性
        question = example.get("question", "").strip()
        choices = example.get("choices", [])
        correct_idx = example.get("correct_choice_idx", -1)
        
        if not question or not choices or correct_idx < 0 or correct_idx >= len(choices):
            logger.warning(f"跳过无效数据: question_id={question_id}")
            stats["invalid_data"] += 1
            continue
        
        # 处理图片
        image = example.get("image")
        if image is None:
            logger.warning(f"跳过无图片数据: question_id={question_id}")
            stats["invalid_data"] += 1
            continue
        
        # 计算图片哈希
        image_hash = compute_image_hash(image)
        
        # 检查图片是否已存在（去重）
        if image_hash in image_hash_map:
            image_path = image_hash_map[image_hash]
            stats["duplicate_images"] += 1
        else:
            # 保存新图片
            image_path = save_image(image, question_id, image_hash, images_dir)
            image_hash_map[image_hash] = image_path
            stats["saved_images"] += 1
        
        # 构建 prompt
        prompt = build_prompt(question, choices, use_chat_template)
        
        # 构建输出记录 - 简化数据结构，避免嵌套
        record = {
            "image_path": image_path,  # 直接使用字符串路径
            "prompt": prompt,
            "choices": choices,
            "label_idx": correct_idx,
            "question_id": question_id
        }
        
        processed_data.append(record)
    
    logger.info(f"{split_name} 处理完成 - 统计: {stats}")
    return processed_data, stats


def save_parquet(data: List[Dict], output_path: Path, split_name: str):
    """保存数据为 parquet 格式"""
    logger.info(f"保存 {split_name} 数据到: {output_path}")
    
    if not data:
        logger.warning(f"{split_name} 没有数据可保存")
        return
    
    # 构建 Arrow Table - 使用简化的数据结构
    table = pa.Table.from_pydict({
        "image_path": [item["image_path"] for item in data],
        "prompt": [item["prompt"] for item in data],
        "choices": [item["choices"] for item in data],
        "label_idx": [item["label_idx"] for item in data],
        "question_id": [item["question_id"] for item in data]
    })
    
    # 保存 parquet
    pq.write_table(table, output_path)
    logger.info(f"已保存 {len(data)} 条记录到 {output_path}")


def generate_readme(out_dir: Path, stats: Dict[str, Dict], use_chat_template: bool, train_size: int, eval_size: int):
    """生成 README.md 文档"""
    readme_path = out_dir / "README.md"
    
    content = f"""# A-OKVQA TRL 数据集（测试版本）

本数据集由 A-OKVQA 原始数据转换而来，专门用于 TRL/GRPO 多模态强化学习训练。
数据分割策略：前 {train_size} 个用于训练，最后 {eval_size} 个用于评估。

## 数据字段

| 字段名 | 类型 | 描述 |
|--------|------|------|
| image_path | string | 图片相对路径 |
| prompt | string | 组装后的多选题提示文本 |
| choices | List[string] | 原始选项列表 |
| label_idx | int | 正确答案的索引（0-based） |
| question_id | string | 原始问题ID，用于追踪 |

## Prompt 格式

{"### Chat Template 模式" if use_chat_template else "### 标准模式"}

{"使用 HuggingFace chat template 格式，prompt 字段为 JSON 字符串。" if use_chat_template else "标准文本格式："}

```
Question: {{question}}
Choices:
A. {{choice_0}}
B. {{choice_1}}
C. {{choice_2}}
D. {{choice_3}}
Please select the correct answer (A/B/C/D).
```

## 数据统计

"""
    
    for split_name, split_stats in stats.items():
        if split_stats:
            content += f"### {split_name}\n"
            content += f"- 总样本数: {split_stats.get('total', 0)}\n"
            content += f"- 有效样本数: {split_stats.get('total', 0) - split_stats.get('filtered_by_id', 0) - split_stats.get('invalid_data', 0)}\n"
            content += f"- 去重图片数: {split_stats.get('saved_images', 0)}\n"
            content += f"- 重复图片数: {split_stats.get('duplicate_images', 0)}\n\n"
    
    content += f"""## 运行命令

```bash
# 默认分割（5000训练，500评估）
python prepare_aokvqa_for_trl_test.py \\
    --dataset_path HuggingFaceM4/A-OKVQA \\
    --out_dir ./aokvqa_trl_test_data \\
    --question_id_file ./A-OKVQA_question_id.txt

# 自定义分割
python prepare_aokvqa_for_trl_test.py \\
    --dataset_path HuggingFaceM4/A-OKVQA \\
    --out_dir ./aokvqa_trl_test_data \\
    --question_id_file ./A-OKVQA_question_id.txt \\
    --train_size 4000 \\
    --eval_size 400
```

## TRL/GRPO 对接示例

### 在 Collator 中使用

```python
import pyarrow.parquet as pq
from PIL import Image

# 读取数据
table = pq.read_table("train.parquet")
data = table.to_pydict()

# 处理单条数据
def process_example(example):
    # 读取图片
    image_path = example["image_path"]
    image = Image.open(image_path)
    
    # 获取 prompt
    prompt = example["prompt"]
    
    # 模型生成后解析答案
    model_output = "A"  # 模型输出
    predicted_idx = ord(model_output) - ord('A')
    correct_idx = example["label_idx"]
    
    return {{
        "image": image,
        "prompt": prompt,
        "correct": predicted_idx == correct_idx
    }}
```

### 自定义 Reward 函数

```python
def accuracy_reward(example, model_output):
    # 解析模型输出为索引
    if model_output.strip().upper() in ['A', 'B', 'C', 'D']:
        predicted_idx = ord(model_output.strip().upper()) - ord('A')
        correct_idx = example["label_idx"]
        return 1.0 if predicted_idx == correct_idx else 0.0
    return 0.0
```

## 常见问题

### Q: 为什么有些样本被跳过了？
A: 可能的原因：
- question_id 不在过滤列表中
- 数据不完整（空问题、无效索引等）
- 图片加载失败

### Q: 图片去重是如何工作的？
A: 使用图片内容的 MD5 哈希前8位进行去重，相同内容的图片只保存一份。

### Q: 如何切换到 chat template 模式？
A: 使用 `--use_chat_template` 参数，prompt 字段将变为 JSON 格式。

### Q: 数据分割是如何进行的？
A: 按照 question_id 文件中的顺序，前 {train_size} 个用于训练，最后 {eval_size} 个用于评估。

## 文件结构

```
{out_dir.name}/
├── train.parquet          # 训练集（前 {train_size} 个）
├── eval.parquet           # 评估集（最后 {eval_size} 个）
├── images/               # 图片目录
│   ├── question_id_hash.jpg
│   └── ...
└── README.md            # 本文档
```
"""
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    logger.info(f"已生成 README.md: {readme_path}")


def main():
    """主函数"""
    args = parse_args()
    
    logger.info("开始 A-OKVQA 数据预处理（测试版本）")
    logger.info(f"参数: {args}")
    
    # 创建输出目录
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    images_dir = out_dir / "images"
    images_dir.mkdir(exist_ok=True)
    
    # 加载 question_id 过滤列表
    question_ids = load_question_ids(args.question_id_file)
    
    # 分割 question_id
    train_question_ids, eval_question_ids = split_question_ids(
        question_ids, args.train_size, args.eval_size
    )
    
    # 加载数据集
    logger.info(f"加载数据集: {args.dataset_path}")
    try:
        dataset = load_dataset(args.dataset_path)
    except Exception as e:
        logger.error(f"加载数据集失败: {e}")
        return
    
    # 处理训练集和评估集（都从train split中处理）
    all_stats = {}
    
    if "train" not in dataset:
        logger.error("数据集中没有 train split")
        return
    
    # 处理训练集（从train split中找前5000个question_id）
    logger.info("处理训练集（从train split中找前5000个question_id）")
    train_data, train_stats = process_split(
        dataset["train"],
        train_question_ids,
        images_dir,
        args.use_chat_template,
        "train"
    )
    
    if train_data:
        train_path = out_dir / "train.parquet"
        save_parquet(train_data, train_path, "train")
        all_stats["train"] = train_stats
    else:
        logger.warning("训练集没有有效数据")
        all_stats["train"] = train_stats
    
    # 处理评估集（从train split中找最后500个question_id）
    logger.info("处理评估集（从train split中找最后500个question_id）")
    eval_data, eval_stats = process_split(
        dataset["train"],
        eval_question_ids,
        images_dir,
        args.use_chat_template,
        "eval"
    )
    
    if eval_data:
        eval_path = out_dir / "eval.parquet"
        save_parquet(eval_data, eval_path, "eval")
        all_stats["eval"] = eval_stats
    else:
        logger.warning("评估集没有有效数据")
        all_stats["eval"] = eval_stats
    
    # 生成 README
    generate_readme(out_dir, all_stats, args.use_chat_template, args.train_size, args.eval_size)
    
    logger.info("数据预处理完成！")
    logger.info(f"输出目录: {out_dir}")
    logger.info(f"训练集: {len(train_data) if 'train_data' in locals() else 0} 个样本")
    logger.info(f"评估集: {len(eval_data) if 'eval_data' in locals() else 0} 个样本")


if __name__ == "__main__":
    main()
