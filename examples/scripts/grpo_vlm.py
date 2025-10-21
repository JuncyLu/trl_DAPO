# Copyright 2020-2025 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# /// script
# dependencies = [
#     "trl",
#     "Pillow",
#     "peft",
#     "math-verify",
#     "latex2sympy2_extended",
#     "torchvision",
#     "trackio",
#     "kernels",
# ]
# ///

"""
pip install math_verify

# For Qwen/Qwen2.5-VL-3B-Instruct (local parquet dir)
accelerate launch \
    --config_file examples/accelerate_configs/deepspeed_zero3.yaml \
    examples/scripts/grpo_vlm.py \
    --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct \
    --output_dir grpo-Qwen2.5-VL-3B-Instruct \
    --learning_rate 1e-5 \
    --gradient_checkpointing \
    --dtype bfloat16 \
    --max_prompt_length 2048 \
    --max_completion_length 1024 \
    --dataset_path ./aokvqa_trl_data_simple \
    --log_completions

# Or explicitly pass data_files (JSON or comma pairs):
#   --data_files '{"train": "./aokvqa_trl_data_simple/train.parquet", "test": "./aokvqa_trl_data_simple/sample_200.parquet"}'
#   --data_files train=./aokvqa_trl_data_simple/train.parquet,test=./aokvqa_trl_data_simple/sample_200.parquet

# For HuggingFaceTB/SmolVLM2-2.2B-Instruct
pip install num2words==0.5.14

accelerate launch \
    --config_file examples/accelerate_configs/deepspeed_zero3.yaml \
    examples/scripts/grpo_vlm.py \
    --model_name_or_path HuggingFaceTB/SmolVLM2-2.2B-Instruct \
    --output_dir grpo-SmolVLM2-2.2B-Instruct \
    --learning_rate 1e-5 \
    --dtype bfloat16 \
    --max_prompt_length 2048 \
    --max_completion_length 1024 \
    --use_peft \
    --lora_target_modules "q_proj", "v_proj" \
    --log_completions \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 2 \
    --num_generations 2

"""

import os
import sys
import re
from dataclasses import dataclass, field
from typing import Optional, Union, Dict

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
from trl.rewards import accuracy_reward, think_format_reward


# Enable logging in a Hugging Face Space
os.environ.setdefault("TRACKIO_SPACE_ID", "trl-trackio")


@dataclass
class DataArguments:
    """Script-specific dataset arguments.

    - dataset_path: HF dataset name or local directory with parquet files.
    - data_files: JSON string or comma-separated 'split=path' pairs for the parquet loader.
    - eval_size: If no eval split exists, take this many examples from train for eval (map-style only).
    """

    dataset_path: Optional[str] = field(
        default=None, metadata={"help": "HF dataset name or local directory with parquet files."}
    )
    data_files: Optional[str] = field(
        default=None,
        metadata={
            "help": "JSON string or comma-separated 'split=path' pairs; used with 'parquet' loader."
        },
    )
    eval_size: Optional[int] = field(
        default=100, metadata={"help": "If no eval split exists, take this many examples from train for eval."}
    )


def _parse_data_files_arg(s: str) -> Dict[str, Union[str, list[str]]]:
    import json

    try:
        obj = json.loads(s)
        if isinstance(obj, dict):
            return obj
    except Exception:
        pass

    mapping: Dict[str, Union[str, list[str]]] = {}
    for item in s.split(","):
        item = item.strip()
        if not item:
            continue
        if "=" not in item:
            raise ValueError(f"Invalid data_files item '{item}'. Expected 'split=path'.")
        split, path = item.split("=", 1)
        mapping[split.strip()] = path.strip()
    return mapping


def _infer_parquet_files(base_dir: str) -> Optional[Dict[str, Union[str, list[str]]]]:
    candidates = [
        ("train", os.path.join(base_dir, "train.parquet")),
        ("validation", os.path.join(base_dir, "validation.parquet")),
        ("test", os.path.join(base_dir, "test.parquet")),
        ("test", os.path.join(base_dir, "sample_200.parquet")),
    ]
    mapping: Dict[str, str] = {}
    for split, path in candidates:
        if os.path.isfile(path):
            mapping[split] = path
    return mapping or None


if __name__ == "__main__":
    # Manually intercept standalone bool flags that HF dataclass parser treats as value-required.
    # Note: we intentionally do NOT include --compute_attention_metrics here; we force-enable it later.
    manual_true_flags = {"--use_subset"}
    manual_overrides = {}
    filtered_argv = [sys.argv[0]]
    skip_next = False
    for i, token in enumerate(sys.argv[1:]):
        if skip_next:
            skip_next = False
            continue
        if token in manual_true_flags:
            manual_overrides[token] = True
            continue
        # Preserve original CLI shape for other arguments
        filtered_argv.append(token)

    sys.argv = filtered_argv

    parser = TrlParser((ScriptArguments, GRPOConfig, ModelConfig, DataArguments))
    script_args, training_args, model_args, data_args = parser.parse_args_and_config()
    # Force DAPO strategy by default for this VLM script.
    # Users can still override via CLI: --loss_type grpo|dr_grpo|bnpo
    training_args.loss_type = "dapo"
    # Recommended with DAPO to avoid penalizing truncated completions
    if getattr(training_args, "mask_truncated_completions", None) is not True:
        training_args.mask_truncated_completions = True
    # DAPO paper recommends asymmetric clipping with higher upper bound
    if getattr(training_args, "epsilon_high", None) is None:
        training_args.epsilon_high = 0.28
    # 强制启用注意力指标计算（MDI reward必需）
    training_args.compute_attention_metrics = True
    # 确保模型生成时输出注意力（供真实MDI使用）
    try:
        if getattr(training_args, "generation_kwargs", None) is None:
            training_args.generation_kwargs = {}
        training_args.generation_kwargs["output_attentions"] = True
        training_args.generation_kwargs["return_dict_in_generate"] = True
    except Exception:
        pass
    # Ensure training log directory for rollout/attention files only
    try:
        os.makedirs("/home/lujunxi57/trl/training_logs/", exist_ok=True)
    except Exception:
        pass
    ################
    # Model
    ################
    dtype = model_args.dtype if model_args.dtype in ["auto", None] else getattr(torch, model_args.dtype)
    training_args.model_init_kwargs = dict(
        revision=model_args.model_revision,
        attn_implementation=model_args.attn_implementation,
        dtype=dtype,
    )
    quantization_config = get_quantization_config(model_args)
    if quantization_config is not None:
        # Passing None would not be treated the same as omitting the argument, so we include it only when valid.
        training_args.model_init_kwargs["device_map"] = get_kbit_device_map()
        training_args.model_init_kwargs["quantization_config"] = quantization_config

    ################
    # Dataset
    ################
    # Flexible dataset loader (prefers map-style for known length)
    dataset_root: Optional[str] = None
    loaded: Union[DatasetDict, Dataset]

    if data_args.data_files:
        mapping = _parse_data_files_arg(data_args.data_files)
        loaded = load_dataset("parquet", data_files=mapping, streaming=script_args.dataset_streaming)
        first_path = next(iter(mapping.values()))
        if isinstance(first_path, list):
            first_path = first_path[0]
        if isinstance(first_path, str):
            dataset_root = os.path.dirname(os.path.abspath(first_path))
    elif data_args.dataset_path:
        if os.path.isdir(data_args.dataset_path):
            mapping = _infer_parquet_files(data_args.dataset_path)
            if mapping:
                loaded = load_dataset("parquet", data_files=mapping, streaming=script_args.dataset_streaming)
                dataset_root = os.path.abspath(data_args.dataset_path)
            else:
                loaded = load_dataset(data_args.dataset_path, streaming=script_args.dataset_streaming)
                dataset_root = os.path.abspath(data_args.dataset_path)
        elif os.path.isfile(data_args.dataset_path) and data_args.dataset_path.endswith(".parquet"):
            loaded = load_dataset("parquet", data_files={"train": data_args.dataset_path}, streaming=script_args.dataset_streaming)
            dataset_root = os.path.dirname(os.path.abspath(data_args.dataset_path))
        else:
            loaded = load_dataset(
                data_args.dataset_path,
                name=script_args.dataset_config,
                streaming=script_args.dataset_streaming,
            )
    elif script_args.dataset_name:
        loaded = load_dataset(
            script_args.dataset_name,
            name=script_args.dataset_config,
            streaming=script_args.dataset_streaming,
        )
    else:
        raise ValueError("Please provide either --dataset_path or --data_files or --dataset_name.")

    # Derive train/eval datasets
    if isinstance(loaded, DatasetDict):
        has_train = script_args.dataset_train_split in loaded
        has_test = script_args.dataset_test_split in loaded
        if has_train:
            train_dataset = loaded[script_args.dataset_train_split]
        else:
            # Use the first available split
            train_dataset = loaded[next(iter(loaded.keys()))]

        if training_args.eval_strategy != "no":
            if has_test:
                eval_dataset = loaded[script_args.dataset_test_split]
            else:
                if not script_args.dataset_streaming and data_args.eval_size and len(train_dataset) > data_args.eval_size:
                    split = train_dataset.train_test_split(test_size=data_args.eval_size, seed=42)
                    train_dataset, eval_dataset = split["train"], split["test"]
                else:
                    eval_dataset = None
        else:
            eval_dataset = None
    else:
        # Single dataset returned
        train_dataset = loaded
        if training_args.eval_strategy != "no" and not script_args.dataset_streaming and data_args.eval_size and len(train_dataset) > data_args.eval_size:
            split = train_dataset.train_test_split(test_size=data_args.eval_size, seed=42)
            train_dataset, eval_dataset = split["train"], split["test"]
        else:
            eval_dataset = None

    SYSTEM_PROMPT = (
        "A conversation between user and assistant. The user asks a question, and the assistant solves it. The "
        "assistant first thinks about the reasoning process in the mind and then provides the user with the answer. "
        "The reasoning process is enclosed within <think></think> tags, i.e., <think>\nThis is my reasoning.\n</think>. "
        "For multiple-choice questions (A-J), conclude your response with a single line: 'Answer: X' where X is the "
        "correct option letter."
    )

    def make_conversation(example):
        # 检查数据集字段，适应不同的数据格式
        if "problem" in example:
            # 原始 lmms-lab 数据集格式
            user_content = example["problem"]
        elif "prompt" in example:
            # A-OKVQA 数据集格式
            user_content = example["prompt"]
        else:
            raise KeyError("数据集必须包含 'problem' 或 'prompt' 字段")
        
        prompt = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
        ]
        return {"prompt": prompt}

    train_dataset = train_dataset.map(make_conversation)
    if eval_dataset is not None:
        eval_dataset = eval_dataset.map(make_conversation)

    # Filter have big images
    def _resolve_image_path(path: str) -> str:
        if os.path.isabs(path):
            return path
        if os.path.exists(path):
            return path
        if dataset_root is not None:
            return os.path.join(dataset_root, path)
        return path

    def filter_big_images(example):
        # 检查数据格式，适应不同的数据结构
        if "image_path" in example:
            # 我们的 A-OKVQA 数据格式：从路径加载图片
            from PIL import Image
            image_path = _resolve_image_path(example["image_path"])
            try:
                pil_image = Image.open(image_path)
                return pil_image.size[0] < 1024 and pil_image.size[1] < 1024
            except:
                return False
        elif "image" in example:
            image = example["image"]
            if isinstance(image, dict):
                # 嵌套格式：从路径加载图片
                from PIL import Image
                image_path = _resolve_image_path(image["path"])
                try:
                    pil_image = Image.open(image_path)
                    return pil_image.size[0] < 1024 and pil_image.size[1] < 1024
                except:
                    return False
            else:
                # 原始格式：直接使用 PIL Image
                return image.size[0] < 1024 and image.size[1] < 1024
        else:
            return True  # 如果没有图片字段，保留样本

    train_dataset = train_dataset.filter(filter_big_images)
    if eval_dataset is not None:
        eval_dataset = eval_dataset.filter(filter_big_images)

    def convert_to_rgb(example):
        # 检查数据格式，适应不同的数据结构
        if "image_path" in example:
            # 我们的 A-OKVQA 数据格式：从路径加载并转换
            from PIL import Image
            image_path = _resolve_image_path(example["image_path"])
            pil_image = Image.open(image_path)
            if pil_image.mode != "RGB":
                pil_image = pil_image.convert("RGB")
            example["image"] = pil_image
        elif "image" in example:
            image = example["image"]
            if isinstance(image, dict):
                # 嵌套格式：从路径加载并转换
                from PIL import Image
                image_path = _resolve_image_path(image["path"])
                pil_image = Image.open(image_path)
                if pil_image.mode != "RGB":
                    pil_image = pil_image.convert("RGB")
                example["image"] = pil_image
            else:
                # 原始格式：直接转换
                if image.mode != "RGB":
                    image = image.convert("RGB")
                example["image"] = image
        return example

    train_dataset = train_dataset.map(convert_to_rgb)
    if eval_dataset is not None:
        eval_dataset = eval_dataset.map(convert_to_rgb)

    if not script_args.dataset_streaming:
        try:
            print(f"Loaded train size: {len(train_dataset)}")
            if eval_dataset is not None:
                print(f"Loaded eval size: {len(eval_dataset)}")
        except Exception:
            pass

    ################
    # Training
    ################
    def mdi_reward(completions, **kwargs):
        """基于真实MDI计算奖励。
        从trainer获取真实的MDI平衡分数，应用奖励公式：r = w * (2*balance - 1)
        """
        trainer = kwargs.get("trainer")
        if trainer is None:
            return [0.0] * len(completions)
        balances = getattr(trainer, "_mdi_balance_scores_current_batch", None)
        if balances is None or len(balances) < len(completions):
            return [0.0] * len(completions)
        weight = 1.0
        rewards = []
        for b in balances[: len(completions)]:
            try:
                rewards.append(weight * (2.0 * float(b) - 1.0))
            except Exception:
                rewards.append(0.0)
        return rewards

    def mc_idx_reward(completions, label_idx, **kwargs):
        """Match predicted letter to gold letter from label_idx (0->A, 1->B, ...).
        Robustly extracts letter via 'Answer: X' or last standalone A-J.
        """
        scores = []
        for comp, idx in zip(completions, label_idx):
            try:
                # Extract model text
                if isinstance(comp, list) and comp and isinstance(comp[0], dict):
                    content = comp[0].get("content", "")
                else:
                    content = str(comp)
                text = str(content)
                # Prefer explicit Answer: X patterns
                m = re.search(r"(?i)(?:final\s*answer|answer)\s*[:\-]?\s*([A-J])", text)
                if not m:
                    # Fallback: last standalone capital letter A-J
                    cands = re.findall(r"\b([A-J])\b", text)
                    pred = cands[-1].upper() if cands else None
                else:
                    pred = m.group(1).upper()
                # Gold from index
                try:
                    gi = int(idx)
                    gold = chr(ord('A') + gi) if 0 <= gi <= 25 else None
                except Exception:
                    gold = None
                scores.append(1.0 if (pred and gold and pred == gold) else 0.0)
            except Exception:
                scores.append(0.0)
        return scores

    # 设置奖励函数权重：mc_idx_reward:think_format_reward:mdi_reward = 4:1:1
    # 将trainer注入MDI奖励函数
    trainer_ref = {"t": None}
    def mdi_reward_with_trainer(completions, **kwargs):
        return mdi_reward(completions, trainer=trainer_ref["t"], **kwargs)
    reward_funcs = [mc_idx_reward, think_format_reward, mdi_reward_with_trainer]
    reward_weights = [4.0, 1.0, 1.0]

    # 设置奖励权重到训练参数中
    training_args.reward_weights = reward_weights

    trainer = GRPOTrainer(
        model=model_args.model_name_or_path,
        args=training_args,
        reward_funcs=reward_funcs,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        peft_config=get_peft_config(model_args),
    )
    trainer_ref["t"] = trainer

    trainer.train()

    # Save and push to hub
    trainer.save_model(training_args.output_dir)
    if training_args.push_to_hub:
        trainer.push_to_hub(dataset_name=script_args.dataset_name)
