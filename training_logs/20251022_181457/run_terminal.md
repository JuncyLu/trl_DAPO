# Training Logs

- Time: 2025-10-22 18:14:57
- Model: Qwen/Qwen2.5-VL-3B-Instruct
- Dataset: None
- Output Dir: runs/grpo-Qwen2.5-VL-3B-Instruct

---

```text
# Training Logs

- Time: 2025-10-22 18:14:57
- Model: Qwen/Qwen2.5-VL-3B-Instruct
- Dataset: None
- Output Dir: runs/grpo-Qwen2.5-VL-3B-Instruct

---

```text
Map:   0%|          | 0/1400 [00:00<?, ? examples/s]Map:  71%|#######1  | 1000/1400 [00:00<00:00, 9411.74 examples/s]Map: 100%|##########| 1400/1400 [00:00<00:00, 9526.31 examples/s]
Map:   0%|          | 0/100 [00:00<?, ? examples/s]Map: 100%|##########| 100/100 [00:00<00:00, 7251.69 examples/s]
Filter:   0%|          | 0/1400 [00:00<?, ? examples/s]Filter: 100%|##########| 1400/1400 [00:00<00:00, 11006.30 examples/s]Filter: 100%|##########| 1400/1400 [00:00<00:00, 10896.96 examples/s]
Filter:   0%|          | 0/100 [00:00<?, ? examples/s]Filter: 100%|##########| 100/100 [00:00<00:00, 8921.01 examples/s]
Map:   0%|          | 0/1400 [00:00<?, ? examples/s]Map:  31%|###       | 429/1400 [00:00<00:00, 3869.50 examples/s]Map:  67%|######7   | 941/1400 [00:00<00:00, 4522.91 examples/s]Map: 100%|##########| 1400/1400 [00:00<00:00, 4227.98 examples/s]Map: 100%|##########| 1400/1400 [00:00<00:00, 4213.32 examples/s]
Map:   0%|          | 0/100 [00:00<?, ? examples/s]Map: 100%|##########| 100/100 [00:00<00:00, 4180.30 examples/s]
Map:   0%|          | 0/1400 [00:00<?, ? examples/s]Map:  71%|#######1  | 1000/1400 [00:00<00:00, 9711.04 examples/s]Map: 100%|##########| 1400/1400 [00:00<00:00, 9711.77 examples/s]
Map:   0%|          | 0/100 [00:00<?, ? examples/s]Map: 100%|##########| 100/100 [00:00<00:00, 5046.08 examples/s]
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|#####     | 1/2 [00:00<00:00,  5.46it/s]Loading checkpoint shards: 100%|##########| 2/2 [00:00<00:00,  8.08it/s]
  0%|          | 0/43 [00:00<?, ?it/s]  2%|2         | 1/43 [01:40<1:10:29, 100.69s/it]  5%|4         | 2/43 [03:10<1:04:33, 94.48s/it]   7%|6         | 3/43 [04:11<52:38, 78.96s/it]    9%|9         | 4/43 [05:42<54:26, 83.76s/it] 12%|#1        | 5/43 [07:09<53:49, 85.00s/it] 14%|#3        | 6/43 [08:53<56:27, 91.54s/it] 16%|#6        | 7/43 [10:15<52:58, 88.30s/it] 19%|#8        | 8/43 [11:39<50:39, 86.83s/it] 21%|##        | 9/43 [12:55<47:24, 83.68s/it] 23%|##3       | 10/43 [14:12<44:45, 81.39s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.5750
   rewards/mc_idx_reward/std: 0.4649
   rewards/think_format_reward/mean: 0.5750
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 38.3664
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 430669.0000
   completions/mean_length: 142.7391
   completions/min_length: 47.4000
   ... and 11 more metrics
============================================================
                                               {'loss': -0.0447, 'grad_norm': 0.3019393980503082, 'learning_rate': 7.906976744186048e-06, 'num_tokens': 430669.0, 'completions/mean_length': 142.7390625, 'completions/min_length': 47.4, 'completions/max_length': 243.5, 'completions/clipped_ratio': 0.296875, 'completions/mean_terminated_length': 117.59325637817383, 'completions/min_terminated_length': 47.4, 'completions/max_terminated_length': 214.7, 'attention/early/mdi': 38.366425323486325, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.973306393623352, 'attention/early/aei_vision': 0.09831414073705673, 'attention/middle/mdi': 29.745932006835936, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.8922077417373657, 'attention/middle/aei_vision': 0.13319545686244966, 'attention/late/mdi': 28.90217514038086, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.9228398323059084, 'attention/late/aei_vision': 0.12333440706133843, 'attention/all/mdi': 30.770908737182616, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.929451274871826, 'attention/all/aei_vision': 0.11828119605779648, 'rewards/mc_idx_reward/mean': 0.575, 'rewards/mc_idx_reward/std': 0.46493403017520907, 'rewards/think_format_reward/mean': 0.575, 'rewards/think_format_reward/std': 0.44175774455070493, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 1.875, 'reward_std': 1.2727922081947327, 'frac_reward_zero_std': 0.4, 'entropy': 1.0277012687176466, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 1.875, 'epoch': 0.23}
 23%|##3       | 10/43 [14:12<44:45, 81.39s/it]MDI(late): 28.902
 26%|##5       | 11/43 [15:29<42:45, 80.18s/it] 28%|##7       | 12/43 [16:48<41:14, 79.83s/it] 30%|###       | 13/43 [18:05<39:24, 78.81s/it] 33%|###2      | 14/43 [19:21<37:46, 78.16s/it] 35%|###4      | 15/43 [20:40<36:34, 78.37s/it] 37%|###7      | 16/43 [21:57<35:03, 77.89s/it] 40%|###9      | 17/43 [23:14<33:39, 77.69s/it] 42%|####1     | 18/43 [24:29<32:01, 76.87s/it] 44%|####4     | 19/43 [25:46<30:47, 76.98s/it] 47%|####6     | 20/43 [27:05<29:42, 77.50s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.3703
   rewards/mc_idx_reward/std: 0.4778
   rewards/think_format_reward/mean: 0.0125
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 41.7323
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 930365.0000
   completions/mean_length: 253.8000
   completions/min_length: 192.9000
   ... and 11 more metrics
============================================================
                                               {'loss': -0.0078, 'grad_norm': 0.0, 'learning_rate': 5.58139534883721e-06, 'num_tokens': 930365.0, 'completions/mean_length': 253.8, 'completions/min_length': 192.9, 'completions/max_length': 256.0, 'completions/clipped_ratio': 0.965625, 'completions/mean_terminated_length': 133.57333526611328, 'completions/min_terminated_length': 116.1, 'completions/max_terminated_length': 157.1, 'attention/early/mdi': 41.73229446411133, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.985492491722107, 'attention/early/aei_vision': 0.08753430619835853, 'attention/middle/mdi': 44.84088554382324, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 2.9661134243011475, 'attention/middle/aei_vision': 0.09551888182759286, 'attention/late/mdi': 40.456610107421874, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 2.974137473106384, 'attention/late/aei_vision': 0.09362149015069007, 'attention/all/mdi': 40.754585647583006, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9752476453781127, 'attention/all/aei_vision': 0.09222500398755074, 'rewards/mc_idx_reward/mean': 0.3703125, 'rewards/mc_idx_reward/std': 0.47779352962970734, 'rewards/think_format_reward/mean': 0.0125, 'rewards/think_format_reward/std': 0.04395764470100403, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 0.49375, 'reward_std': 1.1711455762386322, 'frac_reward_zero_std': 0.58125, 'entropy': 0.11270770318806171, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 0.49375, 'epoch': 0.47}
 47%|####6     | 20/43 [27:05<29:42, 77.50s/it]MDI(late): 40.457
 49%|####8     | 21/43 [28:23<28:28, 77.64s/it] 51%|#####1    | 22/43 [29:40<27:07, 77.50s/it] 53%|#####3    | 23/43 [30:59<25:55, 77.75s/it] 56%|#####5    | 24/43 [32:15<24:31, 77.43s/it] 58%|#####8    | 25/43 [33:34<23:19, 77.73s/it] 60%|######    | 26/43 [34:51<22:02, 77.77s/it] 63%|######2   | 27/43 [36:09<20:42, 77.67s/it] 65%|######5   | 28/43 [37:24<19:14, 76.96s/it] 67%|######7   | 29/43 [38:42<18:01, 77.26s/it] 70%|######9   | 30/43 [39:59<16:42, 77.09s/it]
📊 Logging 44 metrics for train mode
============================================================
🎯 Reward Metrics:
   rewards/mc_idx_reward/mean: 0.4813
   rewards/mc_idx_reward/std: 0.4993
   rewards/think_format_reward/mean: 0.0000
   ... and 7 more reward metrics
🧠 Attention Metrics:
   attention/early/mdi: 43.6731
   attention/early/mdi_balance: 0.0000
   attention/early/mdi_penalty: 1.0000
   ... and 17 more attention metrics
📈 Other Metrics:
   num_tokens: 1432250.0000
   completions/mean_length: 255.7641
   completions/min_length: 241.8000
   ... and 11 more metrics
============================================================
                                               {'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 3.2558139534883724e-06, 'num_tokens': 1432250.0, 'completions/mean_length': 255.7640625, 'completions/min_length': 241.8, 'completions/max_length': 256.0, 'completions/clipped_ratio': 0.9953125, 'completions/mean_terminated_length': 42.0, 'completions/min_terminated_length': 37.0, 'completions/max_terminated_length': 47.0, 'attention/early/mdi': 43.67305717468262, 'attention/early/mdi_balance': 0.0, 'attention/early/mdi_penalty': 1.0, 'attention/early/aei_text': 2.9941179513931275, 'attention/early/aei_vision': 0.08520474284887314, 'attention/middle/mdi': 53.923907089233396, 'attention/middle/mdi_balance': 0.0, 'attention/middle/mdi_penalty': 1.0, 'attention/middle/aei_text': 3.004776382446289, 'attention/middle/aei_vision': 0.08001000136137008, 'attention/late/mdi': 44.616035079956056, 'attention/late/mdi_balance': 0.0, 'attention/late/mdi_penalty': 1.0, 'attention/late/aei_text': 3.0010396957397463, 'attention/late/aei_vision': 0.08361794054508209, 'attention/all/mdi': 45.65910453796387, 'attention/all/mdi_balance': 0.0, 'attention/all/mdi_penalty': 1.0, 'attention/all/aei_text': 2.9999778032302857, 'attention/all/aei_vision': 0.08294433876872062, 'rewards/mc_idx_reward/mean': 0.48125, 'rewards/mc_idx_reward/std': 0.4992718011140823, 'rewards/think_format_reward/mean': 0.0, 'rewards/think_format_reward/std': 0.0, 'rewards/mdi_reward/mean': -1.0, 'rewards/mdi_reward/std': 0.0, 'reward': 0.925, 'reward_std': 1.1844038248062134, 'frac_reward_zero_std': 0.58125, 'entropy': 0.008489236235618591, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'rewards/total_reward': 0.925, 'epoch': 0.7}
 70%|######9   | 30/43 [39:59<16:42, 77.09s/it]MDI(late): 44.616
 72%|#######2  | 31/43 [41:16<15:25, 77.12s/it] 74%|#######4  | 32/43 [42:32<14:02, 76.63s/it] 77%|#######6  | 33/43 [43:50<12:50, 77.06s/it] 79%|#######9  | 34/43 [45:07<11:33, 77.02s/it] 81%|########1 | 35/43 [46:25<10:20, 77.57s/it] 84%|########3 | 36/43 [47:42<09:00, 77.24s/it] 86%|########6 | 37/43 [49:00<07:44, 77.39s/it]