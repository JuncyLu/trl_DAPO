# 数据集格式说明

本项目使用的数据集格式基于 HuggingFace Datasets 库。

## 必需字段

数据集必须包含以下三个字段：

| 字段名 | 类型 | 说明 | 示例 |
|--------|------|------|------|
| `image` | PIL.Image | 输入图像 | RGB 图像，尺寸 ≤ 1024×1024 |
| `problem` | str | 多选题问题（包含选项） | "What is the man by the bags awaiting?\nA: skateboarder\nB: train\nC: delivery\nD: cab" |
| `solution` | str | 正确答案（单个字母） | "D" |

## 字段详细要求

### 1. `image` 字段
- 格式：PIL Image 对象
- 尺寸：宽度和高度都不超过 1024 像素
- 颜色模式：RGB（会自动转换）

### 2. `problem` 字段
- 格式：字符串
- 内容：包含问题描述和选项（A-J）
- 选项格式建议：每个选项用换行分隔，格式为 "字母: 选项内容"

### 3. `solution` 字段
- 格式：单个大写字母（A-J）
- 示例：`"A"`, `"B"`, `"C"`, `"D"` 等

## 数据集示例

```python
{
    "image": <PIL.Image.Image (640×480 RGB)>,
    "problem": "What is the man by the bags awaiting?\nA: skateboarder\nB: train\nC: delivery\nD: cab",
    "solution": "D"
}
```

## 训练时的处理流程

1. **图像预处理**：
   - 过滤掉尺寸 > 1024×1024 的图像
   - 将所有图像转换为 RGB 模式

2. **对话构建**：系统会自动将 `problem` 字段包装成对话格式：
   ```python
   [
       {"role": "system", "content": "<系统提示词>"},
       {"role": "user", "content": "<problem 字段内容>"}
   ]
   ```

3. **奖励计算**：模型生成回答后，从回答中提取答案字母，与 `solution` 字段比较：
   - 正确：奖励 = 1.0
   - 错误：奖励 = 0.0

## 如何创建数据集

### 方法 1：使用 Pandas + Datasets 库

```python
import pandas as pd
from PIL import Image
from datasets import Dataset, Features, Image as ImageFeature, Value

# 准备数据
data = {
    "image": [Image.open("path/to/image1.jpg"), Image.open("path/to/image2.jpg")],
    "problem": [
        "What color is the sky?\nA: red\nB: blue\nC: green",
        "How many cats?\nA: one\nB: two\nC: three"
    ],
    "solution": ["B", "A"]
}

# 创建 Dataset
dataset = Dataset.from_dict(data)

# 保存为 parquet 格式
dataset.save_to_disk("./my_dataset")
```

### 方法 2：从现有数据转换

```python
from datasets import Dataset, Image as ImageFeature
from PIL import Image
import os

def create_dataset_from_folder(image_folder, annotation_file):
    """
    从图像文件夹和标注文件创建数据集
    
    Args:
        image_folder: 图像文件夹路径
        annotation_file: 标注文件路径（JSON/CSV，包含 problem 和 solution）
    """
    import json
    
    # 读取标注
    with open(annotation_file, 'r', encoding='utf-8') as f:
        annotations = json.load(f)
    
    data = {
        "image": [],
        "problem": [],
        "solution": []
    }
    
    for item in annotations:
        image_path = os.path.join(image_folder, item["image_filename"])
        img = Image.open(image_path).convert("RGB")
        
        # 检查尺寸
        if img.size[0] <= 1024 and img.size[1] <= 1024:
            data["image"].append(img)
            data["problem"].append(item["problem"])
            data["solution"].append(item["solution"])
    
    dataset = Dataset.from_dict(data)
    return dataset

# 使用示例
dataset = create_dataset_from_folder(
    image_folder="./images",
    annotation_file="./annotations.json"
)
dataset.save_to_disk("./my_dataset")
```

### 标注文件格式示例（JSON）

```json
[
    {
        "image_filename": "image_001.jpg",
        "problem": "What is the main object in the image?\nA: car\nB: tree\nC: building\nD: person",
        "solution": "A"
    },
    {
        "image_filename": "image_002.jpg",
        "problem": "What color is the shirt?\nA: red\nB: blue\nC: green\nD: yellow",
        "solution": "B"
    }
]
```

## 加载和使用数据集

```python
from datasets import load_dataset

# 从本地路径加载
dataset = load_dataset("./my_dataset", split="train")

# 查看数据集信息
print(f"数据集大小: {len(dataset)}")
print(f"列名: {dataset.column_names}")
print(f"第一个样本: {dataset[0]}")
```

## 数据集目录结构

保存后的数据集目录结构应该如下：

```
my_dataset/
└── data/
    └── train-00000-of-00001.parquet
```

或者也可以是：

```
my_dataset/
├── dataset_info.json
└── data/
    └── train-00000-of-00001.arrow
```

## 注意事项

1. ⚠️ **图像尺寸**：超过 1024×1024 的图像会在训练时被自动过滤掉
2. ⚠️ **答案格式**：`solution` 必须是单个大写字母（A-J）
3. ⚠️ **编码问题**：建议使用 UTF-8 编码保存所有文本文件
4. ✅ **可选字段**：可以添加其他字段（如 `original_question`, `original_answer`），不会影响训练

## 验证数据集

创建数据集后，建议运行以下代码验证：

```python
from datasets import load_dataset

dataset = load_dataset("./my_dataset", split="train")

# 检查必需字段
required_fields = ["image", "problem", "solution"]
assert all(field in dataset.column_names for field in required_fields), "缺少必需字段！"

# 检查第一个样本
example = dataset[0]
print("✅ image:", type(example["image"]), example["image"].size)
print("✅ problem:", example["problem"][:100] + "...")
print("✅ solution:", example["solution"])

# 检查图像尺寸
for i, item in enumerate(dataset):
    if item["image"].size[0] > 1024 or item["image"].size[1] > 1024:
        print(f"⚠️ 警告: 第 {i} 个样本图像过大: {item['image'].size}")

print(f"\n✅ 数据集验证完成！总共 {len(dataset)} 个样本")
```

## 联系方式

如有问题，请联系：[您的联系方式]

