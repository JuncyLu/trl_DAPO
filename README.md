# DAPO VLM Training

This repository has been refactored to provide a minimal, focused implementation for DAPO (Data-Augmented Policy Optimization) VLM training. The following structure is optimized for training vision-language models with DAPO.

## Quick Start

### Directory Structure

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

### Training Command

```bash
# Activate conda environment
conda activate trl

# Run training
./dapo_train.sh
```

Or manually:

```bash
accelerate launch \
    --config_file src/configs/deepspeed_zero2.yaml \
    src/scripts/train_grpo_vlm.py \
    --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct \
    --output_dir runs/dapo-Qwen2.5-VL-3B-Instruct-$(date +%Y%m%d_%H%M%S) \
    --learning_rate 5e-5 \
    --gradient_checkpointing \
    --dtype bfloat16 \
    --max_prompt_length 2048 \
    --max_completion_length 512 \
    --report_to wandb \
    --do_eval \
    --log_completions \
    --logging_steps 1.0 \
    --eval_strategy steps \
    --eval_steps 10 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 8 \
    --num_generations 4
```

## Refactoring Summary

This minimal version removes:
- All unused trainer implementations (DPO, PPO, SFT, etc.)
- Example scripts and notebooks
- Test files
- Experimental features
- Unused reward functions
- Documentation and templates

**File count reduction**: ~200+ files → ~168 files (16% reduction)

All removed files are preserved in the `archive/` directory for easy rollback.

## Key Changes

- **DAPO Focus**: Renamed GRPO to DAPO (Data-Augmented Policy Optimization) and moved to `src/dapo/`
- **Centralized Source**: All main code moved to `src/` directory for better organization
- **Minimal TRL**: Kept only essential TRL components needed for DAPO training
- **Clean Separation**: Clear separation between DAPO-specific code and TRL utilities

## Requirements

- Python 3.11+
- PyTorch 2.0+
- Transformers 4.49+
- Accelerate
- DeepSpeed
- Wandb (for logging)

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd trl

# Install in development mode
pip install -e .
```

## License

Apache 2.0