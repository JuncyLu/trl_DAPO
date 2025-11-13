TS=$(TZ='Asia/Shanghai' date +%Y%m%d_%H%M%S)
mkdir -p training_logs/$TS
export TRAINING_LOG_TS=$TS

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

accelerate launch \
  --config_file src/configs/deepspeed_zero2.yaml \
  src/scripts/train_grpo_vlm.py \
  --model_name_or_path Qwen/Qwen2.5-7B-Instruct \
  --output_dir training_logs/$TS/runs/dapo-Qwen2.5-7B-Instruct \
  --rollout_log_path training_logs/$TS/rollout_results.md \
  --eval_log_path training_logs/$TS/eval_results.md \
  --dtype bfloat16 \
  --gradient_checkpointing \
  --max_prompt_length 2048 \
  --max_completion_length 512 \
  --per_device_train_batch_size 2 \
  --gradient_accumulation_steps 4 \
  --num_generations 8 \
  --num_train_epochs 1 \
  --report_to wandb \
  --log_completions \
  --logging_steps 1.0 \
  --do_eval \
  --eval_strategy steps \
  --eval_steps 10 \
  --eval_num_generations 2 \
  --per_device_eval_batch_size 4 \
  --save_strategy steps \
  --save_steps 500 \
  --learning_rate 1e-5 \
  --lr_scheduler_type cosine \
  --warmup_ratio 0.05 \
  --max_grad_norm 1.0 \
  --vgr_hard_negative \
  --reward_weights 2.5 1.0 0.5 0.5 1.0 \
  --early_reward_weights 1.0 1.0 2.0 2.0 1.0 \
  --use_peft \
  --lora_target_modules "q_proj", "v_proj" \
  --max_steps 20 \
  >> training_logs/$TS/train.log 2>&1

    # --use_vllm \
    # --vllm_mode colocate \
    # --vllm_gpu_memory_utilization 0.5
  #     --reward_weights 2.5 1.0 0.5 0.5 1.0 \
  # --early_reward_weights 1.0 1.0 2.0 2.0 1.0 \
