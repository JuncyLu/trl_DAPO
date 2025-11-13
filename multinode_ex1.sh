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

# -------- 多机多卡相关参数（在每台机器上按需覆盖） --------
NUM_MACHINES=${NUM_MACHINES:-1}          # 机器总数
GPUS_PER_MACHINE=${GPUS_PER_MACHINE:-4}  # 每台机器使用的 GPU 数
NUM_PROCESSES=${NUM_PROCESSES:-$GPUS_PER_MACHINE * $NUM_MACHINES}
MACHINE_RANK=${MACHINE_RANK:-0}          # 当前机器的 rank（0..NUM_MACHINES-1）
MASTER_ADDR=${MASTER_ADDR:-127.0.0.1}
MASTER_PORT=${MASTER_PORT:-29500}
SAME_NETWORK=${SAME_NETWORK:-true}

# 为避免多机写同一路径产生冲突，按机器 rank 划分输出目录
RUN_ROOT="training_logs/ex1/r${MACHINE_RANK}"
mkdir -p "$RUN_ROOT/runs"

ACCELERATE_DISTRIBUTED_ARGS=(
  --config_file src/configs/deepspeed_zero2.yaml
  --num_processes "${NUM_PROCESSES}"
  --num_machines "${NUM_MACHINES}"
)

if (( NUM_MACHINES > 1 )); then
  ACCELERATE_DISTRIBUTED_ARGS+=(
    --machine_rank "${MACHINE_RANK}"
    --main_process_ip "${MASTER_ADDR}"
    --main_process_port "${MASTER_PORT}"
  )
  if [[ "${SAME_NETWORK}" == "true" ]]; then
    ACCELERATE_DISTRIBUTED_ARGS+=(--same_network)
  fi
fi

accelerate launch \
  "${ACCELERATE_DISTRIBUTED_ARGS[@]}" \
  src/scripts/train_grpo_vlm.py \
  --model_name_or_path Qwen/Qwen2.5-VL-7B-Instruct \
  --output_dir "$RUN_ROOT/runs/dapo-Qwen2.5-VL-7B-Instruct" \
  --rollout_log_path "$RUN_ROOT/rollout_results.md" \
  --eval_log_path "$RUN_ROOT/eval_results.md" \
  --dtype bfloat16 \
  --gradient_checkpointing \
  --max_prompt_length 4096 \
  --max_completion_length 1024 \
  --per_device_train_batch_size 2 \
  --gradient_accumulation_steps 4 \
  --num_generations 8 \
  --num_train_epochs 2 \
  --report_to wandb \
  --log_completions \
  --logging_steps 5.0 \
  --do_eval \
  --eval_strategy steps \
  --eval_steps 400 \
  --eval_num_generations 2 \
  --per_device_eval_batch_size 2 \
  --save_strategy steps \
  --save_steps 400 \
  --learning_rate 1e-5 \
  --lr_scheduler_type cosine \
  --warmup_ratio 0.05 \
  --max_grad_norm 1.0 \
  --reward_weights 2.5 0.0 0.5 0.5 1.0 \
  --early_reward_weights 1.0 0.0 2.0 2.0 1.0 \
  --use_vllm \
  --vllm_mode colocate \
  --vllm_gpu_memory_utilization 0.5
