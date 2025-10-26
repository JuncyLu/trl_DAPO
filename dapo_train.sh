accelerate launch \
    --config_file src/configs/deepspeed_zero3.yaml \
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
    --num_generations 4 \
    --reward_weights 2.0 1.0 0.5 \
    --soft_punish_cache 50 \
    --replay_buffer_size 64 \
    --filter_min_reward 2.0 \
    --replay_var_epsilon 1e-6
    # --use_vllm \
    # --vllm_mode colocate \
    # --vllm_gpu_memory_utilization 0.5