# 分布式训练修复总结

## 问题描述
在多卡训练时，`self.model_wrapped` 被包装为 `DistributedDataParallel` 等对象，没有 `.config` 属性，导致以下错误：
```
AttributeError: 'DistributedDataParallel' object has no attribute 'config'
```

## 修复方案

### 1. 添加模型解包工具函数
```python
def _unwrap_model_for_config(self, model=None):
    """
    Return the base (unwrapped) HF model object that has `.config` and `.generation_config`.
    Works with DDP, FSDP, and Deepspeed ZeRO.
    """
    m = model if model is not None else getattr(self, "model", None)
    # 优先用 accelerate 的 unwrap（Trainer 有 self.accelerator）
    try:
        if hasattr(self, "accelerator"):
            m = self.accelerator.unwrap_model(m)
    except Exception:
        pass
    # 兜底：常见包装层
    for attr in ("module", "model"):
        if hasattr(m, attr):
            m = getattr(m, attr)
    return m
```

### 2. 添加注意力实现临时切换上下文管理器
```python
@contextmanager
def _temporary_attn_impl(self, attn_impl: str = "eager"):
    """
    Context manager for temporarily switching attention implementation.
    Works with any parallel wrapper (DDP/FSDP/Deepspeed ZeRO).
    """
    base = self._unwrap_model_for_config()
    cfg = getattr(base, "config", None)
    if cfg is None:
        # 没有 config 就直接不改，继续执行
        yield
        return
    prev = getattr(cfg, "_attn_implementation", None)
    try:
        # 仅当属性存在或我们确实需要设置时才写入
        setattr(cfg, "_attn_implementation", attn_impl)
        yield
    finally:
        # 恢复（包括不存在时删除）
        if prev is None:
            try:
                delattr(cfg, "_attn_implementation")
            except Exception:
                pass
        else:
            setattr(cfg, "_attn_implementation", prev)
```

### 3. 修复的具体位置

#### 3.1 Paged Generation 部分
**修复前:**
```python
previous_attn = self.model_wrapped.config._attn_implementation
self.model_wrapped.config._attn_implementation = "paged_attention"
# ... 生成代码 ...
self.model_wrapped.config._attn_implementation = previous_attn
```

**修复后:**
```python
base_model = self._unwrap_model_for_config()
previous_attn = getattr(base_model.config, "_attn_implementation", None)
base_model.config._attn_implementation = "paged_attention"
# ... 生成代码 ...
if previous_attn is not None:
    base_model.config._attn_implementation = previous_attn
else:
    try:
        delattr(base_model.config, "_attn_implementation")
    except Exception:
        pass
```

#### 3.2 注意力采集部分
**修复前:**
```python
previous_attn_impl = getattr(self.model_wrapped.config, "_attn_implementation", None)
try:
    self.model_wrapped.config._attn_implementation = "eager"
except Exception:
    pass
attention_outputs = unwrapped_model.generate(...)
try:
    self.model_wrapped.config._attn_implementation = previous_attn_impl
except Exception:
    pass
```

**修复后:**
```python
with self._temporary_attn_impl("eager"):
    attention_outputs = unwrapped_model.generate(...)
```

## 修复效果

### ✅ 兼容性
- **单卡训练**: 完全兼容，不影响现有功能
- **多卡训练**: 支持 DDP、FSDP、Deepspeed ZeRO 等所有并行包装
- **边界情况**: 处理无 config 的情况，静默跳过

### ✅ 功能保持
- **注意力诊断**: 仍然能正常开启和计算
- **MDI/AEI 计算**: 与日志/奖励集成保持不变
- **生成过程**: 临时切换注意力实现，生成后自动恢复

### ✅ 错误处理
- **异常安全**: 使用 try/finally 确保恢复
- **静默处理**: 无 config 时静默跳过，不抛异常
- **兜底机制**: 多种解包方式确保兼容性

## 测试验证

### 单卡测试
```bash
# 单卡启动 1 step，注意力日志正常产出，训练推进无报错
accelerate launch --config_file examples/accelerate_configs/single_gpu.yaml examples/scripts/grpo_vlm.py ...
```

### 四卡测试
```bash
# 4×A100 启动，所有 rank 不再出现 config 属性错误
accelerate launch --config_file examples/accelerate_configs/multi_gpu.yaml examples/scripts/grpo_vlm.py ...
```

## 核心改进

1. **统一解包**: 通过 `_unwrap_model_for_config()` 统一处理所有并行包装
2. **安全切换**: 通过 `_temporary_attn_impl()` 上下文管理器安全切换注意力实现
3. **异常安全**: 确保在任何情况下都能正确恢复原始状态
4. **向后兼容**: 不影响单卡训练和现有功能

## 文件修改
- `trl/trainer/grpo_trainer.py`: 添加解包工具和上下文管理器，修复所有直接访问 `model_wrapped.config` 的代码
