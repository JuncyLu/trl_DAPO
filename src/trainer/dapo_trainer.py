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
import math
import os
import textwrap
import warnings
from collections import defaultdict, deque
from copy import deepcopy
from contextlib import nullcontext
from functools import partial
from pathlib import Path
from typing import Any, Callable, List, Optional, Union

import datasets
import torch
import torch.utils.data
import transformers
from accelerate import logging
from accelerate.utils import gather, gather_object, is_peft_model, set_seed


def safe_gather_object(data, max_items=None, max_str_len=1000):
    """
    Safe wrapper for gather_object that prevents OOM by limiting data size.
    
    Args:
        data: List of items to gather across ranks
        max_items: Maximum number of items to gather (None = no limit)
        max_str_len: Maximum string length for text items
    
    Returns:
        Gathered list of items, or local data if gathering fails
    """
    try:
        # Truncate strings if they're too long
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], str):
            data = [s[:max_str_len] if isinstance(s, str) else s for s in data]
        
        # Limit number of items if specified
        if max_items is not None and len(data) > max_items:
            data = data[:max_items]
        
        # Try to gather
        result = gather_object(data)
        return result
    except (RuntimeError, torch.OutOfMemoryError) as e:
        # If gather fails due to OOM or other issues, return local data only
        return data
    except Exception:
        # For any other errors, return local data
        return data


def log_memory_usage(accelerator, prefix=""):
    """
    Log current GPU memory usage.
    
    Args:
        accelerator: Accelerator instance
        prefix: Prefix for log message
    """
    if torch.cuda.is_available() and accelerator.is_main_process:
        try:
            allocated = torch.cuda.memory_allocated() / 1024**3  # GB
            reserved = torch.cuda.memory_reserved() / 1024**3  # GB
            max_allocated = torch.cuda.max_memory_allocated() / 1024**3  # GB
            logger.info(
                f"{prefix}GPU Memory: allocated={allocated:.2f}GB, "
                f"reserved={reserved:.2f}GB, max_allocated={max_allocated:.2f}GB"
            )
        except Exception:
            pass
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
from transformers.utils import is_datasets_available, is_peft_available, is_rich_available

from trl.data_utils import (
    apply_chat_template,
    is_conversational,
    prepare_multimodal_messages,
)
from trl.extras.profiling import profiling_context, profiling_decorator
from trl.import_utils import is_liger_kernel_available
from trl.models import prepare_deepspeed, prepare_fsdp, prepare_peft_model, unwrap_model_for_generation
from trl.models.utils import _ForwardRedirection
from trl.trainer.base_trainer import BaseTrainer
from trl.trainer.callbacks import SyncRefModelCallback
from .dapo_config import DAPOConfig
from ..rewards.reward_utils import create_reward_weight_manager, calculate_reward_metrics
from ..utils.attention_metrics import (
    compute_qwen_attention_metrics_for_batch,
    AttentionSampleResult,
    process_attention_context,
)
from ..utils import build_token_vgr_weights_for_batch
from ..rewards.accuracy_rewards_v2 import accuracy_reward
from ..utils.dapo_logging import (
    emit_eval_logs,
    compute_real_vgr_metrics,
    perform_realtime_rollout_logging,
    print_compact_logs,
    perform_eval_logging,
    record_vgr_raw_stats,
)
from contextlib import contextmanager
from trl.trainer.utils import (
    RepeatSampler,
    disable_dropout_in_model,
    entropy_from_logits,
    get_config_model_id,
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

if is_wandb_available():
    import wandb


logger = logging.get_logger(__name__)

# What we call a reward function is a callable that takes a list of prompts and completions and returns a list of
# rewards. When it's a string, it's a model ID, so it's loaded as a pretrained model.
RewardFunc = Union[str, PreTrainedModel, Callable[[list, list], list[float]]]

# What we call a rollout function is a callable that takes prompts (list), args (GRPOConfig), and processing_class as
# parameters and returns a dict of generation results. Those results must include "prompt_ids", "completion_ids", and
# "logprobs" fields. Any extra fields (per-completion) are forwarded to the reward functions.
RolloutFunc = Callable[[list[str], Any, Any], dict[str, Any]]


class DAPOTrainer(BaseTrainer):
    """
    Trainer for the DAPO (Data-Augmented Policy Optimization) method. This algorithm was initially proposed in the
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
        args ([`DAPOConfig`], *optional*):
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
        rollout_func (`RolloutFunc`, *optional*):
            Function to use for generating completions. It must take prompts, args, and processing_class as parameters
            and return a dict with `"prompt_ids"`, `"completion_ids"`, and `"logprobs"` fields. Any other fields that
            are forwarded to the reward functions. This feature is experimental and may change or be removed at any
            time without prior notice.
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
        args: Optional[DAPOConfig] = None,
        train_dataset: Optional[Union[Dataset, IterableDataset]] = None,
        eval_dataset: Optional[Union[Dataset, IterableDataset, dict[str, Union[Dataset, IterableDataset]]]] = None,
        processing_class: Optional[Union[PreTrainedTokenizerBase, ProcessorMixin]] = None,
        reward_processing_classes: Optional[Union[PreTrainedTokenizerBase, list[PreTrainedTokenizerBase]]] = None,
        callbacks: Optional[list[TrainerCallback]] = None,
        optimizers: tuple[Optional[torch.optim.Optimizer], Optional[torch.optim.lr_scheduler.LambdaLR]] = (None, None),
        peft_config: Optional["PeftConfig"] = None,
        rollout_func: Optional[RolloutFunc] = None,
    ):
        # Args
        if args is None:
            model_name = model if isinstance(model, str) else get_config_model_id(model.config)
            model_name = model_name.split("/")[-1]
            args = DAPOConfig(f"{model_name}-DAPO")

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
                    "Invalid `dtype` passed to `DAPOConfig`. Expected either 'auto' or a string representing "
                    f"a `torch.dtype` (e.g., 'float32'), but got {dtype}."
                )
            # Disable caching if gradient checkpointing is enabled (not supported)
            config = AutoConfig.from_pretrained(model_id)
            architecture = getattr(transformers, config.architectures[0])
            model = architecture.from_pretrained(model_id, **model_init_kwargs)
        else:
            model_id = get_config_model_id(model.config)
            if args.model_init_kwargs is not None:
                logger.warning(
                    "You passed `model_init_kwargs` to the `DAPOConfig`, but your model is already instantiated. "
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
                get_config_model_id(model.config), 
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
            if isinstance(reward_funcs[i], nn.Module):  # Use Module over PretrainedModel for compat w/ compiled models
                self.reward_func_names.append(get_config_model_id(reward_funcs[i].config).split("/")[-1])
            else:
                self.reward_func_names.append(reward_funcs[i].__name__)
        self.reward_funcs = reward_funcs

        # Initialize reward weight manager
        self.reward_weight_manager = create_reward_weight_manager(
            reward_weights=args.reward_weights,
            early_weights=args.early_reward_weights,
            warmup_ratio=args.warmup_ratio,
            reward_func_names=self.reward_func_names,
            reward_weight_schedule=getattr(args, "reward_weight_schedule", None),
        )

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
                    reward_processing_class = AutoTokenizer.from_pretrained(get_config_model_id(reward_func.config))
                if reward_processing_class.pad_token_id is None:
                    reward_processing_class.pad_token = reward_processing_class.eos_token
                # The reward model computes the reward for the latest non-padded token in the input sequence.
                # So it's important to set the pad token ID to the padding token ID of the processing class.
                reward_func.config.pad_token_id = reward_processing_class.pad_token_id
                reward_processing_classes[i] = reward_processing_class

        self.reward_processing_classes = reward_processing_classes

        # Rollout function
        if rollout_func is not None and os.environ.get("TRL_EXPERIMENTAL_SILENCE", "0") != "1":
            warnings.warn(
                "You are importing from 'rollout_func', which is an experimental feature. This API may change or be "
                "removed at any time without prior notice. Silence this warning by setting environment variable "
                "TRL_EXPERIMENTAL_SILENCE=1.",
                UserWarning,
                stacklevel=2,
            )
        self.rollout_func = rollout_func

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

        # Dynamic sampling (DAPO paper)
        self.dynamic_sample = args.dynamic_sample
        self.max_resample_times = args.max_resample_times
        self._pending_dynsample_log = None  # Store DynSample log message for delayed output
        
        # Debug: Confirm initialization - use print() to ensure visibility
        print(f"[INIT] Dynamic sampling: enabled={self.dynamic_sample}, max_resample_times={self.max_resample_times}")

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
            # global accumulated batch. To control scaling ourselves, we must disable Trainer's built-in scaling. The
            # simplest (though a bit hacky) way is to set `compute_loss_func` to any non-None value, which bypasses
            # that behavior without rewriting `training_step`.
            compute_loss_func="non-None value to disable scaling",
        )

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
        # Effective KL beta (with schedule if enabled)
        self._beta_eff = float(self.beta) if hasattr(self, "beta") else 0.0
        self._total_train_tokens = 0
        self.log_completions = args.log_completions
        self.wandb_log_unique_prompts = args.wandb_log_unique_prompts
        self.num_completions_to_print = args.num_completions_to_print
        # Evaluation can use a different number of generations per sample
        self.eval_num_generations = getattr(args, "eval_num_generations", 2) or 2
        # Initialize attention/metrics flags and internal logs
        self.compute_attention_metrics = args.compute_attention_metrics
        self._reset_internal_logs()

        # Ensure each process receives a unique seed to prevent duplicate completions when generating.
        set_seed(args.seed, device_specific=True)

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

        # Initialize dynamic resampling iterator if enabled
        if self.dynamic_sample:
            self._prepare_dynamic_resample_iterator()

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
            mini_repeat_count=self.eval_num_generations,
            seed=self.args.seed,
        )

    def _prepare_dynamic_resample_iterator(self):
        """
        Prepare a cyclic iterator for dynamic resampling.
        Uses a different seed to ensure the resample dataset does not overlap with train_dataset.
        """

        def cyclic_iter(iterable):
            while True:
                for x in iterable:
                    yield x

        # Use a different seed (original + 1) to avoid overlap
        original_seed = self.args.seed
        self.args.seed = original_seed + 1
        self.dynamic_resample_iterator = cyclic_iter(self.get_train_dataloader())
        self.args.seed = original_seed  # restore

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
        # Handle empty batch early to avoid zero step in range() and downstream indexing
        if input_ids.size(0) == 0:
            empty = torch.empty((0, logits_to_keep), dtype=torch.float32, device=input_ids.device)
            return empty, (empty if compute_entropy else None)

        # Chunk inputs into smaller batches to reduce memory peak; ensure positive step
        if batch_size is None or int(batch_size) <= 0:
            # If caller didn't pass a valid batch_size, default to process all available rows
            batch_size = int(max(1, input_ids.size(0)))
        else:
            batch_size = int(batch_size)
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
                end_idx = min(start + batch_size, input_ids.size(0))
                row_start, row_end = cum_rows[start].item(), cum_rows[end_idx].item()
                model_inputs["pixel_values"] = pixel_values[row_start:row_end]
                cum_imgs = torch.tensor([0] + num_images).cumsum(0)
                img_start, img_end = cum_imgs[start], cum_imgs[end_idx]
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
            assert isinstance(generation_batch, list), "GRPO expects identity-collated list of dicts."
            generate_every = self.args.steps_per_generation * self.num_iterations
            if self._step % generate_every == 0 or self._buffered_inputs is None:
                try:
                    processed_batch = self._generate_and_score_completions(generation_batch)
                except RuntimeError as e:
                    if getattr(self.args, "oom_backoff_enable", False) and "out of memory" in str(e).lower():
                        if self.accelerator.is_main_process:
                            print("[OOM backoff] Generation failed due to OOM; clearing cache and re-raising")
                        torch.cuda.empty_cache()
                    raise

                processed_batch = split_pixel_values_by_grid(processed_batch)

                # Remove metadata before shuffling tensors, then reapply permutation manually
                metadata = {}
                for meta_key in ("original_prompts", "original_images"):
                    if meta_key in processed_batch:
                        metadata[meta_key] = processed_batch.pop(meta_key)

                if metadata:
                    processed_batch, permutation = shuffle_sequence_dict(
                        processed_batch, return_permutation=True
                    )
                    indices = permutation.tolist()

                    for meta_key, meta_value in metadata.items():
                        if meta_value is None:
                            continue
                        # Ensure we always store lists so split_tensor_dict can slice consistently
                        shuffled_meta = [meta_value[i] for i in indices]
                        processed_batch[meta_key] = shuffled_meta
                else:
                    processed_batch = shuffle_sequence_dict(processed_batch)

                generation_batches = split_tensor_dict(processed_batch, self.args.steps_per_generation)
                self._buffered_inputs = [unsplit_pixel_values_by_grid(batch) for batch in generation_batches]

            step_index = self._step % self.args.steps_per_generation
            inputs = self._buffered_inputs[step_index]
            self._step += 1
        else:
            # In evaluation, there is neither batch grouping for generation, nor multiple iterations, hence
            # local generation batch == local eval batch
            inputs = self._generate_and_score_completions(generation_batch)

        # Note: num_items_in_batch is already computed in _generate_and_score_completions
        # It represents the total completion tokens across all processes for the entire generation batch.
        # Do NOT recompute it here as that would break DAPO loss normalization semantics.
        # The split_tensor_dict broadcast behavior ensures all mini-batches share this global value.

        return inputs

    @profiling_decorator
    def _calculate_rewards(self, inputs, prompts, completions, completion_ids_list):
        mode = "train" if self.model.training else "eval"
        device = self.accelerator.device
        rewards_per_func = torch.zeros(len(prompts), len(self.reward_funcs), device=device)

        # Repeat all input columns (but "prompt", "completion", and "completion_ids") to match the num of generations
        keys = [key for key in inputs[0] if key not in ["prompt", "completion", "completion_ids"]]
        reward_kwargs = {key: [example[key] for example in inputs] for key in keys}

        # This allows for dynamic reward shaping based on training progress.
        reward_kwargs["trainer_state"] = self.state

        # Add num_generations for group-wise reward calculation
        reward_kwargs["num_generations"] = self.num_generations if self.model.training else self.eval_num_generations

        # Add attention data for reward functions if available
        if self.compute_attention_metrics and hasattr(self, "_logs") and "attention" in self._logs:
            att_list = list(self._logs["attention"])

            if att_list:
                # Get the most recent attention results for this batch
                sample_results = att_list[-len(prompts):]

                # Align skip reasons with the same recent slice
                if hasattr(self, "_attention_skip_reasons"):
                    skips = list(self._attention_skip_reasons)
                    if len(skips) >= len(sample_results):
                        skip_slice = skips[-len(sample_results):]
                    else:
                        skip_slice = [None] * len(sample_results)
                else:
                    skip_slice = [None] * len(sample_results)

                vgr_metrics = compute_real_vgr_metrics(sample_results, skip_slice)

                # Attach metrics to inputs for consistent logging (important for dynamic sampling)
                for idx, m in enumerate(vgr_metrics):
                    if idx < len(inputs):
                        inputs[idx]["vgr_metrics"] = m

                reward_kwargs["attention_text"] = [m.get("attention_text", 0.0) for m in vgr_metrics]
                reward_kwargs["attention_vision"] = [m.get("attention_vision", 0.0) for m in vgr_metrics]
                reward_kwargs["num_text_tokens"] = [m.get("num_text_tokens", 0) for m in vgr_metrics]
                reward_kwargs["num_vision_tokens"] = [m.get("num_vision_tokens", 0) for m in vgr_metrics]
                record_vgr_raw_stats(vgr_metrics, self._metrics, mode, self.accelerator)

        # 计算逐样本准确率，并传递给奖励函数（供 vgr_accuracy_reward 使用）
        try:
            solutions_for_batch = reward_kwargs.get("solution", None)
            if solutions_for_batch is None:
                solutions_for_batch = reward_kwargs.get("solutions", None)

            if solutions_for_batch is not None:
                acc_scores = accuracy_reward(
                    completions=completions,
                    solution=solutions_for_batch,
                )
                # 将 None 安全转为 0.0
                reward_kwargs["accuracies"] = [float(x) if x is not None else 0.0 for x in acc_scores]
        except Exception:
            pass

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

        # NOTE: Unlike the original implementation, we intentionally keep rewards_per_func local
        # to each rank here. Dynamic sampling and logging operate per-rank, and global aggregation
        # is handled separately via accelerator utilities where needed.
        return rewards_per_func

    def _get_dynamic_sampling_scores(self, rewards_per_func: torch.Tensor) -> torch.Tensor:
        """
        Build scalar scores for dynamic sampling using a weighted sum of accuracy, vgr, and format rewards.
        """
        if rewards_per_func.numel() == 0:
            return rewards_per_func.new_zeros(rewards_per_func.size(0))

        device = rewards_per_func.device
        weights = self.reward_weight_manager.get_current_weights().to(device)

        target_groups = [
            {"accuracy_reward", "accuracy_reward_v2"},
            {"vgr_reward", "vgr_reward_as_additive", "vgr_hard_negative"},
            {"think_format_reward", "format_reward"},
        ]

        selected_terms = []
        for group in target_groups:
            idx = next((i for i, name in enumerate(self.reward_func_names) if name in group), None)
            if idx is not None and idx < rewards_per_func.size(1):
                term = rewards_per_func[:, idx] * weights[idx]
                term = torch.nan_to_num(term, nan=0.0)
                selected_terms.append(term)

        if selected_terms:
            scores = torch.stack(selected_terms, dim=0).sum(dim=0)
        else:
            scores = self.reward_weight_manager.calculate_total_reward(rewards_per_func, device=device)
        return scores

    def compute_group_validity(
        self, scores: torch.Tensor, num_generations: int, tol: float = 1e-6
    ) -> torch.Tensor:
        """
        Check if each group should be kept based on the variance of the provided scores.
        Groups are invalid (0) if all scores inside the group are (near) identical.

        Args:
            scores: Tensor of shape (total_samples,) with scalar values to test variance on
            num_generations: Number of generations per prompt group
            tol: Numerical tolerance used to decide whether std≈0

        Returns:
            Tensor of shape (total_samples,) with 1 for valid groups, 0 for invalid groups
        """
        device = self.accelerator.device

        if scores.size(0) % num_generations != 0:
            return torch.ones(scores.size(0), dtype=torch.float32, device=device)

        safe_scores = torch.nan_to_num(scores, nan=0.0)
        grouped = safe_scores.view(-1, num_generations)
        std = grouped.std(dim=1, unbiased=False)
        invalid_groups = std <= tol
        valid_groups = ~invalid_groups
        valid_mask = valid_groups.float().repeat_interleave(num_generations)
        return valid_mask

    @profiling_decorator
    def _dynamic_sampling(
        self,
        inputs: list,
        prompts: list,
        completions: list,
        prompt_ids_list: list[list[int]],
        completion_ids_list: list[list[int]],
            rewards_per_func: torch.Tensor,
            total_rewards: torch.Tensor,
            filter_scores: torch.Tensor,
        images: Optional[list] = None,
        token_weights_list: Optional[list] = None,
    ):
        """
        Perform dynamic sampling by replacing flat total-reward groups with resampled data.
        
        Key mechanism (inspired by ms-swift):
        1. ALL ranks enter the resampling loop synchronously (to avoid dataloader deadlock)
        2. Collect valid samples from ALL ranks into a global pool (via gather_object)
        3. Each rank slices its portion from the global pool
        4. Exit when global pool has enough valid groups

        Args:
            inputs: Local input samples (list[dict])
            prompts: Prompts corresponding to the local samples
            completions: Generated completions for the local samples
            prompt_ids_list: Tokenized prompts produced during generation
            completion_ids_list: Tokenized completions
            rewards_per_func: Reward tensor for local samples on this rank
            total_rewards: Weighted reward tensor for local samples
            filter_scores: Scalar scores used to detect flat groups (accuracy + format)
            images: Optional multimodal payload accompanying each sample
            token_weights_list: Optional per-sample token weights

        Returns:
            Tuple containing potentially resampled (inputs, prompts, completions, prompt_ids_list, completion_ids_list,
            rewards_per_func, total_rewards, filter_scores, images, token_weights_list) aligned across ranks.
        """
        device = self.accelerator.device
        mode = "train" if self.model.training else "eval"
        ng = self.num_generations if mode == "train" else self.eval_num_generations
        
        # Target: number of samples each rank should have
        local_target = len(inputs)
        # Global target: total samples across all ranks
        global_target = local_target * self.accelerator.num_processes

        # Save original data for fallback
        origin_data = (
            inputs,
            prompts,
            completions,
            prompt_ids_list,
            completion_ids_list,
            rewards_per_func,
            total_rewards,
            filter_scores,
            images,
            token_weights_list,
        )

        # Initialize containers for GLOBAL valid samples (collected from all ranks)
        resample_count = 0
        global_valid_samples: list = []  # Will hold dicts with all necessary data
        
        if self.accelerator.is_main_process:
            log_memory_usage(self.accelerator, "[DynSample Start] ")

        # Initial check: compute validity for current batch
        validity_mask = self.compute_group_validity(filter_scores, ng) > 0
        num_groups = filter_scores.numel() // max(1, ng)
        
        # Gather global group stats for debugging
        try:
            global_filter_scores = gather(filter_scores)
            if self.accelerator.is_main_process and global_filter_scores is not None:
                pass
        except Exception as e:
            if self.accelerator.is_main_process:
                logger.warning(f"[DynSample] Failed to gather global stats: {e}")
        
        # Collect valid samples from ALL ranks (gather_object for cross-rank sharing)
        # Build a list of sample dicts, each containing all necessary data for one sample
        # CRITICAL: Mark each sample with its source rank to prevent duplicates when a rank falls back
        local_samples_with_validity = []
        current_rank = self.accelerator.process_index
        for idx in range(len(inputs)):
            sample_dict = {
                "input": inputs[idx],
                "prompt": prompts[idx],
                "completion": completions[idx],
                "prompt_ids": prompt_ids_list[idx],
                "completion_ids": completion_ids_list[idx],
                "rewards_per_func": rewards_per_func[idx],
                "total_reward": total_rewards[idx],
                "filter_score": filter_scores[idx],
                "image": images[idx] if images is not None else None,
                "token_weights": token_weights_list[idx] if token_weights_list is not None else None,
                "valid": validity_mask[idx].item(),  # Boolean indicating if this sample's group is valid
                "source_rank": current_rank,  # Mark which rank this sample came from
            }
            local_samples_with_validity.append(sample_dict)
        
        # Gather samples from all ranks
        try:
            all_samples_nested = safe_gather_object(local_samples_with_validity, max_items=50, max_str_len=500)
            # Flatten nested list: gather_object returns [[rank0_samples], [rank1_samples], ...]
            all_samples = []
            if isinstance(all_samples_nested, list):
                for rank_samples in all_samples_nested:
                    if isinstance(rank_samples, list):
                        all_samples.extend(rank_samples)
                    else:
                        all_samples.append(rank_samples)
            else:
                all_samples = local_samples_with_validity  # Fallback
        except Exception as e:
            if self.accelerator.is_main_process:
                logger.warning(f"[DynSample] Failed to gather samples across ranks: {e}")
            all_samples = local_samples_with_validity  # Fallback to local only
        
        # Filter out valid samples (groups with std > 0)
        for sample in all_samples:
            if sample["valid"]:
                global_valid_samples.append(sample)
        
        
        # Resample loop: ALL ranks enter synchronously to avoid dataloader deadlock
        # Continue until global pool has enough samples OR max attempts reached
        while len(global_valid_samples) < global_target and resample_count < self.max_resample_times:

            # CRITICAL: ALL ranks must call next() simultaneously to avoid deadlock!
            try:
                new_inputs = next(self.dynamic_resample_iterator)
            except StopIteration:
                break
            except Exception as e:
                break
                
            new_prompts = [example["prompt"] for example in new_inputs]

            # Extract multimodal payloads
            if new_inputs and "images" in new_inputs[0]:
                new_images = [example.get("images") for example in new_inputs]
            elif new_inputs and "image" in new_inputs[0]:
                new_images = [
                    [example.get("image")] if example.get("image") is not None else None for example in new_inputs
                ]
            else:
                new_images = None
            if new_images is not None and all(imgs in (None, []) for imgs in new_images):
                new_images = None

            mm_prompts = (
                [
                    prepare_multimodal_messages(prompt, image_list)
                    for prompt, image_list in zip(new_prompts, new_images)
                ]
                if new_images is not None
                else new_prompts
            )

            # Generate completions for new batch (ALL ranks participate)
            new_prompt_ids_list, new_completion_ids_list, _, _, extra_fields = self._generate(mm_prompts, new_images)
            new_token_weights_list = extra_fields.pop("token_weights", None) if extra_fields else None

            # Decode completions
            vocab_size = len(self.processing_class.tokenizer)
            completion_ids_filtered = [
                [token_id for token_id in ids if 0 <= token_id < vocab_size] for ids in new_completion_ids_list
            ]
            completions_decoded = self.processing_class.batch_decode(
                completion_ids_filtered,
                skip_special_tokens=True,
            )

            new_completions = completions_decoded
            if new_inputs and is_conversational(new_inputs[0]):
                new_completions_conv = []
                for sample, completion_text in zip(new_inputs, completions_decoded):
                    prompt_messages = sample["prompt"]
                    bootstrap = prompt_messages[-1]["content"] if prompt_messages and prompt_messages[-1]["role"] == "assistant" else ""
                    new_completions_conv.append([{"role": "assistant", "content": bootstrap + completion_text}])
                new_completions = new_completions_conv

            # Calculate rewards for new batch (ALL ranks)
            new_rewards_per_func = self._calculate_rewards(
                new_inputs, new_prompts, new_completions, new_completion_ids_list
            )
            new_total_rewards = self.reward_weight_manager.calculate_total_reward(new_rewards_per_func, device)
            new_filter_scores = self._get_dynamic_sampling_scores(new_rewards_per_func)
            
            # Check validity of new groups
            new_validity_mask = self.compute_group_validity(new_filter_scores, ng) > 0
            
            # Gather global stats for this resample
            try:
                global_new_scores = gather(new_filter_scores)
                if self.accelerator.is_main_process and global_new_scores is not None:
                    pass
            except Exception as e:
                if self.accelerator.is_main_process:
                    logger.warning(f"[DynSample] Failed to gather resample stats: {e}")
            
            # Build sample dicts for this resample batch
            # CRITICAL: Mark each sample with its source rank to prevent duplicates when a rank falls back
            new_samples_with_validity = []
            current_rank = self.accelerator.process_index
            for idx in range(len(new_inputs)):
                sample_dict = {
                    "input": new_inputs[idx],
                    "prompt": new_prompts[idx],
                    "completion": new_completions[idx],
                    "prompt_ids": new_prompt_ids_list[idx],
                    "completion_ids": new_completion_ids_list[idx],
                    "rewards_per_func": new_rewards_per_func[idx],
                    "total_reward": new_total_rewards[idx],
                    "filter_score": new_filter_scores[idx],
                    "image": new_images[idx] if new_images is not None else None,
                    "token_weights": new_token_weights_list[idx] if new_token_weights_list is not None else None,
                    "valid": new_validity_mask[idx].item(),
                    "source_rank": current_rank,  # Mark which rank this sample came from
                }
                new_samples_with_validity.append(sample_dict)
            
            # Gather new samples from ALL ranks (cross-rank sharing)
            try:
                all_new_samples_nested = safe_gather_object(new_samples_with_validity, max_items=50, max_str_len=500)
                # Flatten nested list
                all_new_samples = []
                if isinstance(all_new_samples_nested, list):
                    for rank_samples in all_new_samples_nested:
                        if isinstance(rank_samples, list):
                            all_new_samples.extend(rank_samples)
                        else:
                            all_new_samples.append(rank_samples)
                else:
                    all_new_samples = new_samples_with_validity  # Fallback
            except Exception as e:
                all_new_samples = new_samples_with_validity  # Fallback to local only
            
            # Add valid samples to global pool
            for sample in all_new_samples:
                if sample["valid"] and len(global_valid_samples) < global_target:
                    global_valid_samples.append(sample)

            # Clean up intermediate tensors to prevent memory buildup
            del new_rewards_per_func, new_total_rewards, new_filter_scores
            del new_validity_mask
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            
            # Log memory usage after cleanup
            if self.accelerator.is_main_process and resample_count % 2 == 0:
                log_memory_usage(self.accelerator, f"[DynSample Resample #{resample_count + 1}] ")
            
            resample_count += 1

        # Finalize: Distribute global valid samples to each rank
        if len(global_valid_samples) == 0:
            # No valid samples collected at all – fall back to original batch
            (
                inputs,
                prompts,
                completions,
                prompt_ids_list,
                completion_ids_list,
                rewards_per_func,
                total_rewards,
                filter_scores,
                images,
                token_weights_list,
            ) = origin_data
        else:
            # Slice global pool for this rank (like ms-swift does)
            # Each rank gets: global_valid_samples[rank_idx * local_target : (rank_idx + 1) * local_target]
            rank_idx = self.accelerator.process_index
            start_idx = rank_idx * local_target
            end_idx = min(start_idx + local_target, len(global_valid_samples))
            
            # If global pool is smaller than target, take what we can
            if end_idx <= start_idx:
                # This rank has no samples in the global pool - fallback to original
                # CRITICAL: To prevent duplicates, only use INVALID samples from origin_data
                # (valid samples are already in global pool and used by other ranks)
                
                # Extract only invalid samples from origin_data
                origin_inputs, origin_prompts, origin_completions, origin_prompt_ids, origin_completion_ids, \
                    origin_rewards_per_func, origin_total_rewards, origin_filter_scores, origin_images, origin_token_weights = origin_data
                
                # Recompute validity mask for origin_data (in case it wasn't computed)
                origin_validity_mask = self.compute_group_validity(origin_filter_scores, ng) > 0
                invalid_indices = (~origin_validity_mask).nonzero(as_tuple=True)[0]
                
                if len(invalid_indices) > 0:
                    # Use invalid samples only
                    inputs = [origin_inputs[i] for i in invalid_indices]
                    prompts = [origin_prompts[i] for i in invalid_indices]
                    completions = [origin_completions[i] for i in invalid_indices]
                    prompt_ids_list = [origin_prompt_ids[i] for i in invalid_indices]
                    completion_ids_list = [origin_completion_ids[i] for i in invalid_indices]
                    rewards_per_func = origin_rewards_per_func[invalid_indices]
                    total_rewards = origin_total_rewards[invalid_indices]
                    filter_scores = origin_filter_scores[invalid_indices]
                    images = [origin_images[i] for i in invalid_indices] if origin_images is not None else None
                    token_weights_list = [origin_token_weights[i] for i in invalid_indices] if origin_token_weights is not None else None
                else:
                    # No invalid samples available - use all origin_data (fallback of last resort)
                    (inputs, prompts, completions, prompt_ids_list, completion_ids_list, rewards_per_func, total_rewards, filter_scores, images, token_weights_list) = origin_data
            else:
                my_samples = global_valid_samples[start_idx:end_idx]
                
                # Unpack samples into separate lists
                inputs = [s["input"] for s in my_samples]
                prompts = [s["prompt"] for s in my_samples]
                completions = [s["completion"] for s in my_samples]
                prompt_ids_list = [s["prompt_ids"] for s in my_samples]
                completion_ids_list = [s["completion_ids"] for s in my_samples]
                
                # Stack tensors - CRITICAL: Move all tensors to current rank's device
                # Samples may come from different ranks (different cuda devices)
                rewards_per_func = torch.stack([s["rewards_per_func"].to(device) for s in my_samples])
                total_rewards = torch.stack([s["total_reward"].to(device) for s in my_samples])
                filter_scores = torch.stack([s["filter_score"].to(device) for s in my_samples])
                
                images = [s["image"] for s in my_samples] if my_samples[0]["image"] is not None else None
                token_weights_list = [s["token_weights"] for s in my_samples] if my_samples[0]["token_weights"] is not None else None
                
                if self.accelerator.is_main_process:
                    final_groups = len(my_samples) // ng
                    # Store DynSample message for later output in log() method
                    self._pending_dynsample_log = (
                        f"[DynSample] Rank {self.accelerator.process_index}: ✅ Using {len(my_samples)} valid samples "
                        f"({final_groups} groups) from global pool after {resample_count} resample(s)"
                    )
                    log_memory_usage(self.accelerator, f"[DynSample Success] ")

        # Clean up to prevent memory leaks
        # Check if we need to clear pending log before deleting global_valid_samples
        if self.accelerator.is_main_process and len(global_valid_samples) == 0:
            self._pending_dynsample_log = None
        del global_valid_samples
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        # Final memory check
        if self.accelerator.is_main_process:
            log_memory_usage(self.accelerator, "[DynSample End] ")

        return (
            inputs,
            prompts,
            completions,
            prompt_ids_list,
            completion_ids_list,
            rewards_per_func,
            total_rewards,
            filter_scores,
            images,
            token_weights_list,
        )

    def _generate_single_turn(self, prompts: list, images: Optional[list] = None):
        device = self.accelerator.device
        # Use eval-specific generations when not training
        ng = self.num_generations if self.model.training else self.eval_num_generations

        # Generate completions using either paged transformers kernels or the regular path
        if self.use_transformers_paged:
            processor_kwargs = {"max_length": self.max_prompt_length, "truncation": True, "add_special_tokens": False}
            if is_conversational({"prompt": prompts[0]}):
                generate_inputs = self.processing_class.apply_chat_template(
                    conversation=prompts, add_generation_prompt=True, **processor_kwargs, tokenize=True, return_dict=True
                )
            else:
                generate_inputs = self.processing_class(text=prompts, **processor_kwargs)
            generate_inputs["inputs"] = generate_inputs.pop("input_ids")

            # 打印 prompt token 数统计，帮助排查 OOM
            try:
                _lens = [len(ids) for ids in generate_inputs["input_ids"]]
                if _lens:
                    _min, _max = min(_lens), max(_lens)
                    _mean = sum(_lens) / len(_lens)
                    print(f"[PromptToken] batch_size={len(_lens)} min/mean/max={_min}/{_mean:.1f}/{_max}")
            except Exception:
                pass

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
                        **generate_inputs, generation_config=self.generation_config, progress_bar=False
                    )
                    unwrapped_model.train()  # restore training mode, as generate_batch forces eval mode
            completion_ids = [output.generated_tokens for output in all_outputs.values()]
            prompt_ids = generate_inputs["inputs"]
            logprobs = None  # not used in this case
            extra_fields = {}  # No extra fields for paged mode
            attention_context = None  # paged mode doesn't support attention output

        else:
            # Regular generation path
            processor_kwargs = {
                "return_tensors": "pt",
                "padding": True,
                "padding_side": "left",
                "max_length": self.max_prompt_length,
                "truncation": True,
                "add_special_tokens": False,
            }
            # Build text with chat template and include images if provided
            prompts_text = [
                apply_chat_template({"prompt": prompt}, self.processing_class)["prompt"]
                for prompt in prompts
            ]
            if images is not None:
                generate_inputs = self.processing_class(text=prompts_text, images=images, **processor_kwargs)
            else:
                generate_inputs = self.processing_class(text=prompts_text, **processor_kwargs)
            generate_inputs = super()._prepare_inputs(generate_inputs)

            with (
                profiling_context(self, "transformers.generate"),
                unwrap_model_for_generation(
                    self.model_wrapped, self.accelerator, gather_deepspeed3_params=self.args.ds3_gather_for_generation
                ) as unwrapped_model,
                torch.no_grad(),
                FSDP.summon_full_params(self.model_wrapped, recurse=False) if self.is_fsdp_enabled else nullcontext(),
            ):
                # Collect attention data if enabled
                attention_context = None
                if self.compute_attention_metrics:
                    # Store original values
                    cfg = getattr(unwrapped_model, "config", None)
                    lm_cfg = getattr(unwrapped_model.language_model, "config", None) if hasattr(unwrapped_model, "language_model") else None
                    
                    prev_main = getattr(cfg, "_attn_implementation", None) if cfg else None
                    prev_lm = getattr(lm_cfg, "_attn_implementation", None) if lm_cfg else None
                    
                    try:
                        # Set to eager
                        if cfg:
                            setattr(cfg, "_attn_implementation", "eager")
                        if lm_cfg:
                            setattr(lm_cfg, "_attn_implementation", "eager")
                        
                        with self._attn_last_k_layers_only(
                            unwrapped_model, last_k_layers=getattr(self.args, "attention_last_k_layers", 6)
                        ):
                            attention_outputs = unwrapped_model.generate(
                                **generate_inputs,
                                generation_config=self.generation_config,
                                disable_compile=True,
                                return_dict_in_generate=True,
                                output_attentions=True,
                            )
                    finally:
                        # Restore original values
                        if cfg:
                            if prev_main is None:
                                try:
                                    delattr(cfg, "_attn_implementation")
                                except Exception:
                                    pass
                            else:
                                setattr(cfg, "_attn_implementation", prev_main)
                        if lm_cfg:
                            if prev_lm is None:
                                try:
                                    delattr(lm_cfg, "_attn_implementation")
                                except Exception:
                                    pass
                            else:
                                setattr(lm_cfg, "_attn_implementation", prev_lm)
                    
                    prompt_completion_ids = attention_outputs.sequences
                    attention_context = {"outputs": attention_outputs, "inputs": generate_inputs}
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
            extra_fields = {}  # No extra fields for non-rollout_func paths

        return prompt_ids, completion_ids, logprobs, extra_fields, attention_context

    def _generate(self, prompts: list, images: Optional[list] = None):
        device = self.accelerator.device
        mode = "train" if self.model.training else "eval"

        prompt_ids, completion_ids, logprobs, extra_fields, attention_context = self._generate_single_turn(
            prompts, images
        )

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

        # Process attention metrics if available and put token_weights into extra_fields
        tw_list = self._process_attention_metrics(attention_context, mode)
        if tw_list is not None:
            extra_fields = extra_fields or {}
            extra_fields["token_weights"] = tw_list

        return prompt_ids, completion_ids, total_completion_tokens, logprobs, extra_fields

    def _generate_and_score_completions(
        self, inputs: list[dict[str, Union[torch.Tensor, Any]]]
    ) -> dict[str, Union[torch.Tensor, Any]]:
        device = self.accelerator.device
        mode = "train" if self.model.training else "eval"
        # Preferred generations per prompt for current mode
        preferred_num_generations = self.num_generations if mode == "train" else self.eval_num_generations
        
        if mode == "train":
            weight_metrics = self.reward_weight_manager.update_weights(
                self.state.global_step, 
                self.args.max_steps if self.args.max_steps > 0 else self.state.max_steps
            )
            for key, value in weight_metrics.items():
                self._metrics[mode][key].append(value)

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

        if images is not None:
            mm_prompts = [prepare_multimodal_messages(prompt, image_list) for prompt, image_list in zip(prompts, images)]
        else:
            mm_prompts = prompts
        
        if self.accelerator.is_main_process:
            logger.info(
                "[Debug][Generate] step=%s batch=%s images=%s dyn_sample=%s -> start _generate",
                getattr(self.state, "global_step", None),
                len(mm_prompts),
                images is not None,
                self.dynamic_sample,
            )
        prompt_ids_list, completion_ids_list, num_items_in_batch, sampling_per_token_logps_list, extra_fields = (
            self._generate(mm_prompts, images)
        )
        if self.accelerator.is_main_process:
            logger.info(
                "[Debug][Generate] step=%s finished _generate prompt_lens_sample=%s completion_lens_sample=%s",
                getattr(self.state, "global_step", None),
                [len(ids) for ids in prompt_ids_list[:4]],
                [len(ids) for ids in completion_ids_list[:4]],
            )
        
        # Extract token_weights from extra_fields to keep it with samples
        token_weights_list = extra_fields.pop("token_weights", None) if extra_fields else None

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

        with torch.no_grad():
            # If the generation and optimization steps are misaligned—i.e., if generation does not occur at the end of
            # a full optimizer step (when gradient_accumulation_steps is not a multiple of generate_every)—then the
            # samples may come from an earlier version of the model. In that case, we need to track old_per_token_logps
            # for importance sampling. If the steps are aligned, importance sampling isn't necessary and we set
            # old_per_token_logps to None.
            generate_every = self.args.steps_per_generation * self.num_iterations  # generation frequency
            if self.args.gradient_accumulation_steps % generate_every != 0:
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
        prompts_text = self.processing_class.batch_decode(prompt_ids, skip_special_tokens=False)
        # Model outputs kept as plain text (no special tokens)
        # Filter out invalid token IDs that are out of vocabulary range
        vocab_size = len(self.processing_class.tokenizer)
        completion_ids_filtered = []
        has_invalid_tokens = False
        for batch_idx, ids in enumerate(completion_ids):
            # Convert to list and filter out invalid token IDs
            ids_list = ids.cpu().tolist() if torch.is_tensor(ids) else ids
            invalid_ids = [id for id in ids_list if not (0 <= id < vocab_size)]
            if invalid_ids:
                has_invalid_tokens = True
                if self.accelerator.is_main_process:
                    print(f"[Warning] Found {len(invalid_ids)} invalid token IDs in batch {batch_idx}: {invalid_ids[:10]}")  # Show first 10
            filtered_ids = [id for id in ids_list if 0 <= id < vocab_size]
            completion_ids_filtered.append(filtered_ids)
        
        if has_invalid_tokens and self.accelerator.is_main_process:
            print(f"[Warning] Vocabulary size: {vocab_size}, filtered invalid tokens before decoding")
        
        completions_text = self.processing_class.batch_decode(completion_ids_filtered, skip_special_tokens=True)
        if is_conversational(inputs[0]):
            completions = []
            for prompt, completion in zip(prompts, completions_text):
                bootstrap = prompt.pop()["content"] if prompt[-1]["role"] == "assistant" else ""
                completions.append([{"role": "assistant", "content": bootstrap + completion}])
        else:
            completions = completions_text

        # Merge extra_fields from rollout_func into inputs for reward functions
        if extra_fields:
            for i, inp in enumerate(inputs):
                for key, values in extra_fields.items():
                    if isinstance(values, list) and i < len(values):
                        inp[key] = values[i]
                    elif not isinstance(values, list):
                        inp[key] = values

        # Prepare multimodal tensors aligned with the current prompts/images
        num_images = [len(img_list) for img_list in images] if images is not None else None
        forward_kwargs = {}
        if images is not None:
            prompts_text_for_processing = [
                apply_chat_template({"prompt": prompt}, self.processing_class)["prompt"] for prompt in prompts
            ]
            prompt_inputs = self.processing_class(
                images=images, text=prompts_text_for_processing, padding=True, return_tensors="pt"
            )
            prompt_inputs = super()._prepare_inputs(prompt_inputs)
            forward_kwargs = {k: v for k, v in prompt_inputs.items() if k not in ["input_ids", "attention_mask"]}

        # Calculate rewards for each reward function. rewards_per_func is kept local to each rank;
        # aggregation across processes (if needed) is handled separately by accelerator utilities.
        rewards_per_func = self._calculate_rewards(inputs, prompts, completions, completion_ids_list)
        total_rewards_local = self.reward_weight_manager.calculate_total_reward(rewards_per_func, device)
        filter_scores = self._get_dynamic_sampling_scores(rewards_per_func)
        
        # Dynamic sampling: filter out flat (accuracy + format + tag) groups and resample (only in training mode).
        if self.dynamic_sample and mode == "train":
            if self.accelerator.is_main_process:
                logger.info(
                    "[DynSample] step=%s enter: batch=%s rewards_shape=%s",
                    getattr(self.state, "global_step", None),
                    len(inputs),
                    tuple(rewards_per_func.shape),
                )
                log_memory_usage(self.accelerator, "[Before DynSample] ")
            
            (
                inputs,
                prompts,
                completions,
                prompt_ids_list,
                completion_ids_list,
                rewards_per_func,
                total_rewards_local,
                filter_scores,
                images,
                token_weights_list,
            ) = self._dynamic_sampling(
                inputs,
                prompts,
                completions,
                prompt_ids_list,
                completion_ids_list,
                rewards_per_func,
                total_rewards_local,
                filter_scores,
                images,
                token_weights_list,
            )
            if self.accelerator.is_main_process:
                logger.info(
                    "[DynSample] step=%s exit: batch=%s",
                    getattr(self.state, "global_step", None),
                    len(inputs),
                )
                log_memory_usage(self.accelerator, "[After DynSample] ")
            
            # After dynamic sampling, rebuild tensors/pixel inputs based on the new token ids
            completion_ids_tensors = [torch.tensor(ids, device=device) for ids in completion_ids_list]
            completion_mask = [torch.ones_like(ids, dtype=torch.long) for ids in completion_ids_tensors]
            completion_ids = pad(completion_ids_tensors, padding_value=self.pad_token_id, padding_side="right")
            completion_mask = pad(completion_mask, padding_value=0, padding_side="right")

            prompt_id_tensors = [torch.tensor(ids, device=device) for ids in prompt_ids_list]
            prompt_mask = [torch.ones_like(ids, dtype=torch.long) for ids in prompt_id_tensors]
            prompt_ids = pad(prompt_id_tensors, padding_value=self.pad_token_id, padding_side="left")
            prompt_mask = pad(prompt_mask, padding_value=0, padding_side="left")

            prompt_completion_ids = torch.cat([prompt_ids, completion_ids], dim=1)
            attention_mask = torch.cat([prompt_mask, completion_mask], dim=1)
            logits_to_keep = completion_ids.size(1)

            # Update decoded text for logging based on final tokens
            prompts_text = self.processing_class.batch_decode(prompt_ids, skip_special_tokens=False)
            vocab_size = len(self.processing_class.tokenizer)
            completion_ids_filtered = []
            for ids in completion_ids:
                ids_list = ids.cpu().tolist()
                valid_ids = [idx for idx in ids_list if 0 <= idx < vocab_size]
                completion_ids_filtered.append(valid_ids)
            completions_text = self.processing_class.batch_decode(
                completion_ids_filtered,
                skip_special_tokens=True,
            )
            if is_conversational(inputs[0]):
                completions = []
                for prompt, completion in zip(prompts, completions_text):
                    bootstrap = prompt.pop()["content"] if prompt[-1]["role"] == "assistant" else ""
                    completions.append([{"role": "assistant", "content": bootstrap + completion}])
            else:
                completions = completions_text

            num_images = [len(img_list) for img_list in images] if images is not None else None
            forward_kwargs = {}
            if images is not None:
                prompts_text_for_processing = [
                    apply_chat_template({"prompt": prompt}, self.processing_class)["prompt"] for prompt in prompts
                ]
                prompt_inputs = self.processing_class(
                    images=images, text=prompts_text_for_processing, padding=True, return_tensors="pt"
                )
                prompt_inputs = super()._prepare_inputs(prompt_inputs)
                forward_kwargs = {k: v for k, v in prompt_inputs.items() if k not in ["input_ids", "attention_mask"]}

        # If token_type_ids are used, extend them with zeros for the completion part
        if "token_type_ids" in forward_kwargs:
            token_type_ids = forward_kwargs["token_type_ids"]
            forward_kwargs["token_type_ids"] = torch.cat(
                [token_type_ids, token_type_ids.new_zeros(completion_ids.shape)], dim=1
            )

        # Apply weights to each reward function's output and sum using reward weight manager
        rewards = self.reward_weight_manager.calculate_total_reward(rewards_per_func, device)

        # Compute grouped-wise rewards
        group_ng = preferred_num_generations
        if group_ng is None or group_ng < 1:
            group_ng = 1
        # If the current batch size is not divisible by group_ng (can happen in eval), fall back to 1
        if rewards.numel() % group_ng != 0:
            group_ng = 1
        mean_grouped_rewards = rewards.view(-1, group_ng).mean(dim=1)

        # Normalize the rewards to compute the advantages
        mean_grouped_rewards = mean_grouped_rewards.repeat_interleave(group_ng, dim=0)
        advantages = rewards - mean_grouped_rewards

        if self.scale_rewards in ["group", "none"]:
            # If self.scale_rewards = "none", we'll still log group level std
            std_rewards = rewards.view(-1, group_ng).std(dim=1, unbiased=False)
            std_rewards = std_rewards.repeat_interleave(group_ng, dim=0)
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

        # Keep advantages local to this rank. We no longer slice a globally-gathered
        # tensor here, since dynamic sampling and reward computation are done per-rank.
        all_process_advantages = advantages.clone()

        # Calculate reward metrics using utility function
        reward_metrics = calculate_reward_metrics(rewards_per_func, self.reward_func_names, device)
        for key, value in reward_metrics.items():
            self._metrics[mode][key].append(value)
        self._metrics[mode]["reward"].append(mean_grouped_rewards.mean().item())
        self._metrics[mode]["reward_std"].append(std_rewards.mean().item())
        self._metrics[mode]["frac_reward_zero_std"].append(is_std_zero.float().mean().item())

        try:
            vgr_mean_alias = None
            vgr_std_alias = None
            # prefer the unified key produced by calculate_reward_metrics; else fallback
            vgr_mean_alias = reward_metrics.get("rewards/vgr/mean")
            vgr_std_alias = reward_metrics.get("rewards/vgr/std")
            if vgr_mean_alias is None:
                # fallback to underlying keys
                if getattr(self.args, "vgr_hard_negative", False):
                    vgr_mean_alias = reward_metrics.get("rewards/vgr_hard_negative/mean")
                    vgr_std_alias = reward_metrics.get("rewards/vgr_hard_negative/std")
                else:
                    vgr_mean_alias = reward_metrics.get("rewards/vgr_reward/mean", reward_metrics.get("rewards/vgr_reward_as_additive/mean"))
                    vgr_std_alias = reward_metrics.get("rewards/vgr_reward/std", reward_metrics.get("rewards/vgr_reward_as_additive/std"))
            if vgr_mean_alias is not None:
                self._metrics[mode]["rewards/vgr/mean"].append(float(vgr_mean_alias))
            if vgr_std_alias is not None:
                self._metrics[mode]["rewards/vgr/std"].append(float(vgr_std_alias))
        except Exception:
            pass

        # Build ChatML prompt strings for logging; keep completion as plain text
        try:
            if is_conversational(inputs[0]):
                rendered_prompts = [
                    apply_chat_template({"prompt": p}, self.processing_class)["prompt"] for p in prompts
                ]
            else:
                rendered_prompts = prompts_text
        except Exception:
            rendered_prompts = prompts_text

        # Log prompt and completion texts (ChatML prompt, plain completion)
        # Use safe_gather_object to prevent OOM from large text collections
        self._logs["prompt"].extend(safe_gather_object(prompts_text, max_str_len=8192))
        self._logs["completion"].extend(safe_gather_object(completions_text, max_str_len=8192))
        self._logs["prompt_chatml"].extend(safe_gather_object(rendered_prompts, max_str_len=8192))
        # Gather rewards from all processes to match prompt/completion counts
        for i, name in enumerate(self.reward_func_names):
            reward_values = rewards_per_func[:, i].tolist()
            self._logs["rewards"][name].extend(safe_gather_object(reward_values, max_str_len=None))
        total_reward_values = rewards.tolist()
        self._logs["rewards"]["total"].extend(safe_gather_object(total_reward_values, max_str_len=None))
        advantage_values = all_process_advantages.tolist()
        self._logs["advantages"].extend(safe_gather_object(advantage_values, max_str_len=None))
        # Also log mean rewards for each group (for better understanding of advantages)
        if "mean_reward" not in self._logs:
            self._logs["mean_reward"] = deque(maxlen=self.args.generation_batch_size)
        self._logs["mean_reward"].extend(mean_grouped_rewards.tolist())

        if images is not None:
            # Don't gather images as they can be very large; keep local only
            self._logs["images"].extend(images)

        # Optional: construct token_weights_tensor from token_weights_list that flows with samples
        # Apply the same normalization/masking/clipping as in the loss, so logs reflect effective weights.
        token_weights_tensor = None
        try:
            if getattr(self.args, "token_weights", False) and token_weights_list is not None:
                T = completion_ids.size(1)
                tw_tensors = []
                for w in token_weights_list:
                    w = w or []
                    t = torch.ones(T, dtype=torch.float32, device=device)
                    n = min(len(w), T)
                    if n > 0:
                        t[:n] = torch.tensor(w[:n], dtype=torch.float32, device=device)
                    tw_tensors.append(t)
                token_weights_tensor = torch.stack(tw_tensors, dim=0)
                token_weights_tensor = self._postprocess_token_weights(token_weights_tensor, completion_ids)
        except Exception:
            token_weights_tensor = None

        output = {
            "prompt_ids": prompt_ids,
            "prompt_mask": prompt_mask,
            "completion_ids": completion_ids,
            "completion_mask": completion_mask,
            "advantages": advantages,
            "num_items_in_batch": num_items_in_batch,
            # Save original data for re-encoding in compute_loss
            "original_prompts": [deepcopy(p) for p in prompts],
        }
        if images is not None:
            output["original_images"] = deepcopy(images)
        if old_per_token_logps is not None:
            output["old_per_token_logps"] = old_per_token_logps
        if ref_per_token_logps is not None:
            output["ref_per_token_logps"] = ref_per_token_logps
        # Note: pixel_values, image_grid_thw, num_images, etc. will be regenerated in compute_loss
        # based on original_prompts and original_images, so we don't copy them here
        if token_weights_tensor is not None:
            output["token_weights"] = token_weights_tensor

        # Emit rollout logs if enabled (moved to logging utils).
        # For per-rank logging we use the full local batch slice.
        process_slice = slice(0, rewards_per_func.size(0))
        perform_realtime_rollout_logging(
            is_main_process=self.accelerator.is_main_process,
            mode=mode,
            args=self.args,
            state_step=self.state.global_step,
            state_epoch=self.state.epoch,
            compute_attention_metrics=self.compute_attention_metrics,
            attention_logs=self._logs.get("attention") if hasattr(self, "_logs") else None,
            attention_skip_reasons=getattr(self, "_attention_skip_reasons", None),
            processing_class=self.processing_class,
            prompts=prompts,
            inputs=inputs,
            prompts_text=prompts_text,
            completions_text=completions_text,
            rewards_per_func_local=rewards_per_func,
            total_rewards_local=rewards,
            reward_names=self.reward_func_names,
            advantages_tensor=advantages,
            token_weights_tensor=token_weights_tensor,
            completion_ids=completion_ids,
            completion_mask=completion_mask,
            process_slice=process_slice,
        )

        return output

    def _postprocess_token_weights(
        self,
        w: torch.Tensor,
        completion_ids: Optional[torch.Tensor],
    ) -> torch.Tensor:
        """
        Apply per-sequence normalization, formatting tag reweighting, hard/soft stopword
        handling, and per-sequence upper-quantile clipping to token weights.

        This is used both for logging (token_weights.md) and for training.
        """
        try:
            if w is None:
                return w

            # Per-sequence normalization to keep mean scale ~1
            if w.dim() == 2 and w.size(0) > 0:
                row_mean = w.mean(dim=1, keepdim=True).clamp_min(1e-6)
                w = w / row_mean

            tokenizer = getattr(self.processing_class, "tokenizer", self.processing_class)

            # Formatting tags (<think>, </think>, <answer>, </answer>, <|im_end|>, etc.)
            try:
                tag_token_ids = getattr(self, "_tag_token_ids", None)
                if tag_token_ids is None:
                    tag_strs = ["<", ">", "</", "<think", "</think", "<answer", "</answer", "<|im_end|>"]
                    tag_token_ids = set()
                    for s in tag_strs:
                        try:
                            encoded = tokenizer(s, add_special_tokens=False)
                            input_ids = encoded["input_ids"] if isinstance(encoded, dict) else encoded.input_ids
                            for tid in input_ids:
                                tag_token_ids.add(int(tid))
                        except Exception:
                            continue
                    self._tag_token_ids = tag_token_ids
                if tag_token_ids and completion_ids is not None:
                    tag_mask = torch.zeros_like(completion_ids, dtype=torch.bool, device=completion_ids.device)
                    for tid in tag_token_ids:
                        tag_mask |= completion_ids == tid
                    tag_weight = float(getattr(self.args, "format_tag_weight", 1.5))
                    w = torch.where(tag_mask.to(w.device), torch.full_like(w, tag_weight), w)
            except Exception:
                pass

            # Hard stopwords: force w -> 1.0
            try:
                if completion_ids is not None:
                    hard_stop_token_ids = getattr(self, "_hard_stop_token_ids", None)
                    if hard_stop_token_ids is None:
                        hard_stop_strs = [
                            "a", "A", "an", "the", "The",
                            "and", "of", "in", "on", "or",
                            "to", "be", "is", "are", "it",
                            ",", ".", "?", "!", ";", ":", "\"", "'", "'s",
                            "(", ")", "-",
                        ]
                        hard_stop_token_ids = set()
                        for s in hard_stop_strs:
                            for variant in (s, f" {s}"):
                                try:
                                    enc = tokenizer(variant, add_special_tokens=False)
                                    ids = enc["input_ids"] if isinstance(enc, dict) else enc.input_ids
                                    for tid in ids:
                                        hard_stop_token_ids.add(int(tid))
                                except Exception:
                                    continue
                        self._hard_stop_token_ids = hard_stop_token_ids

                    if hard_stop_token_ids:
                        hard_mask = torch.zeros_like(completion_ids, dtype=torch.bool, device=completion_ids.device)
                        for tid in hard_stop_token_ids:
                            hard_mask |= completion_ids == tid
                        if hard_mask.any():
                            w = torch.where(hard_mask.to(w.device), torch.ones_like(w), w)
            except Exception:
                pass

            # Soft stopwords: attenuate amplification (w>1), keep w >= 1.0
            try:
                if completion_ids is not None:
                    soft_stop_token_ids = getattr(self, "_soft_stop_token_ids", None)
                    if soft_stop_token_ids is None:
                        soft_stop_strs = [
                            "with", "by", "including", "from", "at",
                            "into", "between", "within",
                            "as", "have", "has", "being",
                            "some", "many", "all", "both", "each",
                            "over", "under", "where", "while", "during",
                            "more", "less", "out", "its", "their",
                        ]
                        soft_stop_token_ids = set()
                        for s in soft_stop_strs:
                            for variant in (s, f" {s}"):
                                try:
                                    enc = tokenizer(variant, add_special_tokens=False)
                                    ids = enc["input_ids"] if isinstance(enc, dict) else enc.input_ids
                                    for tid in ids:
                                        soft_stop_token_ids.add(int(tid))
                                except Exception:
                                    continue
                        self._soft_stop_token_ids = soft_stop_token_ids

                    if soft_stop_token_ids:
                        soft_mask = torch.zeros_like(completion_ids, dtype=torch.bool, device=completion_ids.device)
                        for tid in soft_stop_token_ids:
                            soft_mask |= completion_ids == tid
                        if soft_mask.any():
                            alpha = 0.3
                            w_soft = 1.0 + alpha * torch.relu(w - 1.0)
                            w = torch.where(soft_mask.to(w.device), w_soft, w)
            except Exception:
                pass

            # Upper-quantile clipping per sequence
            try:
                if w.dim() == 2 and w.size(0) > 0:
                    q = torch.quantile(
                        w,
                        float(getattr(self.args, "token_weight_quantile", 0.95)),
                        dim=1,
                        keepdim=True,
                    )
                    w = torch.minimum(w, q)
            except Exception:
                pass

        except Exception:
            return w

        return w

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
        # If multimodal data exists, re-encode to ensure consistency
        if "original_images" in inputs and inputs["original_images"] is not None:
            original_prompts = inputs["original_prompts"]
            original_images = inputs["original_images"]
            
            # Re-encode prompts and images (matching logic from _generate_and_score_completions line 2068-2079)
            from trl.data_utils import apply_chat_template
            prompts_text = [
                apply_chat_template({"prompt": prompt}, self.processing_class)["prompt"] 
                for prompt in original_prompts
            ]
            mm_inputs = self.processing_class(
                images=original_images, 
                text=prompts_text, 
                padding=True, 
                return_tensors="pt"
            )
            # Use super()._prepare_inputs to ensure correct device and precision
            mm_inputs = super(DAPOTrainer, self)._prepare_inputs(mm_inputs)
            
            # Update multimodal fields in inputs (only update encoding-related fields, preserve other fields)
            for k in ["pixel_values", "image_grid_thw", "pixel_attention_mask", "image_sizes", "token_type_ids"]:
                if k in mm_inputs:
                    inputs[k] = mm_inputs[k]
            
            # Calculate num_images on the fly (no need to maintain in dynamic sampling)
            inputs["num_images"] = [len(img_list) for img_list in original_images]
        
        # Compute the per-token log probabilities for the model
        prompt_ids, prompt_mask = inputs["prompt_ids"], inputs["prompt_mask"]
        completion_ids, completion_mask = inputs["completion_ids"], inputs["completion_mask"]
        input_ids = torch.cat([prompt_ids, completion_ids], dim=1)
        attention_mask = torch.cat([prompt_mask, completion_mask], dim=1)
        logits_to_keep = completion_ids.size(1)  # we only need to compute the logits for the completion tokens

        # Expect non-empty batch with valid completion tokens at this point

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

        # Two-sided clipping (upper bound on r)
        if self.args.delta is not None:
            coef_1 = torch.clamp(coef_1, max=self.args.delta)

        # Token-weighted advantage guardrails (optional)
        adv_matrix = advantages.unsqueeze(1)
        if getattr(self.args, "token_weights", False) and ("token_weights" in inputs) and (inputs["token_weights"] is not None):
            try:
                w = inputs["token_weights"].to(coef_1.device)
                # Scale negative-advantage sequences
                pos = (advantages > 0).float().unsqueeze(1)
                neg = 1.0 - pos
                scale = pos + neg * float(getattr(self.args, "neg_adv_token_scale", 0.5))
                adv_matrix = advantages.unsqueeze(1) * w * scale
            except Exception:
                adv_matrix = advantages.unsqueeze(1)

        # VERL-style asymmetric clip (low/high) + dual-clip lower bound c for A<0
        per_token_ratio = coef_1
        pg_losses1 = -adv_matrix * per_token_ratio
        pg_losses2 = -adv_matrix * coef_2
        clip_pg_losses1 = torch.maximum(pg_losses1, pg_losses2)

        c = float(getattr(self.args, "clip_ratio_c", 3.0) or 3.0)
        if c <= 1.0:
            c = 1.0001
        pg_losses3 = -adv_matrix * c
        per_token_loss = torch.where(adv_matrix < 0, torch.min(pg_losses3, clip_pg_losses1), clip_pg_losses1)
        # For metrics: which tokens got clipped by high/low and by dual-clip lower bound
        with torch.no_grad():
            try:
                pg_clipfrac = (pg_losses2 > pg_losses1).float()
                pg_clipfrac_lower = (clip_pg_losses1 > pg_losses3).float() * (adv_matrix < 0).float()
            except Exception:
                pg_clipfrac = None
                pg_clipfrac_lower = None
        if entropy_mask is not None:
            per_token_loss = per_token_loss * entropy_mask

        # Lightweight KL schedule
        beta_eff = float(self.beta)
        if getattr(self.args, "kl_beta_schedule", "off") == "linear10" and (self.state.max_steps or 0) > 0:
            warm = max(1, int(0.1 * self.state.max_steps))
            t = min(1.0, self.state.global_step / warm)
            beta_eff = float((1.0 - t) * 0.02)
        self._beta_eff = beta_eff
        if beta_eff != 0.0 and self.beta != 0.0:
            per_token_loss = per_token_loss + beta_eff * per_token_kl

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
            loss = loss / self.current_gradient_accumulation_steps
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

        # Compute clipping indicators for reporting
        is_low_clipped = (per_token_ratio < 1 - self.epsilon_low) & (advantages.unsqueeze(1) < 0)
        is_high_clipped = (per_token_ratio > 1 + self.epsilon_high) & (advantages.unsqueeze(1) > 0)
        is_region_clipped = is_low_clipped | is_high_clipped

        low_clip = masked_batch_mean(is_low_clipped.float())
        high_clip = masked_batch_mean(is_high_clipped.float())
        clip_region = masked_batch_mean(is_region_clipped.float())

        gathered_low_clip = self.accelerator.gather(low_clip)
        self._metrics[mode]["clip_ratio/low_mean"].append(gathered_low_clip.nanmean().item())
        self._metrics[mode]["clip_ratio/low_min"].append(nanmin(gathered_low_clip).item())
        gathered_high_clip = self.accelerator.gather(high_clip)
        self._metrics[mode]["clip_ratio/high_mean"].append(gathered_high_clip.nanmean().item())
        self._metrics[mode]["clip_ratio/high_max"].append(nanmax(gathered_high_clip).item())
        gathered_clip_region = self.accelerator.gather(clip_region)
        self._metrics[mode]["clip_ratio/region_mean"].append(gathered_clip_region.nanmean().item())

        # pg_clipfrac metrics
        if 'pg_clipfrac' not in self._metrics[mode]:
            self._metrics[mode]["pg_clipfrac"] = []
        if 'pg_clipfrac_lower' not in self._metrics[mode]:
            self._metrics[mode]["pg_clipfrac_lower"] = []
        if pg_clipfrac is not None:
            try:
                val = (pg_clipfrac * completion_mask).sum() / completion_mask.sum().clamp(min=1.0)
                self._metrics[mode]["pg_clipfrac"].append(self.accelerator.gather(val).nanmean().item())
            except Exception:
                pass
        if pg_clipfrac_lower is not None:
            try:
                val = (pg_clipfrac_lower * completion_mask).sum() / completion_mask.sum().clamp(min=1.0)
                self._metrics[mode]["pg_clipfrac_lower"].append(self.accelerator.gather(val).nanmean().item())
            except Exception:
                pass

        self._metrics[mode]["kl_beta_eff"].append(self._beta_eff)
        self._metrics[mode]["kl/beta_eff"].append(self._beta_eff)
        return loss

    def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys: Optional[list[str]] = None):
        inputs = self._prepare_inputs(inputs)
        # For DeepSpeed ZeRO-3, we need to gather parameters during evaluation
        # Use the same ds3_gather_for_generation setting as in generation
        gather_params = self.args.ds3_gather_for_generation if self.is_deepspeed_enabled else False
        with (
            torch.no_grad(),
            unwrap_model_for_generation(
                self.model_wrapped, self.accelerator, gather_deepspeed3_params=gather_params
            ) if gather_params else nullcontext(),
        ):
            with self.compute_loss_context_manager():
                loss = self.compute_loss(model, inputs)
            loss = loss.mean().detach()
        return loss, None, None

    def log(self, logs: dict[str, float], start_time: Optional[float] = None) -> None:
        mode = "train" if self.model.training else "eval"
        metrics = {key: sum(val) / len(val) for key, val in self._metrics[mode].items()}  # average the metrics

        # This method can be called both in training and evaluation. When called in evaluation, the keys in `logs`
        # start with "eval_". We need to add the prefix "eval_" to the keys in `metrics` to match the format.
        if mode == "eval":
            metrics = {f"eval_{key}": val for key, val in metrics.items()}

        logs = {**logs, **metrics}

        # Pretty print compact grouped logs to terminal (moved to logging utils)
        if self.accelerator.is_main_process:
            try:
                # First output DynSample log if available (before Rewards/Optim)
                if hasattr(self, '_pending_dynsample_log') and self._pending_dynsample_log is not None:
                    print(self._pending_dynsample_log)
                    self._pending_dynsample_log = None  # Clear after output
                    import sys
                    sys.stdout.flush()  # Ensure DynSample is printed before Rewards/Optim
                
                print_compact_logs(logs, mode, use_hard_negative=getattr(self.args, "vgr_hard_negative", False))
                # Emit evaluation markdown logs: moved to logging utils
                perform_eval_logging(
                    is_main_process=self.accelerator.is_main_process,
                    mode=mode,
                    args=self.args,
                    state_step=self.state.global_step,
                    state_epoch=self.state.epoch,
                    metrics=metrics,
                    logs=logs,
                    internal_logs=self._logs,
                    reward_names=self.reward_func_names,
                )
            except Exception:
                pass

        super().log(logs, start_time)
        self._metrics[mode].clear()


    # Ensure the model card is saved along with the checkpoint
    def _save_checkpoint(self, model, trial):
        if self.args.hub_model_id is None:
            model_name = Path(self.args.output_dir).name
        else:
            model_name = self.args.hub_model_id.split("/")[-1]
        self.create_model_card(model_name=model_name)
        super()._save_checkpoint(model, trial)

    def _unwrap_model_for_config(self, model=None):
        """Return the base unwrapped model for config access."""
        if model is None:
            model = self.model
        return unwrap_model_for_generation(model, self.accelerator)

    @contextmanager
    def _attn_last_k_layers_only(self, model: nn.Module, last_k_layers: Optional[int] = None):
        """
        Temporarily limit returned attentions to the last-K decoder layers by wrapping layer/attention forwards.
        Does not alter computations; only prevents returning/storing attention weights for earlier layers.
        """
        if not self.compute_attention_metrics or not last_k_layers or last_k_layers <= 0:
            yield
            return

        def _get_attr(obj, path: str):
            cur = obj
            for p in path.split('.'):
                if not hasattr(cur, p):
                    return None
                cur = getattr(cur, p)
            return cur

        # Candidate decoder layer paths
        candidates = [
            "language_model.model.layers",
            "model.layers",
            "model.decoder.layers",
            "gpt_neox.layers",
            "transformer.h",
        ]
        layers = None
        for cand in candidates:
            lst = _get_attr(model, cand)
            if lst is not None and hasattr(lst, "__len__") and len(lst) > 0:
                layers = lst
                break
        if layers is None:
            for _, module in model.named_modules():
                if isinstance(module, torch.nn.ModuleList) and len(module) > 0:
                    # Heuristic: treat as decoder layers only if majority of items look like decoder blocks
                    hits = 0
                    total = len(module)
                    for item in module:
                        for nm in ["self_attn", "attn", "attention", "mha", "self_attention"]:
                            if hasattr(item, nm):
                                hits += 1
                                break
                    if hits >= max(1, total // 2):
                        layers = module
                        break

        if layers is None or len(layers) == 0:
            yield
            return

        num_layers = len(layers)
        keep = max(1, min(int(last_k_layers), num_layers))
        keep_indices = set(range(num_layers - keep, num_layers))

        attn_attr_names = ["self_attn", "attn", "attention", "mha", "self_attention"]
        patched = []

        try:
            for idx, layer in enumerate(layers):
                keep_flag = idx in keep_indices

                # Patch attention submodule forward if present
                for name in attn_attr_names:
                    if hasattr(layer, name):
                        attn_mod = getattr(layer, name)
                        if hasattr(attn_mod, "forward"):
                            orig = attn_mod.forward
                            def make_attn_wrapper(ofn, kf):
                                def _wrapped(*args, **kwargs):
                                    if not kf and "output_attentions" in kwargs:
                                        kwargs = dict(kwargs)
                                        kwargs["output_attentions"] = False
                                    return ofn(*args, **kwargs)
                                return _wrapped
                            attn_mod.forward = make_attn_wrapper(orig, keep_flag)
                            patched.append((attn_mod, "forward", orig))
                        break

                # Also patch layer forward (force per-layer output_attentions=False for early layers)
                if hasattr(layer, "forward"):
                    orig_layer = layer.forward
                    def make_layer_wrapper(ofn, kf):
                        def _wrapped(*args, **kwargs):
                            if not kf and "output_attentions" in kwargs:
                                kwargs = dict(kwargs)
                                kwargs["output_attentions"] = False
                            return ofn(*args, **kwargs)
                        return _wrapped
                    layer.forward = make_layer_wrapper(orig_layer, keep_flag)
                    patched.append((layer, "forward", orig_layer))

            yield
        finally:
            for mod, attr, orig in patched:
                try:
                    setattr(mod, attr, orig)
                except Exception:
                    pass

    # Attention metrics processing moved to utils (no AEI, only last-K aggregation)
    def _process_attention_metrics(self, attention_context: Optional[dict], mode: str) -> Optional[list]:
        """Process attention metrics and return token weights list for current batch.
        
        Returns:
            Optional[list]: Token weights list for the current batch if token_weights is enabled, None otherwise.
        """
        if not self.compute_attention_metrics or attention_context is None:
            return None
        tw_list = process_attention_context(
            attention_context=attention_context,
            model=self.model,
            processor=self.processing_class,
            args=self.args,
            attention_deque=self._logs.get("attention") if hasattr(self, "_logs") else None,
            attention_skip_reasons_deque=getattr(self, "_attention_skip_reasons", None),
            token_weights_deque=None, 
        )
        return tw_list

    def _reset_internal_logs(self, force_eval_mode: bool = False) -> None:
        """
        Reset internal logging buffers used to assemble rollout/eval samples.
        This is called at init time and when switching into evaluation to avoid
        mixing train and eval samples inside the same deques.
        
        Args:
            force_eval_mode: If True, use eval-sized buffers regardless of model.training state.
                            This is useful when entering eval mode before model.eval() is called.
        """
        # Keep logs sized to the generation batch to record only outputs from the latest model update.
        gbatch = self.args.generation_batch_size
        
        # For eval, use a larger buffer to accommodate multiple eval batches without data loss.
        # For train, use standard generation_batch_size to only keep the latest rollout.
        is_eval_mode = force_eval_mode or (hasattr(self, "model") and not self.model.training)
        if is_eval_mode:
            # Use a large buffer for eval to avoid losing samples across multiple batches
            log_size = max(gbatch * 20, 1000)  # At least 1000 samples
        else:
            log_size = gbatch
        
        # Fix defaultdict lambda to properly capture log_size
        def make_reward_deque():
            return deque(maxlen=log_size)
        
        self._logs = {
            "images": deque(maxlen=log_size),
            "prompt": deque(maxlen=log_size),
            "completion": deque(maxlen=log_size),
            "prompt_chatml": deque(maxlen=log_size),
            "rewards": defaultdict(make_reward_deque),
            "advantages": deque(maxlen=log_size),
        }
        # Initialize attention tracking deques
        if getattr(self, "compute_attention_metrics", False):
            self._logs["attention"] = deque(maxlen=2000)  # Increased for eval
            self._attention_skip_reasons = deque(maxlen=2000)
        # Initialize token weights tracking (optional)
        if getattr(self.args, "token_weights", False):
            self._logs["token_weights"] = deque(maxlen=2000)

    def evaluate(self, *args, **kwargs):
        """
        Run evaluation with a fresh set of internal logs so that eval markdown
        logs and attention-based metrics are computed only from eval batches.
        
        This method clears internal logs before and after eval to prevent:
        1. Train data contaminating eval logs (before eval)
        2. Eval data contaminating next train batch rewards (after eval)
        """
        # Clear train history before eval to avoid mixing train/eval samples.
        # Use force_eval_mode=True since model.eval() may not be called yet.
        self._reset_internal_logs(force_eval_mode=True)
        
        try:
            result = super().evaluate(*args, **kwargs)
        finally:
            self._reset_internal_logs(force_eval_mode=False)
        
        return result

    def predict(self, *args, **kwargs):
        """
        Run prediction with a fresh set of internal logs, mirroring evaluate().
        """
        self._reset_internal_logs(force_eval_mode=True)
        
        try:
            result = super().predict(*args, **kwargs)
        finally:
            self._reset_internal_logs(force_eval_mode=False)
        
        return result
