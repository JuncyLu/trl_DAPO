#!/bin/bash
# 系统提示词测试脚本 - 使用 4 卡加速

TS=$(TZ='Asia/Shanghai' date +%Y%m%d_%H%M%S)
mkdir -p prompt_test_logs/$TS
export PROMPT_TEST_TS=$TS

echo "======================================================================"
echo "系统提示词测试 - $TS"
echo "======================================================================"
echo "使用 4 卡并行测试 50 个样本"
echo "日志目录: prompt_test_logs/$TS"
echo "======================================================================"

# 线程与并行设置
export OMP_NUM_THREADS=6
export MKL_NUM_THREADS=6
export TOKENIZERS_PARALLELISM=false

# 通信与容错
export TORCH_NCCL_ASYNC_ERROR_HANDLING=1
export CUDA_DEVICE_MAX_CONNECTIONS=1

# 内存优化
export PYTORCH_ALLOC_CONF=expandable_segments:True
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

# 运行测试（使用 accelerate 多卡并行）
accelerate launch \
  --num_processes=4 \
  --num_machines=1 \
  --mixed_precision=bf16 \
  --multi_gpu \
  test_system_prompt.py \
  2>&1 | tee prompt_test_logs/$TS/test.log

echo ""
echo "======================================================================"
echo "测试完成！"
echo "======================================================================"
echo "查看结果："
echo "  详细日志: prompt_test_logs/$TS/*/test_results.md"
echo "  统计信息: prompt_test_logs/$TS/*/statistics.json"
echo "  运行日志: prompt_test_logs/$TS/test.log"
echo "======================================================================"

