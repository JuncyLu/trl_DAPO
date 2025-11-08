你现在作为代码改造助手，请在当前仓库中基于我给出的"对齐 DAPO/GRPO 的 5 项最小补丁"完成实现，并输出 **git diff** 形式的补丁（包含新增/修改的代码与必要注释），同时在最后给出"变更摘要 + 自检清单"。只改源码与配置，不改文档与依赖。不要输出与修改无关的内容。

=====================

目标与范围

=====================

目标：在不破坏现有训练流程和默认结果的前提下，引入更贴近 DAPO 的稳健性增强与可控性选项，保留开关以便做消融。

范围：主要涉及
- `src/trainer/dapo_trainer.py`
- `src/trainer/dapo_config.py`
- `src/rewards/reward_utils.py`
- 如需要：`src/rewards/attention_rewards.py`（仅暴露参数，不改变默认行为）

=====================

必须完成的 5 项补丁（带开关，默认保持现状）

=====================

(1) 解耦剪裁 / 正负优势分路 + 轻量 KL 调度（默认关闭，兼容现状）

- 在 `dapo_trainer.py::_compute_loss(...)` 中加入 `--decoupled_clip`（布尔）开关：
  - 若开启：对优势分正/负两路。正优势仅上界裁剪 `r_pos=min(r, 1+ε_high)`；负优势仅下界裁剪 `r_neg=max(r, 1-ε_low)`；`loss = -(r_pos*A_pos + r_neg*A_neg)`。
  - 若关闭：保留原先单路 `-min(r*A, r_clip*A)` 实现。

- 引入可选轻量 KL 调度（`--kl_beta_schedule`，默认 "off"）。提供 `_update_kl_beta()` 方法，示例策略：前 10% 步线性从 0.02→0，其余为 0。若未开启，保持原 `beta=0` 行为。

实现位置：
- 在 `_compute_loss` 方法中，约第 2283-2295 行（构造 `adv_matrix` 之后、计算 `per_token_loss` 之前）插入解耦剪裁逻辑
- 在 `DAPOConfig` 中添加 `decoupled_clip: bool = False` 和 `kl_beta_schedule: str = "off"` 字段
- 在 `DAPOTrainer.__init__` 或训练循环中调用 `_update_kl_beta()`（若启用）

(2) 重放缓冲替换 → 替换后就地重算该组 rewards / advantages

- 在完成替换的逻辑处（约 `dapo_trainer.py:1991-2040`）记录 `replaced_groups`，新增私有方法 `_recompute_group_advantages(inputs, start, end)`：
  - 仅对替换的组子批重算：`rewards_per_func → rewards → group mean/std → advantages`（遵循当前 `scale_rewards` 策略）。
  - 写回 `advantages[start:end]`。如有必要，最少量缓存本地张量以避免全局 gather。

- 增加 `--replay_recompute_adv`（布尔，默认 True）控制此行为；置 False 时保持旧逻辑（直接使用缓冲中的 advantages）。

实现位置：
- 在 `_generate_and_score_completions` 方法中，替换逻辑完成后（约第 2040 行之后）调用重算方法
- 新增 `_recompute_group_advantages` 私有方法，复用 `_calculate_rewards` 的逻辑

(3) 奖励权重"表驱动阶段调度"（支持单个奖励晚开/小开；默认兼容 early/normal）

- 在 `reward_utils.py` 中扩展：
  - 新增 `RewardWeightSchedule` 类（`milestones: List[Tuple[float, List[float]]]`，基于 step_ratio 的阶段阈值与整行权重）。
  - `RewardWeightManager` 支持 `reward_weight_schedule`；若提供，则覆盖 early/normal 逻辑；若未提供，保持现逻辑不变。

- 在 Trainer 端把当前权重（含每个奖励名）记录进 metrics，便于核对。

实现位置：
- 修改 `src/rewards/reward_utils.py` 中的 `RewardWeightConfig` 和 `RewardWeightManager`
- 在 `DAPOConfig` 中添加 `reward_weight_schedule: Optional[List[Tuple[float, List[float]]]] = None` 字段
- 在 `dapo_trainer.py::_generate_and_score_completions` 中（约第 1558-1565 行）已记录权重指标，确保新增调度也写入

(4) token-weighted advantage 护栏（默认不开启或等价现状）

- 当 `--token_weights` 为 True 时（已在 `dapo_config.py` 中定义）：
  1) 每序列归一化：`tw = tw / tw.sum(dim=-1, keepdim=True).clamp_min(1e-6)`
  2) 上分位截断：按 `--token_weight_quantile`（默认 0.95）对每序列截断
  3) 仅对正优势全量施加，对负优势乘以 `--neg_adv_token_scale`（默认 0.5，可设为 1.0 以回退）

- 若未开启 `--token_weights`，完全不改变现行为。

实现位置：
- 在 `dapo_trainer.py::_compute_loss` 中，约第 2284-2291 行（处理 `token_weights` 处）添加归一化、分位截断和正负优势分路逻辑
- 在 `DAPOConfig` 中添加 `token_weight_quantile: float = 0.95` 和 `neg_adv_token_scale: float = 0.5` 字段

(5) 生成规模双保险：硬上限 + OOM 退让（默认不触发）

- 在 `dapo_config.py::__post_init__` 中加入：
  - `--generation_batch_cap`（整型，可为 None；若设置且 `generation_batch_size > cap`，自动下调并据此重算 `steps_per_generation`）
  - 提供默认 `None` 保持现状。

- 在 `_generate_and_score_completions(...)` 或 `_prepare_inputs(...)` 外层加 OOM 退让：
  - 捕获 "CUDA out of memory"，将 `steps_per_generation = max(1, steps_per_generation // 2)`，清缓存后重试一次；打印告警。
  - 新增 `--oom_backoff_enable`（默认 False）；不开启则维持现行为。

实现位置：
- 在 `dapo_config.py::__post_init__` 中，约第 750-768 行（计算 `generation_batch_size` 处）添加上限检查
- 在 `dapo_trainer.py::_generate_and_score_completions` 或 `_prepare_inputs` 中添加 try-except 捕获 OOM
- 在 `DAPOConfig` 中添加 `generation_batch_cap: Optional[int] = None` 和 `oom_backoff_enable: bool = False` 字段

=====================

实现要求

=====================

- 兼容性：所有新增行为都必须由开关控制；不开启时训练可复现当前默认曲线与日志。
- 可读性：新增代码含简短注释，变量名与项目风格一致。
- 指标：将新增开关的生效与当前权重/β/裁剪方式写入 metrics，便于回看（如 `metrics/train/decoupled_clip=0/1`）。
- 侵入性：不重构模块边界，不引入新依赖。
- 冲突处理：如果新功能与现有实现冲突，直接替换旧逻辑（不做兼容层）。

=====================

输出格式

=====================

1) 以 `git diff` 形式输出完整补丁（包含文件路径、变更行、注释）。

2) 最后追加"变更摘要 + 自检清单"：
   - 变更摘要：列出新增参数及默认值、受影响函数、关键路径。
   - 自检清单（勾选式）：逐条说明默认配置是否不改变旧结果；各新开关是否可独立启用；异常路径（OOM 退让）是否只在触发时生效等。

=====================

参考占位（变量/参数命名建议，可微调）

=====================

- `--decoupled_clip`（bool, default: False）
- `--kl_beta_schedule`（str/choice: "linear10", "off"; default: "off"）
- `--replay_recompute_adv`（bool, default: True）
- `--token_weight_quantile`（float, default: 0.95）
- `--neg_adv_token_scale`（float, default: 0.5）
- `--generation_batch_cap`（int|None, default: None）
- `--oom_backoff_enable`（bool, default: False）
- `--reward_weight_schedule`（Optional[List[Tuple[float, List[float]]]], default: None）

请开始修改并输出 `git diff` 与"变更摘要 + 自检清单"。

