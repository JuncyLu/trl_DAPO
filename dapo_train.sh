accelerate launch \
    --config_file src/configs/deepspeed_zero3.yaml \
    src/scripts/train_grpo_vlm.py \
    --model_name_or_path Qwen/Qwen2.5-VL-7B-Instruct \
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
    --num_generations 8 \
    --soft_punish_cache 50 \
    --replay_buffer_size 64 \
    --filter_min_reward 1.5 \
    --replay_var_epsilon 1e-6 \
    --lr_scheduler_type cosine \
    --warmup_ratio 0.05 \
    --max_grad_norm 1.0 \
    --use_segmented_reward_weights \
    --early_reward_weights 2.5 1.0 0.5 \
    --late_reward_weights 0.5 1.0 2.5 \
    --use_peft \
    --lora_target_modules "q_proj", "v_proj" \
    > train.log 2>&1

    # --use_vllm \
    # --vllm_mode colocate \
    # --vllm_gpu_memory_utilization 0.5