"""
查看wandb离线曲线数据的脚本

使用方式（离线模式）：
  # 列出所有可用的runs
  python view_wandb.py --wandb_dir ./wandb

  # 查看特定run的指标
  python view_wandb.py --wandb_dir ./wandb --run <run-name>

  # 查看并绘制特定指标
  python view_wandb.py --wandb_dir ./wandb --run <run-name> --metrics loss reward --plot

在线模式：
  python view_wandb.py --entity <your-entity> --project <your-project> --run <run-id>
"""
import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd

try:
    import wandb
    WANDB_AVAILABLE = True
except ImportError:
    WANDB_AVAILABLE = False
    print("警告: wandb未安装，部分功能可能不可用。尝试安装: pip install wandb")

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False


def read_offline_wandb_run(run_dir: Path, use_api: bool = True) -> Optional[Dict]:
    """读取离线wandb run目录的数据"""
    if not run_dir.exists() or not run_dir.is_dir():
        return None
    
    # 优先使用wandb API读取（能处理.wandb二进制文件）
    if use_api and WANDB_AVAILABLE:
        try:
            # 使用wandb API读取离线run
            # wandb API需要知道wandb目录的位置
            wandb_dir = run_dir.parent
            run_name = run_dir.name
            
            # 尝试直接使用run目录
            api = wandb.Api()
            # 对于离线数据，需要指定wandb目录
            # 由于离线数据格式复杂，我们先尝试读取文件
            
            # 查找.wandb文件
            wandb_file = list(run_dir.glob("*.wandb"))
            if wandb_file:
                # 使用wandb内部工具读取
                try:
                    # wandb API可以处理离线数据，但需要正确的路径格式
                    # 对于离线run，我们使用文件系统方式读取
                    pass
                except Exception:
                    pass
        except Exception:
            pass
    
    # 回退到文件系统方式读取
    metadata_file = run_dir / "files" / "wandb-metadata.json"
    summary_file = run_dir / "wandb-summary.json"
    events_file = run_dir / "wandb-events.jsonl"
    
    # 也尝试在files目录下查找
    if not metadata_file.exists():
        metadata_file = run_dir / "wandb-metadata.json"
    
    metadata = {}
    summary = {}
    events = []
    
    if metadata_file.exists():
        try:
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
        except Exception as e:
            print(f"警告: 无法读取metadata: {e}")
    
    if summary_file.exists():
        try:
            with open(summary_file, 'r') as f:
                summary = json.load(f)
        except Exception as e:
            pass  # summary文件可能不存在
    
    if events_file.exists():
        try:
            with open(events_file, 'r') as f:
                for line in f:
                    if line.strip():
                        events.append(json.loads(line))
        except Exception as e:
            pass  # events文件可能不存在
    
    return {
        'metadata': metadata,
        'summary': summary,
        'events': events,
        'run_dir': run_dir,
        'run_name': run_dir.name,
        'wandb_file': list(run_dir.glob("*.wandb"))[0] if list(run_dir.glob("*.wandb")) else None
    }


def events_to_dataframe(events: List[Dict]) -> pd.DataFrame:
    """将wandb events转换为DataFrame"""
    if not events:
        return pd.DataFrame()
    
    rows = []
    for event in events:
        if '_wandb' in event:
            continue
        
        row = {}
        # 提取step
        if '_step' in event:
            row['step'] = event['_step']
        if '_timestamp' in event:
            row['timestamp'] = event['_timestamp']
        
        # 提取所有指标
        for key, value in event.items():
            if key.startswith('_'):
                continue
            if isinstance(value, (int, float)):
                row[key] = value
        
        if row:
            rows.append(row)
    
    if not rows:
        return pd.DataFrame()
    
    df = pd.DataFrame(rows)
    # 如果有step列，按step排序
    if 'step' in df.columns:
        df = df.sort_values('step')
    
    return df




def view_offline_wandb(wandb_dir: Path, run_name: Optional[str] = None, 
                       metric_keys: Optional[List[str]] = None, plot: bool = False):
    """查看离线wandb数据"""
    wandb_dir = Path(wandb_dir).resolve()
    
    if not wandb_dir.exists():
        print(f"错误: wandb目录不存在: {wandb_dir}")
        return
    
    # 查找所有run目录
    run_dirs = [d for d in wandb_dir.iterdir() if d.is_dir() and d.name.startswith('run-')]
    
    if not run_dirs:
        print(f"在 {wandb_dir} 中未找到任何run目录")
        return
    
    if run_name:
        # 查找特定run
        run_dir = None
        for d in run_dirs:
            if run_name in d.name or d.name == run_name:
                run_dir = d
                break
        
        if not run_dir:
            print(f"错误: 未找到run: {run_name}")
            print(f"可用的runs: {[d.name for d in run_dirs]}")
            return
        
        # 尝试使用wandb API读取（如果有.wandb文件）
        wandb_file = list(run_dir.glob("*.wandb"))
        df = None
        
        if wandb_file and WANDB_AVAILABLE:
            print("检测到.wandb文件，尝试使用wandb API读取...")
            try:
                # 使用wandb的内部函数读取离线run
                # 需要设置环境变量
                original_wandb_dir = os.environ.get('WANDB_DIR')
                os.environ['WANDB_DIR'] = str(wandb_dir.parent)
                
                try:
                    # 尝试使用wandb的内部方法
                    # 由于wandb API的限制，离线.wandb文件需要使用sync或者直接解析
                    # 我们尝试另一种方法：使用wandb的run文件读取器
                    api = wandb.Api()
                    # 对于离线run，我们需要知道entity和project
                    # 从metadata中获取
                    metadata_file = run_dir / "files" / "wandb-metadata.json"
                    if metadata_file.exists():
                        with open(metadata_file, 'r') as f:
                            metadata = json.load(f)
                            # 尝试构造run路径
                            # 但这通常不工作，因为离线数据没有entity/project信息
                            pass
                except Exception:
                    pass
                finally:
                    if original_wandb_dir:
                        os.environ['WANDB_DIR'] = original_wandb_dir
                    elif 'WANDB_DIR' in os.environ:
                        del os.environ['WANDB_DIR']
                
                # 如果API方法失败，提示用户使用其他方法
                if df is None:
                    print("提示: 对于.wandb格式的离线数据，建议使用以下方法之一:")
                    print("  1. 使用 'wandb sync {run_dir}' 将数据上传到wandb.ai后在线查看")
                    print("  2. 查看训练日志文件 (training_logs/) 获取指标信息")
                    print("  3. 如果有wandb账号，可以配置后使用wandb API在线查看")
                    print()
            except Exception as e:
                print(f"使用API读取失败: {e}\n")
        
        # 读取并显示数据（从文件系统）
        run_data = read_offline_wandb_run(run_dir, use_api=False)
        if not run_data:
            print(f"错误: 无法读取run数据: {run_dir}")
            return
        
        print(f"Run: {run_data['run_name']}")
        print(f"目录: {run_dir}\n")
        
        # 显示summary
        if run_data['summary']:
            print("Summary指标:")
            for key, value in run_data['summary'].items():
                if isinstance(value, (int, float)):
                    print(f"  {key}: {value}")
            print()
        
        # 转换为DataFrame
        if not df:
            df = events_to_dataframe(run_data['events'])
        
        if df.empty:
            print("警告: 没有找到事件数据（.wandb文件需要使用wandb工具读取）")
            print(f"提示: 可以使用 'wandb sync {run_dir}' 将数据上传到wandb.ai查看")
            # 尝试查找output.log文件
            log_file = run_dir / "files" / "output.log"
            if log_file.exists():
                print(f"\n找到日志文件: {log_file}")
                print("可以查看日志文件获取训练信息")
            return None
        
        print(f"指标数量: {len(df.columns)}")
        print(f"数据点数: {len(df)}\n")
        
        # 显示可用指标
        metric_cols = [col for col in df.columns if col not in ['step', 'timestamp']]
        print("可用指标:")
        for col in metric_cols:
            print(f"  - {col}")
        print()
        
        # 显示指定指标的数据
        if metric_keys:
            available_metrics = [m for m in metric_keys if m in df.columns]
            if available_metrics:
                print(f"指定指标的数据 (前10行):")
                cols_to_show = ['step'] + available_metrics
                print(df[cols_to_show].dropna().head(10).to_string())
                print()
        
        # 保存到CSV
        output_file = Path(f"wandb_metrics_{run_data['run_name']}.csv")
        df.to_csv(output_file, index=False)
        print(f"完整数据已保存到: {output_file}\n")
        
        # 绘制图表
        if plot and MATPLOTLIB_AVAILABLE:
            plot_metrics(df, metric_keys or metric_cols[:5], run_data['run_name'])
        elif plot and not MATPLOTLIB_AVAILABLE:
            print("警告: matplotlib未安装，无法绘图。安装: pip install matplotlib")
        
        return df
    
    else:
        # 列出所有runs
        print(f"找到 {len(run_dirs)} 个runs:\n")
        run_summaries = []
        
        for run_dir in sorted(run_dirs, key=lambda x: x.stat().st_mtime, reverse=True):
            run_data = read_offline_wandb_run(run_dir)
            if not run_data:
                continue
            
            summary = run_data['summary']
            run_info = {
                'run_name': run_data['run_name'],
                'path': str(run_dir),
            }
            
            # 添加summary中的数值指标
            for key, value in summary.items():
                if isinstance(value, (int, float)):
                    run_info[key] = value
            
            run_summaries.append(run_info)
            print(f"  {run_data['run_name']}")
            if summary:
                for key, value in summary.items():
                    if isinstance(value, (int, float)):
                        print(f"    {key}: {value}")
            print()
        
        # 保存摘要
        if run_summaries:
            df_summary = pd.DataFrame(run_summaries)
            output_file = Path(f"wandb_runs_summary.csv")
            df_summary.to_csv(output_file, index=False)
            print(f"Runs摘要已保存到: {output_file}")
        
        return run_summaries


def plot_metrics(df: pd.DataFrame, metric_keys: List[str], run_name: str):
    """绘制指标曲线"""
    if 'step' not in df.columns:
        print("警告: 数据中没有step列，无法绘图")
        return
    
    available_metrics = [m for m in metric_keys if m in df.columns]
    if not available_metrics:
        print("警告: 没有可用的指标进行绘图")
        return
    
    n_metrics = len(available_metrics)
    n_cols = min(2, n_metrics)
    n_rows = (n_metrics + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 4 * n_rows))
    if n_metrics == 1:
        axes = [axes]
    else:
        axes = axes.flatten() if n_rows > 1 else axes
    
    for idx, metric in enumerate(available_metrics):
        ax = axes[idx]
        metric_data = df[['step', metric]].dropna()
        if len(metric_data) > 0:
            ax.plot(metric_data['step'], metric_data[metric], marker='o', markersize=2)
            ax.set_xlabel('Step')
            ax.set_ylabel(metric)
            ax.set_title(f'{metric}')
            ax.grid(True, alpha=0.3)
    
    # 隐藏多余的子图
    for idx in range(len(available_metrics), len(axes)):
        axes[idx].set_visible(False)
    
    plt.suptitle(f'Run: {run_name}', fontsize=14)
    plt.tight_layout()
    
    output_file = Path(f"wandb_plot_{run_name}.png")
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"图表已保存到: {output_file}")
    plt.close()


def view_online_wandb(entity: str, project: str, run_id: Optional[str] = None, 
                      metric_keys: Optional[List[str]] = None):
    """查看在线wandb数据（原有功能）"""
    if not WANDB_AVAILABLE:
        print("错误: wandb未安装，无法查看在线数据")
        return
    
    api = wandb.Api()
    
    if run_id:
        run = api.run(f"{entity}/{project}/{run_id}")
        print(f"Run名称: {run.name}")
        print(f"Run ID: {run.id}")
        print(f"状态: {run.state}")
        print(f"URL: {run.url}\n")
        
        history = run.history()
        print(f"指标数量: {len(history.columns)}")
        print(f"数据点数: {len(history)}\n")
        
        print("可用指标:")
        for col in history.columns:
            if col not in ['_timestamp', '_runtime', '_step']:
                print(f"  - {col}")
        
        if metric_keys:
            print(f"\n指定指标的数据:")
            for key in metric_keys:
                if key in history.columns:
                    print(f"\n{key}:")
                    print(history[['_step', key]].dropna().head(10))
        
        output_file = Path(f"wandb_metrics_{run_id}.csv")
        history.to_csv(output_file, index=False)
        print(f"\n完整数据已保存到: {output_file}")
        
        return history
    else:
        runs = api.runs(f"{entity}/{project}")
        print(f"项目中共有 {len(runs)} 个runs\n")
        
        summary_data = []
        for run in runs:
            summary = run.summary
            summary_data.append({
                'run_id': run.id,
                'name': run.name,
                'state': run.state,
                'url': run.url,
                **{k: v for k, v in summary.items() if isinstance(v, (int, float))}
            })
        
        df = pd.DataFrame(summary_data)
        print("Runs摘要:")
        print(df[['run_id', 'name', 'state']].to_string())
        
        output_file = Path(f"wandb_runs_summary_{project}.csv")
        df.to_csv(output_file, index=False)
        print(f"\n摘要数据已保存到: {output_file}")
        
        return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="查看wandb曲线数据（支持离线和在线模式）")
    
    # 离线模式参数
    parser.add_argument("--wandb_dir", type=str, default="./wandb", 
                       help="wandb离线数据目录（默认: ./wandb）")
    parser.add_argument("--run", type=str, default=None, 
                       help="运行名称或ID（可选）")
    parser.add_argument("--metrics", type=str, nargs="+", default=None, 
                       help="要查看的指标键列表，如: --metrics loss reward eval_loss")
    parser.add_argument("--plot", action="store_true", 
                       help="绘制指标曲线图")
    
    # 在线模式参数
    parser.add_argument("--entity", type=str, default=None, 
                       help="wandb用户名或团队名（在线模式）")
    parser.add_argument("--project", type=str, default=None, 
                       help="项目名称（在线模式）")
    
    args = parser.parse_args()
    
    # 判断使用哪种模式
    if args.entity and args.project:
        # 在线模式
        view_online_wandb(args.entity, args.project, args.run, args.metrics)
    else:
        # 离线模式（默认）
        view_offline_wandb(Path(args.wandb_dir), args.run, args.metrics, args.plot)

