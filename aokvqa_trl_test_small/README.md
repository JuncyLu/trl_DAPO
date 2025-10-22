# A-OKVQA TRL 数据集（测试版本）

本数据集由 A-OKVQA 原始数据转换而来，专门用于 TRL/GRPO 多模态强化学习训练。
数据分割策略：前 1500 个用于训练，最后 150 个用于评估。

## 数据字段

| 字段名 | 类型 | 描述 |
|--------|------|------|
| image_path | string | 图片相对路径 |
| prompt | string | 组装后的多选题提示文本 |
| choices | List[string] | 原始选项列表 |
| label_idx | int | 正确答案的索引（0-based） |
| question_id | string | 原始问题ID，用于追踪 |

## Prompt 格式

### 标准模式

标准文本格式：

```
Question: {question}
Choices:
A. {choice_0}
B. {choice_1}
C. {choice_2}
D. {choice_3}
Please select the correct answer (A/B/C/D).
```

## 数据统计

### train
- 总样本数: 17056
- 有效样本数: 1500
- 去重图片数: 1496
- 重复图片数: 4

### eval
- 总样本数: 17056
- 有效样本数: 150
- 去重图片数: 150
- 重复图片数: 0

## 运行命令

```bash
# 默认分割（5000训练，500评估）
python prepare_aokvqa_for_trl_test.py \
    --dataset_path HuggingFaceM4/A-OKVQA \
    --out_dir ./aokvqa_trl_test_data \
    --question_id_file ./A-OKVQA_question_id.txt

# 自定义分割
python prepare_aokvqa_for_trl_test.py \
    --dataset_path HuggingFaceM4/A-OKVQA \
    --out_dir ./aokvqa_trl_test_data \
    --question_id_file ./A-OKVQA_question_id.txt \
    --train_size 4000 \
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
    
    return {
        "image": image,
        "prompt": prompt,
        "correct": predicted_idx == correct_idx
    }
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
A: 按照 question_id 文件中的顺序，前 1500 个用于训练，最后 150 个用于评估。

## 文件结构

```
aokvqa_trl_test_small/
├── train.parquet          # 训练集（前 1500 个）
├── eval.parquet           # 评估集（最后 150 个）
├── images/               # 图片目录
│   ├── question_id_hash.jpg
│   └── ...
└── README.md            # 本文档
```
