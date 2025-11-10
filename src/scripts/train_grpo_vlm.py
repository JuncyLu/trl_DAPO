import sys
import os

import torch
from datasets import load_dataset
from PIL import Image

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
from src.rewards import (
    accuracy_reward,
    think_format_reward,
    get_accuracy_conditioned_length_reward,
    vgr_reward,
    vgr_hard_negative,
)


# Enable logging in a Hugging Face Space
os.environ.setdefault("TRACKIO_SPACE_ID", "trl-trackio")
os.environ.setdefault("WANDB_HTTP_TIMEOUT", "60")
# os.environ["WANDB_MODE"] = "offline"  # Uncomment to enable offline mode


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
    # dataset = load_dataset("lujunxi57/DMD", split="train")
    dataset = load_dataset("./dataset/aokvqa_openr1", split="train")
    dataset = dataset.train_test_split(test_size=100, seed=42)

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

    # Resize overly large images to fit within 1024x1024 (maintain aspect ratio)
    def resize_large_images(example):
        image = example["image"]
        width, height = image.size
        if width > 1024 or height > 1024:
            image.thumbnail((1024, 1024), resample=Image.LANCZOS)
        example["image"] = image
        return example

    dataset = dataset.map(resize_large_images)

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
    length_reward_func = get_accuracy_conditioned_length_reward(
        max_completion_len=training_args.max_completion_length,
        lower_ratio=0.2,
        upper_ratio=0.5,
        alpha=0.5,
    )
    
    vgr_func = vgr_hard_negative if getattr(training_args, "vgr_hard_negative", False) else vgr_reward

    trainer = DAPOTrainer(
        model=model_args.model_name_or_path,
        args=training_args,
        reward_funcs=[accuracy_reward, vgr_func, think_format_reward, length_reward_func],
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
