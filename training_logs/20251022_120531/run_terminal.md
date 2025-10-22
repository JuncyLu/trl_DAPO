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
  1%|          | 181/29790 [11:03<29:45:07,  3.62s/it]  1%|          | 182/29790 [11:06<29:00:36,  3.53s/it]  1%|          | 183/29790 [11:10<29:05:44,  3.54s/it]  1%|          | 184/29790 [11:13<28:22:35,  3.45s/it]  1%|          | 185/29790 [11:17<28:36:12,  3.48s/it]  1%|          | 186/29790 [11:20<28:52:47,  3.51s/it]  1%|          | 187/29790 [11:24<30:42:30,  3.73s/it]  1%|          | 188/29790 [11:28<29:38:26,  3.60s/it]  1%|          | 189/29790 [11:31<28:44:55,  3.50s/it]  1%|          | 190/29790 [11:35<29:08:36,  3.54s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 17.1380
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 195046.0000
   completions/mean_length: 4.5000
   completions/min_length: 4.5000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.936555891238671e-06, 'num_tokens': 195046.0, 'completions/mean_length': 4.5, 'completions/min_length': 4.5, 'completions/max_length': 4.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.5, 'completions/min_terminated_length': 4.5, 'completions/max_terminated_length': 4.5, 'attention/early/mdi': 17.138013935089113, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.0553325414657593, 'attention/early/aei_vision': 0.1884582035243511, 'attention/middle/mdi': 11.564956188201904, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.8636585474014282, 'attention/middle/aei_vision': 0.26725181490182875, 'attention/late/mdi': 19.596726608276366, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.127666640281677, 'attention/late/aei_vision': 0.16080232858657836, 'attention/all/mdi': 15.117444515228271, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 3.015552592277527, 'attention/all/aei_vision': 0.2055041179060936, 'rewards/mc_idx_reward/mean': 0.95, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.8, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.0474378471262753, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.8, 'epoch': 0.02}
  1%|          | 190/29790 [11:35<29:08:36,  3.54s/it]MDI(late): 19.597
  1%|          | 191/29790 [11:38<29:14:18,  3.56s/it]  1%|          | 192/29790 [11:42<29:43:00,  3.61s/it]  1%|          | 193/29790 [11:45<28:58:51,  3.53s/it]  1%|          | 194/29790 [11:48<27:58:22,  3.40s/it]  1%|          | 195/29790 [11:52<28:12:23,  3.43s/it]  1%|          | 196/29790 [11:56<28:56:48,  3.52s/it]  1%|          | 197/29790 [11:58<26:58:22,  3.28s/it]  1%|          | 198/29790 [12:02<26:51:17,  3.27s/it]  1%|          | 199/29790 [12:05<26:48:17,  3.26s/it]  1%|          | 200/29790 [12:08<27:06:03,  3.30s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.6000
   rewards/mc_idx_reward/std: 0.1414
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 15.8062
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 205075.0000
   completions/mean_length: 4.6500
   completions/min_length: 4.6000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0079, 'grad_norm': 0.0, 'learning_rate': 9.933199060087278e-06, 'num_tokens': 205075.0, 'completions/mean_length': 4.65, 'completions/min_length': 4.6, 'completions/max_length': 4.7, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.65, 'completions/min_terminated_length': 4.6, 'completions/max_terminated_length': 4.7, 'attention/early/mdi': 15.806175708770752, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.858423137664795, 'attention/early/aei_vision': 0.19159721136093139, 'attention/middle/mdi': 10.904240560531616, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.649207329750061, 'attention/middle/aei_vision': 0.28383336812257765, 'attention/late/mdi': 18.577902221679686, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.914691925048828, 'attention/late/aei_vision': 0.16529424116015434, 'attention/all/mdi': 14.152844858169555, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.8074407815933227, 'attention/all/aei_vision': 0.21357493847608566, 'rewards/mc_idx_reward/mean': 0.6, 'rewards/mc_idx_reward/std': 0.1414213538169861, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 1.4, 'reward_std': 0.5656854152679444, 'frac_reward_zero_std': 0.8, 'entropy': 0.05283102933899499, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 1.4, 'epoch': 0.02}
  1%|          | 200/29790 [12:08<27:06:03,  3.30s/it]MDI(late): 18.578
  1%|          | 201/29790 [12:11<26:23:53,  3.21s/it]  1%|          | 202/29790 [12:15<26:27:23,  3.22s/it]  1%|          | 203/29790 [12:18<27:26:21,  3.34s/it]  1%|          | 204/29790 [12:22<27:38:46,  3.36s/it]  1%|          | 205/29790 [12:25<28:30:16,  3.47s/it]  1%|          | 206/29790 [12:29<27:58:41,  3.40s/it]  1%|          | 207/29790 [12:32<28:26:56,  3.46s/it]  1%|          | 208/29790 [12:36<28:47:19,  3.50s/it]  1%|          | 209/29790 [12:40<30:09:04,  3.67s/it]  1%|          | 210/29790 [12:44<30:35:57,  3.72s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8500
   rewards/mc_idx_reward/std: 0.2121
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 17.4849
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 215527.0000
   completions/mean_length: 4.9000
   completions/min_length: 4.9000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.929842228935885e-06, 'num_tokens': 215527.0, 'completions/mean_length': 4.9, 'completions/min_length': 4.9, 'completions/max_length': 4.9, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.9, 'completions/min_terminated_length': 4.9, 'completions/max_terminated_length': 4.9, 'attention/early/mdi': 17.484871196746827, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.9947338819503786, 'attention/early/aei_vision': 0.18294825330376624, 'attention/middle/mdi': 11.92380986213684, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.789523792266846, 'attention/middle/aei_vision': 0.2680178165435791, 'attention/late/mdi': 19.499609756469727, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.049432611465454, 'attention/late/aei_vision': 0.1604654684662819, 'attention/all/mdi': 15.281217002868653, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9445634126663207, 'attention/all/aei_vision': 0.20381051301956177, 'rewards/mc_idx_reward/mean': 0.85, 'rewards/mc_idx_reward/std': 0.21213203072547912, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.4, 'reward_std': 0.8485281229019165, 'frac_reward_zero_std': 0.7, 'entropy': 0.036932255019200964, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.4, 'epoch': 0.02}
  1%|          | 210/29790 [12:44<30:35:57,  3.72s/it]MDI(late): 19.500
  1%|          | 211/29790 [12:47<28:35:28,  3.48s/it]  1%|          | 212/29790 [12:50<28:02:37,  3.41s/it]  1%|          | 213/29790 [12:53<28:24:09,  3.46s/it]  1%|          | 214/29790 [12:57<28:41:05,  3.49s/it]  1%|          | 215/29790 [13:01<29:46:12,  3.62s/it]  1%|          | 216/29790 [13:04<29:05:35,  3.54s/it]  1%|          | 217/29790 [13:08<29:21:20,  3.57s/it]  1%|          | 218/29790 [13:12<29:50:28,  3.63s/it]  1%|          | 219/29790 [13:16<30:55:24,  3.76s/it]  1%|          | 220/29790 [13:19<30:48:37,  3.75s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 19.6935
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 226219.0000
   completions/mean_length: 4.3000
   completions/min_length: 4.2000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.926485397784491e-06, 'num_tokens': 226219.0, 'completions/mean_length': 4.3, 'completions/min_length': 4.2, 'completions/max_length': 4.4, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.3, 'completions/min_terminated_length': 4.2, 'completions/max_terminated_length': 4.4, 'attention/early/mdi': 19.693452835083008, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.1213385105133056, 'attention/early/aei_vision': 0.16653185784816743, 'attention/middle/mdi': 11.713134384155273, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.861613941192627, 'attention/middle/aei_vision': 0.2727513238787651, 'attention/late/mdi': 21.93872537612915, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.149860167503357, 'attention/late/aei_vision': 0.15311499312520027, 'attention/all/mdi': 16.28294153213501, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 3.044270920753479, 'attention/all/aei_vision': 0.19746605902910233, 'rewards/mc_idx_reward/mean': 0.8, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.2, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.034817102167289705, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.2, 'epoch': 0.02}
  1%|          | 220/29790 [13:19<30:48:37,  3.75s/it]MDI(late): 21.939
  1%|          | 221/29790 [13:23<30:47:37,  3.75s/it]  1%|          | 222/29790 [13:27<30:12:28,  3.68s/it]  1%|          | 223/29790 [13:30<28:44:17,  3.50s/it]  1%|          | 224/29790 [13:33<28:47:27,  3.51s/it]  1%|          | 225/29790 [13:37<28:52:14,  3.52s/it]  1%|          | 226/29790 [13:40<27:31:36,  3.35s/it]  1%|          | 227/29790 [13:43<27:27:14,  3.34s/it]  1%|          | 228/29790 [13:47<27:58:07,  3.41s/it]  1%|          | 229/29790 [13:50<27:49:23,  3.39s/it]  1%|          | 230/29790 [13:54<28:07:15,  3.42s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 1.0000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.5609
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 236365.0000
   completions/mean_length: 4.5000
   completions/min_length: 4.5000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.923128566633098e-06, 'num_tokens': 236365.0, 'completions/mean_length': 4.5, 'completions/min_length': 4.5, 'completions/max_length': 4.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.5, 'completions/min_terminated_length': 4.5, 'completions/max_terminated_length': 4.5, 'attention/early/mdi': 16.56086187362671, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.8914178371429444, 'attention/early/aei_vision': 0.17737441658973693, 'attention/middle/mdi': 11.239607286453246, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.642721676826477, 'attention/middle/aei_vision': 0.2861193954944611, 'attention/late/mdi': 20.44236488342285, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.941608691215515, 'attention/late/aei_vision': 0.1572719432413578, 'attention/all/mdi': 14.63321590423584, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.8252493858337404, 'attention/all/aei_vision': 0.20692192018032074, 'rewards/mc_idx_reward/mean': 1.0, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 3.0, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.027784441091353074, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 3.0, 'epoch': 0.02}
  1%|          | 230/29790 [13:54<28:07:15,  3.42s/it]MDI(late): 20.442
  1%|          | 231/29790 [13:57<28:32:50,  3.48s/it]  1%|          | 232/29790 [14:00<27:53:12,  3.40s/it]  1%|          | 233/29790 [14:03<26:20:03,  3.21s/it]  1%|          | 234/29790 [14:06<26:27:45,  3.22s/it]  1%|          | 235/29790 [14:10<26:39:13,  3.25s/it]  1%|          | 236/29790 [14:13<26:43:02,  3.25s/it]  1%|          | 237/29790 [14:16<25:34:36,  3.12s/it]  1%|          | 238/29790 [14:19<25:55:35,  3.16s/it]  1%|          | 239/29790 [14:23<27:14:31,  3.32s/it]  1%|          | 240/29790 [14:25<26:01:00,  3.17s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 15.7744
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 245738.0000
   completions/mean_length: 4.3500
   completions/min_length: 4.3000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.919771735481705e-06, 'num_tokens': 245738.0, 'completions/mean_length': 4.35, 'completions/min_length': 4.3, 'completions/max_length': 4.4, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.35, 'completions/min_terminated_length': 4.3, 'completions/max_terminated_length': 4.4, 'attention/early/mdi': 15.774425983428955, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.7273515939712523, 'attention/early/aei_vision': 0.18217068314552307, 'attention/middle/mdi': 10.870440244674683, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.526510715484619, 'attention/middle/aei_vision': 0.27544006109237673, 'attention/late/mdi': 18.05921001434326, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.772262525558472, 'attention/late/aei_vision': 0.15762414559721946, 'attention/all/mdi': 13.676620483398438, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.6753749370574953, 'attention/all/aei_vision': 0.20507829785346984, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.06272358645801432, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.02}
  1%|          | 240/29790 [14:26<26:01:00,  3.17s/it]MDI(late): 18.059
  1%|          | 241/29790 [14:29<26:24:16,  3.22s/it]  1%|          | 242/29790 [14:32<26:32:42,  3.23s/it]  1%|          | 243/29790 [14:36<27:38:27,  3.37s/it]  1%|          | 244/29790 [14:39<28:32:09,  3.48s/it]  1%|          | 245/29790 [14:43<28:28:27,  3.47s/it]  1%|          | 246/29790 [14:46<28:10:49,  3.43s/it]  1%|          | 247/29790 [14:50<28:52:00,  3.52s/it]  1%|          | 248/29790 [14:54<28:49:15,  3.51s/it]  1%|          | 249/29790 [14:57<28:07:08,  3.43s/it]  1%|          | 250/29790 [15:00<27:49:29,  3.39s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.3541
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 256176.0000
   completions/mean_length: 4.5000
   completions/min_length: 4.5000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.916414904330312e-06, 'num_tokens': 256176.0, 'completions/mean_length': 4.5, 'completions/min_length': 4.5, 'completions/max_length': 4.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.5, 'completions/min_terminated_length': 4.5, 'completions/max_terminated_length': 4.5, 'attention/early/mdi': 16.354108810424805, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.966778874397278, 'attention/early/aei_vision': 0.18829617276787758, 'attention/middle/mdi': 12.231393909454345, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.814402198791504, 'attention/middle/aei_vision': 0.24771914780139923, 'attention/late/mdi': 18.459844970703124, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.022762632369995, 'attention/late/aei_vision': 0.16483373790979386, 'attention/all/mdi': 15.015249347686767, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9346478939056397, 'attention/all/aei_vision': 0.20028301775455476, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.027819848753279076, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.03}
  1%|          | 250/29790 [15:00<27:49:29,  3.39s/it]MDI(late): 18.460
  1%|          | 251/29790 [15:03<27:39:06,  3.37s/it]  1%|          | 252/29790 [15:07<27:29:02,  3.35s/it]  1%|          | 253/29790 [15:11<28:41:32,  3.50s/it]  1%|          | 254/29790 [15:14<28:31:02,  3.48s/it]  1%|          | 255/29790 [15:17<28:41:24,  3.50s/it]  1%|          | 256/29790 [15:20<26:51:15,  3.27s/it]  1%|          | 257/29790 [15:23<26:31:27,  3.23s/it]  1%|          | 258/29790 [15:27<26:59:19,  3.29s/it]  1%|          | 259/29790 [15:31<29:00:29,  3.54s/it]  1%|          | 260/29790 [15:34<28:30:01,  3.47s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.7500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.3870
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 266267.0000
   completions/mean_length: 4.5500
   completions/min_length: 4.5000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 112.0, 'learning_rate': 9.913058073178919e-06, 'num_tokens': 266267.0, 'completions/mean_length': 4.55, 'completions/min_length': 4.5, 'completions/max_length': 4.6, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.55, 'completions/min_terminated_length': 4.5, 'completions/max_terminated_length': 4.6, 'attention/early/mdi': 16.38701972961426, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.8914130687713624, 'attention/early/aei_vision': 0.17889281511306762, 'attention/middle/mdi': 10.816261816024781, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.694432806968689, 'attention/middle/aei_vision': 0.2622073844075203, 'attention/late/mdi': 18.157799243927002, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.926704502105713, 'attention/late/aei_vision': 0.1669865667819977, 'attention/all/mdi': 14.233931732177734, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.8375168323516844, 'attention/all/aei_vision': 0.20269559174776078, 'rewards/mc_idx_reward/mean': 0.75, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.0, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.08013210261124186, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.0, 'epoch': 0.03}
  1%|          | 260/29790 [15:34<28:30:01,  3.47s/it]MDI(late): 18.158
  1%|          | 261/29790 [15:38<28:32:41,  3.48s/it]  1%|          | 262/29790 [15:41<26:58:40,  3.29s/it]  1%|          | 263/29790 [15:43<25:00:29,  3.05s/it]  1%|          | 264/29790 [15:47<26:16:00,  3.20s/it]  1%|          | 265/29790 [15:50<26:33:36,  3.24s/it]  1%|          | 266/29790 [15:53<27:02:35,  3.30s/it]  1%|          | 267/29790 [15:57<26:53:22,  3.28s/it]  1%|          | 268/29790 [16:00<27:40:52,  3.38s/it]  1%|          | 269/29790 [16:04<28:48:12,  3.51s/it]  1%|          | 270/29790 [16:08<29:33:22,  3.60s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 1.0000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 15.4899
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 276201.0000
   completions/mean_length: 4.5000
   completions/min_length: 4.5000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.909701242027527e-06, 'num_tokens': 276201.0, 'completions/mean_length': 4.5, 'completions/min_length': 4.5, 'completions/max_length': 4.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.5, 'completions/min_terminated_length': 4.5, 'completions/max_terminated_length': 4.5, 'attention/early/mdi': 15.489862871170043, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.8181715965270997, 'attention/early/aei_vision': 0.19551354348659516, 'attention/middle/mdi': 10.495360517501831, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.5984790682792664, 'attention/middle/aei_vision': 0.30275083556771276, 'attention/late/mdi': 16.857155132293702, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.86297767162323, 'attention/late/aei_vision': 0.17357569187879562, 'attention/all/mdi': 13.355361986160279, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.759876084327698, 'attention/all/aei_vision': 0.22394668757915498, 'rewards/mc_idx_reward/mean': 1.0, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 3.0, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.01969574545219075, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 3.0, 'epoch': 0.03}
  1%|          | 270/29790 [16:08<29:33:22,  3.60s/it]MDI(late): 16.857
  1%|          | 271/29790 [16:11<29:01:50,  3.54s/it]  1%|          | 272/29790 [16:15<28:24:03,  3.46s/it]  1%|          | 273/29790 [16:18<28:08:17,  3.43s/it]  1%|          | 274/29790 [16:21<28:30:40,  3.48s/it]  1%|          | 275/29790 [16:25<29:17:45,  3.57s/it]  1%|          | 276/29790 [16:29<28:30:13,  3.48s/it]  1%|          | 277/29790 [16:32<28:56:30,  3.53s/it]  1%|          | 278/29790 [16:36<30:32:55,  3.73s/it]  1%|          | 279/29790 [16:40<30:52:53,  3.77s/it]  1%|          | 280/29790 [16:44<29:38:46,  3.62s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.7000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 19.0329
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 286930.0000
   completions/mean_length: 4.2500
   completions/min_length: 4.2000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.906344410876134e-06, 'num_tokens': 286930.0, 'completions/mean_length': 4.25, 'completions/min_length': 4.2, 'completions/max_length': 4.3, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.25, 'completions/min_terminated_length': 4.2, 'completions/max_terminated_length': 4.3, 'attention/early/mdi': 19.03292074203491, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.1101556062698363, 'attention/early/aei_vision': 0.17155682891607285, 'attention/middle/mdi': 12.574462175369263, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.9058412313461304, 'attention/middle/aei_vision': 0.2527985259890556, 'attention/late/mdi': 20.736707878112792, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.156445097923279, 'attention/late/aei_vision': 0.153434619307518, 'attention/all/mdi': 16.396506690979002, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 3.0574806928634644, 'attention/all/aei_vision': 0.1925966575741768, 'rewards/mc_idx_reward/mean': 0.7, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 1.8, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.051431936537846924, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 1.8, 'epoch': 0.03}
  1%|          | 280/29790 [16:44<29:38:46,  3.62s/it]MDI(late): 20.737
  1%|          | 281/29790 [16:46<28:03:53,  3.42s/it]  1%|          | 282/29790 [16:50<28:23:17,  3.46s/it]  1%|          | 283/29790 [16:53<27:50:26,  3.40s/it]  1%|          | 284/29790 [16:57<27:34:57,  3.37s/it]  1%|          | 285/29790 [17:00<27:36:07,  3.37s/it]  1%|          | 286/29790 [17:03<27:35:07,  3.37s/it]  1%|          | 287/29790 [17:07<28:16:10,  3.45s/it]  1%|          | 288/29790 [17:10<26:50:31,  3.28s/it]  1%|          | 289/29790 [17:14<29:11:40,  3.56s/it]  1%|          | 290/29790 [17:17<28:41:15,  3.50s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.7000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.8892
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 296982.0000
   completions/mean_length: 4.7000
   completions/min_length: 4.7000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.90298757972474e-06, 'num_tokens': 296982.0, 'completions/mean_length': 4.7, 'completions/min_length': 4.7, 'completions/max_length': 4.7, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.7, 'completions/min_terminated_length': 4.7, 'completions/max_terminated_length': 4.7, 'attention/early/mdi': 16.889183712005615, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.874567413330078, 'attention/early/aei_vision': 0.17746822237968446, 'attention/middle/mdi': 10.851164722442627, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.6744808673858644, 'attention/middle/aei_vision': 0.267114482820034, 'attention/late/mdi': 17.537621307373048, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.8956963300704954, 'attention/late/aei_vision': 0.16691183894872666, 'attention/all/mdi': 14.204094791412354, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.814914870262146, 'attention/all/aei_vision': 0.2038315162062645, 'rewards/mc_idx_reward/mean': 0.7, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 1.8, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.046972978650592266, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 1.8, 'epoch': 0.03}
  1%|          | 290/29790 [17:17<28:41:15,  3.50s/it]MDI(late): 17.538
  1%|          | 291/29790 [17:20<27:05:59,  3.31s/it]  1%|          | 292/29790 [17:24<27:32:45,  3.36s/it]  1%|          | 293/29790 [17:27<27:19:39,  3.34s/it]  1%|          | 294/29790 [17:31<27:52:02,  3.40s/it]  1%|          | 295/29790 [17:34<27:33:44,  3.36s/it]  1%|          | 296/29790 [17:37<28:11:12,  3.44s/it]  1%|          | 297/29790 [17:41<29:15:01,  3.57s/it]  1%|1         | 298/29790 [17:45<28:40:38,  3.50s/it]  1%|1         | 299/29790 [17:48<28:17:34,  3.45s/it]  1%|1         | 300/29790 [17:52<28:37:27,  3.49s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.2770
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 307106.0000
   completions/mean_length: 4.8000
   completions/min_length: 4.8000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.899630748573347e-06, 'num_tokens': 307106.0, 'completions/mean_length': 4.8, 'completions/min_length': 4.8, 'completions/max_length': 4.8, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.8, 'completions/min_terminated_length': 4.8, 'completions/max_terminated_length': 4.8, 'attention/early/mdi': 16.276996612548828, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.868638443946838, 'attention/early/aei_vision': 0.18069154918193817, 'attention/middle/mdi': 10.273377275466919, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.6601945877075197, 'attention/middle/aei_vision': 0.26830820441246034, 'attention/late/mdi': 17.983819675445556, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.9098377227783203, 'attention/late/aei_vision': 0.16379527151584625, 'attention/all/mdi': 13.981552791595458, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.8128902673721314, 'attention/all/aei_vision': 0.20426500886678695, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.02391213210648857, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.03}
  1%|1         | 300/29790 [17:52<28:37:27,  3.49s/it]MDI(late): 17.984
  1%|1         | 301/29790 [17:56<29:46:44,  3.64s/it]  1%|1         | 302/29790 [17:59<29:36:51,  3.62s/it]  1%|1         | 303/29790 [18:03<29:38:51,  3.62s/it]  1%|1         | 304/29790 [18:06<29:03:28,  3.55s/it]  1%|1         | 305/29790 [18:10<29:18:13,  3.58s/it]  1%|1         | 306/29790 [18:13<29:20:56,  3.58s/it]  1%|1         | 307/29790 [18:17<28:36:46,  3.49s/it]  1%|1         | 308/29790 [18:20<28:09:33,  3.44s/it]  1%|1         | 309/29790 [18:24<28:22:52,  3.47s/it]  1%|1         | 310/29790 [18:27<28:28:08,  3.48s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.4370
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 317590.0000
   completions/mean_length: 4.7000
   completions/min_length: 4.7000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.896273917421954e-06, 'num_tokens': 317590.0, 'completions/mean_length': 4.7, 'completions/min_length': 4.7, 'completions/max_length': 4.7, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.7, 'completions/min_terminated_length': 4.7, 'completions/max_terminated_length': 4.7, 'attention/early/mdi': 16.436995220184325, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.989505910873413, 'attention/early/aei_vision': 0.18412692248821258, 'attention/middle/mdi': 9.78285002708435, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.7361828804016115, 'attention/middle/aei_vision': 0.2874688312411308, 'attention/late/mdi': 22.17178554534912, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.061031675338745, 'attention/late/aei_vision': 0.15523534640669823, 'attention/all/mdi': 14.31392412185669, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9289068460464476, 'attention/all/aei_vision': 0.20894369930028917, 'rewards/mc_idx_reward/mean': 0.85, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.4, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.030040350157651118, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.4, 'epoch': 0.03}
  1%|1         | 310/29790 [18:27<28:28:08,  3.48s/it]MDI(late): 22.172
  1%|1         | 311/29790 [18:31<28:50:47,  3.52s/it]  1%|1         | 312/29790 [18:34<28:32:42,  3.49s/it]  1%|1         | 313/29790 [18:38<28:26:12,  3.47s/it]  1%|1         | 314/29790 [18:42<31:08:33,  3.80s/it]  1%|1         | 315/29790 [18:45<30:06:09,  3.68s/it]  1%|1         | 316/29790 [18:49<30:46:28,  3.76s/it]  1%|1         | 317/29790 [18:53<29:54:43,  3.65s/it]  1%|1         | 318/29790 [18:57<30:34:22,  3.73s/it]  1%|1         | 319/29790 [19:00<29:23:38,  3.59s/it]  1%|1         | 320/29790 [19:03<28:32:44,  3.49s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 17.3475
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 328132.0000
   completions/mean_length: 5.8000
   completions/min_length: 5.8000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.892917086270561e-06, 'num_tokens': 328132.0, 'completions/mean_length': 5.8, 'completions/min_length': 5.8, 'completions/max_length': 5.8, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 5.8, 'completions/min_terminated_length': 5.8, 'completions/max_terminated_length': 5.8, 'attention/early/mdi': 17.347477149963378, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.9642354011535645, 'attention/early/aei_vision': 0.18454466238617898, 'attention/middle/mdi': 11.689776706695557, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.719580340385437, 'attention/middle/aei_vision': 0.28583023995161055, 'attention/late/mdi': 18.776623058319093, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.0063628435134886, 'attention/late/aei_vision': 0.16722793206572534, 'attention/all/mdi': 14.911917686462402, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.896726202964783, 'attention/all/aei_vision': 0.2125342771410942, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.024068745819386096, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.03}
  1%|1         | 320/29790 [19:03<28:32:44,  3.49s/it]MDI(late): 18.777
  1%|1         | 321/29790 [19:06<27:00:55,  3.30s/it]  1%|1         | 322/29790 [19:10<27:43:00,  3.39s/it]  1%|1         | 323/29790 [19:13<27:45:55,  3.39s/it]  1%|1         | 324/29790 [19:17<30:07:17,  3.68s/it]  1%|1         | 325/29790 [19:21<29:07:18,  3.56s/it]  1%|1         | 326/29790 [19:25<29:43:50,  3.63s/it]  1%|1         | 327/29790 [19:28<28:13:57,  3.45s/it]  1%|1         | 328/29790 [19:32<29:33:39,  3.61s/it]  1%|1         | 329/29790 [19:35<29:34:56,  3.61s/it]  1%|1         | 330/29790 [19:38<28:47:24,  3.52s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.5514
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 338528.0000
   completions/mean_length: 4.7000
   completions/min_length: 4.7000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.889560255119168e-06, 'num_tokens': 338528.0, 'completions/mean_length': 4.7, 'completions/min_length': 4.7, 'completions/max_length': 4.7, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.7, 'completions/min_terminated_length': 4.7, 'completions/max_terminated_length': 4.7, 'attention/early/mdi': 16.55141191482544, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.9590837478637697, 'attention/early/aei_vision': 0.18773469775915147, 'attention/middle/mdi': 10.092568111419677, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.6994839668273927, 'attention/middle/aei_vision': 0.29921684712171553, 'attention/late/mdi': 18.101426124572754, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.0068729877471925, 'attention/late/aei_vision': 0.17019052654504777, 'attention/all/mdi': 13.921322107315063, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.888480234146118, 'attention/all/aei_vision': 0.21904735416173934, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.025965183292282746, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.03}
  1%|1         | 330/29790 [19:39<28:47:24,  3.52s/it]MDI(late): 18.101
  1%|1         | 331/29790 [19:42<29:57:14,  3.66s/it]  1%|1         | 332/29790 [19:46<29:41:15,  3.63s/it]  1%|1         | 333/29790 [19:50<29:51:54,  3.65s/it]  1%|1         | 334/29790 [19:52<27:27:09,  3.36s/it]  1%|1         | 335/29790 [19:56<28:35:57,  3.50s/it]  1%|1         | 336/29790 [19:59<27:42:57,  3.39s/it]  1%|1         | 337/29790 [20:04<29:43:07,  3.63s/it]  1%|1         | 338/29790 [20:07<29:00:08,  3.55s/it]  1%|1         | 339/29790 [20:10<29:10:51,  3.57s/it]  1%|1         | 340/29790 [20:14<28:38:08,  3.50s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 15.9841
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 349012.0000
   completions/mean_length: 4.5000
   completions/min_length: 4.5000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.886203423967775e-06, 'num_tokens': 349012.0, 'completions/mean_length': 4.5, 'completions/min_length': 4.5, 'completions/max_length': 4.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.5, 'completions/min_terminated_length': 4.5, 'completions/max_terminated_length': 4.5, 'attention/early/mdi': 15.984062576293946, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.975176286697388, 'attention/early/aei_vision': 0.19441206902265548, 'attention/middle/mdi': 11.66304407119751, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.7768784523010255, 'attention/middle/aei_vision': 0.27668256387114526, 'attention/late/mdi': 18.006647872924805, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.026029109954834, 'attention/late/aei_vision': 0.17412574142217635, 'attention/all/mdi': 14.441991662979126, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.926027941703796, 'attention/all/aei_vision': 0.21507345885038376, 'rewards/mc_idx_reward/mean': 0.95, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.8, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.035687485319795084, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.8, 'epoch': 0.03}
  1%|1         | 340/29790 [20:14<28:38:08,  3.50s/it]MDI(late): 18.007
  1%|1         | 341/29790 [20:18<29:09:45,  3.56s/it]  1%|1         | 342/29790 [20:20<27:27:24,  3.36s/it]  1%|1         | 343/29790 [20:24<28:04:51,  3.43s/it]  1%|1         | 344/29790 [20:27<27:24:30,  3.35s/it]  1%|1         | 345/29790 [20:31<27:46:46,  3.40s/it]  1%|1         | 346/29790 [20:34<27:33:28,  3.37s/it]  1%|1         | 347/29790 [20:38<28:00:41,  3.42s/it]  1%|1         | 348/29790 [20:41<28:18:40,  3.46s/it]  1%|1         | 349/29790 [20:45<29:14:53,  3.58s/it]  1%|1         | 350/29790 [20:49<29:44:29,  3.64s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 17.2193
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 359075.0000
   completions/mean_length: 5.0500
   completions/min_length: 5.0000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.882846592816381e-06, 'num_tokens': 359075.0, 'completions/mean_length': 5.05, 'completions/min_length': 5.0, 'completions/max_length': 5.1, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 5.05, 'completions/min_terminated_length': 5.0, 'completions/max_terminated_length': 5.1, 'attention/early/mdi': 17.219272422790528, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.878404068946838, 'attention/early/aei_vision': 0.17760223820805549, 'attention/middle/mdi': 10.542015218734742, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.6702837467193605, 'attention/middle/aei_vision': 0.2681324392557144, 'attention/late/mdi': 17.674666786193846, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.9001448154449463, 'attention/late/aei_vision': 0.16779273748397827, 'attention/all/mdi': 14.098438453674316, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.816277503967285, 'attention/all/aei_vision': 0.20450914055109023, 'rewards/mc_idx_reward/mean': 0.8, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.2, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.04636644781567156, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.2, 'epoch': 0.04}
  1%|1         | 350/29790 [20:49<29:44:29,  3.64s/it]MDI(late): 17.675
  1%|1         | 351/29790 [20:52<29:57:29,  3.66s/it]  1%|1         | 352/29790 [20:56<30:17:49,  3.71s/it]  1%|1         | 353/29790 [21:00<30:46:42,  3.76s/it]  1%|1         | 354/29790 [21:04<30:38:40,  3.75s/it]  1%|1         | 355/29790 [21:08<32:17:12,  3.95s/it]  1%|1         | 356/29790 [21:12<30:55:52,  3.78s/it]  1%|1         | 357/29790 [21:15<29:52:27,  3.65s/it]  1%|1         | 358/29790 [21:19<30:10:57,  3.69s/it]  1%|1         | 359/29790 [21:23<31:30:48,  3.85s/it]  1%|1         | 360/29790 [21:27<30:32:05,  3.74s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.1414
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 19.9451
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 370102.0000
   completions/mean_length: 4.5500
   completions/min_length: 4.5000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0079, 'grad_norm': 0.0, 'learning_rate': 9.879489761664988e-06, 'num_tokens': 370102.0, 'completions/mean_length': 4.55, 'completions/min_length': 4.5, 'completions/max_length': 4.6, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.55, 'completions/min_terminated_length': 4.5, 'completions/max_terminated_length': 4.6, 'attention/early/mdi': 19.945056915283203, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.1883429050445558, 'attention/early/aei_vision': 0.17118156403303147, 'attention/middle/mdi': 12.7273099899292, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.9805203437805177, 'attention/middle/aei_vision': 0.24774961024522782, 'attention/late/mdi': 20.168927955627442, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.201833200454712, 'attention/late/aei_vision': 0.164405021071434, 'attention/all/mdi': 16.70904674530029, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 3.1235654830932615, 'attention/all/aei_vision': 0.1944453999400139, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.1414213538169861, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.5656854152679444, 'frac_reward_zero_std': 0.8, 'entropy': 0.03999841546174139, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.04}
  1%|1         | 360/29790 [21:27<30:32:05,  3.74s/it]MDI(late): 20.169
  1%|1         | 361/29790 [21:30<29:47:15,  3.64s/it]  1%|1         | 362/29790 [21:34<30:56:30,  3.79s/it]  1%|1         | 363/29790 [21:38<30:51:05,  3.77s/it]  1%|1         | 364/29790 [21:42<31:10:44,  3.81s/it]  1%|1         | 365/29790 [21:45<30:49:39,  3.77s/it]  1%|1         | 366/29790 [21:49<29:40:32,  3.63s/it]  1%|1         | 367/29790 [21:52<29:00:22,  3.55s/it]  1%|1         | 368/29790 [21:56<29:41:50,  3.63s/it]  1%|1         | 369/29790 [22:00<29:58:37,  3.67s/it]  1%|1         | 370/29790 [22:03<30:04:22,  3.68s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 1.0000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.1858
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 380890.0000
   completions/mean_length: 5.4000
   completions/min_length: 5.4000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.876132930513595e-06, 'num_tokens': 380890.0, 'completions/mean_length': 5.4, 'completions/min_length': 5.4, 'completions/max_length': 5.4, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 5.4, 'completions/min_terminated_length': 5.4, 'completions/max_terminated_length': 5.4, 'attention/early/mdi': 16.185803413391113, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.0361748933792114, 'attention/early/aei_vision': 0.19279610067605973, 'attention/middle/mdi': 9.624293327331543, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.7388644456863402, 'attention/middle/aei_vision': 0.3094305470585823, 'attention/late/mdi': 19.407532215118408, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.107512354850769, 'attention/late/aei_vision': 0.16553197652101517, 'attention/all/mdi': 13.759040927886963, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9608505725860597, 'attention/all/aei_vision': 0.22258620858192443, 'rewards/mc_idx_reward/mean': 1.0, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 3.0, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.006510117411380634, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 3.0, 'epoch': 0.04}
  1%|1         | 370/29790 [22:03<30:04:22,  3.68s/it]MDI(late): 19.408
  1%|1         | 371/29790 [22:06<28:02:25,  3.43s/it]  1%|1         | 372/29790 [22:10<28:26:44,  3.48s/it]  1%|1         | 373/29790 [22:13<28:09:14,  3.45s/it]  1%|1         | 374/29790 [22:17<28:00:02,  3.43s/it]  1%|1         | 375/29790 [22:20<28:25:18,  3.48s/it]  1%|1         | 376/29790 [22:24<29:12:03,  3.57s/it]  1%|1         | 377/29790 [22:28<31:15:28,  3.83s/it]  1%|1         | 378/29790 [22:32<30:35:35,  3.74s/it]  1%|1         | 379/29790 [22:36<30:16:40,  3.71s/it]  1%|1         | 380/29790 [22:38<28:29:02,  3.49s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.7500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 17.9479
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 391218.0000
   completions/mean_length: 4.7000
   completions/min_length: 4.7000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.872776099362202e-06, 'num_tokens': 391218.0, 'completions/mean_length': 4.7, 'completions/min_length': 4.7, 'completions/max_length': 4.7, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.7, 'completions/min_terminated_length': 4.7, 'completions/max_terminated_length': 4.7, 'attention/early/mdi': 17.94793243408203, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.9735509157180786, 'attention/early/aei_vision': 0.17186284959316253, 'attention/middle/mdi': 10.671830797195435, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.709278702735901, 'attention/middle/aei_vision': 0.2794130027294159, 'attention/late/mdi': 21.48428792953491, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.0320316314697267, 'attention/late/aei_vision': 0.14654771611094475, 'attention/all/mdi': 15.040570545196534, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.904953718185425, 'attention/all/aei_vision': 0.19927452504634857, 'rewards/mc_idx_reward/mean': 0.75, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.0, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.07235476889181883, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.0, 'epoch': 0.04}
  1%|1         | 380/29790 [22:39<28:29:02,  3.49s/it]MDI(late): 21.484
  1%|1         | 381/29790 [22:42<28:59:09,  3.55s/it]  1%|1         | 382/29790 [22:46<28:48:51,  3.53s/it]  1%|1         | 383/29790 [22:49<28:29:55,  3.49s/it]  1%|1         | 384/29790 [22:53<28:35:02,  3.50s/it]  1%|1         | 385/29790 [22:55<26:34:52,  3.25s/it]  1%|1         | 386/29790 [22:59<27:27:33,  3.36s/it]  1%|1         | 387/29790 [23:02<27:53:25,  3.41s/it]  1%|1         | 388/29790 [23:06<28:08:04,  3.44s/it]  1%|1         | 389/29790 [23:10<28:31:31,  3.49s/it]  1%|1         | 390/29790 [23:13<27:38:26,  3.38s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.7000
   rewards/mc_idx_reward/std: 0.1414
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 15.3154
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 401167.0000
   completions/mean_length: 4.8500
   completions/min_length: 4.8000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0079, 'grad_norm': 0.0, 'learning_rate': 9.86941926821081e-06, 'num_tokens': 401167.0, 'completions/mean_length': 4.85, 'completions/min_length': 4.8, 'completions/max_length': 4.9, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.85, 'completions/min_terminated_length': 4.8, 'completions/max_terminated_length': 4.9, 'attention/early/mdi': 15.31541175842285, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.8723380327224732, 'attention/early/aei_vision': 0.19236124604940413, 'attention/middle/mdi': 9.101696300506593, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.615219330787659, 'attention/middle/aei_vision': 0.29851437360048294, 'attention/late/mdi': 18.322033500671388, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.9238223791122437, 'attention/late/aei_vision': 0.17083529159426689, 'attention/all/mdi': 12.914132881164551, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.8037932395935057, 'attention/all/aei_vision': 0.22057030498981475, 'rewards/mc_idx_reward/mean': 0.7, 'rewards/mc_idx_reward/std': 0.1414213538169861, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 1.8, 'reward_std': 0.5656854152679444, 'frac_reward_zero_std': 0.8, 'entropy': 0.050061339139938356, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 1.8, 'epoch': 0.04}
  1%|1         | 390/29790 [23:13<27:38:26,  3.38s/it]MDI(late): 18.322
  1%|1         | 391/29790 [23:16<28:19:50,  3.47s/it]  1%|1         | 392/29790 [23:20<28:05:27,  3.44s/it]  1%|1         | 393/29790 [23:23<28:19:06,  3.47s/it]  1%|1         | 394/29790 [23:27<29:30:10,  3.61s/it]  1%|1         | 395/29790 [23:31<28:50:24,  3.53s/it]  1%|1         | 396/29790 [23:33<27:01:49,  3.31s/it]  1%|1         | 397/29790 [23:38<29:17:49,  3.59s/it]  1%|1         | 398/29790 [23:42<31:19:04,  3.84s/it]  1%|1         | 399/29790 [23:46<30:35:19,  3.75s/it]  1%|1         | 400/29790 [23:49<29:16:30,  3.59s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 1.0000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 18.7940
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 412081.0000
   completions/mean_length: 4.7000
   completions/min_length: 4.7000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.866062437059417e-06, 'num_tokens': 412081.0, 'completions/mean_length': 4.7, 'completions/min_length': 4.7, 'completions/max_length': 4.7, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.7, 'completions/min_terminated_length': 4.7, 'completions/max_terminated_length': 4.7, 'attention/early/mdi': 18.793966388702394, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.1149385929107667, 'attention/early/aei_vision': 0.17389353066682817, 'attention/middle/mdi': 14.09228458404541, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.9470538854599, 'attention/middle/aei_vision': 0.24056297540664673, 'attention/late/mdi': 20.846850776672362, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.1726725101470947, 'attention/late/aei_vision': 0.15495800226926804, 'attention/all/mdi': 17.00355272293091, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 3.078221654891968, 'attention/all/aei_vision': 0.1898048371076584, 'rewards/mc_idx_reward/mean': 1.0, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 3.0, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.003692195537587395, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 3.0, 'epoch': 0.04}
  1%|1         | 400/29790 [23:49<29:16:30,  3.59s/it]MDI(late): 20.847
  1%|1         | 401/29790 [23:53<30:59:24,  3.80s/it]  1%|1         | 402/29790 [23:56<28:28:51,  3.49s/it]  1%|1         | 403/29790 [23:59<28:44:29,  3.52s/it]  1%|1         | 404/29790 [24:03<28:53:28,  3.54s/it]  1%|1         | 405/29790 [24:06<26:36:18,  3.26s/it]  1%|1         | 406/29790 [24:09<26:50:59,  3.29s/it]  1%|1         | 407/29790 [24:13<27:44:38,  3.40s/it]  1%|1         | 408/29790 [24:16<28:03:17,  3.44s/it]  1%|1         | 409/29790 [24:18<24:50:13,  3.04s/it]  1%|1         | 410/29790 [24:22<27:11:36,  3.33s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 14.3338
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 422012.0000
   completions/mean_length: 4.7500
   completions/min_length: 4.7000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0079, 'grad_norm': 0.0, 'learning_rate': 9.862705605908024e-06, 'num_tokens': 422012.0, 'completions/mean_length': 4.75, 'completions/min_length': 4.7, 'completions/max_length': 4.8, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.75, 'completions/min_terminated_length': 4.7, 'completions/max_terminated_length': 4.8, 'attention/early/mdi': 14.333790946006776, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.8230753421783445, 'attention/early/aei_vision': 0.21500832438468934, 'attention/middle/mdi': 10.445383858680724, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.6551929354667663, 'attention/middle/aei_vision': 0.2896109908819199, 'attention/late/mdi': 17.965151691436766, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.924971854686737, 'attention/late/aei_vision': 0.16899206787347792, 'attention/all/mdi': 13.37709596157074, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.801080071926117, 'attention/all/aei_vision': 0.22453712821006774, 'rewards/mc_idx_reward/mean': 0.85, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.4, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.029296850277751217, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.4, 'epoch': 0.04}
  1%|1         | 410/29790 [24:22<27:11:36,  3.33s/it]MDI(late): 17.965
  1%|1         | 411/29790 [24:26<27:20:18,  3.35s/it]  1%|1         | 412/29790 [24:29<27:09:07,  3.33s/it]  1%|1         | 413/29790 [24:32<27:33:26,  3.38s/it]  1%|1         | 414/29790 [24:36<28:34:45,  3.50s/it]  1%|1         | 415/29790 [24:39<27:56:49,  3.42s/it]  1%|1         | 416/29790 [24:43<28:11:42,  3.46s/it]  1%|1         | 417/29790 [24:46<26:44:34,  3.28s/it]  1%|1         | 418/29790 [24:49<27:04:48,  3.32s/it]  1%|1         | 419/29790 [24:53<27:37:47,  3.39s/it]  1%|1         | 420/29790 [24:56<27:30:56,  3.37s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 14.6065
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 432082.0000
   completions/mean_length: 4.6000
   completions/min_length: 4.6000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.85934877475663e-06, 'num_tokens': 432082.0, 'completions/mean_length': 4.6, 'completions/min_length': 4.6, 'completions/max_length': 4.6, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.6, 'completions/min_terminated_length': 4.6, 'completions/max_terminated_length': 4.6, 'attention/early/mdi': 14.606486606597901, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.826189088821411, 'attention/early/aei_vision': 0.212610425055027, 'attention/middle/mdi': 10.133792829513549, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.6432307243347166, 'attention/middle/aei_vision': 0.2907312124967575, 'attention/late/mdi': 17.230192565917967, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.9210949897766114, 'attention/late/aei_vision': 0.1705712541937828, 'attention/all/mdi': 12.99053888320923, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.7968382596969605, 'attention/all/aei_vision': 0.2246376320719719, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.061312925655511205, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.04}
  1%|1         | 420/29790 [24:56<27:30:56,  3.37s/it]MDI(late): 17.230
  1%|1         | 421/29790 [25:00<28:18:17,  3.47s/it]  1%|1         | 422/29790 [25:03<28:41:23,  3.52s/it]  1%|1         | 423/29790 [25:07<28:47:15,  3.53s/it]  1%|1         | 424/29790 [25:10<28:08:50,  3.45s/it]  1%|1         | 425/29790 [25:13<26:34:00,  3.26s/it]  1%|1         | 426/29790 [25:16<26:10:21,  3.21s/it]  1%|1         | 427/29790 [25:19<25:29:33,  3.13s/it]  1%|1         | 428/29790 [25:22<25:53:52,  3.18s/it]  1%|1         | 429/29790 [25:26<26:11:33,  3.21s/it]  1%|1         | 430/29790 [25:29<27:05:22,  3.32s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 13.0173
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 441894.0000
   completions/mean_length: 4.4000
   completions/min_length: 4.4000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.855991943605237e-06, 'num_tokens': 441894.0, 'completions/mean_length': 4.4, 'completions/min_length': 4.4, 'completions/max_length': 4.4, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.4, 'completions/min_terminated_length': 4.4, 'completions/max_terminated_length': 4.4, 'attention/early/mdi': 13.017295360565186, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.764787721633911, 'attention/early/aei_vision': 0.21897731423377992, 'attention/middle/mdi': 9.22913122177124, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.5524682641029357, 'attention/middle/aei_vision': 0.3137057974934578, 'attention/late/mdi': 20.710254192352295, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.9227243661880493, 'attention/late/aei_vision': 0.14818429872393607, 'attention/all/mdi': 12.716671085357666, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.7466601133346558, 'attention/all/aei_vision': 0.22695580422878264, 'rewards/mc_idx_reward/mean': 0.85, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.4, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.05803904625354335, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.4, 'epoch': 0.04}
  1%|1         | 430/29790 [25:29<27:05:22,  3.32s/it]MDI(late): 20.710
  1%|1         | 431/29790 [25:34<30:02:49,  3.68s/it]  1%|1         | 432/29790 [25:37<29:53:07,  3.66s/it]  1%|1         | 433/29790 [25:41<28:54:27,  3.54s/it]  1%|1         | 434/29790 [25:44<27:57:40,  3.43s/it]  1%|1         | 435/29790 [25:48<29:09:45,  3.58s/it]  1%|1         | 436/29790 [25:51<28:23:15,  3.48s/it]  1%|1         | 437/29790 [25:55<29:30:34,  3.62s/it]  1%|1         | 438/29790 [25:58<28:49:08,  3.53s/it]  1%|1         | 439/29790 [26:02<28:53:54,  3.54s/it]  1%|1         | 440/29790 [26:05<28:55:12,  3.55s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 17.1955
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 452773.0000
   completions/mean_length: 4.4500
   completions/min_length: 4.4000
   ... and 11 more metrics
============================================================
                                                      {'loss': -0.0079, 'grad_norm': 0.0, 'learning_rate': 9.852635112453844e-06, 'num_tokens': 452773.0, 'completions/mean_length': 4.45, 'completions/min_length': 4.4, 'completions/max_length': 4.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.45, 'completions/min_terminated_length': 4.4, 'completions/max_terminated_length': 4.5, 'attention/early/mdi': 17.195494747161867, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.075485444068909, 'attention/early/aei_vision': 0.19627902656793594, 'attention/middle/mdi': 12.044764947891235, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.8776360034942625, 'attention/middle/aei_vision': 0.27396078780293465, 'attention/late/mdi': 20.31239595413208, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.1782559156417847, 'attention/late/aei_vision': 0.16077396869659424, 'attention/all/mdi': 15.488282489776612, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 3.0437925100326537, 'attention/all/aei_vision': 0.21033792644739152, 'rewards/mc_idx_reward/mean': 0.85, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.4, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.06749801244877744, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.4, 'epoch': 0.04}
  1%|1         | 440/29790 [26:05<28:55:12,  3.55s/it]MDI(late): 20.312
  1%|1         | 441/29790 [26:09<28:33:24,  3.50s/it]  1%|1         | 442/29790 [26:12<28:43:15,  3.52s/it]  1%|1         | 443/29790 [26:15<26:49:12,  3.29s/it]  1%|1         | 444/29790 [26:19<28:01:05,  3.44s/it]  1%|1         | 445/29790 [26:22<27:53:08,  3.42s/it]  1%|1         | 446/29790 [26:26<28:25:45,  3.49s/it]  2%|1         | 447/29790 [26:29<28:04:51,  3.45s/it]  2%|1         | 448/29790 [26:33<28:06:42,  3.45s/it]  2%|1         | 449/29790 [26:36<28:42:23,  3.52s/it]  2%|1         | 450/29790 [26:40<29:11:47,  3.58s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 18.1418
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 463131.0000
   completions/mean_length: 4.5000
   completions/min_length: 4.5000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.849278281302451e-06, 'num_tokens': 463131.0, 'completions/mean_length': 4.5, 'completions/min_length': 4.5, 'completions/max_length': 4.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.5, 'completions/min_terminated_length': 4.5, 'completions/max_terminated_length': 4.5, 'attention/early/mdi': 18.141811561584472, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.0002060651779177, 'attention/early/aei_vision': 0.17418564558029176, 'attention/middle/mdi': 12.411754751205445, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.8181298971176147, 'attention/middle/aei_vision': 0.24629459530115128, 'attention/late/mdi': 19.84348611831665, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.0438035249710085, 'attention/late/aei_vision': 0.15798766314983367, 'attention/all/mdi': 15.866237545013428, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9540465116500854, 'attention/all/aei_vision': 0.19282263666391372, 'rewards/mc_idx_reward/mean': 0.8, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.2, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.0439480157190701, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.2, 'epoch': 0.05}
  2%|1         | 450/29790 [26:40<29:11:47,  3.58s/it]MDI(late): 19.843
  2%|1         | 451/29790 [26:43<28:33:21,  3.50s/it]  2%|1         | 452/29790 [26:47<28:42:37,  3.52s/it]  2%|1         | 453/29790 [26:51<28:47:34,  3.53s/it]  2%|1         | 454/29790 [26:54<28:44:22,  3.53s/it]  2%|1         | 455/29790 [26:57<28:00:20,  3.44s/it]  2%|1         | 456/29790 [27:01<27:45:26,  3.41s/it]  2%|1         | 457/29790 [27:05<28:50:43,  3.54s/it]  2%|1         | 458/29790 [27:08<29:05:44,  3.57s/it]  2%|1         | 459/29790 [27:12<29:04:20,  3.57s/it]  2%|1         | 460/29790 [27:15<28:58:57,  3.56s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.8500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.8937
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 473635.0000
   completions/mean_length: 4.3000
   completions/min_length: 4.3000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.845921450151058e-06, 'num_tokens': 473635.0, 'completions/mean_length': 4.3, 'completions/min_length': 4.3, 'completions/max_length': 4.3, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.3, 'completions/min_terminated_length': 4.3, 'completions/max_terminated_length': 4.3, 'attention/early/mdi': 16.893723011016846, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.013120985031128, 'attention/early/aei_vision': 0.1846933275461197, 'attention/middle/mdi': 9.655761432647704, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.742449998855591, 'attention/middle/aei_vision': 0.295053006708622, 'attention/late/mdi': 20.836427688598633, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.09585497379303, 'attention/late/aei_vision': 0.15099794268608094, 'attention/all/mdi': 14.277926540374756, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.950475287437439, 'attention/all/aei_vision': 0.21024809181690216, 'rewards/mc_idx_reward/mean': 0.85, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.4, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.03356994348578155, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.4, 'epoch': 0.05}
  2%|1         | 460/29790 [27:15<28:58:57,  3.56s/it]MDI(late): 20.836
  2%|1         | 461/29790 [27:19<28:44:54,  3.53s/it]  2%|1         | 462/29790 [27:22<28:02:10,  3.44s/it]  2%|1         | 463/29790 [27:26<29:43:48,  3.65s/it]  2%|1         | 464/29790 [27:29<28:36:29,  3.51s/it]  2%|1         | 465/29790 [27:33<28:55:13,  3.55s/it]  2%|1         | 466/29790 [27:36<28:39:07,  3.52s/it]  2%|1         | 467/29790 [27:40<29:00:50,  3.56s/it]  2%|1         | 468/29790 [27:43<28:26:52,  3.49s/it]  2%|1         | 469/29790 [27:47<28:18:24,  3.48s/it]  2%|1         | 470/29790 [27:50<28:20:05,  3.48s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 18.1400
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 483991.0000
   completions/mean_length: 4.5000
   completions/min_length: 4.5000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.842564618999665e-06, 'num_tokens': 483991.0, 'completions/mean_length': 4.5, 'completions/min_length': 4.5, 'completions/max_length': 4.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.5, 'completions/min_terminated_length': 4.5, 'completions/max_terminated_length': 4.5, 'attention/early/mdi': 18.139981174468993, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 3.0076746225357054, 'attention/early/aei_vision': 0.17891029715538026, 'attention/middle/mdi': 10.94464602470398, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.761039900779724, 'attention/middle/aei_vision': 0.28025530129671095, 'attention/late/mdi': 17.861194896698, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.021860408782959, 'attention/late/aei_vision': 0.1704116776585579, 'attention/all/mdi': 14.514493560791015, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9301916122436524, 'attention/all/aei_vision': 0.20985909253358842, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.019856610351416747, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.05}
  2%|1         | 470/29790 [27:50<28:20:05,  3.48s/it]MDI(late): 17.861
  2%|1         | 471/29790 [27:54<29:19:10,  3.60s/it]  2%|1         | 472/29790 [27:58<29:33:33,  3.63s/it]  2%|1         | 473/29790 [28:02<29:35:08,  3.63s/it]  2%|1         | 474/29790 [28:05<28:48:29,  3.54s/it]  2%|1         | 475/29790 [28:08<28:13:45,  3.47s/it]  2%|1         | 476/29790 [28:12<29:45:33,  3.65s/it]  2%|1         | 477/29790 [28:15<28:16:56,  3.47s/it]  2%|1         | 478/29790 [28:18<27:10:36,  3.34s/it]  2%|1         | 479/29790 [28:22<27:54:22,  3.43s/it]  2%|1         | 480/29790 [28:25<27:45:20,  3.41s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.5500
   rewards/mc_idx_reward/std: 0.0707
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 18.4083
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 494340.0000
   completions/mean_length: 4.3500
   completions/min_length: 4.2000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.839207787848271e-06, 'num_tokens': 494340.0, 'completions/mean_length': 4.35, 'completions/min_length': 4.2, 'completions/max_length': 4.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.35, 'completions/min_terminated_length': 4.2, 'completions/max_terminated_length': 4.5, 'attention/early/mdi': 18.408272361755373, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.9823484420776367, 'attention/early/aei_vision': 0.17678317800164223, 'attention/middle/mdi': 12.09351043701172, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.7462982654571535, 'attention/middle/aei_vision': 0.26880405843257904, 'attention/late/mdi': 22.053655529022215, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.059575629234314, 'attention/late/aei_vision': 0.14688981026411058, 'attention/all/mdi': 16.140522956848145, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9294074058532713, 'attention/all/aei_vision': 0.1974923476576805, 'rewards/mc_idx_reward/mean': 0.55, 'rewards/mc_idx_reward/std': 0.07071067690849304, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 1.2, 'reward_std': 0.2828427076339722, 'frac_reward_zero_std': 0.9, 'entropy': 0.07672400827286766, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 1.2, 'epoch': 0.05}
  2%|1         | 480/29790 [28:25<27:45:20,  3.41s/it]MDI(late): 22.054
  2%|1         | 481/29790 [28:29<27:43:21,  3.41s/it]  2%|1         | 482/29790 [28:32<27:33:45,  3.39s/it]  2%|1         | 483/29790 [28:36<28:32:02,  3.51s/it]  2%|1         | 484/29790 [28:40<29:01:23,  3.57s/it]  2%|1         | 485/29790 [28:43<28:53:23,  3.55s/it]  2%|1         | 486/29790 [28:46<28:31:26,  3.50s/it]  2%|1         | 487/29790 [28:50<29:11:44,  3.59s/it]  2%|1         | 488/29790 [28:53<28:22:22,  3.49s/it]  2%|1         | 489/29790 [28:57<27:52:49,  3.43s/it]  2%|1         | 490/29790 [29:00<26:41:28,  3.28s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.9000
   rewards/mc_idx_reward/std: 0.0000
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 16.6894
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 504700.0000
   completions/mean_length: 4.3000
   completions/min_length: 4.3000
   ... and 11 more metrics
============================================================
                                                      {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 9.835850956696878e-06, 'num_tokens': 504700.0, 'completions/mean_length': 4.3, 'completions/min_length': 4.3, 'completions/max_length': 4.3, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 4.3, 'completions/min_terminated_length': 4.3, 'completions/max_terminated_length': 4.3, 'attention/early/mdi': 16.68938856124878, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.981651520729065, 'attention/early/aei_vision': 0.1851675897836685, 'attention/middle/mdi': 10.458009099960327, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.738731265068054, 'attention/middle/aei_vision': 0.2802723601460457, 'attention/late/mdi': 19.911765384674073, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.0541593074798583, 'attention/late/aei_vision': 0.1557187981903553, 'attention/all/mdi': 14.483894538879394, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9248473167419435, 'attention/all/aei_vision': 0.20705291479825974, 'rewards/mc_idx_reward/mean': 0.9, 'rewards/mc_idx_reward/std': 0.0, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 2.6, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.03762457818083931, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 2.6, 'epoch': 0.05}
  2%|1         | 490/29790 [29:00<26:41:28,  3.28s/it]MDI(late): 19.912
  2%|1         | 491/29790 [29:03<26:45:40,  3.29s/it]  2%|1         | 492/29790 [29:06<26:59:58,  3.32s/it]  2%|1         | 493/29790 [29:10<27:26:57,  3.37s/it]  2%|1         | 494/29790 [29:13<27:24:17,  3.37s/it]  2%|1         | 495/29790 [29:17<27:51:09,  3.42s/it]  2%|1         | 496/29790 [29:21<28:39:58,  3.52s/it]  2%|1         | 497/29790 [29:25<30:50:05,  3.79s/it]  2%|1         | 498/29790 [29:28<29:27:32,  3.62s/it]  2%|1         | 499/29790 [29:32<28:47:01,  3.54s/it]