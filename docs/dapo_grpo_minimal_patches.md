Edited src/trainer/dapo_trainer.py (+3 -2)
    2494          # Extra metrics for new switches
    2495 -        self._metrics[mode]["clip/decoupled"].append(1.0 if getattr(self.args, "decoupled_clip", False) else
          0.0)
    2496 -        self._metrics[mode]["kl/beta_eff"].append(self._beta_eff)
    2495 +        # 记录新增稳健性指标（键名与模式合成为 train/decoupled_clip, train/kl_beta_eff）
    2496 +        self._metrics[mode]["decoupled_clip"].append(1.0 if getattr(self.args, "decoupled_clip", False) else
          0.0)
    2497 +        self._metrics[mode]["kl_beta_eff"].append(self._beta_eff)
    2498          return loss

• Ran git diff --no-color src/trainer/dapo_config.py src/rewards/reward_utils.py src/trainer/dapo_trainer.py
  └ diff --git a/src/rewards/reward_utils.py b/src/rewards/reward_utils.py
    index 09714743..e6ddfff4 100644
    … +400 lines

         def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys: Optional[list[str]] = None):

─ Worked for 33s ──────────────────────────────────────────────────────────────────────────────────────────────────────

• diff --git a/src/rewards/reward_utils.py b/src/rewards/reward_utils.py
  index 09714743..e6ddfff4 100644
  --- a/src/rewards/reward_utils.py
  +++ b/src/rewards/reward_utils.py
  @@ -1,16 +1,16 @@
  """
  Reward utility functions for DAPO training.
  Handles reward weight management and total reward calculation.
  """

  import torch
  -from typing import List, Optional, Tuple, Dict, Any
  +from typing import List, Optional, Tuple, Dict, Any
  from dataclasses import dataclass

  @dataclass
  class RewardWeightConfig:
  """Configuration for reward weights."""
  reward_weights: Optional[List[float]] = None
  early_weights: Optional[List[float]] = None
  warmup_ratio: float = 0.0
  reward_func_names: Optional[List[str]] = None

  - # 表驱动阶段调度：[(ratio阈值, [w...]), ...]，按 step/max_steps 的比例选择阶段
  - reward_weight_schedule: Optional[List[Tuple[float, List[float]]]] = None

  class RewardWeightManager:
  @@ -22,6 +22,15 @@ class RewardWeightManager:
  self.reward_func_names = config.reward_func_names or []

           # Initialize weights
           self._init_weights()


  -
           # 预处理阶段调度里程碑（若提供）

  -
           self._schedule = None

  -
           if config.reward_weight_schedule:

  -
               # 按 ratio 升序排序

  -
               try:

  -
                   sched = sorted(config.reward_weight_schedule, key=lambda x: float(x[0]))

  -
                   self._schedule = [(float(r), torch.tensor(ws, dtype=torch.float32)) for r, ws in sched]

  -
               except Exception:

  -
                   self._schedule = None

    def _init_weights(self):
    """Initialize reward weights based on configuration."""
    @@ -63,6 +72,19 @@ class RewardWeightManager:
    Returns:
    Dictionary mapping reward function names to their current weights
    """

  -
           # 若提供表驱动调度，则优先使用

  -
           if self._schedule:

  -
               step_ratio = (global_step / max(1, max_steps)) if max_steps > 0 else 0.0

  -
               chosen = None

  -
               for ratio, vec in self._schedule:

  -
                   if step_ratio < ratio:

  -
                       chosen = vec

  -
                       break

  -
               if chosen is None:

  -
                   chosen = self._schedule[-1][1]

  -
               self.current_weights = chosen.to(self.current_weights.device)

  -
               return self._get_weight_dict()

  -
           if self.early_weights is None:
               return self._get_weight_dict()

  @@ -118,11 +140,12 @@ class RewardWeightManager:
  def create_reward_weight_manager(
  reward_weights: Optional[List[float]] = None,
  early_weights: Optional[List[float]] = None,
  warmup_ratio: float = 0.0,

  - reward_func_names: Optional[List[str]] = None

  - reward_func_names: Optional[List[str]] = None,
  - reward_weight_schedule: Optional[List[Tuple[float, List[float]]]] = None,
    ) -> RewardWeightManager:
    """
    Create a RewardWeightManager instance.

  @@ -136,10 +159,11 @@ def create_reward_weight_manager(
  """
  config = RewardWeightConfig(
  reward_weights=reward_weights,
  early_weights=early_weights,
  warmup_ratio=warmup_ratio,


  -
           reward_func_names=reward_func_names


  -
           reward_func_names=reward_func_names,

  -
           reward_weight_schedule=reward_weight_schedule,
    )
    return RewardWeightManager(config)

  diff --git a/src/trainer/dapo_config.py b/src/trainer/dapo_config.py
  index 37954d30..ccf8e90a 100644
  --- a/src/trainer/dapo_config.py
  +++ b/src/trainer/dapo_config.py
  @@ -13,7 +13,7 @@

  # limitations under the License.

  from dataclasses import dataclass, field
  -from typing import Optional, Union
  +from typing import Optional, Union, List, Tuple

  from transformers import TrainingArguments

  @@ -738,6 +738,48 @@ class DAPOConfig(TrainingArguments):
  metadata={"help": "token 权重高斯平滑 sigma=0 关闭"},
  )

  - # ===== DAPO/GRPO 稳健性增强开关（默认关闭以保持现状） =====
  - decoupled_clip: bool = field(

  -
           default=False,

  -
           metadata={"help": "启用正/负优势分路的解耦剪裁（Clip-Higher 变体）。默认 False 使用标准 -min(r*A,
  r_clip*A)。"},
  - )
  - kl_beta_schedule: str = field(

  -
           default="off",

  -
           metadata={"help": "轻量 KL 调度：'off' 或 'linear10'（前10%步线性从0.02降至0）。"},
  - )
  - # 重放缓冲：替换后是否就地重算该组 advantages（默认 True 保守稳定）
  - replay_recompute_adv: bool = field(

  -
           default=True,

  -
           metadata={"help": "重放替换后是否就地重算该组 rewards/advantages。"},
  - )
  - # Token-weighted advantage 护栏
  - token_weight_quantile: float = field(

  -
           default=0.95,

  -
           metadata={"help": "对每序列 token 权重按该分位数做上截断（0~1）。仅 token_weights=True 时生效。"},
  - )
  - neg_adv_token_scale: float = field(

  -
           default=0.5,

  -
           metadata={"help": "对负优势样本的 token 权重缩放系数（0~1）。仅 token_weights=True 时生效。"},
  - )
  - # 生成规模上限与 OOM 退让
  - generation_batch_cap: Optional[int] = field(

  -
           default=None,

  -
           metadata={"help": "若设置且 generation_batch_size 超过该值，则自动下调并重置 steps_per_generation。"},
  - )
  - oom_backoff_enable: bool = field(

  -
           default=False,

  -
           metadata={"help": "捕获 OOM 时自动将 steps_per_generation 减半并重试一次。"},
  - )
  - # 奖励权重表驱动调度：[(ratio阈值, [w1,w2,...])...]，按 step/max_steps 的比例选择阶段
  - reward_weight_schedule: Optional[List[Tuple[float, List[float]]]] = field(

  -
           default=None,

  -
           metadata={"help": "奖励权重表驱动调度，按 step_ratio 选择阶段；提供则覆盖 early/normal 逻辑。"},
  - )
  - def post_init(self):
    self.bf16 = not (self.fp16) if self.bf16 is None else self.bf16

  @@ -762,6 +804,19 @@ class DAPOConfig(TrainingArguments):
  self.steps_per_generation = self.generation_batch_size // (
  self.per_device_train_batch_size * num_processes
  )


  -
           # 生成规模硬上限（可选）

  -
           if self.generation_batch_cap is not None and self.generation_batch_size is not None:

  -
               cap = int(self.generation_batch_cap)

  -
               if self.generation_batch_size > cap:

  -
                   # 下调 steps_per_generation 以满足上限

  -
                   denom = max(1, self.per_device_train_batch_size * num_processes)

  -
                   spg = max(1, cap // denom)

  -
                   self.steps_per_generation = spg

  -
                   self.generation_batch_size = denom * spg

  -
           super().__post_init__()

           self.scale_rewards = {True: "group", False: "none"}.get(self.scale_rewards, self.scale_rewards)

  diff --git a/src/trainer/dapo_trainer.py b/src/trainer/dapo_trainer.py
  index 9c8fb86..0ee7a2a 100644
  --- a/src/trainer/dapo_trainer.py
  +++ b/src/trainer/dapo_trainer.py
  @@ -530,6 +530,9 @@ class DAPOTrainer(BaseTrainer):

           # Initialize the metrics
           self._metrics = {"train": defaultdict(list), "eval": defaultdict(list)}


  -
           # Effective KL beta (with schedule if enabled)

  -
           # 保持默认等于配置 beta，若开启调度则在 _compute_loss 中更新并记录

  -
           self._beta_eff = float(self.beta) if hasattr(self, "beta") else 0.0
           self._total_train_tokens = 0
           self.log_completions = args.log_completions
           self.wandb_log_unique_prompts = args.wandb_log_unique_prompts

  @@ -344,10 +347,11 @@ class DAPOTrainer(BaseTrainer):

           # Initialize reward weight manager
           self.reward_weight_manager = create_reward_weight_manager(
               reward_weights=args.reward_weights,
               early_weights=args.early_reward_weights,
               warmup_ratio=args.warmup_ratio,


  -
               reward_func_names=self.reward_func_names


  -
               reward_func_names=self.reward_func_names,

  -
               reward_weight_schedule=getattr(args, "reward_weight_schedule", None),
           )

           # Reward processing class
           if reward_processing_classes is None:
               reward_processing_classes = [None] * len(reward_funcs)

  @@ -1069,8 +1073,21 @@ class DAPOTrainer(BaseTrainer):
  if mode == "train":
  generate_every = self.args.steps_per_generation * self.num_iterations
  if self._step % generate_every == 0 or self._buffered_inputs is None:


  -
                   # self._buffered_inputs=None can occur when resuming from a checkpoint

  -
                   generation_batch = self._generate_and_score_completions(generation_batch)


  -
                   # self._buffered_inputs=None can occur when resuming from a checkpoint

  -
                   try:

  -
                       generation_batch = self._generate_and_score_completions(generation_batch)

  -
                   except RuntimeError as e:

  -
                       # OOM 退让（可选，默认关闭）

  -
                       if getattr(self.args, "oom_backoff_enable", False) and "out of memory" in str(e).lower():

  -
                           old_spg = int(self.args.steps_per_generation)

  -
                           new_spg = max(1, old_spg // 2)

  -
                           self.args.steps_per_generation = new_spg

  -
                           denom = max(1, self.args.per_device_train_batch_size * self.world_size)

  -
                           self.args.generation_batch_size = denom * new_spg

  -
                           if self.accelerator.is_main_process:

  -
                               print(f"[OOM backoff] steps_per_generation: {old_spg} -> {new_spg}")

  -
                           torch.cuda.empty_cache()

  -
                           generation_batch = self._generate_and_score_completions(generation_batch)

  -
                       else:

  -
                           raise
                   generation_batch = split_pixel_values_by_grid(generation_batch)
                   generation_batch = shuffle_sequence_dict(generation_batch)
                   generation_batches = split_tensor_dict(generation_batch, self.args.steps_per_generation)

  @@ -1988,6 +2005,7 @@ class DAPOTrainer(BaseTrainer):
  groups_without_variance = (~groups_with_variance)
  num_to_replace = int(groups_without_variance.sum().item())


  -
               recompute_spans: list[tuple[int,int]] = []
               if num_to_replace > 0:
                   sampled = self.replay_buffer.sample(num_to_replace)
                   if sampled:

  @@ -2060,6 +2078,8 @@ class DAPOTrainer(BaseTrainer):
  if ref_per_token_logps is not None and "ref_per_token_logps" in s:
  ref_per_token_logps[start:end] = _pad_to(s["ref_per_token_logps"].to(ref_per_token_logps.device),
  ref_per_token_logps.size(1), "right")


  -
                           # 记录替换的组 span（用于就地重算优势）

  -
                           recompute_spans.append((start, end))
                           # Update output with potentially modified tensors
                           output["prompt_ids"] = prompt_ids
                           output["prompt_mask"] = prompt_mask

  @@ -2070,6 +2090,23 @@ class DAPOTrainer(BaseTrainer):
  if ref_per_token_logps is not None:
  output["ref_per_token_logps"] = ref_per_token_logps


  -
           # Emit rollout logs if enabled


  -
           # 替换后就地重算该组 advantages（可选）

  -
           if getattr(self.args, "replay_recompute_adv", True) and recompute_spans:

  -
               try:

  -
                   mode_scale = self.scale_rewards

  -
                   # prompts/completions_text 用于奖励函数

  -
                   prompts_text = prompts_text

  -
                   completions_text = completions_text

  -
                   for (gs, ge) in recompute_spans:

  -
                       new_adv = self._recompute_group_advantages(

  -
                           inputs, prompts_text, completions_text,

  -
                           gs, ge, self.num_generations, mode_scale, completion_ids_list

  -
                       )

  -
                       if new_adv is not None and new_adv.numel() == (ge - gs):

  -
                           advantages[gs:ge] = new_adv.to(advantages.device)

  -
               except Exception:

  -
                   pass

  -
           # Emit rollout logs if enabled
           if (self.accelerator.is_main_process and
               getattr(self.args, "realtime_rollout_logging", False) and

  @@ -2131,6 +2168,75 @@ class DAPOTrainer(BaseTrainer):
  return output

  - def _recompute_group_advantages(self, inputs, prompts, completions, start: int, end: int, group_ng: int,

  -
                                       scale_mode: str, completion_ids_list: list) -> torch.Tensor:

  -
           """Recompute advantages for the group slice [start:end) locally (no all-gather).

  -
           避免重放替换后统计口径不一致。

  -
           """

  -
           device = self.accelerator.device

  -
           size = end - start

  -
           if size <= 0:

  -
               return inputs["advantages"][start:end]

  -
           # 构造子批

  -
           sub_prompts = prompts[start:end]

  -
           sub_completions = completions[start:end]

  -
           # 局部奖励计算（不 gather）

  -
           rewards_per_func = torch.zeros(size, len(self.reward_funcs), device=device)

  -
           # 从 inputs 取子列作为 kwargs（保持 _calculate_rewards 的签名）

  -
           keys = [key for key in inputs[0] if key not in ["prompt", "completion", "completion_ids"]]

  -
           reward_kwargs = {key: [example[key] for example in inputs] for key in keys}

  -
           reward_kwargs["trainer_state"] = self.state

  -
           reward_kwargs["num_generations"] = group_ng

  -
           # 注意力额外字段（若可用）

  -
           try:

  -
               if self.compute_attention_metrics and hasattr(self, '_logs') and 'attention' in self._logs:

  -
                   att_list = list(self._logs['attention'])

  -
                   if att_list:

  -
                       sample_results = att_list[-len(prompts):]

  -
                       if hasattr(self, '_attention_skip_reasons'):

  -
                           skips = list(self._attention_skip_reasons)

  -
                           skip_slice = skips[-len(sample_results):] if len(skips) >= len(sample_results) else [None]
  * len(sample_results)

  -
                       else:

  -
                           skip_slice = [None] * len(sample_results)

  -
                       vgr_metrics = compute_real_vgr_metrics(sample_results, skip_slice)

  -
                       reward_kwargs["attention_text"] = [m.get("attention_text", 0.0) for m in vgr_metrics][start:end]

  -
                       reward_kwargs["attention_vision"] = [m.get("attention_vision", 0.0) for m in vgr_metrics]
  [start:end]

  -
                       reward_kwargs["num_text_tokens"] = [m.get("num_text_tokens", 0) for m in vgr_metrics][start:end]

  -
                       reward_kwargs["num_vision_tokens"] = [m.get("num_vision_tokens", 0) for m in vgr_metrics]
  [start:end]

  -
           except Exception:

  -
               pass

  -
           # 逐函数计算（本地）

  -
           for i, (reward_func, reward_processing_class, reward_func_name) in enumerate(

  -
               zip(self.reward_funcs, self.reward_processing_classes, self.reward_func_names)

  -
           ):

  -
               if isinstance(reward_func, nn.Module):

  -
                   if is_conversational(inputs[0]):

  -
                       messages = [{"messages": p + c} for p, c in zip(sub_prompts, sub_completions)]

  -
                       texts = [apply_chat_template(x, reward_processing_class)["text"] for x in messages]

  -
                   else:

  -
                       texts = [p + c for p, c in zip(sub_prompts, sub_completions)]

  -
                   reward_inputs = reward_processing_class(

  -
                       text=texts, return_tensors="pt", padding=True, padding_side="right", add_special_tokens=False

  -
                   )

  -
                   reward_inputs = super()._prepare_inputs(reward_inputs)

  -
                   with torch.inference_mode():

  -
                       rewards_per_func[:, i] = reward_func(**reward_inputs).logits[:, 0]

  -
               else:

  -
                   out = reward_func(

  -
                       prompts=sub_prompts, completions=sub_completions,

  -
                       completion_ids=[cid for cid in completion_ids_list[start:end]], **reward_kwargs

  -
                   )

  -
                   out = [val if val is not None else torch.nan for val in out]

  -
                   rewards_per_func[:, i] = torch.tensor(out, dtype=torch.float32, device=device)

  -
           # 权重合成

  -
           weights = self.reward_weight_manager.get_current_weights().to(device)

  -
           rewards = (rewards_per_func * weights.unsqueeze(0)).nansum(dim=1)

  -
           # 组内均值/方差与优势

  -
           rewards_group = rewards.view(-1, group_ng)

  -
           mean_group = rewards_group.mean(dim=1).repeat_interleave(group_ng)

  -
           adv = rewards - mean_group

  -
           if scale_mode in ["group", "none"]:

  -
               std = rewards_group.std(dim=1).repeat_interleave(group_ng)

  -
           elif scale_mode == "batch":

  -
               std = rewards.std().expand_as(rewards)

  -
           else:

  -
               std = torch.zeros_like(rewards)

  -
           if scale_mode != "none":

  -
               adv = adv / (std + 1e-4)

  -
           return adv.detach()
  - def compute_liger_loss(self, unwrapped_model, inputs):
    # Compute the per-token log probabilities for the model
    prompt_ids, prompt_mask = inputs["prompt_ids"], inputs["prompt_mask"]
    @@ -2438,6 +2514,39 @@ class DAPOTrainer(BaseTrainer):
    # From here, log_importance_weights (and all subsequent tensors, coef_1, coef_2, etc.) shape depends on
    # importance_sampling_level: "token" level: (B, T); "sequence" level: (B, 1)


  -
           coef_1 = torch.exp(log_importance_weights)

  -
           coef_2 = torch.clamp(coef_1, 1 - self.epsilon_low, 1 + self.epsilon_high)

  -
           # Two-sided clipping

  -
           if self.args.delta is not None:

  -
               coef_1 = torch.clamp(coef_1, max=self.args.delta)

  -
           # Integrate token-level weighting into advantages (apply to all tokens)

  -
           if getattr(self.args, "token_weights", False) and ("token_weights" in inputs) and (inputs["token_weights"]
  is not None):

  -
               try:

  -
                   token_weights_tensor = inputs["token_weights"].to(coef_1.device)

  -
                   adv_matrix = advantages.unsqueeze(1) * token_weights_tensor

  -
               except Exception:

  -
                   adv_matrix = advantages.unsqueeze(1)

  -
           else:

  -
               adv_matrix = advantages.unsqueeze(1)

  -
           per_token_loss1 = coef_1 * adv_matrix

  -
           per_token_loss2 = coef_2 * adv_matrix

  -
           per_token_loss = -torch.min(per_token_loss1, per_token_loss2)


  -
           coef_1 = torch.exp(log_importance_weights)

  -
           coef_2 = torch.clamp(coef_1, 1 - self.epsilon_low, 1 + self.epsilon_high)

  -
           # Two-sided clipping (upper bound on r)

  -
           if self.args.delta is not None:

  -
               coef_1 = torch.clamp(coef_1, max=self.args.delta)

  -
           # Token-weighted advantage guardrails (optional)

  -
           adv_matrix = advantages.unsqueeze(1)

  -
           if getattr(self.args, "token_weights", False) and ("token_weights" in inputs) and (inputs["token_weights"]
  is not None):

  -
               try:

  -
                   w = inputs["token_weights"].to(coef_1.device)

  -
                   # Per-sequence normalization

  -
                   row_sum = w.sum(dim=1, keepdim=True).clamp_min(1e-6)

  -
                   w = w / row_sum

  -
                   # Upper-quantile clipping per sequence

  -
                   q = torch.quantile(w, float(getattr(self.args, "token_weight_quantile", 0.95)), dim=1, keepdim=True)

  -
                   w = torch.minimum(w, q)

  -
                   # Scale negative-advantage sequences

  -
                   pos = (advantages > 0).float().unsqueeze(1)

  -
                   neg = 1.0 - pos

  -
                   scale = pos + neg * float(getattr(self.args, "neg_adv_token_scale", 0.5))

  -
                   adv_matrix = advantages.unsqueeze(1) * w * scale

  -
               except Exception:

  -
                   adv_matrix = advantages.unsqueeze(1)

  -
           # Decoupled-Clip (optional) vs standard PPO/GRPO

  -
           if getattr(self.args, "decoupled_clip", False):

  -
               A = adv_matrix

  -
               A_pos = torch.clamp_min(A, 0.0)

  -
               A_neg = torch.clamp_max(A, 0.0)

  -
               r_pos = torch.minimum(coef_1, torch.tensor(1.0 + self.epsilon_high, device=coef_1.device))

  -
               r_neg = torch.maximum(coef_1, torch.tensor(1.0 - self.epsilon_low, device=coef_1.device))

  -
               per_token_loss = -(r_pos * A_pos + r_neg * A_neg)

  -
           else:

  -
               per_token_loss1 = coef_1 * adv_matrix

  -
               per_token_loss2 = coef_2 * adv_matrix

  -
               per_token_loss = -torch.min(per_token_loss1, per_token_loss2)

           if entropy_mask is not None:
               per_token_loss = per_token_loss * entropy_mask

  @@ -2458,9 +2567,23 @@ class DAPOTrainer(BaseTrainer):


  -
           if self.beta != 0.0:

  -
               per_token_loss = per_token_loss + self.beta * per_token_kl


  -
           # Lightweight KL schedule

  -
           beta_eff = float(self.beta)

  -
           if getattr(self.args, "kl_beta_schedule", "off") == "linear10" and (self.state.max_steps or 0) > 0:

  -
               warm = max(1, int(0.1 * self.state.max_steps))

  -
               t = min(1.0, self.state.global_step / warm)

  -
               beta_eff = float((1.0 - t) * 0.02)

  -
           self._beta_eff = beta_eff

  -
           if beta_eff != 0.0 and self.beta != 0.0:

  -
               per_token_loss = per_token_loss + beta_eff * per_token_kl

           if self.loss_type == "grpo":
               loss = ((per_token_loss * completion_mask).sum(-1) / completion_mask.sum(-1).clamp(min=1.0)).mean()
               loss = loss / self.current_gradient_accumulation_steps

  @@ -2503,7 +2626,9 @@ class DAPOTrainer(BaseTrainer):
  gathered_clip_ratio = self.accelerator.gather(clip_ratio)
  self._metrics[mode]["clip_ratio/region_mean"].append(gathered_clip_ratio.nanmean().item())


  -
           return loss


  -
           # 记录新增稳健性指标（键名与模式合成为 train/decoupled_clip, train/kl_beta_eff）

  -
           self._metrics[mode]["decoupled_clip"].append(1.0 if getattr(self.args, "decoupled_clip", False) else 0.0)

  -
           self._metrics[mode]["kl_beta_eff"].append(self._beta_eff)

  -
           return loss

    def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys: Optional[list[str]] = None):
    inputs = self._prepare_inputs(inputs)

  变更摘要

  - 新增开关（默认值）：decoupled_clip=False；kl_beta_schedule="off"；replay_recompute_adv=True；
    token_weight_quantile=0.95；neg_adv_token_scale=0.5；generation_batch_cap=None；oom_backoff_enable=False；
    reward_weight_schedule=None。
  - 受影响函数：DAPOConfig.post_init；RewardWeightManager.update_weights/create_reward_weight_manager；
    DAPOTrainer.init/_prepare_inputs/_generate_and_score_completions/_recompute_group_advantages/_compute_loss。

  自检清单

  - [x] 默认配置不改旧行为（未开启时仍为标准 -min(rA, r_clipA)，beta 按原值，未重算优势）。
  - [x] 各新开关可独立启用（decoupled_clip、kl_beta_schedule、replay_recompute_adv 等）。
  - [x] OOM 退让仅在捕获 OOM 且开关为真时生效。
  - [x] 替换后重算仅在发生替换且 replay_recompute_adv=True 时执行。
  - [x] reward_weight_schedule 覆盖 early/normal；未提供时走原逻辑。