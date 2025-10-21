#!/usr/bin/env python3
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

"""
Train a VLM with GRPO directly from the original A-OKVQA dataset.

This script loads HuggingFaceM4/A-OKVQA (or another dataset) and performs the
minimal in-script preprocessing to produce a map-style dataset compatible with
TRL's GRPOTrainer (prompts + images), then trains.

Examples
--------
Default A-OKVQA training (map-style, known length; no need to set max_steps):

accelerate launch \
  --config_file examples/accelerate_configs/single_gpu.yaml \
  examples/scripts/grpo_vlm_2.py \
  --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct \
  --output_dir grpo-Qwen2.5-VL-3B-Instruct-aokvqa \
  --learning_rate 1e-5 \
  --dtype bfloat16 \
  --max_prompt_length 2048 \
  --max_completion_length 512 \
  --per_device_train_batch_size 1 \
  --gradient_accumulation_steps 2 \
  --num_generations 2

Use a subset for a quick sanity check:

  ... --subset_size 500 --eval_subset_size 100

Note
----
By default, we use a simple think-format reward and a multiple-choice accuracy reward
that compares the model's predicted letter (A/B/C/D, etc.) against the ground-truth
choice index from A-OKVQA.
"""

import os
import re
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


# Enable logging in a Hugging Face Space
os.environ.setdefault("TRACKIO_SPACE_ID", "trl-trackio")


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


SYSTEM_PROMPT = (
    "A conversation between user and assistant. The user asks a question, and the assistant solves it. "
    "The assistant first thinks about the reasoning process in the mind and then provides the user with the answer. "
    "The reasoning process and answer are enclosed within <think></think> tags, i.e., <think>\nThis is my "
    "reasoning.\n</think>\nThis is my answer."
)


def _build_prompt_text(question: str, choices: list[str]) -> str:
    if not question:
        question = ""
    choices = choices or []
    letters = [chr(ord("A") + i) for i in range(len(choices))]
    choices_lines = "\n".join(f"{letter}. {choice}" for letter, choice in zip(letters, choices))
    ask = "/".join(letters) if letters else "A/B/C/D"
    return f"Question: {question}\nChoices:\n{choices_lines}\nPlease select the correct answer ({ask})."


def _make_conversation(example: dict) -> dict:
    # Check if we already have a prompt (for preprocessed datasets)
    if "prompt" in example and isinstance(example["prompt"], str):
        # Convert string prompt to conversation format
        prompt = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": example["prompt"]},
        ]
        example["prompt"] = prompt
    else:
        # Original logic for datasets with question/choices
        question = example.get("question", "")
        choices = example.get("choices", [])
        prompt_text = _build_prompt_text(question, choices)

        prompt = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text},
        ]
        example["prompt"] = prompt
    
    # unify label name for reward function
    if "label_idx" not in example:
        correct_idx = example.get("correct_choice_idx")
        if correct_idx is not None:
            example["label_idx"] = int(correct_idx)
    
    return example


def _filter_big_images(example: dict, max_size: int) -> bool:
    if max_size <= 0:
        return True
    # Check if we have image_path instead of direct image
    image_path = example.get("image_path")
    if image_path is not None:
        # For image_path, we'll skip filtering for now to avoid loading all images
        return True
    # A-OKVQA provides PIL images under key 'image'
    image = example.get("image")
    if image is None:
        return False
    try:
        w, h = image.size
        return w < max_size and h < max_size
    except Exception:
        return False


def _convert_to_rgb(example: dict) -> dict:
    # Skip RGB conversion if we have image_path instead of direct image
    if "image_path" in example:
        return example
    img = example.get("image")
    if img is not None and getattr(img, "mode", None) != "RGB":
        try:
            example["image"] = img.convert("RGB")
        except Exception:
            pass
    return example


def _strip_think(text: str) -> str:
    # remove <think>...</think>
    return re.sub(r"<think>[\s\S]*?</think>", " ", text, flags=re.IGNORECASE)


def _extract_mcq_letter(text: str, valid_letters: str) -> Optional[str]:
    text = _strip_think(text)
    # Heuristics: look for explicit patterns first
    patterns = [
        r"(?i)(?:final\s+answer|answer\s*is|answer\s*:|correct\s*answer\s*is|答案[:： ])\s*([A-Z])",
        r"\\boxed\{([A-Z])\}",
        r"^\s*[\(\[]?([A-Z])[\)\]]?\s*$",
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            letter = m.group(1).upper()
            if letter in valid_letters:
                return letter
    # Fallback: search the last 200 chars for a standalone [A-D]
    tail = text[-200:]
    m = re.search(rf"(?<![A-Z])([{valid_letters}])(?![A-Z])", tail)
    return m.group(1) if m else None


def mcq_accuracy_reward(
    completions: list[list[dict[str, str]]], label_idx: list[int], choices: Optional[list[list[str]]] = None, **kwargs
) -> list[Optional[float]]:
    """Binary reward for MCQ. Extracts a letter (A/B/C/...) from the completion text and compares against label_idx.

    The function is defensive and returns None if a reliable letter cannot be inferred.
    """
    rewards: list[Optional[float]] = []
    for i, completion in enumerate(completions):
        content = completion[0].get("content", "") if completion and completion[0] else ""
        n_choices = len(choices[i]) if choices is not None and i < len(choices) and isinstance(choices[i], list) else 4
        valid_letters = "".join(chr(ord("A") + j) for j in range(max(1, n_choices)))
        letter = _extract_mcq_letter(content, valid_letters)
        if letter is None:
            rewards.append(None)
            continue
        pred_idx = ord(letter) - ord("A")
        gt_idx = label_idx[i] if i < len(label_idx) else None
        if gt_idx is None:
            rewards.append(None)
            continue
        rewards.append(1.0 if pred_idx == int(gt_idx) else 0.0)
    return rewards


if __name__ == "__main__":
    parser = TrlParser((ScriptArguments, GRPOConfig, ModelConfig, DataArguments))
    script_args, training_args, model_args, data_args = parser.parse_args_and_config()

    # ================
    # 手动修改训练参数
    # ================
    # 方法1: 直接在脚本中修改
    # 批次大小相关
    training_args.per_device_train_batch_size = 2
    training_args.gradient_accumulation_steps = 4
    training_args.num_generations = 4
    
    # 学习率相关
    training_args.learning_rate = 2e-5
    training_args.warmup_steps = 100
    training_args.lr_scheduler_type = "cosine"
    
    # 训练步数
    training_args.max_steps = 2000
    training_args.save_steps = 500
    training_args.eval_steps = 250
    
    # 其他参数
    training_args.logging_steps = 10
    training_args.save_strategy = "steps"
    training_args.evaluation_strategy = "steps"
    training_args.load_best_model_at_end = True
    training_args.metric_for_best_model = "eval_loss"
    
    # GRPO 特定参数
    training_args.beta = 0.1
    training_args.epsilon = 0.2
    training_args.loss_type = "dapo"
    training_args.scale_rewards = "group"
    
    # 生成参数
    training_args.max_prompt_length = 2048
    training_args.max_completion_length = 512
    training_args.temperature = 1.0
    training_args.top_p = 0.9
    
    # 方法2: 使用配置文件 (取消注释下面的代码来使用)
    # import sys
    # sys.path.append('/home/lujunxi57/trl')
    # from training_config import TRAINING_CONFIG
    # for key, value in TRAINING_CONFIG.items():
    #     setattr(training_args, key, value)

    # ----------------
    # Model init
    # ----------------
    dtype = model_args.dtype if model_args.dtype in ["auto", None] else getattr(torch, model_args.dtype)
    training_args.model_init_kwargs = dict(
        revision=model_args.model_revision,
        attn_implementation=model_args.attn_implementation,
        dtype=dtype,
    )
    quantization_config = get_quantization_config(model_args)
    if quantization_config is not None:
        training_args.model_init_kwargs["device_map"] = get_kbit_device_map()
        training_args.model_init_kwargs["quantization_config"] = quantization_config

    # ----------------
    # Dataset load (map-style preferred)
    # ----------------
    loaded: Union[DatasetDict, Dataset] = load_dataset(
        data_args.dataset_path,
        name=data_args.dataset_config_name,
        streaming=data_args.streaming,
    )

    if isinstance(loaded, DatasetDict):
        # Choose splits
        train_dataset = loaded.get(data_args.train_split) or loaded[next(iter(loaded.keys()))]
        eval_dataset = (
            loaded.get(data_args.test_split)
            if training_args.eval_strategy != "no"
            else None
        )
    else:
        train_dataset = loaded
        eval_dataset = None if training_args.eval_strategy == "no" else None

    # Optional subsetting for quick runs (map-style only)
    if not data_args.streaming and data_args.subset_size and data_args.subset_size > 0:
        train_dataset = train_dataset.select(range(min(data_args.subset_size, len(train_dataset))))
    if (
        not data_args.streaming
        and eval_dataset is not None
        and data_args.eval_subset_size
        and data_args.eval_subset_size > 0
    ):
        eval_dataset = eval_dataset.select(range(min(data_args.eval_subset_size, len(eval_dataset))))

    # ----------------
    # In-script preprocessing
    # ----------------
    # 1) Filter too-big images if requested
    if data_args.max_image_size and data_args.max_image_size > 0:
        train_dataset = train_dataset.filter(lambda x: _filter_big_images(x, data_args.max_image_size))
        if eval_dataset is not None:
            eval_dataset = eval_dataset.filter(lambda x: _filter_big_images(x, data_args.max_image_size))

    # 2) Ensure RGB
    train_dataset = train_dataset.map(_convert_to_rgb)
    if eval_dataset is not None:
        eval_dataset = eval_dataset.map(_convert_to_rgb)

    # 3) Build conversation prompt + unify label name
    train_dataset = train_dataset.map(_make_conversation)
    if eval_dataset is not None:
        eval_dataset = eval_dataset.map(_make_conversation)

    if not data_args.streaming:
        try:
            print(f"Loaded train size: {len(train_dataset)}")
            if eval_dataset is not None:
                print(f"Loaded eval size: {len(eval_dataset)}")
        except Exception:
            pass

    # ----------------
    # Training
    # ----------------
    reward_funcs = [think_format_reward, mcq_accuracy_reward]

    trainer = GRPOTrainer(
        model=model_args.model_name_or_path,
        args=training_args,
        reward_funcs=reward_funcs,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        peft_config=get_peft_config(model_args),
    )

    trainer.train()

    trainer.save_model(training_args.output_dir)
    if training_args.push_to_hub:
        trainer.push_to_hub(dataset_name=data_args.dataset_path)

