# VGR Token-Level Weights Integration Guide for EasyR1

## 概述

本文档说明如何在 EasyR1 框架中使用 VGR (Vision-Text Gain Ratio) 基于注意力机制的 token-level weights 功能。

## 功能说明

VGR token weights 是一种基于注意力分析的创新方法,用于在多模态强化学习训练中对不同 token 赋予不同的权重:

- **核心思想**: 分析模型在生成每个 token 时对视觉和文本信息的关注程度
- **VGR 计算**: 文本注意力密度 / 视觉注意力密度
- **权重应用**: 将 VGR 转换为 token-level weights,并在 actor loss 中应用

## 集成内容

### 1. 工具函数

新增文件:
- `verl/utils/attention_metrics.py` - 注意力指标计算
- `verl/utils/attention_token_weights.py` - VGR weights 生成

### 2. 配置扩展

#### AlgorithmConfig (verl/trainer/config.py)

```python
enable_token_weights: bool = False
"""启用 VGR token-level weights"""

token_weight_clip: Tuple[float, float] = (0.2, 3.0)
"""token weights 的裁剪范围"""

token_weight_smooth_sigma: float = 0.0
"""高斯平滑的 sigma 值, 0.0 表示不平滑"""

token_weight_last_k_layers: Optional[int] = None
"""仅使用最后 K 层计算注意力, None 表示使用所有层"""
```

#### RolloutConfig (verl/workers/rollout/config.py)

```python
collect_attentions: bool = False
"""是否在 rollout 时收集注意力矩阵"""
```

### 3. RayDAPOTrainer 集成

在 reward 计算后自动提取并应用 token weights:

```python
# 在 fit() 循环中
reward_tensor, reward_metrics = ray.get(reward_ref)
batch.batch["token_level_scores"] = reward_tensor

# 如果启用 token weights
if self.config.algorithm.enable_token_weights:
    token_weights_tensor = self._maybe_compute_token_weights(batch, reward_metrics)
    if token_weights_tensor is not None:
        batch.batch["token_weights"] = token_weights_tensor
```

### 4. Actor Loss 集成

在 `verl/workers/actor/dp_actor.py` 中:

```python
# 在 update_policy 方法中
token_weights = model_inputs.get("token_weights")
if token_weights is not None:
    # 对齐到 response_mask 形状
    response_length = response_mask.size(-1)
    if token_weights.size(-1) < response_length:
        token_weights = torch.nn.functional.pad(token_weights, (0, pad_size), value=1.0)
    elif token_weights.size(-1) > response_length:
        token_weights = token_weights[..., :response_length]
    # 应用到 response_mask
    response_mask = response_mask * token_weights.to(response_mask.device)
```

## 使用方法

### 基础配置示例

```yaml
algorithm:
  adv_estimator: grpo
  enable_token_weights: true  # 启用 VGR weights
  token_weight_clip: [0.2, 3.0]  # 权重裁剪范围
  token_weight_smooth_sigma: 0.0  # 不使用平滑
  token_weight_last_k_layers: 4  # 仅使用最后 4 层

worker:
  rollout:
    collect_attentions: true  # 收集注意力矩阵 (如果使用 HF 生成)
```

### Reward 函数集成

如果您的 reward 函数需要提供 token weights,在 `reward_extra_infos` 中返回:

```python
def compute_reward(batch):
    # ... 计算 reward ...
    
    # 如果需要,计算 token weights
    token_weights = None
    if config.enable_token_weights and hasattr(outputs, 'attentions'):
        from verl.utils import build_token_vgr_weights_for_batch
        token_weights, debug = build_token_vgr_weights_for_batch(
            outputs_attentions=outputs.attentions,
            input_ids=batch.batch["input_ids"],
            sequences=outputs.sequences,
            processor=processor,
            image_grid_thw=batch.batch.get("image_grid_thw"),
            clip_range=config.token_weight_clip,
            smooth_sigma=config.token_weight_smooth_sigma,
            last_k_layers=config.token_weight_last_k_layers,
        )
    
    reward_extra_infos = {
        "overall": overall_scores,
        "token_weights": token_weights,  # 添加到 extra infos
    }
    
    return reward_tensor, reward_extra_infos
```

## 测试验证

运行集成测试:

```bash
cd EasyR1
python3 test_vgr_integration.py
```

测试涵盖:
- ✓ VGR 工具函数导入
- ✓ 配置字段检查
- ✓ 注意力指标计算
- ✓ Token weights 生成

## 注意事项

1. **性能影响**: 启用 token weights 会增加一定的计算开销,主要来自注意力矩阵的处理
2. **内存使用**: 收集注意力矩阵会增加显存使用,建议根据 GPU 显存调整 batch size
3. **兼容性**: 默认情况下 `enable_token_weights=False`,不影响现有训练流程
4. **调试**: 如果 reward 函数未提供 token weights,trainer 会发出一次警告但继续训练

## 参数调优建议

- **token_weight_clip**: 建议范围 `(0.1, 5.0)`,过小会削弱作用,过大可能导致不稳定
- **token_weight_smooth_sigma**: 如果训练不稳定,可以尝试 0.5-1.0 的平滑
- **token_weight_last_k_layers**: 使用最后 4-8 层通常效果较好,可以减少计算量

## 示例训练脚本

参考 `examples/qwen2_5_vl_7b_geo3k_grpo.sh`,添加 VGR 相关配置:

```bash
python3 -m verl.trainer.main \
    algorithm.enable_token_weights=true \
    algorithm.token_weight_clip=[0.2,3.0] \
    algorithm.token_weight_last_k_layers=4 \
    worker.rollout.collect_attentions=true \
    # ... 其他配置 ...
```

## 相关文件

核心实现:
- `verl/utils/attention_metrics.py`
- `verl/utils/attention_token_weights.py`
- `verl/trainer/config.py`
- `verl/trainer/ray_trainer.py`
- `verl/workers/actor/dp_actor.py`
- `verl/workers/rollout/config.py`

测试文件:
- `test_vgr_integration.py`

## 技术支持

如遇到问题,请检查:
1. 配置是否正确设置 `enable_token_weights=true`
2. Reward 函数是否返回 `token_weights` 字段
3. 训练日志中是否有 VGR 相关警告
4. GPU 显存是否足够(启用注意力收集会增加显存使用)





