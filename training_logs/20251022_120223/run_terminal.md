# Training Logs

- Time: 2025-10-22 12:02:23
- Model: Qwen/Qwen2.5-VL-3B-Instruct
- Dataset: /home/lujunxi57/aokvqa_trl_data
- Output Dir: grpo-Qwen2.5-VL-3B-Instruct

---

```text
# Training Logs

- Time: 2025-10-22 12:02:23
- Model: Qwen/Qwen2.5-VL-3B-Instruct
- Dataset: /home/lujunxi57/aokvqa_trl_data
- Output Dir: grpo-Qwen2.5-VL-3B-Instruct

---

```text
Loaded train size: 9930
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|#####     | 1/2 [00:00<00:00,  5.70it/s]Loading checkpoint shards: 100%|##########| 2/2 [00:00<00:00,  8.37it/s]
📁 Training logs directory: /home/lujunxi57/trl/training_logs
📝 Rollout log file: /home/lujunxi57/trl/training_logs/20251022_120223/rollout_results.md
🧠 Attention diagnostics file: /home/lujunxi57/trl/training_logs/20251022_120223/attention_diagnostics.md
  0%|          | 0/29790 [00:00<?, ?it/s]  0%|          | 1/29790 [00:18<155:34:57, 18.80s/it]  0%|          | 2/29790 [00:23<85:35:46, 10.34s/it]   0%|          | 3/29790 [00:26<60:29:51,  7.31s/it]  0%|          | 4/29790 [00:29<46:04:18,  5.57s/it]  0%|          | 5/29790 [00:33<39:03:34,  4.72s/it]  0%|          | 6/29790 [00:35<33:36:25,  4.06s/it]  0%|          | 7/29790 [00:39<31:31:52,  3.81s/it]  0%|          | 8/29790 [00:42<31:29:58,  3.81s/it]  0%|          | 9/29790 [00:45<29:29:52,  3.57s/it]  0%|          | 10/29790 [00:48<28:08:57,  3.40s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/early/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/early/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/early/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/early/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/late/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/late/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/all/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/all/aei_vision is NaN/Inf: nan

📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.6500
   rewards/mc_idx_reward/std: 0.2121
   rewards/think_format_reward/mean: 0.0500
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 10047.0000
   completions/mean_length: 15.0500
   completions/min_length: 10.5000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0541, 'grad_norm': 0.0, 'learning_rate': 9.996978851963747e-06, 'num_tokens': 10047.0, 'completions/mean_length': 15.05, 'completions/min_length': 10.5, 'completions/max_length': 19.6, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 15.05, 'completions/min_terminated_length': 10.5, 'completions/max_terminated_length': 19.6, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 0.65, 'rewards/mc_idx_reward/std': 0.21213203072547912, 'rewards/think_format_reward/mean': 0.05, 'rewards/think_format_reward/std': 0.07071067690849304, 'rewards/mdi_reward/mean': -0.8, 'rewards/mdi_reward/std': 0.0, 'reward': 1.85, 'reward_std': 0.9192387998104096, 'frac_reward_zero_std': 0.6, 'entropy': 0.4556409601122141, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 1.85, 'epoch': 0.0}
  0%|          | 10/29790 [00:49<28:08:57,  3.40s/it]MDI(late): 0.000
  0%|          | 11/29790 [00:52<28:10:38,  3.41s/it]  0%|          | 12/29790 [00:55<28:18:07,  3.42s/it]  0%|          | 13/29790 [00:59<27:50:17,  3.37s/it]  0%|          | 14/29790 [01:01<24:58:06,  3.02s/it]  0%|          | 15/29790 [01:04<24:44:30,  2.99s/it]  0%|          | 16/29790 [01:07<24:48:15,  3.00s/it]  0%|          | 17/29790 [01:10<24:29:14,  2.96s/it]  0%|          | 18/29790 [01:13<25:17:13,  3.06s/it]  0%|          | 19/29790 [01:16<25:11:20,  3.05s/it]  0%|          | 20/29790 [01:18<23:53:41,  2.89s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/early/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/early/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/early/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/early/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/late/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/late/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/all/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/all/aei_vision is NaN/Inf: nan

📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 19489.0000
   completions/mean_length: 2.0000
   completions/min_length: 2.0000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.993622020812354e-06, 'num_tokens': 19489.0, 'completions/mean_length': 2.0, 'completions/min_length': 2.0, 'completions/max_length': 2.0, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 2.0, 'completions/min_terminated_length': 2.0, 'completions/max_terminated_length': 2.0, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 0.85, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': 0.0, 'rewards/mdi_reward/std': 0.0, 'reward': 3.4, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.21660251719877124, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 3.4, 'epoch': 0.0}
  0%|          | 20/29790 [01:19<23:53:41,  2.89s/it]MDI(late): 0.000
  0%|          | 21/29790 [01:22<24:23:59,  2.95s/it]  0%|          | 22/29790 [01:25<24:35:43,  2.97s/it]  0%|          | 23/29790 [01:28<25:15:35,  3.05s/it]  0%|          | 24/29790 [01:31<25:49:23,  3.12s/it]  0%|          | 25/29790 [01:34<25:35:33,  3.10s/it]  0%|          | 26/29790 [01:37<25:27:50,  3.08s/it]  0%|          | 27/29790 [01:40<25:50:02,  3.12s/it]  0%|          | 28/29790 [01:44<26:17:31,  3.18s/it]  0%|          | 29/29790 [01:47<26:37:22,  3.22s/it]  0%|          | 30/29790 [01:50<26:08:33,  3.16s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/early/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/early/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/early/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/early/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/late/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/late/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/all/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/all/aei_vision is NaN/Inf: nan

📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.7000
   rewards/mc_idx_reward/std: 0.1414
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 29769.0000
   completions/mean_length: 2.0000
   completions/min_length: 2.0000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.99026518966096e-06, 'num_tokens': 29769.0, 'completions/mean_length': 2.0, 'completions/min_length': 2.0, 'completions/max_length': 2.0, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 2.0, 'completions/min_terminated_length': 2.0, 'completions/max_terminated_length': 2.0, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 0.7, 'rewards/mc_idx_reward/std': 0.1414213538169861, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': 0.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.8, 'reward_std': 0.5656854152679444, 'frac_reward_zero_std': 0.8, 'entropy': 0.22388231437653303, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.8, 'epoch': 0.0}
  0%|          | 30/29790 [01:50<26:08:33,  3.16s/it]MDI(late): 0.000
  0%|          | 31/29790 [01:54<27:10:01,  3.29s/it]  0%|          | 32/29790 [01:57<27:22:40,  3.31s/it]  0%|          | 33/29790 [02:00<26:14:57,  3.18s/it]  0%|          | 34/29790 [02:03<26:33:56,  3.21s/it]  0%|          | 35/29790 [02:06<26:14:04,  3.17s/it]  0%|          | 36/29790 [02:10<27:11:22,  3.29s/it]  0%|          | 37/29790 [02:13<26:06:54,  3.16s/it]  0%|          | 38/29790 [02:16<26:34:56,  3.22s/it]  0%|          | 39/29790 [02:19<26:18:30,  3.18s/it]  0%|          | 40/29790 [02:23<27:12:55,  3.29s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/early/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/early/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/early/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/early/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/middle/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/late/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/late/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/late/aei_vision is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi_balance is NaN/Inf: nan
⚠️  Warning: Metric attention/all/mdi_penalty is NaN/Inf: nan
⚠️  Warning: Metric attention/all/aei_text is NaN/Inf: nan
⚠️  Warning: Metric attention/all/aei_vision is NaN/Inf: nan

📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.6500
   rewards/mc_idx_reward/std: 0.2121
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 40229.0000
   completions/mean_length: 2.0000
   completions/min_length: 2.0000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.986908358509567e-06, 'num_tokens': 40229.0, 'completions/mean_length': 2.0, 'completions/min_length': 2.0, 'completions/max_length': 2.0, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 2.0, 'completions/min_terminated_length': 2.0, 'completions/max_terminated_length': 2.0, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 0.65, 'rewards/mc_idx_reward/std': 0.21213203072547912, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': 0.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.8485281229019165, 'frac_reward_zero_std': 0.7, 'entropy': 0.2286156103014946, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.0}
  0%|          | 40/29790 [02:23<27:12:55,  3.29s/it]MDI(late): 0.000
  0%|          | 41/29790 [02:26<26:12:43,  3.17s/it]  0%|          | 42/29790 [02:28<24:13:14,  2.93s/it]  0%|          | 43/29790 [02:31<24:28:09,  2.96s/it]  0%|          | 44/29790 [02:34<24:35:20,  2.98s/it]Traceback (most recent call last):
  File "/home/lujunxi57/trl/examples/scripts/grpo_vlm.py", line 660, in <module>
    trainer.train()
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/trainer.py", line 2325, in train
    return inner_training_loop(
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/trainer.py", line 2674, in _inner_training_loop
    tr_loss_step = self.training_step(model, inputs, num_items_in_batch)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/trainer.py", line 4014, in training_step
    inputs = self._prepare_inputs(inputs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/trl/trl/extras/profiling.py", line 98, in wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/trl/trl/trainer/grpo_trainer.py", line 1185, in _prepare_inputs
    generation_batch = self._generate_and_score_completions(generation_batch)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/trl/trl/trainer/grpo_trainer.py", line 1977, in _generate_and_score_completions
    prompt_ids_list, completion_ids_list, num_items_in_batch, sampling_per_token_logps_list = self._generate(
                                                                                              ^^^^^^^^^^^^^^^
  File "/home/lujunxi57/trl/trl/trainer/grpo_trainer.py", line 1550, in _generate
    self._process_attention_metrics(attention_context, mode)
  File "/home/lujunxi57/trl/trl/trainer/grpo_trainer.py", line 792, in _process_attention_metrics
    sample_results = compute_qwen_attention_metrics_for_batch(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/trl/trl/trainer/attention_metrics.py", line 341, in compute_qwen_attention_metrics_for_batch
    per_layer_attn = _collect_llm_attention_for_sample(outputs_attentions, batch_idx)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/trl/trl/trainer/attention_metrics.py", line 105, in _collect_llm_attention_for_sample
    result[layer_idx] = torch.stack(padded_rows, dim=0)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

```

```
