# DAPO: Data-Augmented Policy Optimization for Vision-Language Models

基于注意力机制的多模态强化学习训练框架，通过GRPO (Group Relative Policy Optimization)算法训练视觉语言模型，重点关注注意力多样性和推理过程优化。

## 1. DAPO训练框架

### 核心思想
DAPO (Data-Augmented Policy Optimization) 是一种专门针对多模态模型的强化学习训练方法，通过以下方式优化模型性能：

- **注意力多样性优化**: 通过MDI (Multi-modal Diversity Index) 指标监控和优化注意力分布
- **推理过程引导**: 使用`<think></think>`标签引导模型进行结构化推理
- **多阶段注意力分析**: 分别监控early、middle、late阶段的注意力模式

### 训练流程
```
输入: 图像 + 问题 → 模型推理 → 输出: <think>推理过程</think>Answer: X
                ↓
        奖励计算: 准确性 + 格式 + 注意力分布
                ↓
        DAPO优化: 更新模型参数
```

## 2. 奖励计算机制

### 2.1 多维度奖励函数

**准确性奖励 (Accuracy Reward)**
```python
accuracy_reward = 1.0 if predicted_answer == correct_answer else 0.0
```

**格式奖励 (Format Reward)**
```python
# 检查<think></think>标签格式
pattern = r"^<think>(?!.*<think>)(.*?)</think>.*$"
format_reward = 1.0 if re.match(pattern, completion) else 0.0
```

**注意力多样性奖励 (MDI Reward)**
```python
# 基于注意力机制的多样性指标
mdi_reward = calculate_mdi_penalty(attention_weights)
```

### 2.2 注意力相关Metrics计算

#### MDI (Multi-modal Diversity Index) 计算
```python
def calculate_mdi(attention_weights, text_tokens, vision_tokens):
    """
    计算多模态多样性指数
    """
    # 1. 计算文本和视觉token的注意力分布
    text_attention = attention_weights[:, :len(text_tokens)]
    vision_attention = attention_weights[:, len(text_tokens):]
    
    # 2. 计算注意力熵
    text_entropy = -sum(p * log(p) for p in text_attention if p > 0)
    vision_entropy = -sum(p * log(p) for p in vision_attention if p > 0)
    
    # 3. 计算MDI值
    mdi = text_entropy / (text_entropy + vision_entropy + epsilon)
    return mdi
```

#### 分阶段注意力分析
```python
# Early阶段 (前1/3层)
early_mdi = calculate_mdi(attention_weights[:num_layers//3])

# Middle阶段 (中间1/3层)  
middle_mdi = calculate_mdi(attention_weights[num_layers//3:2*num_layers//3])

# Late阶段 (后1/3层)
late_mdi = calculate_mdi(attention_weights[2*num_layers//3:])

# 整体MDI
all_mdi = calculate_mdi(attention_weights)
```

#### AEI (Attention Entropy Index) 计算
```python
def calculate_aei(attention_weights, token_type):
    """
    计算注意力熵指数
    """
    if token_type == "text":
        attention = attention_weights[:, :num_text_tokens]
    else:  # vision
        attention = attention_weights[:, num_text_tokens:]
    
    # 计算每个token的注意力熵
    token_entropies = []
    for token_idx in range(attention.shape[1]):
        token_attention = attention[:, token_idx]
        entropy = -sum(p * log(p) for p in token_attention if p > 0)
        token_entropies.append(entropy)
    
    return mean(token_entropies)
```

### 2.3 奖励权重平衡
```python
total_reward = (
    3.0 * accuracy_reward +      # 准确性权重最高
    1.0 * format_reward +        # 格式奖励
    mdi_penalty * mdi_reward     # 注意力多样性惩罚
)
```

## 3. 三日志输出系统

### 3.1 Rollout Results Log (`rollout_results.md`)

**总体统计表格**
```markdown
| Metric | Value |
|--------|-------|
| Accuracy Mean | 0.750 ± 0.212 |
| Format Mean | 0.850 ± 0.212 |
| MDI Mean | 6.234 ± 1.456 |
| Total Reward Mean | 2.400 ± 0.848 |
| Success Rate | 0.750 |
```

**MDI统计表格**
```markdown
| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |
|-------|----------|---------|----------|------------|
| Early | 8.234 | 1.456 | 2.634 | 0.275 |
| Middle | 6.123 | 0.890 | 2.361 | 0.396 |
| Late | 4.567 | 0.678 | 2.238 | 0.450 |
| All | 6.234 | 1.456 | 2.411 | 0.374 |
```

**详细样本信息**
```json
{
  "rewards": {
    "accuracy": 1.0,
    "format": 1.0, 
    "mdi": 6.234,
    "total": 4.0
  },
  "attention_metrics": {
    "early": {"mdi": 8.234, "aei_text": 2.634, "aei_vision": 0.275},
    "middle": {"mdi": 6.123, "aei_text": 2.361, "aei_vision": 0.396},
    "late": {"mdi": 4.567, "aei_text": 2.238, "aei_vision": 0.450}
  },
  "token_counts": {
    "vision_tokens": 347,
    "text_tokens": 0,
    "total_tokens": 347
  }
}
```

### 3.2 Attention Diagnostics Log (`attention_diagnostics.md`)

**整体统计信息**
```markdown
| Metric | Early | Middle | Late | All |
|--------|-------|--------|------|-----|
| MDI Mean | 8.234 | 6.123 | 4.567 | 6.234 |
| MDI Std | 1.456 | 0.890 | 0.678 | 1.456 |
| Vision Tokens | 347.0 ± 0.0 |
| Text Tokens | 0.0 ± 0.0 |
| Vision Ratio | 1.000 |
```

**分阶段详细分析**
```json
{
  "attention_metrics": {
    "early": {
      "mdi": 8.234,
      "aei_text": 2.634,
      "aei_vision": 0.275,
      "text_ratio": 0.915,
      "vision_ratio": 0.085
    },
    "middle": {
      "mdi": 6.123,
      "aei_text": 2.361,
      "aei_vision": 0.396,
      "text_ratio": 0.853,
      "vision_ratio": 0.147
    }
  }
}
```

### 3.3 Terminal Markdown Log (`run_terminal.md`)

**训练过程记录**
- 模型加载和配置信息
- 训练进度条和指标更新
- 实时MDI值显示
- 错误和警告信息

**关键训练指标**
```markdown
📊 Logging 44 metrics for train mode
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.7500
   rewards/think_format_reward/mean: 0.8500
🧠 Attention Metrics:
   attention/early/mdi: 8.234
   attention/middle/mdi: 6.123
   attention/late/mdi: 4.567
```