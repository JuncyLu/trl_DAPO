#!/bin/bash

accelerate launch --config_file examples/accelerate_configs/deepspeed_zero2.yaml \
	examples/scripts/grpo_vlm.py \
  --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct \
  --output_dir grpo-Qwen2.5-VL-3B-Instruct \
  --learning_rate 1e-5 \
  --dtype bfloat16 \
  --max_prompt_length 2048 \
  --max_completion_length 2048 \
  --dataset_path /home/lujunxi57/aokvqa_trl_data \
  --per_device_train_batch_size 4 \
  --gradient_accumulation_steps 2 \
  --num_generations 8 \
  --report_to tensorboard \
  --enable_detailed_logging

# accelerate launch --config_file examples/accelerate_configs/deepspeed_zero3.yaml \
# 	examples/scripts/grpo_vlm.py \
#   --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct \
#   --output_dir grpo-Qwen2.5-VL-3B-Instruct \
#   --learning_rate 1e-5 \
#   --dtype bfloat16 \
#   --max_prompt_length 2048 \
#   --max_completion_length 2048 \
#   --dataset_path /home/lujunxi57/aokvqa_trl_data \
#   --per_device_train_batch_size 1 \
#   --gradient_accumulation_steps 2 \
#   --num_generations 4 \
#   --report_to tensorboard \
#   --enable_detailed_logging
