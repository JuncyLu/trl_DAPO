# 查看离线WandB曲线数据

## 方法1: 使用wandb sync上传后在线查看（推荐）

这是最简单和功能最全的方法：

```bash
# 1. 登录wandb（如果还没登录）
wandb login

# 2. 查看所有离线runs
ls wandb/

# 3. 上传特定run到wandb.ai
wandb sync wandb/run-20251226_044041-j19kmzst

# 4. 上传后会在终端显示URL，点击即可在网页查看曲线
# 或者在 https://wandb.ai 查看你的项目
```

## 方法2: 使用Python脚本查看

如果数据是JSON格式（不是.wandb二进制格式），可以使用脚本：

```bash
# 列出所有runs
python3 view_wandb.py --wandb_dir ./wandb

# 查看特定run的指标
python3 view_wandb.py --wandb_dir ./wandb --run run-20251226_044041-j19kmzst

# 查看特定指标并绘制图表
python3 view_wandb.py --wandb_dir ./wandb --run run-20251226_044041-j19kmzst --metrics loss reward --plot
```

## 方法3: 查看训练日志文件

训练过程中的指标也会记录在markdown日志文件中：

```bash
# 查看rollout日志
cat training_logs/*/rollout_results.md

# 查看评估日志
cat training_logs/*/eval_results.md

# 查看训练日志（可能包含一些指标）
cat training_logs/*/train.log | grep -E '(loss|reward|eval)'
```

## 方法4: 使用wandb CLI直接查看

```bash
# 列出所有runs
wandb artifact list .

# 查看特定run的摘要
wandb artifact get <run-path>
```

## 注意事项

- 如果看到`.wandb`二进制文件，建议使用`wandb sync`上传后查看
- JSON格式的数据可以直接用Python脚本解析
- 训练日志文件（markdown格式）包含详细的指标信息




