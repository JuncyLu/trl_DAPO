# TRL Enhanced with MDI-based Multi-Reward GRPO Training

## 项目概述

这是一个基于 [TRL (Transformers Reinforcement Learning)](https://github.com/huggingface/trl) 库的增强版本，专门针对视觉语言模型(VLM)的GRPO训练进行了深度定制。本项目在原有GRPO框架基础上，引入了**多模态注意力平衡奖励(MDI Reward)**和**实时训练诊断系统**，显著提升了多模态模型的训练效果和可观测性。

## 🚀 核心特性

### 1. 三重奖励机制 (4:1:1权重)
- **多选题答案奖励** (权重: 4.0) - 精确匹配A-J选项答案
- **思考格式奖励** (权重: 1.0) - 验证`<think></think>`标签格式
- **MDI平衡奖励** (权重: 1.0) - 基于多模态注意力分布平衡的奖励

### 2. 实时训练诊断系统
- **实时Rollout日志** - 每个训练步骤的详细推理过程记录
- **注意力诊断** - 多模态注意力分布的可视化分析
- **MDI指标监控** - 文本-视觉注意力平衡的实时追踪

### 3. A-OKVQA数据集支持
- **专用数据预处理** - `prepare_aokvqa_for_trl.py`脚本
- **多模态数据格式** - 支持图像路径和文本的联合处理
- **灵活数据加载** - 支持parquet格式和HuggingFace数据集

## 📁 项目结构

```
trl/
├── examples/scripts/
│   ├── grpo_vlm.py              # 增强版GRPO VLM训练脚本
│   └── grpo_vlm_2.py            # A-OKVQA专用训练脚本
├── trl/trainer/
│   ├── grpo_trainer.py          # 增强版GRPO训练器
│   ├── grpo_config.py           # 扩展配置参数
│   └── attention_metrics.py     # 注意力指标计算
├── prepare_aokvqa_for_trl.py    # A-OKVQA数据预处理
├── A-OKVQA_question_id.txt      # 问题ID映射文件
└── training_logs/               # 训练日志目录
    ├── rollout_results_*.md     # 实时rollout日志
    └── attention_diagnostics_*.md # 注意力诊断日志
```

## 🔧 主要改进

### 1. 增强的奖励函数系统

#### MDI奖励函数
```python
def mdi_reward(completions, **kwargs):
    """基于真实MDI计算奖励
    从trainer获取真实的MDI平衡分数，应用奖励公式：r = w * (2*balance - 1)
    """
    trainer = kwargs.get("trainer")
    balances = getattr(trainer, "_mdi_balance_scores_current_batch", None)
    # 计算平衡分数: balance = clip(1 - |log(MDI)|/log(R), 0, 1)
    # 应用奖励公式: r = weight * (2*balance - 1)
```

#### 增强的多选题奖励
```python
def mc_idx_reward(completions, label_idx, **kwargs):
    """支持中英文答案提取的多选题奖励
    - 支持 'Answer: X', '答案: X', '选项: X' 等格式
    - 处理全角字符 (Ａ-Ｊ)
    - 鲁棒的后备匹配机制
    """
```

### 2. 实时诊断系统

#### 配置参数扩展
```python
# 新增GRPO配置参数
realtime_rollout_logging: bool = True      # 实时rollout日志
compute_attention_metrics: bool = True     # 注意力指标计算
rollout_log_path: str                      # rollout日志路径
attention_diag_log_path: str               # 注意力诊断路径
mdi_balance_ratio: float = 2.0             # MDI平衡容忍度
colorize_output: bool = True               # 彩色输出
```

#### 实时日志记录
- **Rollout日志**: 记录每个样本的prompt、completion、reward分数
- **注意力诊断**: 记录MDI、AEI等注意力指标
- **Markdown格式**: 便于阅读和分析的格式化输出

### 3. 多模态数据处理增强

#### 智能图像过滤
```python
def filter_big_images(example):
    """过滤过大图像，避免内存问题"""
    # 支持多种图像格式：PIL Image、路径、嵌套字典
    # 自动转换为RGB格式
    # 过滤 >1024x1024 的图像
```

#### 灵活的数据加载
```python
# 支持多种数据源
--dataset_path ./aokvqa_trl_data_simple          # 本地parquet目录
--data_files train=./train.parquet,test=./test.parquet  # 显式文件映射
--dataset_name HuggingFaceM4/A-OKVQA             # HuggingFace数据集
```

## 🚀 快速开始

### 1. 环境准备
```bash
# 安装依赖
pip install trl Pillow peft math-verify latex2sympy2_extended torchvision trackio kernels

# 激活conda环境 (根据您的环境名调整)
conda activate your_env_name
```

### 2. 数据预处理
```bash
# 准备A-OKVQA数据
python prepare_aokvqa_for_trl.py \
    --dataset_path HuggingFaceM4/A-OKVQA \
    --out_dir ./aokvqa_trl_data_simple \
    --question_id_file ./A-OKVQA_question_id.txt \
    --subset_size 200
```

### 3. 开始训练
```bash
# 使用3B模型训练
accelerate launch \
    --config_file examples/accelerate_configs/deepspeed_zero3.yaml \
    examples/scripts/grpo_vlm.py \
    --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct \
    --output_dir grpo-Qwen2.5-VL-3B-Instruct \
    --learning_rate 1e-5 \
    --gradient_checkpointing \
    --dtype bfloat16 \
    --max_prompt_length 2048 \
    --max_completion_length 1024 \
    --dataset_path ./aokvqa_trl_data_simple \
    --log_completions
```

## 📊 训练监控

### 实时日志查看
```bash
# 查看rollout日志
tail -f /home/lujunxi57/trl/training_logs/rollout_results_*.md

# 查看注意力诊断
tail -f /home/lujunxi57/trl/training_logs/attention_diagnostics_*.md
```

### 关键指标
- **MDI平衡分数**: 文本-视觉注意力平衡度 (0-1)
- **奖励分布**: 三个奖励函数的实时分数
- **生成质量**: 答案准确率和格式正确率
- **注意力模式**: 不同层段的注意力分布

## 🔍 技术细节

### MDI计算原理
```python
# MDI (Multimodal Distribution Index) 计算
mdi = (attention_text / tokens_text) / (attention_vision / tokens_vision)

# 平衡分数计算
balance = clip(1 - |log(MDI)| / log(R), 0, 1)  # R=2.0为容忍度

# 奖励公式
reward = weight * (2 * balance - 1)
```

### 注意力分析
- **层段分析**: early/middle/late层的注意力模式
- **模态分析**: 文本vs视觉token的注意力分布
- **生成阶段**: 区分prompt和generation阶段的注意力

## 🎯 使用场景

1. **多模态推理训练** - 提升VLM的视觉-文本理解能力
2. **注意力平衡优化** - 通过MDI奖励改善多模态注意力分布
3. **训练过程诊断** - 实时监控训练质量和模型行为
4. **研究实验** - 支持多奖励机制的对比实验

## 📈 性能优化

- **内存优化**: 智能图像过滤和梯度检查点
- **计算优化**: 注意力指标的高效计算
- **存储优化**: 压缩的日志格式和增量写入
- **可视化优化**: 彩色输出和Markdown格式化

## 🤝 贡献

本项目基于TRL库进行增强，主要贡献包括：
- 多模态注意力平衡奖励机制
- 实时训练诊断系统
- A-OKVQA数据集支持
- 增强的奖励函数和配置参数

## 📄 许可证

本项目遵循Apache 2.0许可证，与原始TRL库保持一致。

---

**注意**: 本项目专门针对多模态VLM训练进行了优化，特别适合需要平衡文本和视觉注意力的应用场景。通过三重奖励机制和实时诊断系统，能够显著提升训练效果和可观测性。
