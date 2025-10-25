#!/bin/bash

# 线程与并行
export OMP_NUM_THREADS=6
export MKL_NUM_THREADS=6
export TOKENIZERS_PARALLELISM=false

# 通信与容错
export TORCH_NCCL_ASYNC_ERROR_HANDLING=1
export CUDA_DEVICE_MAX_CONNECTIONS=1

# 内存碎片缓解
export PYTORCH_ALLOC_CONF=expandable_segments:True
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export CUDA_LAUNCH_BLOCKING=1

accelerate launch --config_file examples/accelerate_configs/deepspeed_zero2.yaml \
    examples/scripts/dapo_vlm.py \
    --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct \
    --learning_rate 5e-5 \
    --dtype bfloat16 \
    --max_prompt_length 1024 \
    --max_completion_length 256 \
    --data_files '{"train": "./aokvqa_trl_test_large/train.parquet", "test": "./aokvqa_trl_test_large/test.parquet"}' \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --num_train_epochs 2 \
    --num_generations 2 \
    --temperature 0.85 \
    --top_p 0.9 \
    --logging_steps 1 \
    --eval_strategy steps \
    --eval_steps 5 \
    --report_to tensorboard \
    --output_dir runs/dapo-Qwen2.5-VL-3B-Instruct-$(date +%Y%m%d_%H%M%S) \
    --enable_detailed_logging \
    --save_strategy steps \
    --save_steps 562 \
    --accuracy_weight 2.0 \
    --format_weight 1.0 \
    --length_weight 1.0 \
    --mdi_as_coefficient 0 \
    --mdi_add_weight 1.0 \
    --soft_punish_cache 30 \
    --replay_buffer_size 24 \
    --filter_min_reward 1.0 \
    --max_grad_norm 1.0