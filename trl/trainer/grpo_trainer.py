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

import inspect
import os
import textwrap
import json
from datetime import datetime
from collections import defaultdict, deque
from contextlib import nullcontext, contextmanager
from functools import partial
from pathlib import Path
from typing import Any, Callable, Optional, Union

import datasets
import numpy as np
import torch
import torch.utils.data
import transformers
from accelerate import logging
from accelerate.utils import broadcast_object_list, gather, gather_object, is_peft_model, set_seed
from datasets import Dataset, IterableDataset
from torch import nn
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.utils.data import DataLoader, Sampler
from transformers import (
    AutoConfig,
    AutoModelForSequenceClassification,
    AutoProcessor,
    AutoTokenizer,
    GenerationConfig,
    PreTrainedModel,
    PreTrainedTokenizerBase,
    ProcessorMixin,
    TrainerCallback,
    is_wandb_available,
)
from transformers.trainer_utils import seed_worker
from transformers.utils import is_datasets_available, is_flash_attn_2_available, is_peft_available, is_rich_available

from ..data_utils import apply_chat_template, is_conversational, maybe_apply_chat_template, prepare_multimodal_messages
from ..extras.profiling import profiling_context, profiling_decorator
from ..extras.vllm_client import VLLMClient
from ..import_utils import is_liger_kernel_available, is_vllm_available
from ..models import prepare_deepspeed, prepare_fsdp, prepare_peft_model, unwrap_model_for_generation
from ..models.utils import _ForwardRedirection
from .attention_metrics import AttentionSampleResult, compute_qwen_attention_metrics_for_batch
from .base_trainer import BaseTrainer
from .callbacks import SyncRefModelCallback
from .grpo_config import GRPOConfig
from .utils import (
    RepeatSampler,
    disable_dropout_in_model,
    ensure_master_addr_port,
    entropy_from_logits,
    identity,
    nanmax,
    nanmin,
    nanstd,
    pad,
    print_prompt_completions_sample,
    selective_log_softmax,
    shuffle_sequence_dict,
    split_pixel_values_by_grid,
    split_tensor_dict,
    unsplit_pixel_values_by_grid,
)


if is_peft_available():
    from peft import PeftConfig, PeftModel

if is_liger_kernel_available():
    from liger_kernel.chunked_loss import LigerFusedLinearGRPOLoss

if is_vllm_available():
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import GuidedDecodingParams

if is_wandb_available():
    import wandb

# Optional rich console for colored output
try:  # optional dependency
    from rich.console import Console
    from rich.table import Table
    from rich import box
except Exception:
    Console = None
    Table = None
    box = None


logger = logging.get_logger(__name__)

# What we call a reward function is a callable that takes a list of prompts and completions and returns a list of
# rewards. When it's a string, it's a model ID, so it's loaded as a pretrained model.
RewardFunc = Union[str, PreTrainedModel, Callable[[list, list], list[float]]]


class GRPOTrainer(BaseTrainer):
    """
    Trainer for the Group Relative Policy Optimization (GRPO) method. This algorithm was initially proposed in the
    paper [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language
    Models](https://huggingface.co/papers/2402.03300).

    Example:

    ```python
    from datasets import load_dataset
    from trl import GRPOTrainer

    dataset = load_dataset("trl-lib/tldr", split="train")


    def reward_func(completions, **kwargs):
        # Dummy reward function that rewards completions with more unique letters.
        return [float(len(set(completion))) for completion in completions]


    trainer = GRPOTrainer(
        model="Qwen/Qwen2-0.5B-Instruct",
        reward_funcs=reward_func,
        train_dataset=dataset,
    )

    trainer.train()
    ```

    Args:
        model (`Union[str, PreTrainedModel]`):
            Model to be trained. Can be either:

            - A string, being the *model id* of a pretrained model hosted inside a model repo on huggingface.co, or a
              path to a *directory* containing model weights saved using
              [`~transformers.PreTrainedModel.save_pretrained`], e.g., `'./my_model_directory/'`. The model is loaded
              using [`~transformers.AutoModelForCausalLM.from_pretrained`] with the keyword arguments in
              `args.model_init_kwargs`.
            - A [`~transformers.PreTrainedModel`] object. Only causal language models are supported.
        reward_funcs (`Union[RewardFunc, list[RewardFunc]]`):
            Reward functions to be used for computing the rewards. To compute the rewards, we call all the reward
            functions with the prompts and completions and sum the rewards. Can be either:

            - A single reward function, such as:
                - A string: The *model ID* of a pretrained model hosted inside a model repo on huggingface.co, or a
                path to a *directory* containing model weights saved using
                [`~transformers.PreTrainedModel.save_pretrained`], e.g., `'./my_model_directory/'`. The model is loaded
                using [`~transformers.AutoModelForSequenceClassification.from_pretrained`] with `num_labels=1` and the
                keyword arguments in `args.model_init_kwargs`.
                - A [`~transformers.PreTrainedModel`] object: Only sequence classification models are supported.
                - A custom reward function: The function is provided with the prompts and the generated completions,
                  plus any additional columns in the dataset. It should return a list of rewards. Custom reward
                  functions can also return `None` when the reward is not applicable to those samples. This is useful
                  for multi-task training where different reward functions apply to different types of samples. When a
                  reward function returns `None` for a sample, that reward function is excluded from the reward
                  calculation for that sample. For more details, see [Using a custom reward
                  function](#using-a-custom-reward-function).

                  The trainer's state is also passed to the reward function. The trainer's state is an instance of
                  [`~transformers.TrainerState`] and can be accessed by accessing the `trainer_state` argument to the
                  reward function's signature.
            - A list of reward functions, where each item can independently be any of the above types. Mixing different
            types within the list (e.g., a string model ID and a custom reward function) is allowed.
        args ([`GRPOConfig`], *optional*):
            Configuration for this trainer. If `None`, a default configuration is used.
        train_dataset ([`~datasets.Dataset`] or [`~datasets.IterableDataset`]):
            Dataset to use for training. It must include a column `"prompt"`. Any additional columns in the dataset is
            ignored. The format of the samples can be either:

            - [Standard](dataset_formats#standard): Each sample contains plain text.
            - [Conversational](dataset_formats#conversational): Each sample contains structured messages (e.g., role
              and content).
        eval_dataset ([`~datasets.Dataset`], [`~datasets.IterableDataset`] or `dict[str, Union[Dataset, IterableDataset]]`):
            Dataset to use for evaluation. It must meet the same requirements as `train_dataset`.
        processing_class ([`~transformers.PreTrainedTokenizerBase`], [`~transformers.ProcessorMixin`], *optional*):
            Processing class used to process the data. The padding side must be set to "left". If `None`, the
            processing class is loaded from the model's name with [`~transformers.AutoProcessor.from_pretrained`]. A
            padding token, `tokenizer.pad_token`, must be set. If the processing class has not set a padding token,
            `tokenizer.eos_token` will be used as the default.
        reward_processing_classes ([`~transformers.PreTrainedTokenizerBase`] or `list[PreTrainedTokenizerBase]`, *optional*):
            Processing classes corresponding to the reward functions specified in `reward_funcs`. Can be either:

            - A single processing class: Used when `reward_funcs` contains only one reward function.
            - A list of processing classes: Must match the order and length of the reward functions in `reward_funcs`.
            If set to `None`, or if an element of the list corresponding to a [`~transformers.PreTrainedModel`] is
            `None`, the tokenizer for the model is automatically loaded using
            [`~transformers.AutoTokenizer.from_pretrained`]. For elements in `reward_funcs` that are custom reward
            functions (not [`~transformers.PreTrainedModel`]), the corresponding entries in `reward_processing_classes`
            are ignored.
        callbacks (list of [`~transformers.TrainerCallback`], *optional*):
            List of callbacks to customize the training loop. Will add those to the list of default callbacks detailed
            in [here](https://huggingface.co/docs/transformers/main_classes/callback).

            If you want to remove one of the default callbacks used, use the [`~transformers.Trainer.remove_callback`]
            method.
        optimizers (`tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LambdaLR]`, *optional*, defaults to `(None, None)`):
            A tuple containing the optimizer and the scheduler to use. Will default to an instance of [`AdamW`] on your
            model and a scheduler given by [`get_linear_schedule_with_warmup`] controlled by `args`.
        peft_config ([`~peft.PeftConfig`], *optional*):
            PEFT configuration used to wrap the model. If `None`, the model is not wrapped.
    """

    _tag_names = ["trl", "grpo"]
    _name = "GRPO"
    _paper = {
        "title": "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models",
        "id": "2402.03300",
        # docstyle-ignore
        "citation": textwrap.dedent("""\
            @article{shao2024deepseekmath,
                title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
                author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and Junxiao Song and Mingchuan Zhang and Y. K. Li and Y. Wu and Daya Guo},
                year         = 2024,
                eprint       = {arXiv:2402.03300},
            }
            """),
    }

    def __init__(
        self,
        model: Union[str, PreTrainedModel],
        reward_funcs: Union[RewardFunc, list[RewardFunc]],
        args: Optional[GRPOConfig] = None,
        train_dataset: Optional[Union[Dataset, IterableDataset]] = None,
        eval_dataset: Optional[Union[Dataset, IterableDataset, dict[str, Union[Dataset, IterableDataset]]]] = None,
        processing_class: Optional[Union[PreTrainedTokenizerBase, ProcessorMixin]] = None,
        reward_processing_classes: Optional[Union[PreTrainedTokenizerBase, list[PreTrainedTokenizerBase]]] = None,
        callbacks: Optional[list[TrainerCallback]] = None,
        optimizers: tuple[Optional[torch.optim.Optimizer], Optional[torch.optim.lr_scheduler.LambdaLR]] = (None, None),
        peft_config: Optional["PeftConfig"] = None,
    ):
        # Args
        if args is None:
            model_name = model if isinstance(model, str) else model.config._name_or_path
            model_name = model_name.split("/")[-1]
            args = GRPOConfig(f"{model_name}-GRPO")

        # Models
        # Trained model
        model_init_kwargs = args.model_init_kwargs or {}
        if isinstance(model, str):
            model_id = model
            dtype = model_init_kwargs.get("dtype")
            if isinstance(dtype, torch.dtype) or dtype == "auto" or dtype is None:
                pass  # dtype is already a torch.dtype or "auto" or None
            elif isinstance(dtype, str):  # it's a str, but not "auto"
                dtype = getattr(torch, dtype)
                model_init_kwargs["dtype"] = dtype
            else:
                raise ValueError(
                    "Invalid `dtype` passed to `GRPOConfig`. Expected either 'auto' or a string representing "
                    f"a `torch.dtype` (e.g., 'float32'), but got {dtype}."
                )
            # Disable caching if gradient checkpointing is enabled (not supported)
            config = AutoConfig.from_pretrained(model_id)
            architecture = getattr(transformers, config.architectures[0])
            model = architecture.from_pretrained(model_id, **model_init_kwargs)
        else:
            model_id = model.config._name_or_path
            if args.model_init_kwargs is not None:
                logger.warning(
                    "You passed `model_init_kwargs` to the `GRPOConfig`, but your model is already instantiated. "
                    "The `model_init_kwargs` will be ignored."
                )

        # Some models (SmolVLM/Idefics3) don't support `logits_to_keep` argument and error out if we pass it
        # Inspect the forward method before we wrap the model with PEFT
        self.model_kwarg_keys = (
            inspect.signature(model.forward).parameters.keys()
            if not hasattr(model, "get_base_model")
            else inspect.signature(model.get_base_model().forward).parameters.keys()
        )

        if peft_config is not None or (is_peft_available() and isinstance(model, PeftModel)):
            model = prepare_peft_model(model, peft_config, args)

        # Processing class
        if processing_class is None:
            processing_class = AutoProcessor.from_pretrained(
                model.config._name_or_path, 
                truncation_side="left",
                use_fast=False
            )

        # Handle pad token for processors or tokenizers
        if isinstance(processing_class, ProcessorMixin):
            tokenizer = processing_class.tokenizer
        elif isinstance(processing_class, PreTrainedTokenizerBase):
            tokenizer = processing_class
        else:
            raise TypeError("The `processing_class` must be either a `PreTrainedTokenizerBase` or a `ProcessorMixin`")

        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        if hasattr(model, 'config'):
            model.config.pad_token_id = tokenizer.pad_token_id
            model.config.bos_token_id = tokenizer.bos_token_id
            model.config.eos_token_id = tokenizer.eos_token_id
            
            if hasattr(model, 'generation_config') and model.generation_config is not None:
                model.generation_config.pad_token_id = tokenizer.pad_token_id
                model.generation_config.bos_token_id = tokenizer.bos_token_id
                model.generation_config.eos_token_id = tokenizer.eos_token_id

        self.pad_token = tokenizer.pad_token
        self.pad_token_id = tokenizer.pad_token_id
        self.eos_token_id = tokenizer.eos_token_id

        # Reward functions
        if not isinstance(reward_funcs, list):
            reward_funcs = [reward_funcs]
        self.reward_func_names = []
        for i, reward_func in enumerate(reward_funcs):
            if isinstance(reward_func, str):
                reward_funcs[i] = AutoModelForSequenceClassification.from_pretrained(
                    reward_func, num_labels=1, **model_init_kwargs
                )
                
                # 对齐奖励模型的token配置
                if hasattr(reward_funcs[i], 'config'):
                    reward_funcs[i].config.pad_token_id = tokenizer.pad_token_id
                    reward_funcs[i].config.bos_token_id = tokenizer.bos_token_id
                    reward_funcs[i].config.eos_token_id = tokenizer.eos_token_id
                    
                    if hasattr(reward_funcs[i], 'generation_config') and reward_funcs[i].generation_config is not None:
                        reward_funcs[i].generation_config.pad_token_id = tokenizer.pad_token_id
                        reward_funcs[i].generation_config.bos_token_id = tokenizer.bos_token_id
                        reward_funcs[i].generation_config.eos_token_id = tokenizer.eos_token_id
                        
            if isinstance(reward_funcs[i], nn.Module):  # Use Module over PretrainedModel for compat w/ compiled models
                self.reward_func_names.append(reward_funcs[i].config._name_or_path.split("/")[-1])
            else:
                self.reward_func_names.append(reward_funcs[i].__name__)
        self.reward_funcs = reward_funcs

        # Reward weights
        if args.reward_weights is not None:
            if len(args.reward_weights) != len(reward_funcs):
                raise ValueError(
                    f"Number of reward weights ({len(args.reward_weights)}) must match number of reward "
                    f"functions ({len(reward_funcs)})"
                )
            self.reward_weights = torch.tensor(args.reward_weights, dtype=torch.float32)
        else:
            self.reward_weights = torch.ones(len(reward_funcs), dtype=torch.float32)

        # Reward processing class
        if reward_processing_classes is None:
            reward_processing_classes = [None] * len(reward_funcs)
        elif not isinstance(reward_processing_classes, list):
            reward_processing_classes = [reward_processing_classes]
        if len(reward_processing_classes) != len(reward_funcs):
            raise ValueError(
                f"The number of reward processing classes ({len(reward_processing_classes)}) must match the number of "
                f"reward functions ({len(reward_funcs)})."
            )

        for i, (reward_processing_class, reward_func) in enumerate(zip(reward_processing_classes, reward_funcs)):
            if isinstance(reward_func, PreTrainedModel):
                if reward_processing_class is None:
                    reward_processing_class = AutoTokenizer.from_pretrained(reward_func.config._name_or_path)
                if reward_processing_class.pad_token_id is None:
                    reward_processing_class.pad_token = reward_processing_class.eos_token
                # The reward model computes the reward for the latest non-padded token in the input sequence.
                # So it's important to set the pad token ID to the padding token ID of the processing class.
                reward_func.config.pad_token_id = reward_processing_class.pad_token_id
                reward_processing_classes[i] = reward_processing_class

        self.reward_processing_classes = reward_processing_classes

        # Realtime rollout logging setup (main process only)
        self._rollout_step_count = 0
        self._console = None

        # current batch attention parameters for reward
        self._attention_text_current_batch = []
        self._attention_vision_current_batch = []
        self._num_text_tokens_current_batch = []
        self._num_vision_tokens_current_batch = []
        
        # 设置注意力诊断标志（在super().__init__之前）
        self.compute_attention_metrics = args.compute_attention_metrics

        # Training arguments
        self.max_prompt_length = args.max_prompt_length
        self.max_completion_length = args.max_completion_length  # = |o_i| in the GRPO paper
        self.num_generations = args.num_generations  # = G in the GRPO paper
        self.temperature = args.temperature
        self.top_p = args.top_p
        self.top_k = args.top_k
        self.min_p = args.min_p
        self.repetition_penalty = args.repetition_penalty
        self.use_transformers_paged = args.use_transformers_paged
        self.use_vllm = args.use_vllm
        self.vllm_mode = args.vllm_mode
        self.vllm_gpu_memory_utilization = args.vllm_gpu_memory_utilization  # only applies to colocation mode
        self.vllm_tensor_parallel_size = args.vllm_tensor_parallel_size  # only applies to colocation mode
        self.vllm_importance_sampling_correction = args.vllm_importance_sampling_correction
        self.vllm_importance_sampling_cap = args.vllm_importance_sampling_cap
        self.use_liger_loss = args.use_liger_loss
        self.loss_type = args.loss_type
        self.scale_rewards = args.scale_rewards
        self.importance_sampling_level = args.importance_sampling_level
        self.mask_truncated_completions = args.mask_truncated_completions
        self.top_entropy_quantile = args.top_entropy_quantile
        if self.use_liger_loss and self.top_entropy_quantile < 1.0:
            raise NotImplementedError(
                "Liger Kernels don't currently support masking token positions based on entropy."
            )
        if self.use_liger_loss and not self.importance_sampling_level == "token":
            raise NotImplementedError(
                "Liger Kernels currently only support token-level importance sampling. Please set"
                "`importance_sampling_level` to 'token'."
            )

        # Datasets
        self.shuffle_dataset = args.shuffle_dataset

        if (
            isinstance(train_dataset, IterableDataset)
            or isinstance(eval_dataset, IterableDataset)
            or (
                isinstance(eval_dataset, dict) and any(isinstance(ds, IterableDataset) for ds in eval_dataset.values())
            )
        ):
            # See https://github.com/huggingface/trl/issues/3213
            raise NotImplementedError(
                "Iterable datasets are not yet supported in GRPOTrainer. Please use a standard dataset instead."
            )

        # Multi-step
        self.num_iterations = args.num_iterations  # = 𝜇 in the GRPO paper
        self.epsilon_low = args.epsilon
        self.epsilon_high = args.epsilon_high if args.epsilon_high is not None else args.epsilon
        # Tracks the number of iterations (forward + backward passes), including those within a grad accum cycle
        self._step = 0
        # Buffer the batch to reuse generated outputs across multiple updates. For more details, see
        # `_get_train_sampler` and `_prepare_inputs`.
        self._buffered_inputs = None

        # The trainer estimates the number of FLOPs (floating-point operations) using the number of elements in the
        # input tensor associated with the key "input_ids". However, in GRPO, the sampled data does not include the
        # "input_ids" key. Instead, the available keys is "prompt". As a result, the trainer issues the warning:
        # "Could not estimate the number of tokens of the input, floating-point operations will not be computed." To
        # suppress this warning, we set the "estimate_tokens" key in the model's "warnings_issued" dictionary to True.
        # This acts as a flag to indicate that the warning has already been issued.
        model.warnings_issued["estimate_tokens"] = True

        super().__init__(
            model=model,
            args=args,
            data_collator=identity,  # No data collation is needed in GRPO
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            processing_class=processing_class,
            callbacks=callbacks,
            optimizers=optimizers,
            # In Trainer, `training_step` scales the loss by `gradient_accumulation_steps` only if `compute_loss_func`
            # is None. For DAPO, loss scaling instead depends on the total number of completions tokens across the
            # global accumulated batch. To control scaling ourselves, we must disable Trainer’s built-in scaling. The
            # simplest (though a bit hacky) way is to set `compute_loss_func` to any non-None value, which bypasses
            # that behavior without rewriting `training_step`.
            compute_loss_func="non-None value to disable scaling",
        )

        # 添加模型解包工具函数和注意力实现切换上下文管理器
        self._add_model_unwrap_utilities()

        # Reference model
        self.beta = args.beta
        if self.beta == 0.0:
            # If beta is 0.0, the reference model is not needed
            self.ref_model = None
        elif is_peft_model(model):
            # If PEFT is used, the reference model is not needed since the adapter can be disabled
            # to revert to the initial model.
            self.ref_model = None
        else:
            # For deepspeed, fsdp or non-distributed models, create a reference model from scratch
            config = AutoConfig.from_pretrained(model_id)
            architecture = getattr(transformers, config.architectures[0])
            self.ref_model = architecture.from_pretrained(model_id, **model_init_kwargs)
            
            # 对齐参考模型的token配置
            if hasattr(self.ref_model, 'config'):
                self.ref_model.config.pad_token_id = tokenizer.pad_token_id
                self.ref_model.config.bos_token_id = tokenizer.bos_token_id
                self.ref_model.config.eos_token_id = tokenizer.eos_token_id
                
                if hasattr(self.ref_model, 'generation_config') and self.ref_model.generation_config is not None:
                    self.ref_model.generation_config.pad_token_id = tokenizer.pad_token_id
                    self.ref_model.generation_config.bos_token_id = tokenizer.bos_token_id
                    self.ref_model.generation_config.eos_token_id = tokenizer.eos_token_id

        # Disable dropout in the models
        if args.disable_dropout:
            disable_dropout_in_model(model)
            if self.ref_model is not None:
                disable_dropout_in_model(self.ref_model)

        # Liger loss
        if self.use_liger_loss:
            if not is_liger_kernel_available():
                raise ImportError(
                    "Liger is required to use `liger_loss` as the GRPO loss. Run `pip install liger-kernel`."
                )
            # redirect the model.module forward to the model forward to ensure pre-forward hooks are called
            self._forward_redirection = _ForwardRedirection()

            self.liger_grpo_loss = LigerFusedLinearGRPOLoss(
                beta=self.beta,
                epsilon_low=self.epsilon_low,
                epsilon_high=self.epsilon_high,
                temperature=self.temperature,
                use_ref_model=self.beta != 0.0,
                loss_type=self.loss_type,
                max_completion_length=self.max_completion_length,
            )

        # Initialize the metrics
        self._metrics = {"train": defaultdict(list), "eval": defaultdict(list)}
        self._total_train_tokens = 0
        self.log_completions = args.log_completions
        self.wandb_log_unique_prompts = args.wandb_log_unique_prompts
        self.num_completions_to_print = args.num_completions_to_print
        # Keep logs sized to the generation batch to record only outputs from the latest model update.
        self._logs = {
            "images": deque(maxlen=args.generation_batch_size),
            "prompt": deque(maxlen=args.generation_batch_size),
            "completion": deque(maxlen=args.generation_batch_size),
            "rewards": defaultdict(lambda: deque(maxlen=args.generation_batch_size)),
            "advantages": deque(maxlen=args.generation_batch_size),
        }
        # Keep attention sample results if enabled
        if self.compute_attention_metrics:
            self._logs["attention"] = deque(maxlen=args.generation_batch_size)
            self._attention_skip_reasons = deque(maxlen=args.generation_batch_size)
        else:
            self._logs["attention"] = None
            self._attention_skip_reasons = None

        # Ensure each process receives a unique seed to prevent duplicate completions when generating with
        # transformers if num_generations exceeds per_device_train_batch_size. We could skip it if we use vLLM, but
        # it's safer to set it in all cases.
        set_seed(args.seed, device_specific=True)

        if self.use_vllm:
            if not is_vllm_available():
                raise ImportError(
                    "vLLM is not available and `use_vllm` is set to True. Please install vLLM with "
                    "`pip install trl[vllm]` to use it."
                )

            if self.vllm_mode == "server":
                if self.accelerator.is_main_process:
                    if args.vllm_server_base_url is not None:
                        base_url = args.vllm_server_base_url
                    else:
                        base_url = f"http://{args.vllm_server_host}:{args.vllm_server_port}"
                    self.vllm_client = VLLMClient(base_url=base_url, connection_timeout=args.vllm_server_timeout)
                    self.vllm_client.init_communicator(device=torch.cuda.current_device())

            elif self.vllm_mode == "colocate":
                # Make sure vllm_tensor_parallel_size group size evenly divides the world size - each group should have
                # the same number of ranks
                if not self.accelerator.num_processes % self.vllm_tensor_parallel_size == 0:
                    raise ValueError(
                        f"vllm_tensor_parallel_size ({self.vllm_tensor_parallel_size}) must divide world size "
                        f"({self.accelerator.num_processes}) evenly."
                    )

                if self.vllm_tensor_parallel_size > 1:
                    # Create subgroups of ranks for TP, each group with `vllm_tensor_parallel_size` ranks.
                    # For example, if world_size=8 and vllm_tensor_parallel_size=2 → groups: [0,1], [2,3], [4,5], [6,7]
                    self.tp_group, _ = torch.distributed.new_subgroups_by_enumeration(
                        [
                            list(range(i * self.vllm_tensor_parallel_size, (i + 1) * self.vllm_tensor_parallel_size))
                            for i in range(self.accelerator.num_processes // self.vllm_tensor_parallel_size)
                        ]
                    )

                # vLLM requires the environment variables to be set for distributed training.
                os.environ["RANK"] = str(self.accelerator.process_index)
                os.environ["LOCAL_RANK"] = str(self.accelerator.local_process_index)
                os.environ["WORLD_SIZE"] = str(self.accelerator.num_processes)
                # Ensure distributed rendezvous variables are set without colliding across concurrent runs
                ensure_master_addr_port()

                if self.max_prompt_length is not None and self.max_completion_length is not None:
                    max_model_len = self.max_prompt_length + self.max_completion_length
                else:
                    max_model_len = None
                self.llm = LLM(
                    model=model.name_or_path,
                    tensor_parallel_size=args.vllm_tensor_parallel_size,
                    gpu_memory_utilization=self.vllm_gpu_memory_utilization,
                    max_num_seqs=self.args.per_device_train_batch_size
                    * self.vllm_tensor_parallel_size
                    * self.args.steps_per_generation,
                    max_model_len=max_model_len,
                    distributed_executor_backend="external_launcher",
                    # Feed identical seed for tp groups to ensure sampling results are the same across workers
                    seed=self.accelerator.process_index // self.vllm_tensor_parallel_size,
                    # Latest vLLM v1 memory profiler is misled by the high default value (i.e., 32768) - thinking there's not enough memory
                    max_num_batched_tokens=4096,
                    model_impl=self.args.vllm_model_impl,
                    enable_sleep_mode=self.args.vllm_enable_sleep_mode,
                    # Important so temperature scaling/logit tweaking affects the TIS log probs
                    logprobs_mode="processed_logprobs",
                )
                if self.args.vllm_enable_sleep_mode:
                    self.llm.sleep(level=1)
            else:
                raise ValueError(f"vllm_mode must be either 'server' or 'colocate', got '{self.vllm_mode}'.")

            # vLLM specific sampling arguments
            self.guided_decoding_regex = args.vllm_guided_decoding_regex

            self._last_loaded_step = -1  # tag to avoid useless loading during grad accumulation

            # When using vLLM, the main process is responsible for loading the model weights. This can cause process
            # desynchronization and seems to lead to DeepSpeed hanging during initialization. To prevent this, we
            # synchronize all processes after vLLM has been fully initialized.
            self.accelerator.wait_for_everyone()
        else:
            generation_kwargs = {
                "max_new_tokens": self.max_completion_length,
                "do_sample": True,
                "pad_token_id": tokenizer.pad_token_id,
                "bos_token_id": tokenizer.bos_token_id,
                "eos_token_id": tokenizer.eos_token_id,
                "temperature": self.temperature,
                "top_p": self.top_p,
                "top_k": self.top_k,
                "min_p": self.min_p,
                "repetition_penalty": self.repetition_penalty,
                "cache_implementation": args.cache_implementation,
            }
            if args.generation_kwargs is not None:
                generation_kwargs.update(args.generation_kwargs)
            self.generation_config = GenerationConfig(**generation_kwargs)

        # Gradient accumulation requires scaled loss. Normally, loss scaling in the parent class depends on whether the
        # model accepts loss-related kwargs. Since we compute our own loss, this check is irrelevant. We set
        # self.model_accepts_loss_kwargs to False to enable scaling.
        self.model_accepts_loss_kwargs = False

        # Add tags to the model
        self.model.add_model_tags(self._tag_names)

        # 检查并禁用不兼容的注意力诊断选项
        if self.compute_attention_metrics and self.use_vllm:
            logger.warning("`compute_attention_metrics=True` is not supported when using vLLM. Disabling attention diagnostics.")
            self.compute_attention_metrics = False
        if self.compute_attention_metrics and self.use_transformers_paged:
            logger.warning("`compute_attention_metrics=True` is not supported with paged generation. Disabling attention diagnostics.")
            self.compute_attention_metrics = False

        # 确保training_logs目录存在（无论是否启用realtime_rollout_logging）
        if self.accelerator.is_main_process:
            try:
                training_logs_dir = "/home/lujunxi57/trl/training_logs"
                os.makedirs(training_logs_dir, exist_ok=True)
            except Exception as e:
                logger.warning("Failed to create training logs directory: %s", e)
        
        if self.accelerator.is_main_process and getattr(self.args, "realtime_rollout_logging", False):
            try:
                if getattr(self.args, "rollout_log_path", None):
                    os.makedirs(os.path.dirname(self.args.rollout_log_path), exist_ok=True)
                    if not os.path.exists(self.args.rollout_log_path):
                        with open(self.args.rollout_log_path, "w", encoding="utf-8") as f:
                            f.write("# Rollout Results Log\n\n")
                            f.write("This file contains detailed rollout results from GRPO training.\n\n")

                if getattr(self.args, "attention_diag_log_path", None):
                    os.makedirs(os.path.dirname(self.args.attention_diag_log_path), exist_ok=True)
                    if not os.path.exists(self.args.attention_diag_log_path):
                        with open(self.args.attention_diag_log_path, "w", encoding="utf-8") as f:
                            f.write("# Attention Diagnostics Log\n\n")
                            f.write("This file contains MDI attention diagnostics from GRPO training.\n\n")
            except Exception as e:
                logger.exception("Failed to set up logging files: %s", e)
            if getattr(self.args, "colorize_output", False) and Console is not None:
                try:
                    self._console = Console()
                except Exception:
                    self._console = None

        if self.ref_model is not None:
            if self.is_deepspeed_enabled:
                self.ref_model = prepare_deepspeed(self.ref_model, self.accelerator)
            elif self.is_fsdp_enabled:
                self.ref_model = prepare_fsdp(self.ref_model, self.accelerator)
            else:
                self.ref_model = self.accelerator.prepare_model(self.ref_model, evaluation_mode=True)

        if args.sync_ref_model:
            self.add_callback(SyncRefModelCallback(ref_model=self.ref_model, accelerator=self.accelerator))

        for i, reward_func in enumerate(self.reward_funcs):
            if isinstance(reward_func, PreTrainedModel):
                if self.is_deepspeed_enabled:
                    self.reward_funcs[i] = prepare_deepspeed(reward_func, self.accelerator)
                else:
                    # set device placement to True to make `prepare_model` move `reward_func` to device when using fsdp
                    self.reward_funcs[i] = self.accelerator.prepare_model(
                        reward_func, evaluation_mode=True, device_placement=True
                    )

    def _set_signature_columns_if_needed(self):
        # If `self.args.remove_unused_columns` is True, non-signature columns are removed.
        # By default, this method sets `self._signature_columns` to the model's expected inputs.
        # In GRPOTrainer, we preprocess data, so using the model's signature columns doesn't work.
        # Instead, we set them to the columns expected by the `training_step` method, hence the override.
        if self._signature_columns is None:
            self._signature_columns = ["prompt", "image", "images"]

    # This method overrides `Trainer.get_train_dataloader` to support our custom batching strategy.
    # Instead of returning a standard per-step batch (i.e., `per_device_batch_size), our dataloader loads an
    # *generation* batch (i.e., `per_device_batch_size × steps_per_generation`). This allows us to generate completions
    # once every steps_per_generation step—rather than once per accumulation step—which is significantly more
    # efficient. The only change from the original implementation is multiplying the batch size by
    # `steps_per_generation`. Thus, `_prepare_inputs` is called with this *generation* batch, and it handles the
    # splitting internally.
    # Maintenance note: This method is a copy-paste of the original `Trainer.get_train_dataloader` with only one line
    # modification. As a result, some parts of the method aren't relevant to GRPO, but we keep them to stay one line
    # apart from the super method, ensuring easier maintenance in the future.
    def get_train_dataloader(self):
        if self.train_dataset is None:
            raise ValueError("Trainer: training requires a train_dataset.")

        train_dataset = self.train_dataset
        data_collator = self.data_collator
        if is_datasets_available() and isinstance(train_dataset, datasets.Dataset):
            train_dataset = self._remove_unused_columns(train_dataset, description="training")
        else:
            data_collator = self._get_collator_with_removed_columns(data_collator, description="training")

        dataloader_params = {
            "batch_size": self._train_batch_size * self.args.steps_per_generation,  # < this is the change
            "collate_fn": data_collator,
            "num_workers": self.args.dataloader_num_workers,
            "pin_memory": self.args.dataloader_pin_memory,
            "persistent_workers": self.args.dataloader_persistent_workers,
        }

        if not isinstance(train_dataset, torch.utils.data.IterableDataset):
            dataloader_params["sampler"] = self._get_train_sampler()
            dataloader_params["drop_last"] = self.args.dataloader_drop_last
            dataloader_params["worker_init_fn"] = partial(
                seed_worker, num_workers=self.args.dataloader_num_workers, rank=self.args.process_index
            )

            dataloader_params["prefetch_factor"] = self.args.dataloader_prefetch_factor

        return self.accelerator.prepare(DataLoader(train_dataset, **dataloader_params))

    def _get_train_sampler(self, dataset: Optional[Dataset] = None) -> Sampler:
        # Returns a sampler that
        # 1. ensures each prompt is repeated across multiple processes. This guarantees that identical prompts are
        #    distributed to different GPUs, allowing rewards to be computed and normalized correctly within each prompt
        #    group. Using the same seed across processes ensures consistent prompt assignment, preventing discrepancies
        #    in group formation.
        # 2. repeats the batch multiple times to allow reusing generations across multiple updates. Refer to
        #    _prepare_inputs to see how the generations are stored and reused.

        # In the following figure, the values are the prompt indices. The first row shows the first sampled batch, the
        # second row shows the second sampled batch, and so on.
        #
        #                                      |   GPU 0  |   GPU 1  |
        #
        #                 global_step   step    <-───>  num_generations=2
        #                                       <-───────> per_device_train_batch_size=3
        #  grad_accum    ▲  ▲  0          0     0   0   1   1   2   2   <- Generate for the first `steps_per_generation` (prompts 0 to 11); store the completions; use the first slice to compute the loss
        #     =2         ▼  |  0          1     3   3   4   4   5   5   <- Take the stored generations and use the second slice to compute the loss
        #                   |
        #                   |  1          2     6   6   7   7   8   8   <- Take the stored generations and use the third slice to compute the loss
        #  steps_per_gen=4  ▼  1          3     9   9  10  10  11  11   <- Take the stored generations and use the fourth slice to compute the loss
        #
        #                      2          4    12  12  13  13  14  14   <- Generate for the second `steps_per_generation` (prompts 12 to 23); store the completions; use the first slice to compute the loss
        #                      2          5    15  15  16  16  17  17   <- Take the stored generations and use the second slice to compute the loss
        #                                          ...
        if dataset is None:
            dataset = self.train_dataset
        return RepeatSampler(
            data_source=dataset,
            mini_repeat_count=self.num_generations,
            batch_size=self.args.generation_batch_size // self.num_generations,
            repeat_count=self.num_iterations * self.args.steps_per_generation,
            shuffle=self.shuffle_dataset,
            seed=self.args.seed,
        )

    def _get_eval_sampler(self, eval_dataset) -> Sampler:
        # See _get_train_sampler for an explanation of the sampler.
        return RepeatSampler(
            data_source=eval_dataset,
            mini_repeat_count=self.num_generations,
            seed=self.args.seed,
        )

    # ---------- Attention metrics processing ----------
    def _process_attention_metrics(self, attention_context: Optional[dict], mode: str) -> None:
        if not self.compute_attention_metrics or attention_context is None:
            return
        outputs = attention_context.get("outputs")
        generate_inputs = attention_context.get("inputs")
        if outputs is None or getattr(outputs, "attentions", None) is None:
            return
        if generate_inputs is None or "input_ids" not in generate_inputs:
            return
        input_ids = generate_inputs["input_ids"].detach().cpu()
        sequences = outputs.sequences.detach().cpu()
        image_grid_thw = generate_inputs.get("image_grid_thw")
        if isinstance(image_grid_thw, torch.Tensor):
            image_grid_thw_cpu = image_grid_thw.detach().cpu()
        else:
            image_grid_thw_cpu = None
        sample_results_tuple = compute_qwen_attention_metrics_for_batch(
            self.model,
            self.processing_class,
            outputs.attentions,
            input_ids,
            sequences,
            image_grid_thw=image_grid_thw_cpu,
        )
        if isinstance(sample_results_tuple, tuple):
            sample_results, skip_reasons = sample_results_tuple
        else:
            sample_results = sample_results_tuple
            skip_reasons = [None] * len(sample_results)
        outputs.attentions = None
        attention_context["outputs"] = None
        attention_context["inputs"] = None
        if not sample_results:
            return
        self._log_attention_metrics(sample_results, mode, skip_reasons)

    def _log_attention_metrics(
        self,
        sample_results: list[Optional[AttentionSampleResult]],
        mode: str,
        skip_reasons: Optional[list[Optional[str]]] = None,
    ) -> None:
        device = self.accelerator.device
        segments = ["early", "middle", "late", "all"]

        if skip_reasons is None:
            skip_reasons = [None] * len(sample_results)

        valid_results = [(idx, res) for idx, res in enumerate(sample_results) if res is not None]
        if not valid_results:
            if isinstance(self._logs.get("attention"), deque):
                self._logs["attention"].extend(sample_results)
            if isinstance(self._attention_skip_reasons, deque):
                self._attention_skip_reasons.extend(skip_reasons)
            return

        for segment in segments:
            mdi_vals = []
            aei_text_vals = []
            aei_vision_vals = []
            for _, result in valid_results:
                segment_result = result.segments.get(segment)
                if segment_result is None:
                    continue
                mdi_vals.append(segment_result.mdi)
                aei_text_vals.append(segment_result.aei_text)
                aei_vision_vals.append(segment_result.aei_vision)

            if mdi_vals:
                mdi_tensor = torch.tensor(mdi_vals, device=device, dtype=torch.float32)
                mdi_tensor = torch.where(torch.isfinite(mdi_tensor), mdi_tensor, torch.full_like(mdi_tensor, float("nan")))
                gathered_mdi = self.accelerator.gather(mdi_tensor)
                self._metrics[mode][f"attention/{segment}/mdi"].append(torch.nanmean(gathered_mdi).item())

            if aei_text_vals:
                aei_text_tensor = torch.tensor(aei_text_vals, device=device, dtype=torch.float32)
                aei_text_tensor = torch.where(
                    torch.isfinite(aei_text_tensor), aei_text_tensor, torch.full_like(aei_text_tensor, float("nan"))
                )
                gathered_aei_text = self.accelerator.gather(aei_text_tensor)
                self._metrics[mode][f"attention/{segment}/aei_text"].append(torch.nanmean(gathered_aei_text).item())

            if aei_vision_vals:
                aei_vision_tensor = torch.tensor(aei_vision_vals, device=device, dtype=torch.float32)
                aei_vision_tensor = torch.where(
                    torch.isfinite(aei_vision_tensor),
                    aei_vision_tensor,
                    torch.full_like(aei_vision_tensor, float("nan")),
                )
                gathered_aei_vision = self.accelerator.gather(aei_vision_tensor)
                self._metrics[mode][f"attention/{segment}/aei_vision"].append(
                    torch.nanmean(gathered_aei_vision).item()
                )

        # Maintain the per-batch sample results for local logging and reward integration
        if isinstance(self._logs.get("attention"), deque):
            self._logs["attention"].extend(sample_results)
        if isinstance(self._attention_skip_reasons, deque):
            self._attention_skip_reasons.extend(skip_reasons)

        # 为MDI reward准备原始attention参数
        try:
            attention_text_list = []
            attention_vision_list = []
            num_text_tokens_list = []
            num_vision_tokens_list = []
            
            for res in sample_results:
                if res is None:
                    # 提供默认值
                    attention_text_list.append(0.0)
                    attention_vision_list.append(0.0)
                    num_text_tokens_list.append(1)
                    num_vision_tokens_list.append(1)
                    continue
                
                # 获取late segment的attention值，如果没有则使用all segment
                seg = res.segments.get("late") or res.segments.get("all")
                if seg is None:
                    attention_text_list.append(0.0)
                    attention_vision_list.append(0.0)
                    num_text_tokens_list.append(1)
                    num_vision_tokens_list.append(1)
                    continue
                
                # 提取原始attention参数
                attention_text = float(seg.attention_text) if seg.attention_text is not None else 0.0
                attention_vision = float(seg.attention_vision) if seg.attention_vision is not None else 0.0
                num_text_tokens = int(res.num_instruction_tokens) if res.num_instruction_tokens is not None else 1
                num_vision_tokens = int(res.num_vision_tokens) if res.num_vision_tokens is not None else 1
                
                attention_text_list.append(attention_text)
                attention_vision_list.append(attention_vision)
                num_text_tokens_list.append(num_text_tokens)
                num_vision_tokens_list.append(num_vision_tokens)
            
            # 存储原始attention参数供reward函数使用
            self._attention_text_current_batch = attention_text_list
            self._attention_vision_current_batch = attention_vision_list
            self._num_text_tokens_current_batch = num_text_tokens_list
            self._num_vision_tokens_current_batch = num_vision_tokens_list
        except Exception:
            self._attention_text_current_batch = []
            self._attention_vision_current_batch = []
            self._num_text_tokens_current_batch = []
            self._num_vision_tokens_current_batch = []

    @profiling_decorator
    def _get_last_hidden_state(
        self,
        unwrapped_model,
        input_ids,
        attention_mask,
        logits_to_keep,
        pixel_values=None,
        image_grid_thw=None,
        pixel_attention_mask=None,
        image_sizes=None,
    ):
        if is_peft_model(unwrapped_model):
            unwrapped_model = unwrapped_model.base_model.model

        # Build model inputs - check if the model supports logits_to_keep (some models and VLMs don't)
        model_inputs = {"input_ids": input_ids, "attention_mask": attention_mask}

        # For Qwen models:
        if image_grid_thw is not None and pixel_values is not None:
            model_inputs["image_grid_thw"] = image_grid_thw
        # For Gemma, SmolVLM2, LLaVa-Next etc.:
        if pixel_values is not None:
            model_inputs["pixel_values"] = pixel_values
        # For SmolVLM2
        if pixel_attention_mask is not None:
            model_inputs["pixel_attention_mask"] = pixel_attention_mask
        # For LLaVa-Next
        if image_sizes is not None:
            model_inputs["image_sizes"] = image_sizes

        # Only add logits_to_keep if the model supports it
        if "logits_to_keep" in self.model_kwarg_keys:
            # We add 1 to `logits_to_keep` because the last logits of the sequence is later excluded
            model_inputs["logits_to_keep"] = logits_to_keep + 1

        model_inputs["use_cache"] = False  # only used in generation; set False to suppress warnings

        last_hidden_state = unwrapped_model.model(**model_inputs).last_hidden_state
        # Exclude the last value: it corresponds to the next token pred
        last_hidden_state = last_hidden_state[:, :-1, :]  # (B, L-1, H)
        # Only keep the last logits_to_keep. For model that support logits_to_keep, this is a no-op.
        last_hidden_state = last_hidden_state[:, -logits_to_keep:, :]  # (B, logits_to_keep, H)
        return last_hidden_state

    def get_high_entropy_mask(self, entropies: torch.Tensor, mask: torch.Tensor, threshold: float) -> torch.Tensor:
        """
        Returns a binary mask identifying tokens whose entropy exceeds a given quantile threshold.

        Args:
            entropies (`torch.Tensor`):
                Tensor of shape (batch_size, seq_len) with per-token entropy values.
            mask (`torch.Tensor`):
                Binary mask of the same shape as `entropies`, where `1` indicates valid tokens and `0` padding.
            threshold (`float`):
                Quantile threshold between `0.0` and `1.0` to select high-entropy tokens.

        Returns:
            `torch.Tensor`:
                Boolean mask of shape (batch_size, seq_len), where `True` indicates tokens with entropy >= threshold
                and `False` otherwise.
        """
        local = entropies[mask.bool()].float()

        # Use a negative pad_value as a sentinel because entropy values are always >= 0.
        # This guarantees that the sentinel cannot collide with any real entropy value.
        pad_value = -1e9

        # Pad across processes so that every rank has the same tensor length
        padded = self.accelerator.pad_across_processes(local, dim=0, pad_index=pad_value)
        gathered = self.accelerator.gather(padded)

        # Drop sentinel values (safe because no entropy can be negative)
        gathered = gathered[gathered != pad_value]

        if gathered.numel() == 0:
            return torch.zeros_like(entropies, dtype=torch.bool)

        entropy_threshold = torch.quantile(gathered, threshold)
        masked_entropies = entropies * mask.float()
        entropy_mask = masked_entropies >= entropy_threshold
        return entropy_mask & mask.bool()  # ensure padding tokens are always masked out

    @profiling_decorator
    def _get_per_token_logps_and_entropies(
        self,
        model,
        input_ids,
        attention_mask,
        logits_to_keep,
        batch_size=None,
        compute_entropy=False,
        pixel_values=None,
        image_grid_thw=None,
        num_images=None,
        pixel_attention_mask=None,
        image_sizes=None,
        token_type_ids=None,
    ) -> dict[str, Optional[torch.Tensor]]:
        """Compute log-probs and (optionally) entropies for each token."""
        batch_size = batch_size or input_ids.size(0)  # Chunk inputs into smaller batches to reduce memory peak
        all_logps = []
        all_entropies = []
        for start in range(0, input_ids.size(0), batch_size):
            input_ids_batch = input_ids[start : start + batch_size]
            attention_mask_batch = attention_mask[start : start + batch_size]

            # Build model inputs - check if the model supports logits_to_keep (some models and VLMs don't)
            model_inputs = {"input_ids": input_ids_batch, "attention_mask": attention_mask_batch}
            if image_grid_thw is not None and pixel_values is not None:
                rows_per_image = image_grid_thw.prod(dim=-1)
                rows_per_sample = torch.split(rows_per_image, num_images)
                rows_per_sample = torch.stack([s.sum() for s in rows_per_sample])
                cum_rows = torch.cat([torch.tensor([0], device=rows_per_sample.device), rows_per_sample.cumsum(0)])
                row_start, row_end = cum_rows[start].item(), cum_rows[start + batch_size].item()
                model_inputs["pixel_values"] = pixel_values[row_start:row_end]
                cum_imgs = torch.tensor([0] + num_images).cumsum(0)
                img_start, img_end = cum_imgs[start], cum_imgs[start + batch_size]
                model_inputs["image_grid_thw"] = image_grid_thw[img_start:img_end]
            elif pixel_values is not None:
                model_inputs["pixel_values"] = pixel_values[start : start + batch_size]
            if pixel_attention_mask is not None:
                model_inputs["pixel_attention_mask"] = pixel_attention_mask[start : start + batch_size]
            if image_sizes is not None:
                model_inputs["image_sizes"] = image_sizes[start : start + batch_size]
            if token_type_ids is not None:
                model_inputs["token_type_ids"] = token_type_ids[start : start + batch_size]

            # Only add logits_to_keep if the model supports it
            if "logits_to_keep" in self.model_kwarg_keys:
                # We add 1 to `logits_to_keep` because the last logits of the sequence is later excluded
                model_inputs["logits_to_keep"] = logits_to_keep + 1

            model_inputs["use_cache"] = False  # only used in generation; set False to suppress warnings

            logits = model(**model_inputs).logits
            # Exclude the last value: it corresponds to the next token pred
            logits = logits[:, :-1, :]  # (B, L-1, H)
            # Only keep the last logits_to_keep. For model that support logits_to_keep, this is a no-op.
            logits = logits[:, -logits_to_keep:, :]  # (B, logits_to_keep, H)
            # Divide logits by sampling temperature.
            # See https://huggingface.co/blog/the_n_implementation_details_of_rlhf_with_ppo#policy-training-implementation-details
            logits = logits / self.temperature

            completion_ids = input_ids_batch[:, -logits_to_keep:]
            logps = selective_log_softmax(logits, completion_ids)  # compute logprobs
            all_logps.append(logps)

            if compute_entropy:
                with torch.no_grad():
                    entropies = entropy_from_logits(logits)
                all_entropies.append(entropies)

        logps = torch.cat(all_logps, dim=0)
        entropies = torch.cat(all_entropies, dim=0) if compute_entropy else None
        return logps, entropies

    def _fix_param_name_to_vllm(self, name, extra_prefixes: Optional[list[str]] = None):
        extra_prefixes = extra_prefixes or []
        prefixes = ["_checkpoint_wrapped_module."] + extra_prefixes
        for prefix in prefixes:
            name = name.replace(prefix, "")
        return name

    def _sync_fsdp1_params_to_vllm(self, module: nn.Module, prefix: str = "", visited=None):
        """Memory-efficient post-order traversal of FSDP modules to extract full parameters and sync with vLLM."""
        # For FSDP1, we need to recurse into children and also use summon_full_params
        if visited is None:
            visited = set()
        for child_name, child_module in module.named_children():
            child_prefix = f"{prefix}.{child_name}" if prefix else child_name
            self._sync_fsdp1_params_to_vllm(
                child_module, prefix=child_prefix, visited=visited
            )  # recurse into the child

        if isinstance(module, FSDP):
            with FSDP.summon_full_params(module, recurse=False, writeback=False):
                for param_name, param in module.named_parameters():
                    full_name = f"{prefix}.{param_name}" if prefix else param_name
                    full_name = self._fix_param_name_to_vllm(full_name, extra_prefixes=["_fsdp_wrapped_module."])

                    if full_name in visited:
                        continue  # skip FSDP subtrees already traversed
                    visited.add(full_name)

                    if self.vllm_mode == "server" and self.accelerator.is_main_process:
                        self.vllm_client.update_named_param(full_name, param.data)
                    elif self.vllm_mode == "colocate":
                        llm_model = self.llm.llm_engine.model_executor.driver_worker.model_runner.model
                        llm_model.load_weights([(full_name, param.data)])

    def _sync_fsdp2_params_to_vllm(self, module: nn.Module):
        # For FSDP2, module.state_dict() already covers all parameters, so no need for recursion
        for name, param in module.state_dict().items():
            if param.is_cpu:
                param = param.to(torch.device("cuda"))
            param = param.full_tensor()

            if self.vllm_mode == "server" and self.accelerator.is_main_process:
                self.vllm_client.update_named_param(name, param)
            elif self.vllm_mode == "colocate":
                llm_model = self.llm.llm_engine.model_executor.driver_worker.model_runner.model
                llm_model.load_weights([(name, param)])

    @profiling_decorator
    def _move_model_to_vllm(self):
        # For DeepSpeed ZeRO-3 and FSDP, we need to gather all parameters before operations
        deepspeed_plugin = self.accelerator.state.deepspeed_plugin
        zero_stage_3 = deepspeed_plugin is not None and deepspeed_plugin.zero_stage == 3
        if zero_stage_3:
            import deepspeed

            gather_if_zero3 = deepspeed.zero.GatheredParameters
        else:
            gather_if_zero3 = nullcontext

        if is_peft_model(self.model):
            # With PEFT and FSDP/DeepSpeed ZeRO Stage 3, we must gather the full model at once before merging, as
            # merging adapters in a sharded manner is not supported.
            # TODO: does this work with FSDP?
            with gather_if_zero3(list(self.model.parameters())):
                self.model.merge_adapter()

                # Update vLLM weights while parameters are gathered
                if self.is_fsdp_enabled:  # note if using FSDP, gather_if_zero3 is nullcontext
                    # Update vLLM weights while parameters are gathered
                    # For PEFT with FSDP we need to use the memory efficient post-order traversal
                    fsdp_plugin = getattr(self.accelerator.state, "fsdp_plugin", None)
                    fsdp_version = getattr(fsdp_plugin, "fsdp_version", 1) if fsdp_plugin else 1
                    if fsdp_version == 1:
                        self._sync_fsdp1_params_to_vllm(
                            self.model
                        )  # use memory-efficient post-order traversal for FSDP
                    elif fsdp_version == 2:
                        self._sync_fsdp2_params_to_vllm(self.model)
                else:
                    # DeepSpeed ZeRO-3 with PEFT
                    for name, param in self.model.named_parameters():
                        # When using PEFT, we need to recover the original parameter name and discard some parameters
                        name = name.removeprefix("base_model.model.").replace(".base_layer", "")
                        if self.model.prefix in name:
                            continue
                        # When module to save, remove its prefix and discard the original module
                        if "original_module" in name:
                            continue
                        name = self._fix_param_name_to_vllm(name, extra_prefixes=["modules_to_save.default."])

                        if self.vllm_mode == "server" and self.accelerator.is_main_process:
                            self.vllm_client.update_named_param(name, param.data)
                        elif self.vllm_mode == "colocate":
                            llm_model = self.llm.llm_engine.model_executor.driver_worker.model_runner.model
                            llm_model.load_weights([(name, param.data)])
                # Unmerge adapters while parameters are still gathered
                self.model.unmerge_adapter()
                # Parameters will automatically be repartitioned when exiting the context
        else:
            # For non-PEFT models, simply gather (if needed) and update each parameter individually.
            if self.is_fsdp_enabled:
                fsdp_plugin = getattr(self.accelerator.state, "fsdp_plugin", None)
                fsdp_version = getattr(fsdp_plugin, "fsdp_version", 1) if fsdp_plugin else 1
                if fsdp_version == 1:
                    self._sync_fsdp1_params_to_vllm(self.model)  # use memory-efficient post-order traversal for FSDP
                elif fsdp_version == 2:
                    self._sync_fsdp2_params_to_vllm(self.model)
            else:
                for name, param in self.model.named_parameters():
                    name = self._fix_param_name_to_vllm(name)
                    with gather_if_zero3([param]):
                        if self.vllm_mode == "server" and self.accelerator.is_main_process:
                            self.vllm_client.update_named_param(name, param.data)
                        elif self.vllm_mode == "colocate":
                            llm_model = self.llm.llm_engine.model_executor.driver_worker.model_runner.model
                            llm_model.load_weights([(name, param.data)])

        # Reset cache on vLLM
        if self.vllm_mode == "server" and self.accelerator.is_main_process:
            self.vllm_client.reset_prefix_cache()
        elif self.vllm_mode == "colocate":
            self.llm.reset_prefix_cache()

    @profiling_decorator
    def _prepare_inputs(
        self, generation_batch: dict[str, Union[torch.Tensor, Any]]
    ) -> dict[str, Union[torch.Tensor, Any]]:
        # Prepares inputs for model training/evaluation by managing completion generation and batch handling.
        # During training:
        #   - Receives the local generation batch (Per-GPU batch size × steps per generation)
        #     from the modified training dataloader instead of the standard local batch
        #   - Generates completions once for the entire generation batch and splits it into batches of size
        #     `per_device_train_batch_size`
        #   - Buffers these completions and returns the appropriate slice for the current accumulation step
        #   - Optimizes by regenerating completions only periodically (every steps_per_generation * num_iterations)
        # During evaluation:
        #   - The input is treated as a standard local batch (no accumulation, no multiple iterations)
        #   - Completions are generated for each batch without buffering or reuse
        # Returns a single local batch in both cases.

        mode = "train" if self.model.training else "eval"
        if mode == "train":
            generate_every = self.args.steps_per_generation * self.num_iterations
            if self._step % generate_every == 0 or self._buffered_inputs is None:
                # self._buffered_inputs=None can occur when resuming from a checkpoint
                generation_batch = self._generate_and_score_completions(generation_batch)
                generation_batch = split_pixel_values_by_grid(generation_batch)
                generation_batch = shuffle_sequence_dict(generation_batch)
                generation_batches = split_tensor_dict(generation_batch, self.args.steps_per_generation)
                self._buffered_inputs = [unsplit_pixel_values_by_grid(batch) for batch in generation_batches]
            inputs = self._buffered_inputs[self._step % self.args.steps_per_generation]
            self._step += 1
        else:
            # In evaluation, there is neither batch grouping for generation, nor multiple iterations, hence
            # local generation batch == local eval batch
            inputs = self._generate_and_score_completions(generation_batch)
        return inputs

    @profiling_decorator
    def _calculate_rewards(self, inputs, prompts, completions, completion_ids_list):
        device = self.accelerator.device
        rewards_per_func = torch.zeros(len(prompts), len(self.reward_funcs), device=device)

        # Repeat all input columns (but "prompt", "completion", and "completion_ids") to match the num of generations
        keys = [key for key in inputs[0] if key not in ["prompt", "completion", "completion_ids"]]
        reward_kwargs = {key: [example[key] for example in inputs] for key in keys}

        # This allows for dynamic reward shaping based on training progress.
        reward_kwargs["trainer_state"] = self.state

        for i, (reward_func, reward_processing_class, reward_func_name) in enumerate(
            zip(self.reward_funcs, self.reward_processing_classes, self.reward_func_names)
        ):
            with profiling_context(self, reward_func_name):
                if isinstance(reward_func, nn.Module):  # Module (no PretrainedModel) for compat with compiled models
                    if is_conversational(inputs[0]):
                        messages = [{"messages": p + c} for p, c in zip(prompts, completions)]
                        texts = [apply_chat_template(x, reward_processing_class)["text"] for x in messages]
                    else:
                        texts = [p + c for p, c in zip(prompts, completions)]
                    reward_inputs = reward_processing_class(
                        text=texts, return_tensors="pt", padding=True, padding_side="right", add_special_tokens=False
                    )
                    reward_inputs = super()._prepare_inputs(reward_inputs)
                    with torch.inference_mode():
                        rewards_per_func[:, i] = reward_func(**reward_inputs).logits[:, 0]  # Shape (B*G,)
                else:
                    output_reward_func = reward_func(
                        prompts=prompts, completions=completions, completion_ids=completion_ids_list, **reward_kwargs
                    )
                    # Convert None values to NaN
                    output_reward_func = [reward if reward is not None else torch.nan for reward in output_reward_func]

                    rewards_per_func[:, i] = torch.tensor(output_reward_func, dtype=torch.float32, device=device)

        # If all reward functions return None for a given row, issue a detailed warning
        if torch.isnan(rewards_per_func).all(dim=1).any():
            nan_row_idx = torch.isnan(rewards_per_func).all(dim=1).nonzero(as_tuple=True)[0][0]
            row_reward_kwargs = {
                key: value[nan_row_idx] for key, value in reward_kwargs.items() if key != "trainer_state"
            }
            row_reward_kwargs["prompt"] = prompts[nan_row_idx]
            row_reward_kwargs["completion"] = completions[nan_row_idx]
            logger.warning(
                f"All reward functions returned None for the following kwargs:\n{row_reward_kwargs}\n"
                "Please ensure that at least one reward function returns a valid reward."
            )

        # Gather the reward per function: this part is crucial, because the rewards are normalized per group and the
        # completions may be distributed across processes
        rewards_per_func = gather(rewards_per_func)
        return rewards_per_func

    def _generate_single_turn(self, prompts: list[str], images: Optional[list]):
        device = self.accelerator.device

        # If the prompts are conversational and the inputs contain images, we need to convert the prompts from
        # [{"role": "user", "content": "What color is the sky?"}] to
        # [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": "What color is the sky?"}]}]
        kwargs = {}
        if images is not None:
            kwargs = {"images": images}
            for prompt, image_list in zip(prompts, images):
                if isinstance(prompt, list):  # i.e., when using conversational data
                    prepare_multimodal_messages(prompt, num_images=len(image_list))

        prompts_text = [
            maybe_apply_chat_template({"prompt": prompt}, self.processing_class)["prompt"]
            for prompt in prompts
        ]

        # Generate completions using either vLLM or regular generation
        if self.use_vllm:
            if self.vllm_mode == "colocate" and self.args.vllm_enable_sleep_mode:
                # wake up colocated vLLM instances if needed
                torch.cuda.empty_cache()  # required to avoid OOM in some cases
                self.llm.wake_up()

            # First, update the vLLM weights if needed
            if self.state.global_step != self._last_loaded_step:
                self._move_model_to_vllm()
                self._last_loaded_step = self.state.global_step

            # Generate completions using vLLM: gather all prompts and use them in a single call in the main process
            if self.vllm_mode == "server":
                all_prompts_text = gather_object(prompts_text)
                if images is not None:
                    all_images = gather_object(images)

                if self.accelerator.is_main_process:
                    # Since 'prompts' contains 'num_generations' duplicates, we first take unique prompts, and generate
                    # num_generations outputs for each one. This is faster than generating outputs for each duplicate
                    # prompt individually.
                    ordered_set_of_prompts = all_prompts_text[:: self.num_generations]

                    if images is not None:
                        ordered_set_of_images = all_images[:: self.num_generations]
                    else:
                        ordered_set_of_images = None

                    with profiling_context(self, "vLLM.generate"):
                        output = self.vllm_client.generate(
                            prompts=ordered_set_of_prompts,
                            images=ordered_set_of_images,
                            n=self.num_generations,
                            repetition_penalty=self.repetition_penalty,
                            temperature=self.temperature,
                            top_p=self.top_p,
                            top_k=-1 if self.top_k is None else self.top_k,
                            min_p=0.0 if self.min_p is None else self.min_p,
                            max_tokens=self.max_completion_length,
                            truncate_prompt_tokens=self.max_prompt_length,
                            guided_decoding_regex=self.guided_decoding_regex,
                            generation_kwargs=self.args.generation_kwargs,
                        )
                        payload = (output["prompt_ids"], output["completion_ids"], output["logprobs"])
                else:
                    payload = None

                # Broadcast the completions from the main process to all processes, ensuring each process receives its corresponding slice.
                obj_list = [payload]
                broadcast_object_list(obj_list, from_process=0)
                all_prompt_ids, all_completion_ids, all_logprobs = obj_list[0]

                # At this point, we only get 1 copy of each prompt, so we need to repeat them num_generations times
                all_prompt_ids = [ids for ids in all_prompt_ids for _ in range(self.num_generations)]

                process_slice = slice(
                    self.accelerator.process_index * len(prompts),
                    (self.accelerator.process_index + 1) * len(prompts),
                )
                prompt_ids = all_prompt_ids[process_slice]
                completion_ids = all_completion_ids[process_slice]
                logprobs = all_logprobs[process_slice]

            # Generate completions using colocated vLLM instances: each device holds vLLM copy and work on their own batch of prompts
            elif self.vllm_mode == "colocate":
                if self.guided_decoding_regex:
                    guided_decoding = GuidedDecodingParams(regex=self.guided_decoding_regex)
                else:
                    guided_decoding = None

                generation_kwargs = {
                    "n": 1,  # vLLM on each GPU generates only 1 in colocate mode
                    "repetition_penalty": self.repetition_penalty,
                    "temperature": self.temperature,
                    "top_p": self.top_p,
                    "top_k": -1 if self.top_k is None else self.top_k,
                    "min_p": 0.0 if self.min_p is None else self.min_p,
                    "max_tokens": self.max_completion_length,
                    "truncate_prompt_tokens": self.max_prompt_length,
                    "guided_decoding": guided_decoding,
                    "logprobs": 0,  # only return the logprob of the generated token
                }
                if self.args.generation_kwargs is not None:
                    generation_kwargs.update(self.args.generation_kwargs)
                sampling_params = SamplingParams(**generation_kwargs)

                if self.vllm_tensor_parallel_size > 1:
                    # Gather prompts from all ranks in the TP group and flatten.
                    # Each rank starts with its own prompts; after gathering, all ranks see the full group set.
                    orig_size = len(prompts_text)
                    gathered_prompts = [None for _ in range(self.vllm_tensor_parallel_size)]
                    torch.distributed.all_gather_object(gathered_prompts, prompts_text, group=self.tp_group)
                    all_prompts_text = [p for sublist in gathered_prompts for p in sublist]

                    if images is not None:
                        gathered_images = [None for _ in range(self.vllm_tensor_parallel_size)]
                        torch.distributed.all_gather_object(gathered_images, images, group=self.tp_group)
                        all_images = [img for sublist in gathered_images for img in sublist]
                    else:
                        all_images = None
                else:
                    all_prompts_text = prompts_text
                    all_images = images

                if images is not None and all_images:
                    vllm_inputs = []
                    for prompt, image_list in zip(all_prompts_text, all_images):
                        vllm_inputs.append({"prompt": prompt, "multi_modal_data": {"image": image_list}})

                else:
                    vllm_inputs = all_prompts_text

                with profiling_context(self, "vLLM.generate"):
                    all_outputs = self.llm.generate(vllm_inputs, sampling_params=sampling_params, use_tqdm=False)

                all_prompt_ids = [output.prompt_token_ids for output in all_outputs]
                all_completion_ids = [output.token_ids for outputs in all_outputs for output in outputs.outputs]
                all_logprobs = [
                    [next(iter(lp.values())).logprob for lp in output.logprobs]
                    for outputs in all_outputs
                    for output in outputs.outputs
                ]

                if self.vllm_tensor_parallel_size > 1:
                    # Slice completions for this rank within its TP group.
                    # Each rank generates all outputs — we keep only our share.
                    local_rank_in_group = torch.distributed.get_rank(group=self.tp_group)
                    tp_slice = slice(local_rank_in_group * orig_size, (local_rank_in_group + 1) * orig_size)
                    prompt_ids = all_prompt_ids[tp_slice]
                    completion_ids = all_completion_ids[tp_slice]
                    logprobs = all_logprobs[tp_slice]
                else:
                    prompt_ids = all_prompt_ids
                    completion_ids = all_completion_ids
                    logprobs = all_logprobs

                if self.args.vllm_enable_sleep_mode:
                    self.llm.sleep(level=1)

        elif self.use_transformers_paged:
            # Re-process inputs for paged generation if needed
            # Note: images are already validated and preprocessed above
            paged_prompt_inputs = self.processing_class(text=prompts_text, **kwargs)
            base_model = self._unwrap_model_for_config()
            previous_attn = getattr(base_model.config, "_attn_implementation", None)

            if is_flash_attn_2_available():
                base_model.config._attn_implementation = "paged_attention"
            else:
                base_model.config._attn_implementation = "sdpa_paged"
            with (
                profiling_context(self, "transformers.generate_batch"),
                unwrap_model_for_generation(
                    self.model_wrapped, self.accelerator, gather_deepspeed3_params=self.args.ds3_gather_for_generation
                ) as unwrapped_model,
                torch.no_grad(),
                FSDP.summon_full_params(self.model_wrapped, recurse=False) if self.is_fsdp_enabled else nullcontext(),
            ):
                # Cast to the appropriate dtype based on training configuration
                if self.args.bf16:
                    unwrapped_model.to(torch.bfloat16)
                elif self.args.fp16:
                    unwrapped_model.to(torch.float16)
                with torch.inference_mode():
                    all_outputs = unwrapped_model.generate_batch(
                        paged_prompt_inputs.input_ids, generation_config=self.generation_config, progress_bar=False
                    )
                    unwrapped_model.train()  # restore training mode, as generate_batch forces eval mode
            completion_ids = [output.generated_tokens for output in all_outputs.values()]
            prompt_ids = paged_prompt_inputs.input_ids
            # Restore the original attention implementation, training mode
            if previous_attn is not None:
                base_model.config._attn_implementation = previous_attn
            else:
                try:
                    delattr(base_model.config, "_attn_implementation")
                except Exception:
                    pass
            logprobs = None  # not used in this case

        else:
            # Regular generation path
            generate_inputs = self.processing_class(
                text=prompts_text,
                return_tensors="pt",
                padding=True,
                padding_side="left",
                max_length=self.max_prompt_length,
                truncation=True,
                add_special_tokens=False,
                **kwargs,
            )
            generate_inputs = super()._prepare_inputs(generate_inputs)

            with (
                profiling_context(self, "transformers.generate"),
                unwrap_model_for_generation(
                    self.model_wrapped, self.accelerator, gather_deepspeed3_params=self.args.ds3_gather_for_generation
                ) as unwrapped_model,
                torch.no_grad(),
                FSDP.summon_full_params(self.model_wrapped, recurse=False) if self.is_fsdp_enabled else nullcontext(),
            ):
                if self.compute_attention_metrics:
                    # Force eager attention implementation during attention capture
                    with self._temporary_attn_impl("eager"):
                        attention_outputs = unwrapped_model.generate(
                            **generate_inputs,
                            generation_config=self.generation_config,
                            disable_compile=True,
                            return_dict_in_generate=True,
                            output_attentions=True,
                        )
                    prompt_completion_ids = attention_outputs.sequences
                else:
                    prompt_completion_ids = unwrapped_model.generate(
                        **generate_inputs, generation_config=self.generation_config, disable_compile=True
                    )
            # Compute prompt length and extract completion ids
            prompt_ids, prompt_mask = generate_inputs["input_ids"], generate_inputs["attention_mask"]
            prompt_length = prompt_ids.size(1)
            completion_ids = prompt_completion_ids[:, prompt_length:]

            # Mask everything after the first EOS token
            is_eos = completion_ids == self.eos_token_id
            eos_idx = torch.full((is_eos.size(0),), is_eos.size(1), dtype=torch.long, device=device)
            eos_idx[is_eos.any(dim=1)] = is_eos.int().argmax(dim=1)[is_eos.any(dim=1)]
            sequence_indices = torch.arange(is_eos.size(1), device=device).expand(is_eos.size(0), -1)
            completion_mask = (sequence_indices <= eos_idx.unsqueeze(1)).int()
            prompt_ids = [p[m].tolist() for p, m in zip(prompt_ids, prompt_mask.bool())]
            completion_ids = [c[m].tolist() for c, m in zip(completion_ids, completion_mask.bool())]
            logprobs = None  # not used in this case

        attention_context = None
        if self.compute_attention_metrics and 'attention_outputs' in locals():
            attention_context = {"outputs": attention_outputs, "inputs": generate_inputs}
        return prompt_ids, completion_ids, logprobs, attention_context

    def _generate(self, prompts: list[str], images: Optional[list]):
        device = self.accelerator.device
        mode = "train" if self.model.training else "eval"

        prompt_ids, completion_ids, logprobs, attention_context = self._generate_single_turn(prompts, images)

        # Get completion length per sequence, used for logging
        prompt_lengths = torch.tensor([len(ids) for ids in prompt_ids], device=device)
        completion_lengths = torch.tensor([len(ids) for ids in completion_ids], device=device)
        agg_prompt_lengths = self.accelerator.gather(prompt_lengths)
        agg_completion_lengths = self.accelerator.gather(completion_lengths)
        total_prompt_tokens = agg_prompt_lengths.sum()
        total_completion_tokens = agg_completion_lengths.sum()  # = num_items_in_batch, required for the DAPO loss

        # Log the metrics
        if mode == "train":
            self.state.num_input_tokens_seen += (total_prompt_tokens + total_completion_tokens).item()
        self._metrics[mode]["num_tokens"] = [self.state.num_input_tokens_seen]

        # Log completion lengths, mean, min, max
        self._metrics[mode]["completions/mean_length"].append(agg_completion_lengths.float().mean().item())
        self._metrics[mode]["completions/min_length"].append(agg_completion_lengths.float().min().item())
        self._metrics[mode]["completions/max_length"].append(agg_completion_lengths.float().max().item())

        # Identify sequences that terminated with EOS and log their lengths
        eos_and_pad = [self.eos_token_id, self.pad_token_id]
        is_truncated = torch.tensor([ids[-1] not in eos_and_pad for ids in completion_ids], device=device)
        agg_is_truncated = self.accelerator.gather(is_truncated)
        self._metrics[mode]["completions/clipped_ratio"].append(agg_is_truncated.float().mean().item())
        term_completion_lengths = agg_completion_lengths[~agg_is_truncated]
        if len(term_completion_lengths) == 0:  # edge case where no terminated sequences are found
            term_completion_lengths = torch.zeros(1, device=device)
        self._metrics[mode]["completions/mean_terminated_length"].append(term_completion_lengths.float().mean().item())
        self._metrics[mode]["completions/min_terminated_length"].append(term_completion_lengths.float().min().item())
        self._metrics[mode]["completions/max_terminated_length"].append(term_completion_lengths.float().max().item())

        # Process attentions into metrics if enabled
        try:
            if self.compute_attention_metrics:
                self._process_attention_metrics(attention_context, mode)
        except Exception:
            pass
        return prompt_ids, completion_ids, total_completion_tokens, logprobs

    # ---------- Rollout logging helpers ----------
    def _truncate_text(self, s: str, n: int) -> str:
        s = s or ""
        return (s[:n] + "…") if len(s) > n else s

    def _compute_real_mdi_metrics(
        self,
        sample_results: list,
        skip_reasons: Optional[list[Optional[str]]] = None,
    ) -> list[dict]:
        results = []
        if skip_reasons is None:
            skip_reasons = [None] * len(sample_results)

        for idx, res in enumerate(sample_results):
            if res is None:
                reason = skip_reasons[idx] if idx < len(skip_reasons) else None
                default_result = {
                    "mdi": 1.0,
                    "text_ratio": 0.5,
                    "vision_ratio": 0.5,
                    "attention_distribution": [0.5, 0.5],
                    "num_vision_tokens": 0,
                    "num_text_tokens": 0,
                    "early_mdi": 1.0,
                    "middle_mdi": 1.0,
                    "late_mdi": 1.0,
                    "early_aei_text": 0.0,
                    "early_aei_vision": 0.0,
                    "middle_aei_text": 0.0,
                    "middle_aei_vision": 0.0,
                    "late_aei_text": 0.0,
                    "late_aei_vision": 0.0,
                    "aei_text": 0.0,
                    "aei_vision": 0.0,
                    "early_text_ratio": 0.5,
                    "early_vision_ratio": 0.5,
                    "middle_text_ratio": 0.5,
                    "middle_vision_ratio": 0.5,
                    "late_text_ratio": 0.5,
                    "late_vision_ratio": 0.5,
                    "skip_reason": reason,
                }
                results.append(default_result)
                continue

            segments = getattr(res, "segments", {}) if res is not None else {}
            # Align with attention_metrics.AttentionSampleResult fields:
            # text tokens are stored as `num_instruction_tokens` in the result.
            num_vision_tokens = getattr(res, "num_vision_tokens", 0)
            num_text_tokens = getattr(res, "num_instruction_tokens", getattr(res, "num_text_tokens", 0))

            def process_segment(segment_name):
                segment = segments.get(segment_name)
                if segment is None or not hasattr(segment, "mdi") or segment.mdi is None:
                    return {
                        "mdi": 1.0,
                        "aei_text": 0.0,
                        "aei_vision": 0.0,
                        "text_ratio": 0.5,
                        "vision_ratio": 0.5,
                    }

                mdi = float(segment.mdi)
                if not (mdi > 0) or not math.isfinite(mdi):
                    return {
                        "mdi": 1.0,
                        "aei_text": 0.0,
                        "aei_vision": 0.0,
                        "text_ratio": 0.5,
                        "vision_ratio": 0.5,
                    }

                aei_text = float(getattr(segment, "aei_text", 0.0))
                aei_vision = float(getattr(segment, "aei_vision", 0.0))
                text_ratio = mdi / (1.0 + mdi)
                vision_ratio = 1.0 / (1.0 + mdi)

                return {
                    "mdi": round(float(mdi), 6),
                    "aei_text": round(float(aei_text), 6),
                    "aei_vision": round(float(aei_vision), 6),
                    "text_ratio": round(float(text_ratio), 6),
                    "vision_ratio": round(float(vision_ratio), 6),
                }

            early_data = process_segment("early")
            middle_data = process_segment("middle")
            late_data = process_segment("late")
            all_data = process_segment("all")

            main_segment = late_data if late_data["mdi"] != 1.0 else all_data
            mdi = main_segment["mdi"]

            text_ratio = mdi / (1.0 + mdi)
            vision_ratio = 1.0 / (1.0 + mdi)

            result = {
                "mdi": round(float(mdi), 6),
                "text_ratio": round(float(text_ratio), 6),
                "vision_ratio": round(float(vision_ratio), 6),
                "attention_distribution": [round(float(text_ratio), 6), round(float(vision_ratio), 6)],
                "num_vision_tokens": int(num_vision_tokens),
                "num_text_tokens": int(num_text_tokens),
                "early_mdi": early_data["mdi"],
                "middle_mdi": middle_data["mdi"],
                "late_mdi": late_data["mdi"],
                "early_aei_text": early_data["aei_text"],
                "early_aei_vision": early_data["aei_vision"],
                "middle_aei_text": middle_data["aei_text"],
                "middle_aei_vision": middle_data["aei_vision"],
                "late_aei_text": late_data["aei_text"],
                "late_aei_vision": late_data["aei_vision"],
                "aei_text": all_data["aei_text"],
                "aei_vision": all_data["aei_vision"],
                "early_text_ratio": early_data["text_ratio"],
                "early_vision_ratio": early_data["vision_ratio"],
                "middle_text_ratio": middle_data["text_ratio"],
                "middle_vision_ratio": middle_data["vision_ratio"],
                "late_text_ratio": late_data["text_ratio"],
                "late_vision_ratio": late_data["vision_ratio"],
                "skip_reason": None,
            }
            results.append(result)

        return results

    def _emit_rollout_logs(
        self,
        prompts_text: list[str],
        completions_text: list[str],
        solutions: list[Optional[str]],
        rewards_per_func_local: torch.Tensor,
        total_rewards_local: torch.Tensor,
        reward_names: list[str],
        mdi_info: list[dict],
    ) -> None:
        if not (self.accelerator.is_main_process and getattr(self.args, "realtime_rollout_logging", False)):
            return
        # Build header and progress
        self._rollout_step_count += 1
        try:
            max_steps = getattr(self.state, "max_steps", None)
        except Exception:
            max_steps = None
        header = f"=== Rollout Step {self._rollout_step_count} ===\nStep: {self.state.global_step}/{max_steps if max_steps is not None else '?'}"

        # Prepare per-sample summary rows
        rows = []
        name_to_idx = {n: i for i, n in enumerate(reward_names)}
        for idx, (p, c, sol) in enumerate(zip(prompts_text, completions_text, solutions)):
            preview_p = self._truncate_text(p, self.args.prompt_preview_chars)
            preview_c = self._truncate_text(c, self.args.completion_preview_chars)
            # prefer named accuracy_reward; fallback to mc_idx_reward if present
            acc_idx = name_to_idx.get("accuracy_reward")
            if acc_idx is None:
                acc_idx = name_to_idx.get("mc_idx_reward")
            acc = float(rewards_per_func_local[idx, acc_idx].item()) if rewards_per_func_local.numel() and acc_idx is not None else 0.0
            fmt = float(rewards_per_func_local[idx, name_to_idx.get("think_format_reward", 0)].item()) if rewards_per_func_local.numel() and "think_format_reward" in name_to_idx else 0.0
            mdi_val = float(rewards_per_func_local[idx, name_to_idx.get("mdi_reward", 0)].item()) if rewards_per_func_local.numel() and ("mdi_reward" in name_to_idx) else 0.0
            tot = float(total_rewards_local[idx].item()) if total_rewards_local.numel() else 0.0
            rows.append((idx + 1, preview_p, preview_c, sol or "", acc, fmt, mdi_val, tot))

        # Console pretty print
        if 'Console' in globals() and Console is not None and hasattr(self, "_console") and self._console is not None:
            self._console.print(f"\n[bold cyan]{header}[/bold cyan]")
            table = Table(box=box.MINIMAL, show_lines=False)
            table.add_column("#", style="dim")
            table.add_column("Prompt")
            table.add_column("Completion")
            table.add_column("Solution", style="italic")
            table.add_column("acc", style="green")
            table.add_column("format", style="magenta")
            table.add_column("mdi", style="yellow")
            table.add_column("total", style="bold")
            for r in rows:
                table.add_row(str(r[0]), r[1], r[2], r[3], f"{r[4]:.3f}", f"{r[5]:.3f}", f"{r[6]:.3f}", f"{r[7]:.3f}")
            self._console.print(table)

            # MDI section
            self._console.print("\n[bold]MDI Attention Info:[/bold]")
            for i, info in enumerate(mdi_info, start=1):
                self._console.print(
                    json.dumps(
                        {
                            "sample": i,
                            "MDI Value": info.get("mdi"),
                            "Text-Vision Ratio": f"{info.get('text_ratio')}:{info.get('vision_ratio')}",
                            "Attention Distribution": info.get("attention_distribution"),
                        },
                        ensure_ascii=False,
                    )
                )
        else:
            # 不再在终端打印rollout信息，只记录到文件
            pass

        # Append to files with better error handling and formatting
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            if getattr(self.args, "rollout_log_path", None):
                # 确保目录存在
                os.makedirs(os.path.dirname(self.args.rollout_log_path), exist_ok=True)
                with open(self.args.rollout_log_path, "a", encoding="utf-8") as f:
                    f.write(f"\n## {header} | {ts}\n\n")
                    
                    # 添加总体统计信息
                    if rows:
                        f.write("### Overall Statistics\n\n")
                        f.write("| Metric | Value |\n")
                        f.write("|--------|-------|\n")
                        
                        # 计算各种统计信息
                        accuracy_scores = [r[4] for r in rows]
                        format_scores = [r[5] for r in rows]
                        mdi_scores = [r[6] for r in rows]
                        total_scores = [r[7] for r in rows]
                        
                        f.write(f"| Accuracy Mean | {np.mean(accuracy_scores):.3f} ± {np.std(accuracy_scores):.3f} |\n")
                        f.write(f"| Format Mean | {np.mean(format_scores):.3f} ± {np.std(format_scores):.3f} |\n")
                        f.write(f"| MDI Mean | {np.mean(mdi_scores):.3f} ± {np.std(mdi_scores):.3f} |\n")
                        f.write(f"| Total Reward Mean | {np.mean(total_scores):.3f} ± {np.std(total_scores):.3f} |\n")
                        f.write(f"| Accuracy Rate | {np.mean([1 if s > 0 else 0 for s in accuracy_scores]):.3f} |\n")
                        f.write(f"| Format Rate | {np.mean([1 if s > 0 else 0 for s in format_scores]):.3f} |\n")
                        f.write(f"| Success Rate | {np.mean([1 if s > 0 else 0 for s in total_scores]):.3f} |\n\n")
                        
                        # 添加MDI统计信息
                        if mdi_info:
                            f.write("### MDI Statistics\n\n")
                            f.write("| Stage | MDI Mean | MDI Std | AEI Text | AEI Vision |\n")
                            f.write("|-------|----------|---------|----------|------------|\n")
                            
                            early_mdi = [info.get("early_mdi", 0) for info in mdi_info if info.get("early_mdi") is not None]
                            middle_mdi = [info.get("middle_mdi", 0) for info in mdi_info if info.get("middle_mdi") is not None]
                            late_mdi = [info.get("late_mdi", 0) for info in mdi_info if info.get("late_mdi") is not None]
                            all_mdi = [info.get("mdi", 0) for info in mdi_info if info.get("mdi") is not None]
                            
                            early_aei_text = [info.get("early_aei_text", 0) for info in mdi_info]
                            early_aei_vision = [info.get("early_aei_vision", 0) for info in mdi_info]
                            middle_aei_text = [info.get("middle_aei_text", 0) for info in mdi_info]
                            middle_aei_vision = [info.get("middle_aei_vision", 0) for info in mdi_info]
                            late_aei_text = [info.get("late_aei_text", 0) for info in mdi_info]
                            late_aei_vision = [info.get("late_aei_vision", 0) for info in mdi_info]
                            all_aei_text = [info.get("aei_text", 0) for info in mdi_info]
                            all_aei_vision = [info.get("aei_vision", 0) for info in mdi_info]
                            
                            f.write(f"| Early | {np.mean(early_mdi):.3f} | {np.std(early_mdi):.3f} | {np.mean(early_aei_text):.3f} | {np.mean(early_aei_vision):.3f} |\n")
                            f.write(f"| Middle | {np.mean(middle_mdi):.3f} | {np.std(middle_mdi):.3f} | {np.mean(middle_aei_text):.3f} | {np.mean(middle_aei_vision):.3f} |\n")
                            f.write(f"| Late | {np.mean(late_mdi):.3f} | {np.std(late_mdi):.3f} | {np.mean(late_aei_text):.3f} | {np.mean(late_aei_vision):.3f} |\n")
                            f.write(f"| All | {np.mean(all_mdi):.3f} | {np.std(all_mdi):.3f} | {np.mean(all_aei_text):.3f} | {np.mean(all_aei_vision):.3f} |\n\n")
                    
                    # 详细的样本信息
                    for i, (r, info) in enumerate(zip(rows, mdi_info), start=1):
                        f.write(f"### Sample {i}\n\n")
                        f.write(f"**Prompt:** {r[1]}\n\n")
                        f.write(f"**Completion:** {r[2]}\n\n")
                        f.write(f"**Solution:** {r[3]}\n\n")
                        f.write(f"**Rewards:** accuracy={r[4]:.3f}, format={r[5]:.3f}, mdi={r[6]:.3f}, total={r[7]:.3f}\n\n")
                        
                        # 添加详细的metrics信息
                        if info:
                            f.write("**Detailed Metrics:**\n\n")
                            f.write("```json\n")
                            detailed_metrics = {
                                "rewards": {
                                    "accuracy": float(r[4]),
                                    "format": float(r[5]),
                                    "mdi": float(r[6]),
                                    "total": float(r[7])
                                },
                                "attention_metrics": {
                                    "early": {
                                        "mdi": info.get("early_mdi"),
                                        "aei_text": info.get("early_aei_text"),
                                        "aei_vision": info.get("early_aei_vision"),
                                        "text_ratio": info.get("early_text_ratio"),
                                        "vision_ratio": info.get("early_vision_ratio")
                                    },
                                    "middle": {
                                        "mdi": info.get("middle_mdi"),
                                        "aei_text": info.get("middle_aei_text"),
                                        "aei_vision": info.get("middle_aei_vision"),
                                        "text_ratio": info.get("middle_text_ratio"),
                                        "vision_ratio": info.get("middle_vision_ratio")
                                    },
                                    "late": {
                                        "mdi": info.get("late_mdi"),
                                        "aei_text": info.get("late_aei_text"),
                                        "aei_vision": info.get("late_aei_vision"),
                                        "text_ratio": info.get("late_text_ratio"),
                                        "vision_ratio": info.get("late_vision_ratio")
                                    },
                                    "all": {
                                        "mdi": info.get("mdi"),
                                        "aei_text": info.get("aei_text"),
                                        "aei_vision": info.get("aei_vision"),
                                        "text_ratio": info.get("text_ratio"),
                                        "vision_ratio": info.get("vision_ratio")
                                    }
                                },
                                "token_counts": {
                                    "vision_tokens": float(info.get("num_vision_tokens", 0) or 0),
                                    "text_tokens": float(info.get("num_text_tokens", 0) or 0),
                                    "total_tokens": float((info.get("num_vision_tokens", 0) or 0) + (info.get("num_text_tokens", 0) or 0)),
                                },
                                "overall": {
                                    "attention_distribution": info.get("attention_distribution"),
                                    "skip_reason": info.get("skip_reason"),
                                },
                            }
                            f.write(json.dumps(detailed_metrics, ensure_ascii=False, indent=2))
                            f.write("\n```\n\n")
                        
                        f.write("---\n\n")
            if getattr(self.args, "attention_diag_log_path", None):
                # 确保目录存在
                os.makedirs(os.path.dirname(self.args.attention_diag_log_path), exist_ok=True)
                with open(self.args.attention_diag_log_path, "a", encoding="utf-8") as f:
                    f.write(f"\n## {header} | {ts}\n\n")
                    f.write("### Enhanced MDI Attention Diagnostics\n\n")
                    
                    # 添加总体统计信息
                    if mdi_info:
                        f.write("#### Overall Statistics\n\n")
                        f.write("| Metric | Early | Middle | Late | All |\n")
                        f.write("|--------|-------|--------|------|-----|\n")
                        
                        # 计算各阶段的统计信息
                        early_mdi = [info.get("early_mdi", 0) for info in mdi_info if info.get("early_mdi") is not None]
                        middle_mdi = [info.get("middle_mdi", 0) for info in mdi_info if info.get("middle_mdi") is not None]
                        late_mdi = [info.get("late_mdi", 0) for info in mdi_info if info.get("late_mdi") is not None]
                        all_mdi = [info.get("mdi", 0) for info in mdi_info if info.get("mdi") is not None]
                        
                        f.write(f"| MDI Mean | {np.mean(early_mdi):.3f} | {np.mean(middle_mdi):.3f} | {np.mean(late_mdi):.3f} | {np.mean(all_mdi):.3f} |\n")
                        f.write(f"| MDI Std | {np.std(early_mdi):.3f} | {np.std(middle_mdi):.3f} | {np.std(late_mdi):.3f} | {np.std(all_mdi):.3f} |\n")
                        
                        # Vision/Text Token统计
                        vision_tokens = [info.get("num_vision_tokens", 0) for info in mdi_info]
                        text_tokens = [info.get("num_text_tokens", 0) for info in mdi_info]
                        total_tokens = [v + t for v, t in zip(vision_tokens, text_tokens)]
                        
                        f.write(f"| Vision Tokens | {np.mean(vision_tokens):.1f} ± {np.std(vision_tokens):.1f} |\n")
                        f.write(f"| Text Tokens | {np.mean(text_tokens):.1f} ± {np.std(text_tokens):.1f} |\n")
                        f.write(f"| Total Tokens | {np.mean(total_tokens):.1f} ± {np.std(total_tokens):.1f} |\n")
                        # Ratios are computed against total tokens per sample
                        f.write(
                            f"| Vision Ratio | {np.mean([v/tt if tt > 0 else 0 for v, tt in zip(vision_tokens, total_tokens)]):.3f} |\n"
                        )
                        f.write(
                            f"| Text Ratio | {np.mean([(tt - v)/tt if tt > 0 else 0 for v, tt in zip(vision_tokens, total_tokens)]):.3f} |\n\n"
                        )
                    
                    # 详细的样本信息
                    for i, info in enumerate(mdi_info, start=1):
                        f.write(f"#### Sample {i}\n\n")
                        f.write(f"```json\n")
                        
                        # 构建完整的诊断信息
                        sample_data = {
                            "sample": i,
                            "token_counts": {
                                "vision_tokens": float(info.get("num_vision_tokens", 0) or 0),
                                "text_tokens": float(info.get("num_text_tokens", 0) or 0),
                                "total_tokens": float((info.get("num_vision_tokens", 0) or 0) + (info.get("num_text_tokens", 0) or 0)),
                            },
                            "attention_metrics": {
                                "early": {
                                    "mdi": info.get("early_mdi"),
                                    "aei_text": info.get("early_aei_text"),
                                    "aei_vision": info.get("early_aei_vision"),
                                    "text_ratio": info.get("early_text_ratio"),
                                    "vision_ratio": info.get("early_vision_ratio")
                                },
                                "middle": {
                                    "mdi": info.get("middle_mdi"),
                                    "aei_text": info.get("middle_aei_text"),
                                    "aei_vision": info.get("middle_aei_vision"),
                                    "text_ratio": info.get("middle_text_ratio"),
                                    "vision_ratio": info.get("middle_vision_ratio")
                                },
                                "late": {
                                    "mdi": info.get("late_mdi"),
                                    "aei_text": info.get("late_aei_text"),
                                    "aei_vision": info.get("late_aei_vision"),
                                    "text_ratio": info.get("late_text_ratio"),
                                    "vision_ratio": info.get("late_vision_ratio")
                                },
                                "all": {
                                    "mdi": info.get("mdi"),
                                    "aei_text": info.get("aei_text"),
                                    "aei_vision": info.get("aei_vision"),
                                    "text_ratio": info.get("text_ratio"),
                                    "vision_ratio": info.get("vision_ratio")
                                }
                            },
                            "overall": {
                                "attention_distribution": info.get("attention_distribution"),
                                "text_vision_ratio": f"{info.get('text_ratio', 0):.6f}:{info.get('vision_ratio', 0):.6f}",
                                "skip_reason": info.get("skip_reason"),
                            },
                        }
                        
                        f.write(
                            json.dumps(
                                sample_data,
                                ensure_ascii=False,
                                indent=2
                            )
                        )
                        f.write(f"\n```\n\n")
        except Exception as e:
            # 添加调试信息
            print(f"⚠️  Warning: Failed to write to log files: {e}")
            import traceback
            traceback.print_exc()

    def _generate_and_score_completions(
        self, inputs: list[dict[str, Union[torch.Tensor, Any]]]
    ) -> dict[str, Union[torch.Tensor, Any]]:
        device = self.accelerator.device
        mode = "train" if self.model.training else "eval"

        prompts = [x["prompt"] for x in inputs]

        if "images" in inputs[0]:
            images = [example.get("images") for example in inputs]
        elif "image" in inputs[0]:
            images = [[example.get("image")] if example.get("image") is not None else None for example in inputs]
        else:
            images = None
        # Transformers requires at least one image in the batch, otherwise it throws an error
        if images is not None and all(img_list == [] for img_list in images):
            images = None

        prompt_ids_list, completion_ids_list, num_items_in_batch, sampling_per_token_logps_list = self._generate(
            prompts, images
        )

        # Convert lists of token IDs to padded tensors
        prompt_ids = [torch.tensor(ids, device=device) for ids in prompt_ids_list]
        prompt_mask = [torch.ones_like(ids, dtype=torch.long) for ids in prompt_ids]
        prompt_ids = pad(prompt_ids, padding_value=self.pad_token_id, padding_side="left")
        prompt_mask = pad(prompt_mask, padding_value=0, padding_side="left")
        completion_ids = [torch.tensor(ids, device=device) for ids in completion_ids_list]
        completion_mask = [torch.ones_like(ids, dtype=torch.long) for ids in completion_ids]
        completion_ids = pad(completion_ids, padding_value=self.pad_token_id, padding_side="right")
        completion_mask = pad(completion_mask, padding_value=0, padding_side="right")
        if sampling_per_token_logps_list is not None:
            sampling_per_token_logps = [torch.tensor(logps, device=device) for logps in sampling_per_token_logps_list]
            sampling_per_token_logps = pad(sampling_per_token_logps, padding_value=0.0, padding_side="right")
        else:
            sampling_per_token_logps = None

        # If mask_truncated_completions is enabled, zero out truncated completions in completion_mask
        if self.mask_truncated_completions:
            eos_and_pad = [self.eos_token_id, self.pad_token_id]
            is_truncated = torch.tensor([ids[-1] not in eos_and_pad for ids in completion_ids_list], device=device)
            completion_mask = completion_mask * (~is_truncated).unsqueeze(1).int()

        # Concatenate prompt_mask with completion_mask for logit computation
        prompt_completion_ids = torch.cat([prompt_ids, completion_ids], dim=1)  # (B, P+C)
        attention_mask = torch.cat([prompt_mask, completion_mask], dim=1)  # (B, P+C)

        logits_to_keep = completion_ids.size(1)  # we only need to compute the logits for the completion tokens
        batch_size = self.args.per_device_train_batch_size if mode == "train" else self.args.per_device_eval_batch_size

        num_images = [len(img_list) for img_list in images] if images is not None else None

        # Get forward_kwargs for models with multimodal inputs
        if images is not None:
            prompts_text = [
                apply_chat_template({"prompt": prompt}, self.processing_class)["prompt"] for prompt in prompts
            ]
            prompt_inputs = self.processing_class(images=images, text=prompts_text, padding=True, return_tensors="pt")
            prompt_inputs = super()._prepare_inputs(prompt_inputs)
            forward_kwargs = {k: v for k, v in prompt_inputs.items() if k not in ["input_ids", "attention_mask"]}
        else:
            forward_kwargs = {}

        # If token_type_ids are used, extend them with zeros for the completion part
        if "token_type_ids" in forward_kwargs:
            token_type_ids = forward_kwargs["token_type_ids"]
            forward_kwargs["token_type_ids"] = torch.cat(
                [token_type_ids, token_type_ids.new_zeros(completion_ids.shape)], dim=1
            )

        with torch.no_grad():
            # If the generation and optimization steps are misaligned—i.e., if generation does not occur at the end of
            # a full optimizer step (when gradient_accumulation_steps is not a multiple of generate_every)—then the
            # samples may come from an earlier version of the model. In that case, we need to track old_per_token_logps
            # for importance sampling. If the steps are aligned, importance sampling isn't necessary and we set
            # old_per_token_logps to None.
            # When using vLLM, we always compute old_per_token_logps for importance sampling, it was shown that the
            # distribution mismatch between vLLM and the training model can be large and harm the training.
            generate_every = self.args.steps_per_generation * self.num_iterations  # generation frequency
            if self.args.gradient_accumulation_steps % generate_every != 0 or (
                self.use_vllm and self.vllm_importance_sampling_correction
            ):
                old_per_token_logps, _ = self._get_per_token_logps_and_entropies(
                    self.model,
                    prompt_completion_ids,
                    attention_mask,
                    logits_to_keep,
                    batch_size,
                    num_images=num_images,
                    **forward_kwargs,  # may contain pixel_values, image_grid_thw, pixel_attention_mask and image_sizes
                )
            else:
                old_per_token_logps = None

            # Compute the importance sampling ratio when using vLLM, to correct for potential distribution mismatch
            if self.use_vllm and self.vllm_importance_sampling_correction:
                importance_sampling_ratio = torch.exp(old_per_token_logps - sampling_per_token_logps)
                importance_sampling_ratio = torch.clamp(
                    importance_sampling_ratio, max=self.vllm_importance_sampling_cap
                )

            # Compute the per-token log probabilities for the reference model
            if self.beta != 0.0:
                if self.ref_model is not None:
                    ref_per_token_logps, _ = self._get_per_token_logps_and_entropies(
                        self.ref_model,
                        prompt_completion_ids,
                        attention_mask,
                        logits_to_keep,
                        batch_size=batch_size,
                        num_images=num_images,
                        **forward_kwargs,  # may contain pixel_values, image_grid_thw, pixel_attention_mask and image_sizes
                    )
                else:
                    with self.accelerator.unwrap_model(self.model).disable_adapter():
                        ref_per_token_logps, _ = self._get_per_token_logps_and_entropies(
                            self.model,
                            prompt_completion_ids,
                            attention_mask,
                            logits_to_keep,
                            batch_size=batch_size,
                            num_images=num_images,
                            **forward_kwargs,  # may contain pixel_values, image_grid_thw, pixel_attention_mask and image_sizes
                        )
            else:
                ref_per_token_logps = None

        # Decode
        prompts_text = self.processing_class.batch_decode(prompt_ids, skip_special_tokens=True)
        completions_text = self.processing_class.batch_decode(completion_ids, skip_special_tokens=True)
        if is_conversational(inputs[0]):
            completions = []
            for prompt, completion in zip(prompts, completions_text):
                bootstrap = prompt.pop()["content"] if prompt[-1]["role"] == "assistant" else ""
                completions.append([{"role": "assistant", "content": bootstrap + completion}])
        else:
            completions = completions_text

        # Calculate rewards for each reward function. rewards_per_func aggregates rewards across all processes. This is
        # important because rewards will be normalized per group, and completions are distributed. We will later slice
        # rewards_per_func to extract each process's subset.
        rewards_per_func = self._calculate_rewards(inputs, prompts, completions, completion_ids_list)

        # Apply weights to each reward function's output and sum
        rewards = (rewards_per_func * self.reward_weights.to(device).unsqueeze(0)).nansum(dim=1)

        # Compute grouped-wise rewards
        mean_grouped_rewards = rewards.view(-1, self.num_generations).mean(dim=1)

        # Normalize the rewards to compute the advantages
        mean_grouped_rewards = mean_grouped_rewards.repeat_interleave(self.num_generations, dim=0)
        advantages = rewards - mean_grouped_rewards

        if self.scale_rewards in ["group", "none"]:
            # If self.scale_rewards = "none", we'll still log group level std
            std_rewards = rewards.view(-1, self.num_generations).std(dim=1)
            std_rewards = std_rewards.repeat_interleave(self.num_generations, dim=0)
        elif self.scale_rewards == "batch":
            # Compute global std
            std_rewards = rewards.std().expand_as(rewards)
        else:
            raise ValueError(
                f"Invalid value for scale_rewards: {self.scale_rewards}. Must be one of 'batch', 'group', or 'none'."
            )

        is_std_zero = torch.isclose(std_rewards, torch.zeros_like(std_rewards))
        if self.scale_rewards != "none":
            advantages = advantages / (std_rewards + 1e-4)

        # Slice to keep only the local part of the data
        process_slice = slice(
            self.accelerator.process_index * len(prompts),
            (self.accelerator.process_index + 1) * len(prompts),
        )
        all_process_advantages = advantages.clone()  # keep the aggregated advantages for logging
        advantages = advantages[process_slice]

        # Calculate mean reward per function, but only for samples where the function was applied (non-NaN values)
        for i, reward_func_name in enumerate(self.reward_func_names):
            mean_rewards = torch.nanmean(rewards_per_func[:, i]).item()
            std_func_rewards = nanstd(rewards_per_func[:, i]).item()
            
            # 检查数值是否异常
            if torch.isnan(torch.tensor(mean_rewards)) or torch.isinf(torch.tensor(mean_rewards)):
                print(f"⚠️  Warning: {reward_func_name} mean reward is NaN/Inf: {mean_rewards}")
            if torch.isnan(torch.tensor(std_func_rewards)) or torch.isinf(torch.tensor(std_func_rewards)):
                print(f"⚠️  Warning: {reward_func_name} std reward is NaN/Inf: {std_func_rewards}")
            
            self._metrics[mode][f"rewards/{reward_func_name}/mean"].append(mean_rewards)
            self._metrics[mode][f"rewards/{reward_func_name}/std"].append(std_func_rewards)
        
        # 检查总奖励是否异常
        total_reward_mean = mean_grouped_rewards.mean().item()
        total_reward_std = std_rewards.mean().item()
        
        if torch.isnan(torch.tensor(total_reward_mean)) or torch.isinf(torch.tensor(total_reward_mean)):
            print(f"⚠️  Warning: Total reward mean is NaN/Inf: {total_reward_mean}")
        if torch.isnan(torch.tensor(total_reward_std)) or torch.isinf(torch.tensor(total_reward_std)):
            print(f"⚠️  Warning: Total reward std is NaN/Inf: {total_reward_std}")
            
        self._metrics[mode]["reward"].append(total_reward_mean)
        self._metrics[mode]["reward_std"].append(total_reward_std)
        self._metrics[mode]["frac_reward_zero_std"].append(is_std_zero.float().mean().item())

        # Log prompt and completion texts
        self._logs["prompt"].extend(gather_object(prompts_text))
        self._logs["completion"].extend(gather_object(completions_text))
        for i, name in enumerate(self.reward_func_names):
            self._logs["rewards"][name].extend(rewards_per_func[:, i].tolist())
        self._logs["advantages"].extend(all_process_advantages.tolist())

        if images is not None:
            self._logs["images"].extend(gather_object(images))

        if self.use_vllm and self.vllm_importance_sampling_correction:
            delta = torch.abs(old_per_token_logps - sampling_per_token_logps)
            delta = delta[completion_mask.bool()]
            mean_delta = torch.mean(delta) if delta.numel() > 0 else torch.tensor(0.0, device=device)
            max_delta = torch.max(delta) if delta.numel() > 0 else torch.tensor(0.0, device=device)
            self._metrics[mode]["sampling/sampling_logp_difference/mean"].append(
                self.accelerator.gather(mean_delta).mean().item()
            )
            self._metrics[mode]["sampling/sampling_logp_difference/max"].append(
                self.accelerator.gather(max_delta).max().item()
            )

            flat_is_ratio = importance_sampling_ratio[completion_mask.bool()]
            min_importance_sampling_ratio = (
                torch.min(flat_is_ratio) if flat_is_ratio.numel() > 0 else torch.tensor(0.0, device=device)
            )
            mean_importance_sampling_ratio = (
                torch.mean(flat_is_ratio) if flat_is_ratio.numel() > 0 else torch.tensor(0.0, device=device)
            )
            max_importance_sampling_ratio = (
                torch.max(flat_is_ratio) if flat_is_ratio.numel() > 0 else torch.tensor(0.0, device=device)
            )
            self._metrics[mode]["sampling/importance_sampling_ratio/min"].append(
                nanmin(self.accelerator.gather(min_importance_sampling_ratio)).item()
            )
            self._metrics[mode]["sampling/importance_sampling_ratio/mean"].append(
                self.accelerator.gather(mean_importance_sampling_ratio).nanmean().item()
            )
            self._metrics[mode]["sampling/importance_sampling_ratio/max"].append(
                nanmax(self.accelerator.gather(max_importance_sampling_ratio)).item()
            )

        # Realtime rollout logging - 移出大的try-except块确保执行
        if self.accelerator.is_main_process and getattr(self.args, "realtime_rollout_logging", False):
            try:
                local_rewards_per_func = rewards_per_func[process_slice]
                local_total_rewards = rewards[process_slice]
                solutions = []
                for ex in inputs:
                    # prefer label_idx -> letter if available
                    if "label_idx" in ex and ex["label_idx"] is not None:
                        try:
                            li = int(ex["label_idx"]) if not isinstance(ex["label_idx"], (list, tuple)) else int(ex["label_idx"][0])
                            if 0 <= li <= 25:
                                sol = chr(ord('A') + li)
                            else:
                                sol = str(li)
                        except Exception:
                            sol = ""
                    else:
                        sol = ex.get("solution") or ex.get("answer") or ex.get("label")
                        if isinstance(sol, (list, tuple)) and len(sol) > 0:
                            sol = sol[0]
                    solutions.append(str(sol) if sol is not None else "")
                if (
                    self.compute_attention_metrics
                    and isinstance(self._logs.get("attention"), deque)
                ):
                    att_list = list(self._logs["attention"])  # recent items
                    sample_results = att_list[-len(prompts_text):] if len(att_list) >= len(prompts_text) else att_list
                    if isinstance(self._attention_skip_reasons, deque):
                        skip_list = list(self._attention_skip_reasons)
                        skip_slice = (
                            skip_list[-len(prompts_text):]
                            if len(skip_list) >= len(prompts_text)
                            else skip_list
                        )
                    else:
                        skip_slice = []
                    if len(skip_slice) < len(sample_results):
                        skip_slice = list(skip_slice) + [None] * (len(sample_results) - len(skip_slice))
                    mdi_info = self._compute_real_mdi_metrics(sample_results, skip_slice)
                else:
                    mdi_info = [{} for _ in inputs]
                
                # 调用rollout日志记录
                self._emit_rollout_logs(
                    prompts_text=prompts_text,
                    completions_text=completions_text,
                    solutions=solutions,
                    rewards_per_func_local=local_rewards_per_func.detach().cpu(),
                    total_rewards_local=local_total_rewards.detach().cpu(),
                    reward_names=self.reward_func_names,
                    mdi_info=mdi_info,
                )
                pass  # Successfully logged rollout results
            except Exception as e:
                # Failed to emit rollout logs - continue training
                pass

        output = {
            "prompt_ids": prompt_ids,
            "prompt_mask": prompt_mask,
            "completion_ids": completion_ids,
            "completion_mask": completion_mask,
            "advantages": advantages,
            "num_items_in_batch": num_items_in_batch,
        }
        if old_per_token_logps is not None:
            output["old_per_token_logps"] = old_per_token_logps
        if self.use_vllm and self.vllm_importance_sampling_correction:
            output["importance_sampling_ratio"] = importance_sampling_ratio
        if ref_per_token_logps is not None:
            output["ref_per_token_logps"] = ref_per_token_logps
        if "pixel_values" in forward_kwargs:
            output["pixel_values"] = forward_kwargs["pixel_values"]
        if "image_grid_thw" in forward_kwargs:
            output["image_grid_thw"] = forward_kwargs["image_grid_thw"]
        if "pixel_attention_mask" in forward_kwargs:
            output["pixel_attention_mask"] = forward_kwargs["pixel_attention_mask"]
        if "image_sizes" in forward_kwargs:
            output["image_sizes"] = forward_kwargs["image_sizes"]
        if "token_type_ids" in forward_kwargs:
            output["token_type_ids"] = forward_kwargs["token_type_ids"]
        if images is not None:
            output["num_images"] = num_images
        return output

    def compute_liger_loss(self, unwrapped_model, inputs):
        # Compute the per-token log probabilities for the model
        prompt_ids, prompt_mask = inputs["prompt_ids"], inputs["prompt_mask"]
        completion_ids, completion_mask = inputs["completion_ids"], inputs["completion_mask"]
        input_ids = torch.cat([prompt_ids, completion_ids], dim=1)
        attention_mask = torch.cat([prompt_mask, completion_mask], dim=1)
        logits_to_keep = completion_ids.size(1)  # we only need to compute the logits for the completion tokens

        # Get the last hidden state of the model
        last_hidden_state = self._get_last_hidden_state(
            unwrapped_model,
            input_ids,
            attention_mask,
            logits_to_keep,
            inputs.get("pixel_values"),
            inputs.get("image_grid_thw"),
            inputs.get("pixel_attention_mask"),
            inputs.get("image_sizes"),
        )

        # compute loss and metrics using liger grpo loss
        loss, metrics = self.liger_grpo_loss(
            _input=last_hidden_state,
            lin_weight=unwrapped_model.lm_head.weight,
            selected_token_ids=completion_ids,
            attention_mask=completion_mask,
            advantages=inputs["advantages"],
            bias=unwrapped_model.lm_head.bias,
            old_per_token_logps=inputs.get("old_per_token_logps"),
            ref_per_token_logps=inputs.get("ref_per_token_logps"),
        )
        # Extract metrics from the liger_grpo_loss output
        # KL divergence is the first metric when beta is non-zero
        mean_kl = metrics[0] if self.beta != 0.0 else None
        clip_ratio = metrics[-1]

        mode = "train" if self.model.training else "eval"
        if self.beta != 0.0:
            self._metrics[mode]["kl"].append(self.accelerator.gather(mean_kl).mean().item())
        self._metrics[mode]["clip_ratio"].append(self.accelerator.gather(clip_ratio).mean().item())
        return loss / self.current_gradient_accumulation_steps

    @profiling_decorator
    def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
        if return_outputs:
            raise ValueError("The GRPOTrainer does not support returning outputs")
        if self.use_liger_loss:
            # Compute the loss using the liger grpo loss
            unwrapped_model = self.accelerator.unwrap_model(model)
            return self._forward_redirection(model, unwrapped_model, self.compute_liger_loss, unwrapped_model, inputs)
        else:
            return self._compute_loss(model, inputs)

    def _compute_loss(self, model, inputs):
        # Compute the per-token log probabilities for the model
        prompt_ids, prompt_mask = inputs["prompt_ids"], inputs["prompt_mask"]
        completion_ids, completion_mask = inputs["completion_ids"], inputs["completion_mask"]
        input_ids = torch.cat([prompt_ids, completion_ids], dim=1)
        attention_mask = torch.cat([prompt_mask, completion_mask], dim=1)
        logits_to_keep = completion_ids.size(1)  # we only need to compute the logits for the completion tokens

        # Compute the per_token_logps and the entropy at each position in the completion
        per_token_logps, entropies = self._get_per_token_logps_and_entropies(
            model,
            input_ids,
            attention_mask,
            logits_to_keep,
            compute_entropy=True,
            pixel_values=inputs.get("pixel_values"),
            image_grid_thw=inputs.get("image_grid_thw"),
            num_images=inputs.get("num_images"),
            pixel_attention_mask=inputs.get("pixel_attention_mask"),
            image_sizes=inputs.get("image_sizes"),
            token_type_ids=inputs.get("token_type_ids"),
        )

        if self.top_entropy_quantile < 1.0:
            entropy_mask = self.get_high_entropy_mask(entropies, completion_mask, 1 - self.top_entropy_quantile)
        else:
            entropy_mask = None

        # Compute the KL divergence between the model and the reference model
        if self.beta != 0.0:
            ref_per_token_logps = inputs["ref_per_token_logps"]
            per_token_kl = (
                torch.exp(ref_per_token_logps - per_token_logps) - (ref_per_token_logps - per_token_logps) - 1
            )

        # Compute the loss
        advantages = inputs["advantages"]
        # When num_iterations == 1 and steps_per_generation <= gradient_accumulation_steps,
        # old_per_token_logps == per_token_logps. In this case we can skip its computation
        # (see _generate_and_score_completions) and instead use per_token_logps.detach().
        # The exception is when using vLLM, where we always compute old_per_token_logps
        # for importance sampling
        old_per_token_logps = inputs.get("old_per_token_logps")
        old_per_token_logps = per_token_logps.detach() if old_per_token_logps is None else old_per_token_logps

        log_ratio = per_token_logps - old_per_token_logps
        if self.importance_sampling_level == "token":
            log_importance_weights = log_ratio
        elif self.importance_sampling_level == "sequence":
            log_importance_weights = (log_ratio * completion_mask).sum(-1) / completion_mask.sum(-1).clamp(min=1.0)
            log_importance_weights = log_importance_weights.unsqueeze(-1)
        else:
            raise ValueError(
                f"Unknown importance sampling level: {self.importance_sampling_level}. Possible values are 'token' "
                "and 'sequence'."
            )
        # From here, log_importance_weights (and all subsequent tensors, coef_1, coef_2, etc.) shape depends on
        # importance_sampling_level: "token" level: (B, T); "sequence" level: (B, 1)

        coef_1 = torch.exp(log_importance_weights)
        coef_2 = torch.clamp(coef_1, 1 - self.epsilon_low, 1 + self.epsilon_high)

        # Two-sided clipping
        if self.args.delta is not None:
            coef_1 = torch.clamp(coef_1, max=self.args.delta)

        per_token_loss1 = coef_1 * advantages.unsqueeze(1)
        per_token_loss2 = coef_2 * advantages.unsqueeze(1)
        per_token_loss = -torch.min(per_token_loss1, per_token_loss2)
        if entropy_mask is not None:
            per_token_loss = per_token_loss * entropy_mask

        if self.use_vllm and self.vllm_importance_sampling_correction:
            per_token_loss = per_token_loss * inputs["importance_sampling_ratio"]

        if self.beta != 0.0:
            per_token_loss = per_token_loss + self.beta * per_token_kl

        if self.loss_type == "grpo":
            loss = ((per_token_loss * completion_mask).sum(-1) / completion_mask.sum(-1).clamp(min=1.0)).mean()
            loss = loss / self.current_gradient_accumulation_steps
        elif self.loss_type == "bnpo":
            loss = (per_token_loss * completion_mask).sum() / completion_mask.sum().clamp(min=1.0)
            loss = loss / self.current_gradient_accumulation_steps
        elif self.loss_type == "dr_grpo":
            loss = (per_token_loss * completion_mask).sum() / (per_token_loss.size(0) * self.max_completion_length)
            loss = loss / self.current_gradient_accumulation_steps
        elif self.loss_type == "dapo":
            normalizer = inputs["num_items_in_batch"] / self.accelerator.num_processes
            loss = (per_token_loss * completion_mask).sum() / normalizer
        else:
            raise ValueError(f"Unknown loss type: {self.loss_type}")

        # Log the metrics
        mode = "train" if self.model.training else "eval"

        completion_token_count = completion_mask.sum().clamp(min=1.0)

        def masked_batch_mean(x):
            if x.shape[1] == 1:  # when importance_sampling_level == "sequence"
                return x.mean()
            else:
                return (x * completion_mask).sum() / completion_token_count

        if self.beta != 0.0:
            mean_kl = masked_batch_mean(per_token_kl)
            self._metrics[mode]["kl"].append(self.accelerator.gather(mean_kl).nanmean().item())

        mean_entropy = masked_batch_mean(entropies)
        self._metrics[mode]["entropy"].append(self.accelerator.gather(mean_entropy).nanmean().item())

        # Compute the clipped probability ratios
        is_low_clipped = (coef_1 < 1 - self.epsilon_low) & (advantages.unsqueeze(1) < 0)
        is_high_clipped = (coef_1 > 1 + self.epsilon_high) & (advantages.unsqueeze(1) > 0)
        is_region_clipped = is_low_clipped | is_high_clipped

        low_clip = masked_batch_mean(is_low_clipped.float())
        high_clip = masked_batch_mean(is_high_clipped.float())
        clip_ratio = masked_batch_mean(is_region_clipped.float())

        gathered_low_clip = self.accelerator.gather(low_clip)
        self._metrics[mode]["clip_ratio/low_mean"].append(gathered_low_clip.nanmean().item())
        self._metrics[mode]["clip_ratio/low_min"].append(nanmin(gathered_low_clip).item())
        gathered_high_clip = self.accelerator.gather(high_clip)
        self._metrics[mode]["clip_ratio/high_mean"].append(gathered_high_clip.nanmean().item())
        self._metrics[mode]["clip_ratio/high_max"].append(nanmax(gathered_high_clip).item())
        gathered_clip_ratio = self.accelerator.gather(clip_ratio)
        self._metrics[mode]["clip_ratio/region_mean"].append(gathered_clip_ratio.nanmean().item())
        return loss

    def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys: Optional[list[str]] = None):
        inputs = self._prepare_inputs(inputs)
        with torch.no_grad():
            with self.compute_loss_context_manager():
                loss = self.compute_loss(model, inputs)
            loss = loss.mean().detach()
        return loss, None, None

    def log(self, logs: dict[str, float], start_time: Optional[float] = None) -> None:
        mode = "train" if self.model.training else "eval"
        
        # 计算平均指标，添加异常值检查
        metrics = {}
        for key, val in self._metrics[mode].items():
            if val:  # 确保列表不为空
                avg_val = sum(val) / len(val)
                # 检查数值是否异常
                if torch.isnan(torch.tensor(avg_val)) or torch.isinf(torch.tensor(avg_val)):
                    print(f"⚠️  Warning: Metric {key} is NaN/Inf: {avg_val}")
                    # 用0替换异常值
                    avg_val = 0.0
                metrics[key] = avg_val
            else:
                metrics[key] = 0.0

        # This method can be called both in training and evaluation. When called in evaluation, the keys in `logs`
        # start with "eval_". We need to add the prefix "eval_" to the keys in `metrics` to match the format.
        if mode == "eval":
            metrics = {f"eval_{key}": val for key, val in metrics.items()}

        # Also expose total reward under a structured key for TB
        if "reward" in metrics:
            metrics.setdefault("rewards/total_reward", metrics["reward"])
        
        # 合并日志，添加调试信息
        logs = {**logs, **metrics}
        
        # 添加调试信息（仅在主进程）
        if self.accelerator.is_main_process and len(metrics) > 0:
            print(f"\n📊 Logging {len(metrics)} metrics for {mode} mode")
            print("=" * 60)
            
            # 按类别分组显示指标
            reward_metrics = {k: v for k, v in metrics.items() if 'reward' in k}
            attention_metrics = {k: v for k, v in metrics.items() if 'attention' in k}
            other_metrics = {k: v for k, v in metrics.items() if 'reward' not in k and 'attention' not in k}
            
            if reward_metrics:
                print("🎯 Reward Metrics:")
                for key, val in list(reward_metrics.items())[:3]:
                    print(f"   {key}: {val:.4f}")
                if len(reward_metrics) > 3:
                    print(f"   ... and {len(reward_metrics) - 3} more reward metrics")
            
            if attention_metrics:
                print("🧠 Attention Metrics:")
                for key, val in list(attention_metrics.items())[:3]:
                    print(f"   {key}: {val:.4f}")
                if len(attention_metrics) > 3:
                    print(f"   ... and {len(attention_metrics) - 3} more attention metrics")
            
            if other_metrics:
                print("📈 Other Metrics:")
                for key, val in list(other_metrics.items())[:3]:
                    print(f"   {key}: {val:.4f}")
                if len(other_metrics) > 3:
                    print(f"   ... and {len(other_metrics) - 3} more metrics")
            
            print("=" * 60)
        
        super().log(logs, start_time)
        self._metrics[mode].clear()

        # Optional concise MDI print
        try:
            if self.accelerator.is_main_process and getattr(self.args, "realtime_rollout_logging", False):
                key = ("eval_attention/late/mdi" if mode == "eval" else "attention/late/mdi")
                if key in logs:
                    val = logs[key]
                    if is_rich_available() and 'Console' in globals() and Console is not None and hasattr(self, "_console") and self._console is not None:
                        self._console.print(f"MDI(late) ≈ {val:.3f}")
                    else:
                        print(f"MDI(late): {val:.3f}")
        except Exception:
            pass

        if self.accelerator.is_main_process and self.log_completions:
            if is_rich_available():
                print_prompt_completions_sample(
                    self._logs["prompt"],
                    self._logs["completion"],
                    self._logs["rewards"],
                    self._logs["advantages"],
                    self.state.global_step,
                    self.num_completions_to_print,
                )

            if self.args.report_to and "wandb" in self.args.report_to and wandb.run is not None:
                import pandas as pd

                table = {
                    "step": [str(self.state.global_step)] * len(self._logs["prompt"]),
                    "prompt": self._logs["prompt"],
                    "completion": self._logs["completion"],
                    **self._logs["rewards"],
                    "advantage": self._logs["advantages"],
                }

                if self._logs["images"]:
                    table["images"] = []
                    for image_list in self._logs["images"]:
                        # Convert images to wandb Image objects for proper visualization
                        table["images"].append([wandb.Image(image) for image in image_list])

                df = pd.DataFrame(table)
                if self.wandb_log_unique_prompts:
                    df = df.drop_duplicates(subset=["prompt"])
                wandb.log({"completions": wandb.Table(dataframe=df)})

    # Ensure the model card is saved along with the checkpoint
    def _save_checkpoint(self, model, trial):
        if self.args.hub_model_id is None:
            model_name = Path(self.args.output_dir).name
        else:
            model_name = self.args.hub_model_id.split("/")[-1]
        self.create_model_card(model_name=model_name)
        super()._save_checkpoint(model, trial)

    def _add_model_unwrap_utilities(self):
        """添加模型解包工具函数和注意力实现切换上下文管理器"""
        pass

    def _unwrap_model_for_config(self, model=None):
        """
        Return the base (unwrapped) HF model object that has `.config` and `.generation_config`.
        Works with DDP, FSDP, and Deepspeed ZeRO.
        """
        m = model if model is not None else getattr(self, "model", None)
        # 优先用 accelerate 的 unwrap（Trainer 有 self.accelerator）
        try:
            if hasattr(self, "accelerator"):
                m = self.accelerator.unwrap_model(m)
        except Exception:
            pass
        # 兜底：常见包装层
        for attr in ("module", "model"):
            if hasattr(m, attr):
                m = getattr(m, attr)
        return m

    @contextmanager
    def _temporary_attn_impl(self, attn_impl: str = "eager"):
        """
        Context manager for temporarily switching attention implementation.
        Works with any parallel wrapper (DDP/FSDP/Deepspeed ZeRO).
        """
        base = self._unwrap_model_for_config()
        cfg = getattr(base, "config", None)
        if cfg is None:
            # 没有 config 就直接不改，继续执行
            yield
            return
        prev = getattr(cfg, "_attn_implementation", None)
        try:
            # 仅当属性存在或我们确实需要设置时才写入
            setattr(cfg, "_attn_implementation", attn_impl)
            yield
        finally:
            # 恢复（包括不存在时删除）
            if prev is None:
                try:
                    delattr(cfg, "_attn_implementation")
                except Exception:
                    pass
            else:
                setattr(cfg, "_attn_implementation", prev)
