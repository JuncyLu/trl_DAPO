# DAPO‑VLM：多模态强化学习训练（含注意力度量与 Token 权重）

一个专注于视觉‑语言模型（VLM）的 DAPO 训练实现，内置注意力度量（VGR）与基于注意力的 token 级加权，支持多选题对话数据的 Debias-DAPO 训练与清晰日志。

## 安装与快速开始

### 安装

- 开发安装：`pip install -e .[dev]`
- 可选日志后端：`pip install wandb tensorboard`

### 目录结构（简）

```
.
├── src/                              # Main source code
│   ├── __init__.py                   # DAPO exports
│   ├── configs/                      # Training configurations
│   │   └── deepspeed_zero2.yaml     # DeepSpeed configuration
│   ├── dapo/                         # DAPO trainer components
│   │   ├── __init__.py               # DAPO exports
│   │   ├── dapo_trainer.py           # DAPO trainer implementation
│   │   └── dapo_config.py            # DAPO configuration
│   └── scripts/                      # Training scripts
│       └── train_grpo_vlm.py         # Main training script
├── trl/                              # Minimal TRL core
│   ├── __init__.py                   # Exports only essentials
│   ├── core.py                       # Core utilities
│   ├── data_utils.py                 # Data processing utilities
│   ├── import_utils.py               # Import utilities
│   ├── mergekit_utils.py             # Model merging utilities
│   ├── trainer/                      # Base trainer components
│   │   ├── __init__.py               # Only base exports
│   │   ├── base_trainer.py           # Base trainer class
│   │   ├── model_config.py           # Model configuration
│   │   ├── callbacks.py              # Training callbacks
│   │   ├── judges.py                 # Reward judges
│   │   └── utils.py                  # Trainer utilities
│   ├── rewards/                      # Reward functions
│   │   ├── __init__.py               # Only accuracy & format rewards
│   │   ├── accuracy_rewards.py       # Accuracy-based rewards
│   │   └── format_rewards.py         # Format-based rewards
│   ├── models/                       # Model utilities
│   ├── extras/                       # VLLM integration
│   └── scripts/                      # Script utilities
├── tools/                            # Development tools
│   ├── dependency_sweep.py           # Dependency analysis
│   ├── keep_rules.txt                # Files to keep
│   └── drop_rules.txt                # Files to remove
├── archive/                          # Archived unused modules
├── dapo_train.sh                     # Training script
└── README.md                         # This file
```

### 训练命令

```bash
# 一键脚本
bash dapo_train.sh
```

或自定义：

```bash
accelerate launch \
    --config_file src/configs/deepspeed_zero2.yaml \
    src/scripts/train_grpo_vlm.py \
    --model_name_or_path Qwen/Qwen2.5-VL-7B-Instruct \
    --output_dir training_logs/$(date +%Y%m%d_%H%M%S)/runs/dapo \
    --learning_rate 1e-5 \
    --gradient_checkpointing \
    --dtype bfloat16 \
    --max_prompt_length 1024 \
    --max_completion_length 384 \
    --report_to wandb \
    --do_eval \
    --log_completions \
    --logging_steps 1.0 \
    --eval_strategy steps \
    --eval_steps 10 \
    --per_device_eval_batch_size 8 \
    --gradient_accumulation_steps 8 \
    --num_generations 8
```

## 项目优势（简要）

- Token 级注意力加权
  - 损失函数在 token 级直接乘以注意力导出的权重（VGR→1/(VGR+eps)→均值归一→裁剪/可选平滑），更精细地强化关键 token。
- 注意力度量与对齐
  - 计算 VGR 与 early/middle/late/all 分段指标，支持 Qwen‑VL 特殊符号解析；日志清晰可读。
- DAPO 损失健壮
  - 默认 DAPO 归一化消除长度偏置，截断样本可屏蔽计入损失。
- 动态采样与稳定性
  - 可选重放缓冲，按“方差与均值阈值”替换低信息组；奖励权重支持“早期/常规”两阶段切换。
- 日志可解释性强
  - rollout 总览 + token_weights 独立文件；逐 token 权重按“词(权重)”直观串联，便于人工审阅。

## 日志与数据

- 日志文件：
  - 总览：`training_logs/<TS>/rollout_results.md`
  - 逐 token：`training_logs/<TS>/token_weights.md`
- 数据：默认从 `lujunxi57/DDM` 读取（已标准化为 image/problem/solution）
- 消融：`experiment1.sh` ~ `experiment5.sh`（第 5 个仅启用 token 权重、关闭 VGR 奖励）

## 注意事项

- 需注意力输出的功能（VGR/Token 权重）必须走常规 `transformers.generate` 路径；vLLM/paged 不产出 attentions，将自动回退未加权、VGR 奖励置中性。

## License

Apache 2.0
