#!/bin/bash
# 用法: bash wait_pid_then_run.sh <PID> "<命令>"
# 示例: bash ./wait_pid_then_run.sh 667395 "bash mdi_dapo_train.sh"
# codex resume 019a2c91-c3f2-7e51-bd23-13ae3afe514b
#!/bin/bash

PID=$1
NEXT_CMD=$2

if [ -z "$PID" ] || [ -z "$NEXT_CMD" ]; then
    echo "用法: bash wait_pid_then_run.sh <PID> \"<命令>\""
    exit 1
fi

echo "🕒 正在监控进程 PID=$PID ..."
while kill -0 "$PID" 2>/dev/null; do
    sleep 30  # 每30秒检测一次
done

echo "✅ 进程 $PID 已结束，开始执行: $NEXT_CMD"
eval "$NEXT_CMD"

