#!/bin/bash
# 查看离线wandb数据的脚本

WANDB_DIR="${1:-./wandb}"

if [ ! -d "$WANDB_DIR" ]; then
    echo "错误: wandb目录不存在: $WANDB_DIR"
    exit 1
fi

echo "找到的wandb runs:"
ls -d "$WANDB_DIR"/run-* 2>/dev/null | while read run_dir; do
    run_name=$(basename "$run_dir")
    echo "  $run_name"
done

echo ""
echo "要查看特定run的曲线，有以下方法："
echo ""
echo "方法1: 使用wandb sync上传后在线查看（推荐）"
echo "  1. 登录wandb: wandb login"
echo "  2. 上传离线数据: wandb sync $WANDB_DIR/run-<run-name>"
echo "  3. 在 https://wandb.ai 查看曲线"
echo ""
echo "方法2: 使用Python脚本查看（如果数据是JSON格式）"
echo "  python3 view_wandb.py --wandb_dir $WANDB_DIR --run <run-name>"
echo ""
echo "方法3: 查看训练日志文件"
echo "  cat training_logs/*/train.log | grep -E '(loss|reward|eval)'"




