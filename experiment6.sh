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
  --model_name_or_path Qwen/Qwen2.5-VL-7B-Instruct \
  --output_dir training_logs/$TS/runs/dapo-Qwen2.5-VL-7B-Instruct \
  --rollout_log_path training_logs/$TS/rollout_results.md \
  --eval_log_path training_logs/$TS/eval_results.md \
  --dtype bfloat16 \
  --gradient_checkpointing \
  --max_prompt_length 4096 \
  --max_completion_length 384 \
  --per_device_train_batch_size 1 \
  --gradient_accumulation_steps 8 \
  --num_generations 8 \
  --num_train_epochs 1 \
  --report_to wandb \
  --log_completions \
  --logging_steps 1.0 \
  --do_eval \
  --eval_strategy steps \
  --eval_steps 12 \
  --eval_num_generations 1 \
  --per_device_eval_batch_size 2 \
  --save_strategy steps \
  --save_steps 400 \
  --learning_rate 1e-5 \
  --lr_scheduler_type cosine \
  --warmup_ratio 0.05 \
  --max_grad_norm 1.0 \
  --replay_buffer_size 64 \
  --filter_min_reward 1.5 \
  --replay_var_epsilon 1e-6 \
  --token_weights \
  --token_weights_smooth_sigma 1.0 \
  --vgr_hard_negative \
  --reward_weights 3.5 2.0 0.5 1.0 \
  --early_reward_weights 2.0 2.0 2.0 1.0 \
  --use_peft \
  --lora_target_modules "q_proj", "v_proj" \
  >> training_logs/$TS/train.log 2>&1

