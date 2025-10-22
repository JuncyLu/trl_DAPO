# Training Logs

- Time: 2025-10-22 12:05:31
- Model: Qwen/Qwen2.5-VL-3B-Instruct
- Dataset: /home/lujunxi57/aokvqa_trl_data
- Output Dir: grpo-Qwen2.5-VL-3B-Instruct

---

```text
# Training Logs

- Time: 2025-10-22 12:05:31
- Model: Qwen/Qwen2.5-VL-3B-Instruct
- Dataset: /home/lujunxi57/aokvqa_trl_data
- Output Dir: grpo-Qwen2.5-VL-3B-Instruct

---

```text
Loaded train size: 9930
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|#####     | 1/2 [00:00<00:00,  5.83it/s]Loading checkpoint shards: 100%|##########| 2/2 [00:00<00:00,  8.66it/s]
📁 Training logs directory: /home/lujunxi57/trl/training_logs
📝 Rollout log file: /home/lujunxi57/trl/training_logs/20251022_120531/rollout_results.md
🧠 Attention diagnostics file: /home/lujunxi57/trl/training_logs/20251022_120531/attention_diagnostics.md
  0%|          | 0/29790 [00:00<?, ?it/s]  0%|          | 1/29790 [00:19<159:06:22, 19.23s/it]  0%|          | 2/29790 [00:26<99:54:13, 12.07s/it]   0%|          | 3/29790 [00:37<98:22:44, 11.89s/it]  0%|          | 4/29790 [00:44<82:26:18,  9.96s/it]  0%|          | 5/29790 [00:51<72:26:26,  8.76s/it]  0%|          | 6/29790 [01:01<74:31:49,  9.01s/it]  0%|          | 7/29790 [01:04<59:00:53,  7.13s/it]  0%|          | 8/29790 [01:11<58:45:16,  7.10s/it]  0%|          | 9/29790 [01:20<63:20:08,  7.66s/it]  0%|          | 10/29790 [01:29<67:59:26,  8.22s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.6500
   rewards/mc_idx_reward/std: 0.3536
   rewards/think_format_reward/mean: 0.1500
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 10.8772
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 10813.0000
   completions/mean_length: 53.3500
   completions/min_length: 35.3000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0751, 'grad_norm': 47.75, 'learning_rate': 9.996978851963747e-06, 'num_tokens': 10813.0, 'completions/mean_length': 53.35, 'completions/min_length': 35.3, 'completions/max_length': 71.4, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 53.35, 'completions/min_terminated_length': 35.3, 'completions/max_terminated_length': 71.4, 'attention/early/mdi': 10.87718563079834, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.6588780641555787, 'attention/early/aei_vision': 0.25412718057632444, 'attention/middle/mdi': 6.781097459793091, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.407701516151428, 'attention/middle/aei_vision': 0.36796994507312775, 'attention/late/mdi': 6.338678407669067, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.3452167749404906, 'attention/late/aei_vision': 0.39591469168663024, 'attention/all/mdi': 7.484827995300293, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.4705987691879274, 'attention/all/aei_vision': 0.3393372744321823, 'rewards/mc_idx_reward/mean': 0.65, 'rewards/mc_idx_reward/std': 0.3535533845424652, 'rewards/think_format_reward/mean': 0.15, 'rewards/think_format_reward/std': 0.21213203072547912, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 1.75, 'reward_std': 1.3435028493404388, 'frac_reward_zero_std': 0.4, 'entropy': 0.9559141263365746, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 1.75, 'epoch': 0.0}
  0%|          | 10/29790 [01:29<67:59:26,  8.22s/it]MDI(late): 6.339
  0%|          | 11/29790 [01:33<56:52:24,  6.88s/it]  0%|          | 12/29790 [01:37<48:17:28,  5.84s/it]  0%|          | 13/29790 [01:40<41:13:07,  4.98s/it]  0%|          | 14/29790 [01:42<34:17:37,  4.15s/it]  0%|          | 15/29790 [01:45<31:42:46,  3.83s/it]  0%|          | 16/29790 [01:48<30:41:25,  3.71s/it]  0%|          | 17/29790 [01:51<28:36:40,  3.46s/it]  0%|          | 18/29790 [01:54<27:35:50,  3.34s/it]  0%|          | 19/29790 [01:57<26:55:31,  3.26s/it]  0%|          | 20/29790 [02:00<25:35:01,  3.09s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
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
   rewards/mc_idx_reward/mean: 1.0000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 20267.0000
   completions/mean_length: 2.6000
   completions/min_length: 2.4000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.993622020812354e-06, 'num_tokens': 20267.0, 'completions/mean_length': 2.6, 'completions/min_length': 2.4, 'completions/max_length': 2.8, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 2.6, 'completions/min_terminated_length': 2.4, 'completions/max_terminated_length': 2.8, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 1.0, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -0.4, 'rewards/mdi_reward/std': 0.0, 'reward': 3.6, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.43631379008293153, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 3.6, 'epoch': 0.0}
  0%|          | 20/29790 [02:00<25:35:01,  3.09s/it]MDI(late): 0.000
  0%|          | 21/29790 [02:03<26:08:29,  3.16s/it]  0%|          | 22/29790 [02:07<26:17:39,  3.18s/it]  0%|          | 23/29790 [02:10<26:33:14,  3.21s/it]  0%|          | 24/29790 [02:13<26:51:02,  3.25s/it]  0%|          | 25/29790 [02:16<26:57:58,  3.26s/it]  0%|          | 26/29790 [02:20<27:03:57,  3.27s/it]  0%|          | 27/29790 [02:23<26:30:49,  3.21s/it]  0%|          | 28/29790 [02:26<26:56:38,  3.26s/it]  0%|          | 29/29790 [02:30<27:10:07,  3.29s/it]  0%|          | 30/29790 [02:33<27:06:34,  3.28s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
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
   rewards/mc_idx_reward/mean: 0.7500
   rewards/mc_idx_reward/std: 0.2121
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 30556.0000
   completions/mean_length: 2.4500
   completions/min_length: 2.2000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0, 'grad_norm': 404.0, 'learning_rate': 9.99026518966096e-06, 'num_tokens': 30556.0, 'completions/mean_length': 2.45, 'completions/min_length': 2.2, 'completions/max_length': 2.7, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 2.45, 'completions/min_terminated_length': 2.2, 'completions/max_terminated_length': 2.7, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 0.75, 'rewards/mc_idx_reward/std': 0.21213203072547912, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -0.3, 'rewards/mdi_reward/std': 0.0, 'reward': 2.7, 'reward_std': 0.8485281229019165, 'frac_reward_zero_std': 0.7, 'entropy': 0.38522780127823353, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.7, 'epoch': 0.0}
  0%|          | 30/29790 [02:33<27:06:34,  3.28s/it]MDI(late): 0.000
  0%|          | 31/29790 [02:36<27:57:31,  3.38s/it]  0%|          | 32/29790 [02:40<27:49:50,  3.37s/it]  0%|          | 33/29790 [02:43<26:46:27,  3.24s/it]  0%|          | 34/29790 [02:46<27:38:15,  3.34s/it]  0%|          | 35/29790 [02:49<27:09:46,  3.29s/it]  0%|          | 36/29790 [02:53<27:30:23,  3.33s/it]  0%|          | 37/29790 [02:56<26:29:19,  3.21s/it]  0%|          | 38/29790 [02:59<27:40:57,  3.35s/it]  0%|          | 39/29790 [03:03<27:48:47,  3.37s/it]  0%|          | 40/29790 [03:06<27:51:27,  3.37s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
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
   rewards/mc_idx_reward/mean: 0.5500
   rewards/mc_idx_reward/std: 0.2121
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 41021.0000
   completions/mean_length: 2.2500
   completions/min_length: 2.0000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.986908358509567e-06, 'num_tokens': 41021.0, 'completions/mean_length': 2.25, 'completions/min_length': 2.0, 'completions/max_length': 2.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 2.25, 'completions/min_terminated_length': 2.0, 'completions/max_terminated_length': 2.5, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 0.55, 'rewards/mc_idx_reward/std': 0.21213203072547912, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -0.2, 'rewards/mdi_reward/std': 0.0, 'reward': 2.0, 'reward_std': 0.8485281229019165, 'frac_reward_zero_std': 0.7, 'entropy': 0.3443282537162304, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.0, 'epoch': 0.0}
  0%|          | 40/29790 [03:06<27:51:27,  3.37s/it]MDI(late): 0.000
  0%|          | 41/29790 [03:09<27:01:53,  3.27s/it]  0%|          | 42/29790 [03:12<25:25:40,  3.08s/it]  0%|          | 43/29790 [03:15<26:04:22,  3.16s/it]  0%|          | 44/29790 [03:18<25:54:02,  3.13s/it]  0%|          | 45/29790 [03:22<26:36:44,  3.22s/it]  0%|          | 46/29790 [03:25<26:16:41,  3.18s/it]  0%|          | 47/29790 [03:27<24:46:47,  3.00s/it]  0%|          | 48/29790 [03:31<26:00:43,  3.15s/it]  0%|          | 49/29790 [03:34<25:07:49,  3.04s/it]  0%|          | 50/29790 [03:37<26:02:11,  3.15s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
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
   rewards/mc_idx_reward/mean: 1.0000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 50479.0000
   completions/mean_length: 2.4000
   completions/min_length: 2.2000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.983551527358176e-06, 'num_tokens': 50479.0, 'completions/mean_length': 2.4, 'completions/min_length': 2.2, 'completions/max_length': 2.6, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 2.4, 'completions/min_terminated_length': 2.2, 'completions/max_terminated_length': 2.6, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 1.0, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -0.3, 'rewards/mdi_reward/std': 0.0, 'reward': 3.7, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.24243310503661633, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 3.7, 'epoch': 0.01}
  0%|          | 50/29790 [03:37<26:02:11,  3.15s/it]MDI(late): 0.000
  0%|          | 51/29790 [03:41<26:49:11,  3.25s/it]  0%|          | 52/29790 [03:45<29:33:01,  3.58s/it]  0%|          | 53/29790 [03:47<26:39:04,  3.23s/it]  0%|          | 54/29790 [03:51<28:15:36,  3.42s/it]  0%|          | 55/29790 [03:54<27:24:37,  3.32s/it]  0%|          | 56/29790 [03:57<24:56:27,  3.02s/it]  0%|          | 57/29790 [04:00<26:07:28,  3.16s/it]  0%|          | 58/29790 [04:03<25:51:13,  3.13s/it]  0%|          | 59/29790 [04:07<27:07:53,  3.29s/it]  0%|          | 60/29790 [04:10<26:33:09,  3.22s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
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
   rewards/mc_idx_reward/mean: 0.8000
   rewards/mc_idx_reward/std: 0.1414
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 60787.0000
   completions/mean_length: 2.6000
   completions/min_length: 2.3000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0, 'grad_norm': 122.5, 'learning_rate': 9.980194696206783e-06, 'num_tokens': 60787.0, 'completions/mean_length': 2.6, 'completions/min_length': 2.3, 'completions/max_length': 2.9, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 2.6, 'completions/min_terminated_length': 2.3, 'completions/max_terminated_length': 2.9, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 0.8, 'rewards/mc_idx_reward/std': 0.1414213538169861, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -0.3, 'rewards/mdi_reward/std': 0.0, 'reward': 2.9, 'reward_std': 0.5656854152679444, 'frac_reward_zero_std': 0.8, 'entropy': 0.2940333716571331, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.9, 'epoch': 0.01}
  0%|          | 60/29790 [04:10<26:33:09,  3.22s/it]MDI(late): 0.000
  0%|          | 61/29790 [04:13<25:12:30,  3.05s/it]  0%|          | 62/29790 [04:16<25:57:01,  3.14s/it]  0%|          | 63/29790 [04:20<27:16:33,  3.30s/it]  0%|          | 64/29790 [04:23<28:24:26,  3.44s/it]  0%|          | 65/29790 [04:27<28:15:52,  3.42s/it]  0%|          | 66/29790 [04:30<28:39:06,  3.47s/it]  0%|          | 67/29790 [04:33<27:36:42,  3.34s/it]  0%|          | 68/29790 [04:37<27:47:55,  3.37s/it]  0%|          | 69/29790 [04:40<28:21:42,  3.44s/it]  0%|          | 70/29790 [04:44<28:44:30,  3.48s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
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
   rewards/mc_idx_reward/std: 0.2121
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 71358.0000
   completions/mean_length: 2.4500
   completions/min_length: 2.0000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0, 'grad_norm': 218.0, 'learning_rate': 9.97683786505539e-06, 'num_tokens': 71358.0, 'completions/mean_length': 2.45, 'completions/min_length': 2.0, 'completions/max_length': 2.9, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 2.45, 'completions/min_terminated_length': 2.0, 'completions/max_terminated_length': 2.9, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 0.85, 'rewards/mc_idx_reward/std': 0.21213203072547912, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -0.3, 'rewards/mdi_reward/std': 0.0, 'reward': 3.1, 'reward_std': 0.8485281229019165, 'frac_reward_zero_std': 0.7, 'entropy': 0.2825064279139042, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 3.1, 'epoch': 0.01}
  0%|          | 70/29790 [04:44<28:44:30,  3.48s/it]MDI(late): 0.000
  0%|          | 71/29790 [04:47<26:37:12,  3.22s/it]  0%|          | 72/29790 [04:50<27:37:56,  3.35s/it]  0%|          | 73/29790 [04:53<27:02:04,  3.28s/it]  0%|          | 74/29790 [04:57<27:07:53,  3.29s/it]  0%|          | 75/29790 [05:00<27:00:58,  3.27s/it]  0%|          | 76/29790 [05:03<27:02:51,  3.28s/it]  0%|          | 77/29790 [05:06<26:30:35,  3.21s/it]  0%|          | 78/29790 [05:09<26:08:31,  3.17s/it]  0%|          | 79/29790 [05:12<24:22:53,  2.95s/it]  0%|          | 80/29790 [05:16<26:36:18,  3.22s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
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
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 81219.0000
   completions/mean_length: 2.3500
   completions/min_length: 2.0000
   ... and 11 more metrics
============================================================
                                                     {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.973481033903996e-06, 'num_tokens': 81219.0, 'completions/mean_length': 2.35, 'completions/min_length': 2.0, 'completions/max_length': 2.7, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 2.35, 'completions/min_terminated_length': 2.0, 'completions/max_terminated_length': 2.7, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -0.3, 'rewards/mdi_reward/std': 0.0, 'reward': 3.3, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.18502182252705096, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 3.3, 'epoch': 0.01}
  0%|          | 80/29790 [05:16<26:36:18,  3.22s/it]MDI(late): 0.000
  0%|          | 81/29790 [05:19<27:05:18,  3.28s/it]  0%|          | 82/29790 [05:22<26:30:28,  3.21s/it]  0%|          | 83/29790 [05:26<27:17:29,  3.31s/it]  0%|          | 84/29790 [05:28<25:22:53,  3.08s/it]  0%|          | 85/29790 [05:31<26:00:13,  3.15s/it]  0%|          | 86/29790 [05:35<25:46:50,  3.12s/it]  0%|          | 87/29790 [05:38<26:24:45,  3.20s/it]  0%|          | 88/29790 [05:41<26:41:02,  3.23s/it]  0%|          | 89/29790 [05:44<24:33:16,  2.98s/it]  0%|          | 90/29790 [05:47<25:21:51,  3.07s/it]⚠️  Warning: Metric attention/early/mdi is NaN/Inf: nan
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
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 0.0000
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 0.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 91116.0000
   completions/mean_length: 2.1500
   completions/min_length: 2.0000
   ... and 11 more metrics
============================================================
                                                     {'loss': -0.0303, 'grad_norm': 77.0, 'learning_rate': 9.970124202752603e-06, 'num_tokens': 91116.0, 'completions/mean_length': 2.15, 'completions/min_length': 2.0, 'completions/max_length': 2.3, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 2.15, 'completions/min_terminated_length': 2.0, 'completions/max_terminated_length': 2.3, 'attention/early/mdi': 0.0, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 0.0, 'attention/early/aei_text': 0.0, 'attention/early/aei_vision': 0.0, 'attention/middle/mdi': 0.0, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 0.0, 'attention/middle/aei_text': 0.0, 'attention/middle/aei_vision': 0.0, 'attention/late/mdi': 0.0, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 0.0, 'attention/late/aei_text': 0.0, 'attention/late/aei_vision': 0.0, 'attention/all/mdi': 0.0, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 0.0, 'attention/all/aei_text': 0.0, 'attention/all/aei_vision': 0.0, 'rewards/mc_idx_reward/mean': 0.65, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -0.1, 'rewards/mdi_reward/std': 0.0, 'reward': 2.5, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.24844736624509095, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.5, 'epoch': 0.01}
  0%|          | 90/29790 [05:47<25:21:51,  3.07s/it]MDI(late): 0.000
  0%|          | 91/29790 [05:50<26:36:01,  3.22s/it]  0%|          | 92/29790 [05:54<26:33:35,  3.22s/it]  0%|          | 93/29790 [05:57<27:54:54,  3.38s/it]  0%|          | 94/29790 [06:01<27:44:31,  3.36s/it]  0%|          | 95/29790 [06:04<27:24:43,  3.32s/it]  0%|          | 96/29790 [06:08<28:03:11,  3.40s/it]  0%|          | 97/29790 [06:12<29:24:52,  3.57s/it]  0%|          | 98/29790 [06:15<29:39:17,  3.60s/it]  0%|          | 99/29790 [06:18<28:33:22,  3.46s/it]  0%|          | 100/29790 [06:21<27:29:45,  3.33s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.7000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 18.3324
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 101486.0000
   completions/mean_length: 4.5000
   completions/min_length: 4.4000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.96676737160121e-06, 'num_tokens': 101486.0, 'completions/mean_length': 4.5, 'completions/min_length': 4.4, 'completions/max_length': 4.6, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.5, 'completions/min_terminated_length': 4.4, 'completions/max_terminated_length': 4.6, 'attention/early/mdi': 18.332365417480467, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.009064555168152, 'attention/early/aei_vision': 0.1717055395245552, 'attention/middle/mdi': 12.065401315689087, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.8183123111724853, 'attention/middle/aei_vision': 0.2489149749279022, 'attention/late/mdi': 19.045203495025635, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.0267826557159423, 'attention/late/aei_vision': 0.16465161740779877, 'attention/all/mdi': 15.589738273620606, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9513865232467653, 'attention/all/aei_vision': 0.19509071260690689, 'rewards/mc_idx_reward/mean': 0.7, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 1.8, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.11085367146879435, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 1.8, 'epoch': 0.01}
  0%|          | 100/29790 [06:21<27:29:45,  3.33s/it]MDI(late): 19.045
  0%|          | 101/29790 [06:26<30:25:45,  3.69s/it]  0%|          | 102/29790 [06:30<30:16:35,  3.67s/it]  0%|          | 103/29790 [06:33<30:21:34,  3.68s/it]  0%|          | 104/29790 [06:36<29:12:47,  3.54s/it]  0%|          | 105/29790 [06:40<29:23:41,  3.56s/it]  0%|          | 106/29790 [06:44<30:02:49,  3.64s/it]  0%|          | 107/29790 [06:48<29:57:30,  3.63s/it]  0%|          | 108/29790 [06:51<29:44:41,  3.61s/it]  0%|          | 109/29790 [06:55<30:14:43,  3.67s/it]  0%|          | 110/29790 [06:58<29:40:54,  3.60s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8000
   rewards/mc_idx_reward/std: 0.1414
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 19.4911
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 112538.0000
   completions/mean_length: 5.1000
   completions/min_length: 5.1000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.963410540449817e-06, 'num_tokens': 112538.0, 'completions/mean_length': 5.1, 'completions/min_length': 5.1, 'completions/max_length': 5.1, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 5.1, 'completions/min_terminated_length': 5.1, 'completions/max_terminated_length': 5.1, 'attention/early/mdi': 19.491099548339843, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.1290583848953246, 'attention/early/aei_vision': 0.16994550377130507, 'attention/middle/mdi': 15.21808671951294, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.980575704574585, 'attention/middle/aei_vision': 0.22846689969301223, 'attention/late/mdi': 20.255282974243165, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.151625895500183, 'attention/late/aei_vision': 0.16033673137426377, 'attention/all/mdi': 17.780261707305907, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 3.0870866537094117, 'attention/all/aei_vision': 0.1862497113645077, 'rewards/mc_idx_reward/mean': 0.8, 'rewards/mc_idx_reward/std': 0.1414213538169861, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.2, 'reward_std': 0.5656854152679444, 'frac_reward_zero_std': 0.8, 'entropy': 0.1013243121560663, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.2, 'epoch': 0.01}
  0%|          | 110/29790 [06:58<29:40:54,  3.60s/it]MDI(late): 20.255
  0%|          | 111/29790 [07:02<29:09:26,  3.54s/it]  0%|          | 112/29790 [07:05<28:22:56,  3.44s/it]  0%|          | 113/29790 [07:08<28:35:15,  3.47s/it]  0%|          | 114/29790 [07:11<27:09:14,  3.29s/it]  0%|          | 115/29790 [07:14<25:18:49,  3.07s/it]  0%|          | 116/29790 [07:17<25:07:22,  3.05s/it]  0%|          | 117/29790 [07:20<26:27:35,  3.21s/it]  0%|          | 118/29790 [07:24<27:44:23,  3.37s/it]  0%|          | 119/29790 [07:28<28:26:28,  3.45s/it]  0%|          | 120/29790 [07:32<30:21:36,  3.68s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.7500
   rewards/mc_idx_reward/std: 0.2121
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 17.3613
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 122694.0000
   completions/mean_length: 4.3000
   completions/min_length: 4.3000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 63.0, 'learning_rate': 9.960053709298424e-06, 'num_tokens': 122694.0, 'completions/mean_length': 4.3, 'completions/min_length': 4.3, 'completions/max_length': 4.3, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.3, 'completions/min_terminated_length': 4.3, 'completions/max_terminated_length': 4.3, 'attention/early/mdi': 17.361336421966552, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.9663779497146607, 'attention/early/aei_vision': 0.17729566097259522, 'attention/middle/mdi': 10.622505950927735, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.7461690425872805, 'attention/middle/aei_vision': 0.26928143203258514, 'attention/late/mdi': 19.112454986572267, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.012393355369568, 'attention/late/aei_vision': 0.1603556826710701, 'attention/all/mdi': 14.637618732452392, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9083134651184084, 'attention/all/aei_vision': 0.2023109257221222, 'rewards/mc_idx_reward/mean': 0.75, 'rewards/mc_idx_reward/std': 0.21213203072547912, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.0, 'reward_std': 0.8485281229019165, 'frac_reward_zero_std': 0.7, 'entropy': 0.1090893654152751, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.0, 'epoch': 0.01}
  0%|          | 120/29790 [07:32<30:21:36,  3.68s/it]MDI(late): 19.112
  0%|          | 121/29790 [07:35<29:17:09,  3.55s/it]  0%|          | 122/29790 [07:39<29:49:26,  3.62s/it]  0%|          | 123/29790 [07:43<29:44:07,  3.61s/it]  0%|          | 124/29790 [07:46<29:02:48,  3.52s/it]  0%|          | 125/29790 [07:49<27:44:03,  3.37s/it]  0%|          | 126/29790 [07:52<27:30:48,  3.34s/it]  0%|          | 127/29790 [07:56<28:48:15,  3.50s/it]  0%|          | 128/29790 [08:00<28:47:12,  3.49s/it]  0%|          | 129/29790 [08:03<28:44:35,  3.49s/it]  0%|          | 130/29790 [08:06<28:12:20,  3.42s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 17.5086
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 133134.0000
   completions/mean_length: 4.5000
   completions/min_length: 4.5000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.95669687814703e-06, 'num_tokens': 133134.0, 'completions/mean_length': 4.5, 'completions/min_length': 4.5, 'completions/max_length': 4.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.5, 'completions/min_terminated_length': 4.5, 'completions/max_terminated_length': 4.5, 'attention/early/mdi': 17.508603477478026, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.9754937171936033, 'attention/early/aei_vision': 0.18397579416632653, 'attention/middle/mdi': 13.532855367660522, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.85328688621521, 'attention/middle/aei_vision': 0.2379412055015564, 'attention/late/mdi': 18.907878971099855, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.025362324714661, 'attention/late/aei_vision': 0.16237508356571198, 'attention/all/mdi': 15.92650842666626, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.95138099193573, 'attention/all/aei_vision': 0.19476402848958968, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.048120107222348454, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.01}
  0%|          | 130/29790 [08:06<28:12:20,  3.42s/it]MDI(late): 18.908
  0%|          | 131/29790 [08:10<28:41:30,  3.48s/it]  0%|          | 132/29790 [08:14<29:04:34,  3.53s/it]  0%|          | 133/29790 [08:16<27:24:10,  3.33s/it]  0%|          | 134/29790 [08:20<27:46:48,  3.37s/it]  0%|          | 135/29790 [08:24<28:56:14,  3.51s/it]  0%|          | 136/29790 [08:27<28:20:52,  3.44s/it]  0%|          | 137/29790 [08:31<28:54:10,  3.51s/it]  0%|          | 138/29790 [08:34<28:28:43,  3.46s/it]  0%|          | 139/29790 [08:38<29:16:28,  3.55s/it]  0%|          | 140/29790 [08:41<28:28:08,  3.46s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 15.8659
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 143356.0000
   completions/mean_length: 4.9000
   completions/min_length: 4.8000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.953340046995637e-06, 'num_tokens': 143356.0, 'completions/mean_length': 4.9, 'completions/min_length': 4.8, 'completions/max_length': 5.0, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.9, 'completions/min_terminated_length': 4.8, 'completions/max_terminated_length': 5.0, 'attention/early/mdi': 15.8658878326416, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.9230202436447144, 'attention/early/aei_vision': 0.19487105011940004, 'attention/middle/mdi': 11.573551654815674, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.7554312467575075, 'attention/middle/aei_vision': 0.2651246875524521, 'attention/late/mdi': 18.000134563446046, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.98762993812561, 'attention/late/aei_vision': 0.16773509830236435, 'attention/all/mdi': 14.373983573913574, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.888693857192993, 'attention/all/aei_vision': 0.20924361199140548, 'rewards/mc_idx_reward/mean': 0.85, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.4, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.07852505892515182, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.4, 'epoch': 0.01}
  0%|          | 140/29790 [08:41<28:28:08,  3.46s/it]MDI(late): 18.000
  0%|          | 141/29790 [08:44<26:58:21,  3.28s/it]  0%|          | 142/29790 [08:48<28:40:04,  3.48s/it]  0%|          | 143/29790 [08:52<29:19:02,  3.56s/it]  0%|          | 144/29790 [08:55<29:24:55,  3.57s/it]  0%|          | 145/29790 [08:58<27:20:44,  3.32s/it]  0%|          | 146/29790 [09:02<27:57:37,  3.40s/it]  0%|          | 147/29790 [09:05<28:31:15,  3.46s/it]  0%|          | 148/29790 [09:09<29:27:36,  3.58s/it]  1%|          | 149/29790 [09:12<28:49:46,  3.50s/it]  1%|          | 150/29790 [09:16<29:15:51,  3.55s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.7500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.6818
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 153634.0000
   completions/mean_length: 5.0000
   completions/min_length: 5.0000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.949983215844244e-06, 'num_tokens': 153634.0, 'completions/mean_length': 5.0, 'completions/min_length': 5.0, 'completions/max_length': 5.0, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 5.0, 'completions/min_terminated_length': 5.0, 'completions/max_terminated_length': 5.0, 'attention/early/mdi': 16.681829929351807, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.937326669692993, 'attention/early/aei_vision': 0.18007534593343735, 'attention/middle/mdi': 12.13274621963501, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.7536618232727053, 'attention/middle/aei_vision': 0.2576021611690521, 'attention/late/mdi': 17.19721031188965, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.9511550426483155, 'attention/late/aei_vision': 0.1764044776558876, 'attention/all/mdi': 14.656765460968018, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.880714511871338, 'attention/all/aei_vision': 0.20469399839639663, 'rewards/mc_idx_reward/mean': 0.75, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.0, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.07291387850418687, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.0, 'epoch': 0.02}
  1%|          | 150/29790 [09:16<29:15:51,  3.55s/it]MDI(late): 17.197
  1%|          | 151/29790 [09:19<27:16:31,  3.31s/it]  1%|          | 152/29790 [09:22<27:47:08,  3.37s/it]  1%|          | 153/29790 [09:26<28:12:18,  3.43s/it]  1%|          | 154/29790 [09:29<28:39:38,  3.48s/it]  1%|          | 155/29790 [09:33<28:04:27,  3.41s/it]  1%|          | 156/29790 [09:36<27:38:24,  3.36s/it]  1%|          | 157/29790 [09:40<30:01:23,  3.65s/it]  1%|          | 158/29790 [09:44<29:45:30,  3.62s/it]  1%|          | 159/29790 [09:47<28:39:34,  3.48s/it]  1%|          | 160/29790 [09:50<28:02:44,  3.41s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.9268
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 163946.0000
   completions/mean_length: 4.2000
   completions/min_length: 4.2000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.94662638469285e-06, 'num_tokens': 163946.0, 'completions/mean_length': 4.2, 'completions/min_length': 4.2, 'completions/max_length': 4.2, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.2, 'completions/min_terminated_length': 4.2, 'completions/max_terminated_length': 4.2, 'attention/early/mdi': 16.92678871154785, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.9852097749710085, 'attention/early/aei_vision': 0.1838765561580658, 'attention/middle/mdi': 9.194416809082032, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.684920406341553, 'attention/middle/aei_vision': 0.3075016409158707, 'attention/late/mdi': 17.880288219451906, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.0102913618087768, 'attention/late/aei_vision': 0.17140035480260848, 'attention/all/mdi': 13.49077639579773, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.8934738397598267, 'attention/all/aei_vision': 0.22092618346214293, 'rewards/mc_idx_reward/mean': 0.85, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.4, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.06559544773772359, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.4, 'epoch': 0.02}
  1%|          | 160/29790 [09:50<28:02:44,  3.41s/it]MDI(late): 17.880
  1%|          | 161/29790 [09:54<29:12:21,  3.55s/it]  1%|          | 162/29790 [09:58<29:31:40,  3.59s/it]  1%|          | 163/29790 [10:01<29:23:28,  3.57s/it]  1%|          | 164/29790 [10:04<27:15:23,  3.31s/it]  1%|          | 165/29790 [10:07<27:12:26,  3.31s/it]  1%|          | 166/29790 [10:10<26:19:45,  3.20s/it]  1%|          | 167/29790 [10:13<25:18:52,  3.08s/it]  1%|          | 168/29790 [10:16<25:46:44,  3.13s/it]  1%|          | 169/29790 [10:20<26:48:16,  3.26s/it]  1%|          | 170/29790 [10:24<28:11:43,  3.43s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.7500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 15.8104
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 173660.0000
   completions/mean_length: 4.5000
   completions/min_length: 4.4000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.943269553541457e-06, 'num_tokens': 173660.0, 'completions/mean_length': 4.5, 'completions/min_length': 4.4, 'completions/max_length': 4.6, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.5, 'completions/min_terminated_length': 4.4, 'completions/max_terminated_length': 4.6, 'attention/early/mdi': 15.810350704193116, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.825649642944336, 'attention/early/aei_vision': 0.1888693854212761, 'attention/middle/mdi': 10.189983081817626, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.6205591201782226, 'attention/middle/aei_vision': 0.2821184411644936, 'attention/late/mdi': 17.75614700317383, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.8691756963729858, 'attention/late/aei_vision': 0.16493448317050935, 'attention/all/mdi': 13.611137390136719, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.771794819831848, 'attention/all/aei_vision': 0.21197410076856613, 'rewards/mc_idx_reward/mean': 0.75, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.0, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.08052601180970669, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.0, 'epoch': 0.02}
  1%|          | 170/29790 [10:24<28:11:43,  3.43s/it]MDI(late): 17.756
  1%|          | 171/29790 [10:27<28:04:43,  3.41s/it]  1%|          | 172/29790 [10:30<27:50:56,  3.38s/it]  1%|          | 173/29790 [10:34<28:38:27,  3.48s/it]  1%|          | 174/29790 [10:37<26:55:51,  3.27s/it]  1%|          | 175/29790 [10:41<30:09:29,  3.67s/it]  1%|          | 176/29790 [10:45<30:08:58,  3.67s/it]  1%|          | 177/29790 [10:49<29:50:05,  3.63s/it]  1%|          | 178/29790 [10:52<28:52:50,  3.51s/it]  1%|          | 179/29790 [10:56<29:25:57,  3.58s/it]  1%|          | 180/29790 [10:59<29:53:31,  3.63s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.1414
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 18.7322
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 184360.0000
   completions/mean_length: 5.0000
   completions/min_length: 4.9000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0141, 'grad_norm': 0.0, 'learning_rate': 9.939912722390064e-06, 'num_tokens': 184360.0, 'completions/mean_length': 5.0, 'completions/min_length': 4.9, 'completions/max_length': 5.1, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 5.0, 'completions/min_terminated_length': 4.9, 'completions/max_terminated_length': 5.1, 'attention/early/mdi': 18.732193851470946, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.0422099113464354, 'attention/early/aei_vision': 0.1774417281150818, 'attention/middle/mdi': 15.0155611038208, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.906351828575134, 'attention/middle/aei_vision': 0.23202956691384316, 'attention/late/mdi': 18.012373065948488, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.0542998790740965, 'attention/late/aei_vision': 0.17123442739248276, 'attention/all/mdi': 16.56054277420044, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 3.0009538888931275, 'attention/all/aei_vision': 0.19356857538223265, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.1414213538169861, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.5656854152679444, 'frac_reward_zero_std': 0.8, 'entropy': 0.0651843729079701, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.02}
  1%|          | 180/29790 [10:59<29:53:31,  3.63s/it]MDI(late): 18.012
  1%|          | 181/29790 [11:03<29:45:07,  3.62s/it]  1%|          | 182/29790 [11:06<29:00:36,  3.53s/it]  1%|          | 183/29790 [11:10<29:05:44,  3.54s/it]  1%|          | 184/29790 [11:13<28:22:35,  3.45s/it]  1%|          | 185/29790 [11:17<28:36:12,  3.48s/it]  1%|          | 186/29790 [11:20<28:52:47,  3.51s/it]  1%|          | 187/29790 [11:24<30:42:30,  3.73s/it]  1%|          | 188/29790 [11:28<29:38:26,  3.60s/it]