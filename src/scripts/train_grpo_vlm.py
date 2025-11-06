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

# For Qwen/Qwen2.5-VL-3B-Instruct
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
    --use_vllm \
    --vllm_mode colocate \
    --use_peft \
    --lora_target_modules "q_proj", "v_proj" \
    --log_completions

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
import sys
import os

import torch
from datasets import load_dataset

from trl import (
    ModelConfig,
    ScriptArguments,
    TrlParser,
    get_kbit_device_map,
    get_peft_config,
    get_quantization_config,
)

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.trainer import DAPOConfig, DAPOTrainer
from src.rewards import accuracy_reward, think_format_reward, get_soft_overlong_punishment, mdi_reward, mdi_hard_negative


# Enable logging in a Hugging Face Space
os.environ.setdefault("TRACKIO_SPACE_ID", "trl-trackio")


if __name__ == "__main__":
    parser = TrlParser((ScriptArguments, DAPOConfig, ModelConfig))
    script_args, training_args, model_args = parser.parse_args_and_config()
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
    dataset = load_dataset("./DDM", split="train")
    dataset = dataset.train_test_split(test_size=0.1, seed=42)

    SYSTEM_PROMPT = (
        "A conversation between user and assistant. The user asks a multiple-choice question about an image, and the "
        "assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the "
        "user with the answer. The reasoning process is enclosed within <think></think> tags, and the final answer must "
        "be enclosed within <answer></answer> tags as exactly one capital letter from A to J with no extra text or symbols. "
        "The response must end immediately after the closing </answer> tag. For example:\n"
        "<think>\nThis is my reasoning.\n</think>\n<answer>C</answer>"
    )

    def make_conversation(example):
        prompt = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": example["problem"]},
        ]
        return {"prompt": prompt}

    dataset = dataset.map(make_conversation)

    # Filter overly large images (allow up to 1024x1024 inclusive)
    def filter_big_images(example):
        image = example["image"]
        return image.size[0] <= 1024 and image.size[1] <= 1024

    dataset = dataset.filter(filter_big_images)

    def convert_to_rgb(example):
        image = example["image"]
        if image.mode != "RGB":
            image = image.convert("RGB")
        example["image"] = image
        return example

    dataset = dataset.map(convert_to_rgb)

    train_dataset = dataset["train"]
    eval_dataset = dataset["test"] if training_args.eval_strategy != "no" else None

    ################
    # Training
    ################
    # 创建length reward函数
    length_reward_func = get_soft_overlong_punishment(
        max_completion_len=training_args.max_completion_length,
        soft_punish_cache=training_args.soft_punish_cache
    )
    
    # 选择使用哪一种 MDI 奖励
    mdi_func = mdi_hard_negative if getattr(training_args, "mdi_hard_negative", False) else mdi_reward

    trainer = DAPOTrainer(
        model=model_args.model_name_or_path,
        args=training_args,
        reward_funcs=[accuracy_reward, mdi_func, think_format_reward, length_reward_func],
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        peft_config=get_peft_config(model_args),
    )

    # Respect external log paths if provided via args (dapo_config.py defaults already set)
    # No internal timestamping here; the shell script should pass fully qualified paths

    trainer.train()

    # Save and push to hub
    trainer.save_model(training_args.output_dir)
    if training_args.push_to_hub:
        trainer.push_to_hub(dataset_name=script_args.dataset_name)
