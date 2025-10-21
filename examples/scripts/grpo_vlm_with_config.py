#!/usr/bin/env python3
"""
使用配置文件的 GRPO VLM 训练脚本示例
"""

import json
import os
from dataclasses import dataclass, field
from typing import Optional, Union

import torch
from datasets import load_dataset, DatasetDict, Dataset

from trl import (
    GRPOConfig,
    GRPOTrainer,
    ModelConfig,
    ScriptArguments,
    TrlParser,
    get_kbit_device_map,
    get_peft_config,
    get_quantization_config,
)
from trl.rewards import think_format_reward


@dataclass
class DataArguments:
    """Dataset and preprocessing arguments for in-script A-OKVQA processing."""

    dataset_path: str = field(
        default="HuggingFaceM4/A-OKVQA",
        metadata={"help": "Dataset name or path (default: HuggingFaceM4/A-OKVQA)."},
    )
    dataset_config_name: Optional[str] = field(
        default=None, metadata={"help": "Optional dataset config name."}
    )
    train_split: str = field(
        default="train", metadata={"help": "Split to use for training."}
    )
    test_split: str = field(
        default="validation", metadata={"help": "Split to use for evaluation (or 'test')."}
    )
    streaming: bool = field(
        default=False,
        metadata={"help": "Whether to stream the dataset. If True, you'll typically need to set --max_steps."},
    )
    subset_size: int = field(
        default=0,
        metadata={"help": "Limit training split to this many examples (0 = use full)."},
    )
    eval_subset_size: int = field(
        default=0,
        metadata={"help": "Limit eval split to this many examples (0 = use full)."},
    )
    max_image_size: int = field(
        default=1024,
        metadata={"help": "Filter out images with width/height >= this size. 0 disables filtering."},
    )


def load_config_from_json(config_path: str):
    """从 JSON 文件加载配置"""
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config


def apply_config_to_args(training_args, model_args, data_args, config):
    """将配置应用到参数对象"""
    # 应用训练参数
    if "training_args" in config:
        for key, value in config["training_args"].items():
            if hasattr(training_args, key):
                setattr(training_args, key, value)
    
    # 应用模型参数
    if "model_args" in config:
        for key, value in config["model_args"].items():
            if hasattr(model_args, key):
                setattr(model_args, key, value)
    
    # 应用数据参数
    if "data_args" in config:
        for key, value in config["data_args"].items():
            if hasattr(data_args, key):
                setattr(data_args, key, value)


if __name__ == "__main__":
    # 加载配置文件
    config_path = "/home/lujunxi57/trl/training_config.json"
    config = load_config_from_json(config_path)
    
    # 解析命令行参数
    parser = TrlParser((ScriptArguments, GRPOConfig, ModelConfig, DataArguments))
    script_args, training_args, model_args, data_args = parser.parse_args_and_config()
    
    # 应用配置文件中的参数
    apply_config_to_args(training_args, model_args, data_args, config)
    
    print("=== 当前训练配置 ===")
    print(f"批次大小: {training_args.per_device_train_batch_size}")
    print(f"梯度累积步数: {training_args.gradient_accumulation_steps}")
    print(f"学习率: {training_args.learning_rate}")
    print(f"最大步数: {training_args.max_steps}")
    print(f"模型路径: {model_args.model_name_or_path}")
    print(f"数据集路径: {data_args.dataset_path}")
    print("==================")
    
    # 这里可以继续添加数据集加载和训练代码
    # ... (省略数据集加载和训练代码，与原脚本相同)
