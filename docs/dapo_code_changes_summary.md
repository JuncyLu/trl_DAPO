# DAPO 代码改造摘要（最小补丁集）

本文总结本仓库针对 DAPO/GRPO 稳健性与可控性增强所做的源码级改造，均以“默认配置 = 现状不变；开关控制新增能力”为原则实现。

## 一、配置新增（src/trainer/dapo_config.py）

新增参数（默认值）——默认不改变旧行为：
- decoupled_clip: bool = False（解耦剪裁开关）
- kl_beta_schedule: str = "off"（KL 调度；支持 "linear10"）
- replay_recompute_adv: bool = True（重放替换后就地重算优势）
- token_weight_quantile: float = 0.95（token 权重分位截断）
- neg_adv_token_scale: float = 0.5（负优势样本 token 权重缩放）
- generation_batch_cap: Optional[int] = None（生成规模上限）
- oom_backoff_enable: bool = False（生成 OOM 退让）
- reward_weight_schedule: Optional[List[Tuple[float, List[float]]]] = None（奖励权重表驱动调度）

__post_init__：若设置了 generation_batch_cap 且超限，则下调 steps_per_generation 与 generation_batch_size 以满足 cap。

## 二、奖励权重调度（src/rewards/reward_utils.py）

- RewardWeightConfig 增加 reward_weight_schedule。
- RewardWeightManager：
  - 解析 schedule 并缓存；
  - update_weights() 支持按 step_ratio 选择“≤当前比例的最大里程碑”的整行权重，覆盖 early/normal；
  - create_reward_weight_manager(...) 透传 reward_weight_schedule。

## 三、训练器改动（src/trainer/dapo_trainer.py）

- __init__：初始化 self._beta_eff = float(self.beta)。
- _prepare_inputs：包装 _generate_and_score_completions，若 oom_backoff_enable=True 且捕获 OOM，将 steps_per_generation 对半并重试一次。
- 重放替换后就地重算优势：记录替换组 span；若 replay_recompute_adv=True，调用 _recompute_group_advantages(...) 在本进程子批上重算 rewards→advantages 并写回。
- 新增 _recompute_group_advantages(...)：局部重算 rewards_per_func → rewards → 组内 mean/std → advantages（遵循 scale_rewards 策略）。
- _compute_loss：
  - Token 权重护栏：每序列归一化 + 分位截断 + 负优势缩放；adv_matrix = A*w*scale。
  - 解耦剪裁（decoupled_clip=True）：A_pos/A_neg 分路，r_pos=min(r,1+ε_high)、r_neg=max(r,1-ε_low)，loss = -(r_pos*A_pos + r_neg*A_neg)。
  - 否则保持 -min(r*A, r_clip*A)。
  - KL 调度：若 kl_beta_schedule="linear10"，前 10% 步将 β 从 0.02 线性降至 0，仅用 beta_eff 加 KL。
  - 指标：同时记录 decoupled_clip/clip/decoupled 与 kl_beta_eff/kl/beta_eff 两组键，避免下游依赖冲突。

## 四、默认兼容性与指标

- 默认配置不改变旧行为；cap/退让与替换后重算仅在触发与开关允许时生效。
- 新开关生效状态与有效系数写入 metrics（train/*）。
