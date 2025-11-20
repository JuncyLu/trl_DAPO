# 最终修复：跨Rank Tensor设备不匹配

## 问题描述

### ✅ 好消息：动态采样同步机制完美运行！

从日志可以看到：
```
[DynSample-SYNC] Rank 0: Fetching new batch for resample #1
[DynSample-SYNC] Rank 1: Fetching new batch for resample #1
[DynSample-SYNC] Rank 2: Fetching new batch for resample #1
[DynSample-SYNC] Rank 3: Fetching new batch for resample #1
...
[DynSample-SYNC] Rank 0: After resample #1, global_pool=64/64
[DynSample-SYNC] Rank 1: After resample #1, global_pool=64/64
[DynSample-SYNC] Rank 2: After resample #1, global_pool=64/64
[DynSample-SYNC] Rank 3: After resample #1, global_pool=64/64
```

**完美同步**：
- ✅ 所有rank同时fetch数据
- ✅ 所有rank同时generate
- ✅ 所有rank同时计算rewards
- ✅ 所有rank同时达到global_pool=64/64
- ✅ 不再死锁！

### ❌ 新问题：设备不匹配错误

**错误信息**（第156-158行）：
```python
RuntimeError: Expected all tensors to be on the same device, 
but got tensors is on cuda:3, different from other tensors on cuda:2
```

**具体错误位置**（第1480行）：
```python
rewards_per_func = torch.stack([s["rewards_per_func"] for s in my_samples])
```

---

## 问题根源

### 跨Rank数据共享导致的设备混合

在动态采样中：
1. **Initial batch**：每个rank在自己的设备上生成数据
   - rank0的tensor在 `cuda:0`
   - rank1的tensor在 `cuda:1`
   - rank2的tensor在 `cuda:2`
   - rank3的tensor在 `cuda:3`

2. **gather_object**：收集所有rank的数据到全局池
   ```python
   global_valid_samples = [
       sample1_rank0 (cuda:0),
       sample2_rank0 (cuda:0),
       sample1_rank1 (cuda:1),
       sample2_rank1 (cuda:1),
       sample1_rank2 (cuda:2),
       sample2_rank2 (cuda:2),
       sample1_rank3 (cuda:3),
       sample2_rank3 (cuda:3),
   ]
   ```

3. **切片分配**：每个rank从全局池切片
   - rank2切片 `[32:48]`，可能包含：
     - rank2自己的样本（cuda:2）✅
     - rank3的样本（cuda:3）❌
   
4. **torch.stack失败**：尝试stack不同设备的tensor
   ```python
   rewards_per_func = torch.stack([
       tensor_on_cuda2,  # ✅
       tensor_on_cuda2,  # ✅
       tensor_on_cuda3,  # ❌ Device mismatch!
       ...
   ])
   ```

---

## 修复方案

### 在stack之前将所有tensor移动到当前rank的设备

**修改位置**：`src/trainer/dapo_trainer.py` 第1480-1482行

**修改前**（错误）：
```python
# Stack tensors
rewards_per_func = torch.stack([s["rewards_per_func"] for s in my_samples])
total_rewards = torch.stack([s["total_reward"] for s in my_samples])
filter_scores = torch.stack([s["filter_score"] for s in my_samples])
```

**修改后**（正确）：
```python
# Stack tensors - CRITICAL: Move all tensors to current rank's device
# Samples may come from different ranks (different cuda devices)
rewards_per_func = torch.stack([s["rewards_per_func"].to(device) for s in my_samples])
total_rewards = torch.stack([s["total_reward"].to(device) for s in my_samples])
filter_scores = torch.stack([s["filter_score"].to(device) for s in my_samples])
```

**关键点**：
- `.to(device)` 将tensor移动到当前rank的device
- `device = self.accelerator.device` 是在函数开头定义的
- 对于已经在正确设备上的tensor，`.to(device)` 是no-op（不产生额外开销）

---

## 为什么其他数据不需要移动？

1. **`inputs`, `prompts`, `completions`**：这些是Python对象（dict, str），不在GPU上
2. **`prompt_ids_list`, `completion_ids_list`**：这些是Python list，不在GPU上
3. **`images`, `token_weights_list`**：在后续处理中会被正确移动到设备上

只有**reward相关的tensor**需要立即移动，因为它们要被stack。

---

## 预期效果

修复后，训练应该能够顺利进行：

```
[DynSample] Initial batch: collected 56/64 valid samples globally
[DynSample] Resample #1/3: global_collected=56/64, need 8 more

[DynSample-SYNC] Rank 0: Fetching new batch for resample #1
[DynSample-SYNC] Rank 1: Fetching new batch for resample #1
[DynSample-SYNC] Rank 2: Fetching new batch for resample #1
[DynSample-SYNC] Rank 3: Fetching new batch for resample #1

[DynSample-SYNC] Rank 0: After resample #1, global_pool=64/64
[DynSample-SYNC] Rank 1: After resample #1, global_pool=64/64
[DynSample-SYNC] Rank 2: After resample #1, global_pool=64/64
[DynSample-SYNC] Rank 3: After resample #1, global_pool=64/64

[DynSample-FINAL] Rank 0: Slicing global pool [0:16], got 16 samples
[DynSample-FINAL] Rank 1: Slicing global pool [16:32], got 16 samples
[DynSample-FINAL] Rank 2: Slicing global pool [32:48], got 16 samples
[DynSample-FINAL] Rank 3: Slicing global pool [48:64], got 16 samples

[DynSample] Rank 0: ✅ Using 16 valid samples (2 groups) from global pool after 1 resample(s)

# 继续正常训练
  0%|          | 2/1236 [05:30<56:42:15, 165.39s/it]Rewards: ...
```

---

## 验证要点

1. ✅ 不再出现 `RuntimeError: Expected all tensors to be on the same device`
2. ✅ 所有rank的日志同步出现
3. ✅ 训练继续进行到step 2, 3, ...
4. ✅ GPU显存均衡（nvidia-smi显示4个GPU显存相近）

---

## 完整的动态采样流程总结

### 当Initial batch有无效组（如56/64）：

1. **所有rank同步进入重采样循环**
2. **所有rank同时fetch新数据**（避免dataloader死锁）
3. **所有rank同时generate**
4. **所有rank同时计算rewards**
5. **gather新样本到全局池**（跨rank共享）
6. **检查全局池是否足够**（64/64）→ 足够则退出循环
7. **每个rank从全局池切片自己的部分**
   - rank0: [0:16]
   - rank1: [16:32]
   - rank2: [32:48]
   - rank3: [48:64]
8. **将切片的tensor移动到当前rank的设备**（关键！）
9. **继续训练**

---

## 相关修复历史

1. **V1**: 修复`local_target`计算和移除全局判断逻辑
2. **V2**: 实现跨rank共享机制（解决死锁和显存不均）
3. **V3**: 修复`safe_gather_object`参数和嵌套列表扁平化
4. **V4（本次）**: 修复跨rank tensor设备不匹配问题

---

修复时间: 2025-11-20 (UTC)

