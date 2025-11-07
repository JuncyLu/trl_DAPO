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

import heapq
import inspect
import math
import os
import textwrap
import warnings
from collections import defaultdict, deque
from contextlib import nullcontext
from functools import partial
from pathlib import Path
from typing import Any, Callable, List, Optional, Union

import datasets
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
from transformers.utils import is_datasets_available, is_peft_available, is_rich_available

from trl.data_utils import (
    apply_chat_template,
    is_conversational,
    prepare_multimodal_messages,
    prepare_multimodal_messages_vllm,
)
from trl.extras.profiling import profiling_context, profiling_decorator
from trl.extras.vllm_client import VLLMClient
from trl.import_utils import is_liger_kernel_available, is_vllm_available
from trl.models import prepare_deepspeed, prepare_fsdp, prepare_peft_model, unwrap_model_for_generation
from trl.models.utils import _ForwardRedirection
from trl.trainer.base_trainer import BaseTrainer
from trl.trainer.callbacks import SyncRefModelCallback
from .dapo_config import DAPOConfig
from ..rewards.reward_utils import create_reward_weight_manager, calculate_reward_metrics
from ..utils.attention_metrics import (
    compute_qwen_attention_metrics_for_batch,
    AttentionSampleResult,
)
from ..utils import build_token_vgr_weights_for_batch
from ..rewards.accuracy_rewards import accuracy_reward
from ..utils.dapo_logging import emit_rollout_logs, emit_eval_logs, compute_real_vgr_metrics
from contextlib import contextmanager
from trl.trainer.utils import (
    RepeatSampler,
    disable_dropout_in_model,
    ensure_master_addr_port,
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

if is_vllm_available():
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import GuidedDecodingParams

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
                use_fast=False  # 强制使用 slow processor，避免图像 token 计算不一致
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
            reward_func_names=self.reward_func_names
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

        # --- Dynamic sampling replay buffer (optional; no-op when size==0) ---
        class _ReplayBuffer:
            def __init__(self, max_size: int):
                self.max_size = max_size
                self.heap = []  # min-heap of (score, data)

            def add(self, scores: list[float], data: list[dict]):
                for score, datum in zip(scores, data):
                    # Use id as unique identifier to avoid tensor comparison issues
                    if len(self.heap) < self.max_size:
                        heapq.heappush(self.heap, (float(score), id(datum), datum))
                    else:
                        if float(score) > float(self.heap[0][0]):
                            heapq.heapreplace(self.heap, (float(score), id(datum), datum))

            def sample(self, num_samples: int) -> list[dict]:
                if not self.heap:
                    return None
                scores = torch.tensor([item[0] for item in self.heap], dtype=torch.float32)
                probs = scores / scores.sum().clamp(min=1e-8)
                replacement = num_samples > len(self.heap)
                idxs = torch.multinomial(probs, num_samples, replacement=replacement).tolist()
                return [self.heap[i][2] for i in idxs]  # datum is the 3rd element

        self.replay_buffer = None
        if getattr(args, "replay_buffer_size", 0) and args.replay_buffer_size > 0:
            self.replay_buffer = _ReplayBuffer(args.replay_buffer_size)

        # Initialize the metrics
        self._metrics = {"train": defaultdict(list), "eval": defaultdict(list)}
        self._total_train_tokens = 0
        self.log_completions = args.log_completions
        self.wandb_log_unique_prompts = args.wandb_log_unique_prompts
        self.num_completions_to_print = args.num_completions_to_print
        # Evaluation can use a different number of generations per sample
        self.eval_num_generations = getattr(args, "eval_num_generations", 2) or 2
        # Keep logs sized to the generation batch to record only outputs from the latest model update.
        self._logs = {
            "images": deque(maxlen=args.generation_batch_size),
            "prompt": deque(maxlen=args.generation_batch_size),
            "completion": deque(maxlen=args.generation_batch_size),
            "prompt_chatml": deque(maxlen=args.generation_batch_size),
            "rewards": defaultdict(lambda: deque(maxlen=args.generation_batch_size)),
            "advantages": deque(maxlen=args.generation_batch_size),
        }

        # Initialize attention tracking
        self.compute_attention_metrics = args.compute_attention_metrics
        if self.compute_attention_metrics:
            self._logs["attention"] = deque(maxlen=1000)
            self._attention_skip_reasons = deque(maxlen=1000)
        # Initialize token weights tracking (optional)
        if getattr(args, "token_weights", False):
            self._logs["token_weights"] = deque(maxlen=1000)

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
                    self.llm.sleep(level=2)
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
            mini_repeat_count=self.eval_num_generations,
            seed=self.args.seed,
        )

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

        # Add num_generations for group-wise reward calculation
        reward_kwargs["num_generations"] = self.num_generations if self.model.training else self.eval_num_generations

        # Add attention data for reward functions if available
        if self.compute_attention_metrics and hasattr(self, '_logs') and 'attention' in self._logs:
            att_list = list(self._logs['attention'])
            
            if att_list:
                # Get the most recent attention results for this batch
                sample_results = att_list[-len(prompts):]
                
                # Align skip reasons with the same recent slice
                if hasattr(self, '_attention_skip_reasons'):
                    skips = list(self._attention_skip_reasons)
                    skip_slice = skips[-len(sample_results):] if len(skips) >= len(sample_results) else [None] * len(sample_results)
                else:
                    skip_slice = [None] * len(sample_results)
                    
                vgr_metrics = compute_real_vgr_metrics(sample_results, skip_slice)
                
                # Extract attention data for reward functions
                # Use raw attention values (attention_text/attention_vision) not AEI values
                reward_kwargs["attention_text"] = [m.get("attention_text", 0.0) for m in vgr_metrics]
                reward_kwargs["attention_vision"] = [m.get("attention_vision", 0.0) for m in vgr_metrics]
                reward_kwargs["num_text_tokens"] = [m.get("num_text_tokens", 0) for m in vgr_metrics]
                reward_kwargs["num_vision_tokens"] = [m.get("num_vision_tokens", 0) for m in vgr_metrics]

        # 计算逐样本准确率，并传递给奖励函数（供 vgr_accuracy_reward 使用）
        try:
            solutions_for_batch = reward_kwargs.get("solution", None)
            if solutions_for_batch is None:
                # 有些数据集中可能使用 "solutions" 作为字段名
                solutions_for_batch = reward_kwargs.get("solutions", None)

            if solutions_for_batch is not None:
                acc_scores = accuracy_reward(
                    completions=completions,
                    solution=solutions_for_batch,
                )
                # 将 None 安全转为 0.0
                reward_kwargs["accuracies"] = [float(x) if x is not None else 0.0 for x in acc_scores]
        except Exception:
            # 若准确率计算失败，则跳过传递（保持兼容）
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

        # Gather the reward per function: this part is crucial, because the rewards are normalized per group and the
        # completions may be distributed across processes
        rewards_per_func = gather(rewards_per_func)
        return rewards_per_func

    def _generate_single_turn(self, prompts: list, images: Optional[list] = None):
        device = self.accelerator.device
        # Use eval-specific generations when not training
        ng = self.num_generations if self.model.training else self.eval_num_generations

        # Generate completions using either vLLM or regular generation
        if self.use_vllm:
            if self.vllm_mode == "colocate" and self.args.vllm_enable_sleep_mode:
                # wake up colocated vLLM instances if needed
                torch.cuda.empty_cache()  # required to avoid OOM in some cases
                self.llm.wake_up(tags=["weights"])

            # First, update the vLLM weights if needed
            if self.state.global_step != self._last_loaded_step:
                self._move_model_to_vllm()
                self._last_loaded_step = self.state.global_step

            if is_conversational({"prompt": prompts[0]}):
                prompts = [prepare_multimodal_messages_vllm(prompt) for prompt in prompts]

            # Generate completions using vLLM: gather all prompts and use them in a single call in the main process
            if self.vllm_mode == "server":
                # Ensure grouping alignment when requesting n>1 generations per unique prompt
                if ng > 1 and len(prompts) % ng != 0:
                    prompts = prompts[: len(prompts) - (len(prompts) % ng)]
                all_prompts = gather_object(prompts)

                if self.accelerator.is_main_process:
                    # Since 'prompts' contains 'num_generations' duplicates, we first take unique prompts, and generate
                    # num_generations outputs for each one. This is faster than generating outputs for each duplicate
                    # prompt individually.
                    # Drop any trailing incomplete group to keep alignment across processes
                    total = len(all_prompts)
                    num_unique = total // ng if ng > 0 else total
                    ordered_set_of_prompts = [all_prompts[i * ng] for i in range(num_unique)]

                    sampling_params = {
                        "n": ng,
                        "repetition_penalty": self.repetition_penalty,
                        "temperature": self.temperature,
                        "top_p": self.top_p,
                        "top_k": -1 if self.top_k is None else self.top_k,
                        "min_p": 0.0 if self.min_p is None else self.min_p,
                        "max_tokens": self.max_completion_length,
                        "truncate_prompt_tokens": self.max_prompt_length,
                        "guided_decoding_regex": self.guided_decoding_regex,
                        "generation_kwargs": self.args.generation_kwargs,
                    }
                    with profiling_context(self, "vLLM.generate"):
                        if self.rollout_func is not None:
                            if is_conversational({"prompt": ordered_set_of_prompts[0]}):
                                ordered_set_of_prompts = [
                                    apply_chat_template({"prompt": p}, self.processing_class)["prompt"]
                                    for p in ordered_set_of_prompts
                                ]
                            output = self.rollout_func(
                                ordered_set_of_prompts,
                                self.args,
                                self.processing_class,
                            )
                        else:
                            if is_conversational({"prompt": ordered_set_of_prompts[0]}):
                                # FIXME: this endpoint doesn't exist in vllm_client
                                output = self.vllm_client.chat(prompts=ordered_set_of_prompts, **sampling_params)
                            else:
                                output = self.vllm_client.generate(prompts=ordered_set_of_prompts, **sampling_params)
                        # Extract required fields and collect any extra fields for reward functions
                        required_keys = {"prompt_ids", "completion_ids", "logprobs"}
                        extra_fields = {k: v for k, v in output.items() if k not in required_keys}
                        payload = (output["prompt_ids"], output["completion_ids"], output["logprobs"], extra_fields)
                else:
                    payload = None

                # Broadcast the completions from the main process to all processes, ensuring each process receives its corresponding slice.
                obj_list = [payload]
                broadcast_object_list(obj_list, from_process=0)
                all_prompt_ids, all_completion_ids, all_logprobs, all_extra_fields = obj_list[0]

                # At this point, we only get 1 copy of each prompt, so we need to repeat them ng times
                all_prompt_ids = [ids for ids in all_prompt_ids for _ in range(ng)]

                process_slice = slice(
                    self.accelerator.process_index * len(prompts),
                    (self.accelerator.process_index + 1) * len(prompts),
                )
                prompt_ids = all_prompt_ids[process_slice]
                completion_ids = all_completion_ids[process_slice]
                logprobs = all_logprobs[process_slice]

                # Slice extra fields dict-of-lists per process (extra fields are per-completion, like completion_ids)
                extra_fields = {}
                for key, values in all_extra_fields.items():
                    if isinstance(values, list):
                        extra_fields[key] = values[process_slice]
                    else:
                        extra_fields[key] = values
                attention_context = None  # vLLM server doesn't support attention output

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
                    orig_size = len(prompts)
                    gathered_prompts = [None for _ in range(self.vllm_tensor_parallel_size)]
                    torch.distributed.all_gather_object(gathered_prompts, prompts, group=self.tp_group)
                    all_prompts = [p for sublist in gathered_prompts for p in sublist]
                else:
                    all_prompts = prompts

                if self.args.vllm_enable_sleep_mode:
                    self.llm.wake_up(tags=["kv_cache"])

                with profiling_context(self, "vLLM.generate"):
                    if is_conversational({"prompt": prompts[0]}):
                        all_outputs = self.llm.chat(all_prompts, sampling_params=sampling_params, use_tqdm=False)
                    else:
                        all_outputs = self.llm.generate(all_prompts, sampling_params=sampling_params, use_tqdm=False)

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

                extra_fields = {}  # No extra fields for colocate mode
                attention_context = None  # vLLM doesn't support attention output

                if self.args.vllm_enable_sleep_mode:
                    self.llm.sleep(level=2)

        elif self.use_transformers_paged:
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

        # Process attention metrics if available
        if attention_context is not None:
            self._process_attention_metrics(attention_context, mode)

        return prompt_ids, completion_ids, total_completion_tokens, logprobs, extra_fields

    def _generate_and_score_completions(
        self, inputs: list[dict[str, Union[torch.Tensor, Any]]]
    ) -> dict[str, Union[torch.Tensor, Any]]:
        device = self.accelerator.device
        mode = "train" if self.model.training else "eval"
        # Preferred generations per prompt for current mode
        preferred_num_generations = self.num_generations if mode == "train" else self.eval_num_generations
        
        # 更新分段权重（仅在训练模式下）
        if mode == "train":
            weight_metrics = self.reward_weight_manager.update_weights(
                self.state.global_step, 
                self.args.max_steps if self.args.max_steps > 0 else self.state.max_steps
            )
            # 将权重指标添加到metrics中
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

        # If the prompts are conversational and the inputs contain images, we need to convert the prompts from
        # [{"role": "user", "content": "What color is the sky?"}] to
        # [{"role": "user", "content": [{"type": "image", "image": <Image>}, {"type": "text", "text": "What color is the sky?"}]}]
        if images is not None:
            prompts = [prepare_multimodal_messages(prompt, image_list) for prompt, image_list in zip(prompts, images)]
        
        prompt_ids_list, completion_ids_list, num_items_in_batch, sampling_per_token_logps_list, extra_fields = (
            self._generate(prompts, images)
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

        # Calculate rewards for each reward function. rewards_per_func aggregates rewards across all processes. This is
        # important because rewards will be normalized per group, and completions are distributed. We will later slice
        # rewards_per_func to extract each process's subset.
        rewards_per_func = self._calculate_rewards(inputs, prompts, completions, completion_ids_list)

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
            std_rewards = rewards.view(-1, group_ng).std(dim=1)
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

        # Removed detailed per-step rollout file writing to avoid heavy I/O and potential blocking.

        # Slice to keep only the local part of the data
        process_slice = slice(
            self.accelerator.process_index * len(prompts),
            (self.accelerator.process_index + 1) * len(prompts),
        )
        all_process_advantages = advantages.clone()  # keep the aggregated advantages for logging
        advantages = advantages[process_slice]

        # Calculate reward metrics using utility function
        reward_metrics = calculate_reward_metrics(rewards_per_func, self.reward_func_names, device)
        for key, value in reward_metrics.items():
            self._metrics[mode][key].append(value)
        self._metrics[mode]["reward"].append(mean_grouped_rewards.mean().item())
        self._metrics[mode]["reward_std"].append(std_rewards.mean().item())
        self._metrics[mode]["frac_reward_zero_std"].append(is_std_zero.float().mean().item())

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
        self._logs["prompt"].extend(gather_object(prompts_text))
        self._logs["completion"].extend(gather_object(completions_text))
        self._logs["prompt_chatml"].extend(gather_object(rendered_prompts))
        for i, name in enumerate(self.reward_func_names):
            self._logs["rewards"][name].extend(rewards_per_func[:, i].tolist())
        self._logs["rewards"]["total"].extend(rewards.tolist())
        self._logs["advantages"].extend(all_process_advantages.tolist())
        # Also log mean rewards for each group (for better understanding of advantages)
        if "mean_reward" not in self._logs:
            self._logs["mean_reward"] = deque(maxlen=self.args.generation_batch_size)
        self._logs["mean_reward"].extend(mean_grouped_rewards.tolist())

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

        # Optional: fetch token_weights for this batch and shape to (B, T)
        token_weights_tensor = None
        try:
            if getattr(self.args, "token_weights", False) and self.compute_attention_metrics and "token_weights" in self._logs:
                tw_all = list(self._logs["token_weights"]) if isinstance(self._logs.get("token_weights"), deque) else []
                if tw_all:
                    last_tw = tw_all[-len(prompts):] if len(tw_all) >= len(prompts) else []
                    if last_tw and len(last_tw) == len(prompts):
                        T = completion_ids.size(1)
                        tw_tensors = []
                        for w in last_tw:
                            w = w or []
                            t = torch.ones(T, dtype=torch.float32, device=device)
                            n = min(len(w), T)
                            if n > 0:
                                t[:n] = torch.tensor(w[:n], dtype=torch.float32, device=device)
                            tw_tensors.append(t)
                        token_weights_tensor = torch.stack(tw_tensors, dim=0)
        except Exception:
            token_weights_tensor = None

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
        if token_weights_tensor is not None:
            output["token_weights"] = token_weights_tensor

        # --- Dynamic sampling replay buffer integration ---
        # Only apply during training; evaluation may generate a different number of completions per prompt
        # which can cause shape mismatches (e.g., len(completions) < num_generations).
        if mode == "train" and self.replay_buffer is not None:
            # Per-group views (use local process rewards to match local batch size)
            num_groups = completion_ids.size(0) // self.num_generations
            group_adv = advantages.view(num_groups, self.num_generations)
            local_rewards = rewards[process_slice]
            group_rewards = local_rewards.view(num_groups, self.num_generations)
            group_std = group_rewards.std(dim=1)
            eps_var = float(getattr(self.args, "replay_var_epsilon", 1e-6))
            groups_with_variance = group_std > eps_var

            # Only enqueue groups passing mean reward threshold
            filter_min = getattr(self.args, "filter_min_reward", None)
            if filter_min is not None:
                group_mean = group_rewards.mean(dim=1)
                groups_with_variance = groups_with_variance & (group_mean > float(filter_min))

            # Buffer add: score = sum(|adv|) * std
            if groups_with_variance.any():
                scores = (group_adv.abs().sum(dim=1) * group_std)

                # Build buffered outputs per selected group (trim to max valid length within group)
                buffered_items = []
                for group_idx in groups_with_variance.nonzero(as_tuple=True)[0].tolist():
                    start = group_idx * self.num_generations
                    end = (group_idx + 1) * self.num_generations

                    # Determine max valid completion length in this group
                    group_completion_mask = completion_mask[start:end]
                    group_max_len = group_completion_mask.sum(dim=1).max().item()
                    
                    # Safety check: ensure group_max_len is at least 1 to avoid tensor size mismatch
                    if group_max_len == 0:
                        group_max_len = 1

                    # Safety check for prompt length
                    prompt_max_len = prompt_mask[start:end].sum(dim=1).max().item()
                    if prompt_max_len == 0:
                        prompt_max_len = 1
                    
                    item = {
                        "prompt_ids": prompt_ids[start:end, :prompt_max_len],
                        "prompt_mask": prompt_mask[start:end, :prompt_max_len],
                        "completion_ids": completion_ids[start:end, :group_max_len],
                        "completion_mask": completion_mask[start:end, :group_max_len],
                        "advantages": group_adv[group_idx].detach().cpu().tolist(),
                    }
                    if old_per_token_logps is not None:
                        item["old_per_token_logps"] = old_per_token_logps[start:end, :group_max_len]
                    if ref_per_token_logps is not None:
                        item["ref_per_token_logps"] = ref_per_token_logps[start:end, :group_max_len]
                    # Do not store vision fields in buffer to avoid inconsistency across packed tensors
                    buffered_items.append(item)

                self.replay_buffer.add(scores[groups_with_variance].detach().cpu().tolist(), buffered_items)

            # Replace groups with zero variance using buffer samples
            groups_without_variance = (~groups_with_variance)
            num_to_replace = int(groups_without_variance.sum().item())
            if num_to_replace > 0:
                sampled = self.replay_buffer.sample(num_to_replace)
                if sampled:
                    # Log replacement on main process
                    if self.accelerator.is_main_process:
                        replaced_indices = groups_without_variance.nonzero(as_tuple=True)[0].tolist()
                        print(
                            f"[ReplayBuffer] Replacing {num_to_replace} group(s) with zero/low variance "
                            f"(group indices: {replaced_indices}) using replay buffer samples",
                            flush=True,
                        )
                    # For shape alignment, compute target lengths
                    cur_p_len = prompt_ids.size(1)
                    cur_c_len = completion_ids.size(1)
                    tgt_p_len = cur_p_len
                    tgt_c_len = cur_c_len
                    for s in sampled:
                        tgt_p_len = max(tgt_p_len, s["prompt_ids"].size(1))
                        tgt_c_len = max(tgt_c_len, s["completion_ids"].size(1))

                    # If sampled longer, pad whole batch once
                    if tgt_p_len > cur_p_len:
                        prompt_ids = pad(list(prompt_ids.unbind(0)), padding_value=self.pad_token_id, pad_to_multiple_of=tgt_p_len, padding_side="left")
                        prompt_mask = pad(list(prompt_mask.unbind(0)), padding_value=0, pad_to_multiple_of=tgt_p_len, padding_side="left")
                    if tgt_c_len > cur_c_len:
                        completion_ids = pad(list(completion_ids.unbind(0)), padding_value=self.pad_token_id, pad_to_multiple_of=tgt_c_len, padding_side="right")
                        completion_mask = pad(list(completion_mask.unbind(0)), padding_value=0, pad_to_multiple_of=tgt_c_len, padding_side="right")
                        if old_per_token_logps is not None:
                            old_per_token_logps = pad(list(old_per_token_logps.unbind(0)), padding_value=0.0, pad_to_multiple_of=tgt_c_len, padding_side="right")
                        if ref_per_token_logps is not None:
                            ref_per_token_logps = pad(list(ref_per_token_logps.unbind(0)), padding_value=0.0, pad_to_multiple_of=tgt_c_len, padding_side="right")

                    # Assign replacements
                    replace_groups = groups_without_variance.nonzero(as_tuple=True)[0].tolist()
                    for s, gidx in zip(sampled, replace_groups):
                        start = gidx * self.num_generations
                        end = (gidx + 1) * self.num_generations
                        # Pad sampled tensors up to target lens if needed
                        def _pad_to(t, tgt_len, side):
                            if t.size(1) < tgt_len:
                                return pad(t, padding_value=(0 if t.dtype == torch.long else 0.0), pad_to_multiple_of=tgt_len, padding_side=side)
                            return t
                        sp_ids = _pad_to(s["prompt_ids"].to(prompt_ids.device), prompt_ids.size(1), "left") if "prompt_ids" in s else None
                        sp_msk = _pad_to(s["prompt_mask"].to(prompt_mask.device), prompt_mask.size(1), "left") if "prompt_mask" in s else None
                        sc_ids = _pad_to(s["completion_ids"].to(completion_ids.device), completion_ids.size(1), "right")
                        sc_msk = _pad_to(s["completion_mask"].to(completion_mask.device), completion_mask.size(1), "right")
                        s_adv = torch.tensor(s["advantages"], device=advantages.device, dtype=advantages.dtype)

                        # For multimodal inputs, only replace completion part to maintain image token alignment
                        if images is not None:
                            # Only replace completion_ids, completion_mask, and advantages
                            completion_ids[start:end] = sc_ids
                            completion_mask[start:end] = sc_msk
                            advantages[start:end] = s_adv
                            if old_per_token_logps is not None and "old_per_token_logps" in s:
                                old_per_token_logps[start:end] = _pad_to(s["old_per_token_logps"].to(old_per_token_logps.device), old_per_token_logps.size(1), "right")
                            if ref_per_token_logps is not None and "ref_per_token_logps" in s:
                                ref_per_token_logps[start:end] = _pad_to(s["ref_per_token_logps"].to(ref_per_token_logps.device), ref_per_token_logps.size(1), "right")
                        else:
                            # For text-only inputs, replace both prompt and completion
                            if sp_ids is not None:
                                prompt_ids[start:end] = sp_ids
                            if sp_msk is not None:
                                prompt_mask[start:end] = sp_msk
                            completion_ids[start:end] = sc_ids
                            completion_mask[start:end] = sc_msk
                            advantages[start:end] = s_adv
                            if old_per_token_logps is not None and "old_per_token_logps" in s:
                                old_per_token_logps[start:end] = _pad_to(s["old_per_token_logps"].to(old_per_token_logps.device), old_per_token_logps.size(1), "right")
                            if ref_per_token_logps is not None and "ref_per_token_logps" in s:
                                ref_per_token_logps[start:end] = _pad_to(s["ref_per_token_logps"].to(ref_per_token_logps.device), ref_per_token_logps.size(1), "right")

                    # Update output with potentially modified tensors
                    output["prompt_ids"] = prompt_ids
                    output["prompt_mask"] = prompt_mask
                    output["completion_ids"] = completion_ids
                    output["completion_mask"] = completion_mask
                    output["advantages"] = advantages
                    if old_per_token_logps is not None:
                        output["old_per_token_logps"] = old_per_token_logps
                    if ref_per_token_logps is not None:
                        output["ref_per_token_logps"] = ref_per_token_logps
                    
                    # Clear token_weights after replay buffer replacement to avoid shape mismatch
                    # Replay samples may have different completion lengths than the original batch
                    if "token_weights" in output:
                        output["token_weights"] = None

        # Emit rollout logs if enabled
        if (self.accelerator.is_main_process and 
            getattr(self.args, "realtime_rollout_logging", False) and 
            mode == "train"):
            try:
                # Get VGR info for logging
                vgr_info = []
                if self.compute_attention_metrics and hasattr(self, '_logs') and 'attention' in self._logs:
                    att_list = list(self._logs['attention'])
                    if att_list:
                        sample_results = att_list[-len(prompts):]
                        if hasattr(self, '_attention_skip_reasons'):
                            skips = list(self._attention_skip_reasons)
                            skip_slice = (
                                skips[-len(sample_results):] if len(skips) >= len(sample_results) else [None] * len(sample_results)
                            )
                        else:
                            skip_slice = [None] * len(sample_results)
                        vgr_info = compute_real_vgr_metrics(sample_results, skip_slice)
                
                # Get solutions if available
                solutions = [inp.get("solution", "") for inp in inputs]

                # For logs: ChatML prompt + plain completion
                if is_conversational(inputs[0]):
                    log_prompts_text = [
                        apply_chat_template({"prompt": p}, self.processing_class)["prompt"] for p in prompts
                    ]
                else:
                    log_prompts_text = prompts_text
                log_completions_text = completions_text
                
                # Prepare advantages for summary log
                advantages_for_log = None
                adv_local = advantages  # already sliced earlier to local process
                # Compute token-weighted advantage proxy if token weights available
                try:
                    if getattr(self.args, "token_weights", False) and token_weights_tensor is not None:
                        tw_local = token_weights_tensor[process_slice]
                        cm_local = completion_mask[process_slice].float()
                        valid = cm_local.sum(dim=1).clamp(min=1.0)
                        mean_w = (tw_local * cm_local).sum(dim=1) / valid
                        advantages_for_log = (adv_local * mean_w).detach().cpu().tolist()
                    else:
                        advantages_for_log = adv_local.detach().cpu().tolist()
                except Exception:
                    advantages_for_log = None

                # Call rollout logging
                emit_rollout_logs(
                    prompts_text=log_prompts_text,
                    completions_text=log_completions_text,
                    solutions=solutions,
                    rewards_per_func_local=rewards_per_func[process_slice],
                    total_rewards_local=rewards[process_slice],
                    reward_names=self.reward_func_names,
                    vgr_info=vgr_info,
                    log_path=getattr(self.args, "rollout_log_path", None),
                    prompt_preview_chars=getattr(self.args, "prompt_preview_chars", 2000),
                    completion_preview_chars=getattr(self.args, "completion_preview_chars", 2000),
                    vgr_as_coefficient=getattr(self.args, "vgr_as_coefficient", 0),
                    step=self.state.global_step,
                    epoch=self.state.epoch,
                    advantages_local=advantages_for_log,
                )
                # Append token weights section to the same rollout log file
                if getattr(self.args, "token_weights", False) and token_weights_tensor is not None:
                    from ..utils.dapo_logging import emit_token_weights_logs
                    emit_token_weights_logs(
                        token_weights=token_weights_tensor,
                        log_path=getattr(self.args, "rollout_log_path", None),
                        step=self.state.global_step,
                        epoch=self.state.epoch,
                    )
                    # Also emit per-token annotation for a small preview set
                    try:
                        tokenizer = getattr(self.processing_class, "tokenizer", None)
                        if tokenizer is not None:
                            # Use local tensors directly (do NOT slice by global process_slice)
                            local_ids = completion_ids
                            local_mask = completion_mask
                            local_w = token_weights_tensor
                            token_strs: list[list[str]] = []
                            token_wts: list[list[float]] = []
                            for i in range(local_ids.size(0)):
                                valid_len = int(local_mask[i].sum().item())
                                if valid_len <= 0:
                                    token_strs.append([])
                                    token_wts.append([])
                                    continue
                                ids_i = local_ids[i, :valid_len].detach().cpu().tolist()
                                toks = tokenizer.convert_ids_to_tokens(ids_i, skip_special_tokens=False)
                                token_strs.append([str(t) for t in toks])
                                token_wts.append(local_w[i, :valid_len].detach().cpu().tolist())
                            from ..utils.dapo_logging import emit_tokenwise_weights
                            # 单独的 token 权重文件：与 rollout 同目录，文件名 token_weights.md
                            rollout_path = getattr(self.args, "rollout_log_path", None)
                            if rollout_path:
                                import os as _os
                                token_log_path = _os.path.join(_os.path.dirname(rollout_path), "token_weights.md")
                            else:
                                token_log_path = None  # 由 emit_tokenwise_weights 内部默认到 training_logs/token_weights.md
                            emit_tokenwise_weights(
                                token_strings=token_strs,
                                token_weights=token_wts,
                                log_path=token_log_path,
                                step=self.state.global_step,
                                epoch=self.state.epoch,
                            )
                    except Exception:
                        pass
            except Exception as e:
                logger.warning(f"Failed to emit rollout logs: {e}")

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

        # Integrate token-level weighting into advantages (apply to all tokens)
        if getattr(self.args, "token_weights", False) and ("token_weights" in inputs) and (inputs["token_weights"] is not None):
            try:
                token_weights_tensor = inputs["token_weights"].to(coef_1.device)
                adv_matrix = advantages.unsqueeze(1) * token_weights_tensor
            except Exception:
                adv_matrix = advantages.unsqueeze(1)
        else:
            adv_matrix = advantages.unsqueeze(1)

        per_token_loss1 = coef_1 * adv_matrix
        per_token_loss2 = coef_2 * adv_matrix
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

        # Pretty print compact grouped logs to terminal
        if self.accelerator.is_main_process:
            try:
                # Rewards line
                r_acc = logs.get("rewards/accuracy_reward/mean", logs.get("eval_rewards/accuracy_reward/mean"))
                r_fmt = logs.get("rewards/think_format_reward/mean", logs.get("eval_rewards/think_format_reward/mean"))
                # Prefer new VGR reward key; fall back to legacy additive key if present
                r_vgr = logs.get("rewards/vgr_reward/mean", logs.get("eval_rewards/vgr_reward/mean"))
                if r_vgr is None:
                    r_vgr = logs.get("rewards/vgr_reward_as_additive/mean", logs.get("eval_rewards/vgr_reward_as_additive/mean"))
                r_len = logs.get("rewards/soft_overlong_punishment_reward/mean", logs.get("eval_rewards/soft_overlong_punishment_reward/mean"))
                r_total = logs.get("reward", logs.get("eval_reward"))
                rewards_line = []
                if r_acc is not None: rewards_line.append(f"acc={r_acc:.3f}")
                if r_fmt is not None: rewards_line.append(f"fmt={r_fmt:.3f}")
                if r_vgr is not None: rewards_line.append(f"vgr={r_vgr:.3f}")
                if r_len is not None: rewards_line.append(f"len={r_len:.3f}")
                if r_total is not None: rewards_line.append(f"total={r_total:.3f}")
                if rewards_line:
                    print("Rewards: " + ", ".join(rewards_line))

                # Loss/optim line
                loss = logs.get("loss", logs.get("eval_loss"))
                ent = logs.get("entropy", logs.get("eval_entropy"))
                lr = logs.get("learning_rate")
                grad = logs.get("grad_norm", logs.get("eval_grad_norm"))
                clip_low = logs.get("clip_ratio/low_mean", logs.get("eval_clip_ratio/low_mean"))
                clip_high = logs.get("clip_ratio/high_mean", logs.get("eval_clip_ratio/high_mean"))
                loss_line = []
                if loss is not None: loss_line.append(f"loss={loss:.4f}")
                if ent is not None: loss_line.append(f"entropy={ent:.4f}")
                if lr is not None: loss_line.append(f"lr={lr:.2e}")
                if grad is not None: loss_line.append(f"grad={grad:.3f}")
                if clip_low is not None: loss_line.append(f"clip_low={clip_low:.3f}")
                if clip_high is not None: loss_line.append(f"clip_high={clip_high:.3f}")
                if loss_line:
                    print("Optim:   " + ", ".join(loss_line))

                # Attention line
                a_early = logs.get("attention/early/vgr", logs.get("eval_attention/early/vgr"))
                a_mid = logs.get("attention/middle/vgr", logs.get("eval_attention/middle/vgr"))
                a_late = logs.get("attention/late/vgr", logs.get("eval_attention/late/vgr"))
                a_all = logs.get("attention/all/vgr", logs.get("eval_attention/all/vgr"))
                attn_line = []
                if a_early is not None: attn_line.append(f"early={a_early:.3f}")
                if a_mid is not None: attn_line.append(f"middle={a_mid:.3f}")
                if a_late is not None: attn_line.append(f"late={a_late:.3f}")
                if a_all is not None: attn_line.append(f"all={a_all:.3f}")
                if attn_line:
                    print("VGR:     " + ", ".join(attn_line))

                # Emit evaluation markdown logs: ChatML prompt + plain completion
                if mode == "eval":
                    try:
                        prompts_cm = list(self._logs.get("prompt_chatml", []))
                        completions_cm = list(self._logs.get("completion", []))
                        total_rewards = list(self._logs["rewards"].get("total", [])) if isinstance(self._logs.get("rewards"), dict) else []
                        reward_names = self.reward_func_names
                        reward_lists = {name: list(self._logs["rewards"].get(name, [])) for name in reward_names}
                        sample_count = min(len(prompts_cm), len(completions_cm))
                        eval_samples = []
                        for i in range(sample_count):
                            rewards_map = {}
                            for name in reward_names:
                                vals = reward_lists.get(name, [])
                                if i < len(vals):
                                    try:
                                        rewards_map[name] = float(vals[i])
                                    except Exception:
                                        pass
                            total_val = 0.0
                            if i < len(total_rewards):
                                try:
                                    total_val = float(total_rewards[i])
                                except Exception:
                                    total_val = 0.0
                            eval_samples.append(
                                {
                                    "prompt": prompts_cm[i],
                                    "completion": completions_cm[i],
                                    "rewards": rewards_map,
                                    "total_reward": total_val,
                                }
                            )
                        emit_eval_logs(
                            metrics=metrics,
                            logs=logs,
                            eval_samples=eval_samples,
                            log_path=getattr(self.args, "eval_log_path", None),
                            step=self.state.global_step,
                            epoch=self.state.epoch,
                        )
                    except Exception as e:
                        logger.warning(f"Failed to emit eval logs: {e}")
            except Exception:
                pass

        super().log(logs, start_time)
        self._metrics[mode].clear()

        if self.accelerator.is_main_process and self.log_completions:
            # 注释掉 wandb table 记录，避免网络超时和数据量过大问题
            # 只保留 metrics 曲线图记录（通过 super().log() 自动记录）
            pass
            # 注释掉终端打印
            # if is_rich_available():
            #     print_prompt_completions_sample(
            #         self._logs["prompt"],
            #         self._logs["completion"],
            #         self._logs["rewards"],
            #         self._logs["advantages"],
            #         self.state.global_step,
            #         self.num_completions_to_print,
            #     )

            # 注释掉详细的 wandb table 记录
            # if self.args.report_to and "wandb" in self.args.report_to and wandb.run is not None:
            #     import pandas as pd

            #     # Wandb: ChatML prompt + plain completion
            #     prompts_wb = list(self._logs.get("prompt_chatml", [])) or list(self._logs.get("prompt", []))
            #     completions_wb = list(self._logs.get("completion", []))

            #     n_rows = min(len(prompts_wb), len(completions_wb))
            #     prompts_wb = prompts_wb[:n_rows]
            #     completions_wb = completions_wb[:n_rows]

            #     table = {
            #         "step": [str(self.state.global_step)] * n_rows,
            #         "prompt": prompts_wb,
            #         "completion": completions_wb,
            #     }

            #     # Add rewards columns, sliced to n_rows for consistency
            #     for k, v in self._logs["rewards"].items():
            #         vals = list(v)
            #         table[k] = vals[:n_rows]

            #     # Add advantages, sliced
            #     advantages_list = list(self._logs["advantages"])[:n_rows]
            #     table["advantage"] = advantages_list
                
            #     # Add mean rewards for context
            #     if "mean_reward" in self._logs:
            #         mean_rewards_list = list(self._logs["mean_reward"])[:n_rows]
            #         table["mean_reward"] = mean_rewards_list
                
            #     # Add advantage labels for easy identification
            #     advantage_labels = []
            #     for adv in advantages_list:
            #         if adv > 0:
            #             advantage_labels.append("✅ 加分")
            #         elif adv < 0:
            #             advantage_labels.append("❌ 减分")
            #         else:
            #             advantage_labels.append("⚪ 中性")
            #     table["advantage_label"] = advantage_labels

            #     # Add images if present, sliced
            #     if self._logs["images"]:
            #         images_col = []
            #         for idx, image_list in enumerate(list(self._logs["images"])[:n_rows]):
            #             images_col.append([wandb.Image(image) for image in image_list])
            #         table["images"] = images_col

            #     df = pd.DataFrame(table)
            #     if self.wandb_log_unique_prompts:
            #         df = df.drop_duplicates(subset=["prompt"])
            #     wandb.log({"completions": wandb.Table(dataframe=df)})

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
    def _temporary_attn_impl(self, attn_impl: str = "eager"):
        """
        Temporarily switch attention implementation on the base model config.
        For vision-language models like Qwen2VL, also set on language_model submodule.
        """
        if not self.compute_attention_metrics:
            yield
            return

        base = self._unwrap_model_for_config()
        cfg = getattr(base, "config", None)
        if cfg is None:
            yield
            return
        
        # Store previous values
        prev_main = getattr(cfg, "_attn_implementation", None)
        prev_lm = None
        lm_cfg = None
        
        # For vision-language models, also set on language_model
        if hasattr(base, "language_model"):
            lm_cfg = getattr(base.language_model, "config", None)
            if lm_cfg is not None:
                prev_lm = getattr(lm_cfg, "_attn_implementation", None)
        
        try:
            setattr(cfg, "_attn_implementation", attn_impl)
            if lm_cfg is not None:
                setattr(lm_cfg, "_attn_implementation", attn_impl)
            yield
        finally:
            # Restore main config
            if prev_main is None:
                try:
                    delattr(cfg, "_attn_implementation")
                except Exception:
                    pass
            else:
                setattr(cfg, "_attn_implementation", prev_main)
            
            # Restore language_model config
            if lm_cfg is not None:
                if prev_lm is None:
                    try:
                        delattr(lm_cfg, "_attn_implementation")
                    except Exception:
                        pass
                else:
                    setattr(lm_cfg, "_attn_implementation", prev_lm)

    def _process_attention_metrics(self, attention_context: Optional[dict], mode: str) -> None:
        """Process attention outputs and compute metrics (aligned with old repo logic)."""
        if not self.compute_attention_metrics or attention_context is None:
            return
        try:
            outputs = attention_context.get("outputs")
            generate_inputs = attention_context.get("inputs")
            
            if outputs is None or getattr(outputs, "attentions", None) is None:
                return
            if generate_inputs is None or "input_ids" not in generate_inputs:
                return

            # Move relevant tensors to CPU to reduce GPU pressure during analysis
            input_ids = generate_inputs["input_ids"].detach().cpu()
            sequences = outputs.sequences.detach().cpu()
            image_grid_thw = generate_inputs.get("image_grid_thw")
            
            if isinstance(image_grid_thw, torch.Tensor):
                image_grid_thw_cpu = image_grid_thw.detach().cpu()
            else:
                image_grid_thw_cpu = None

            # Compute per-sample attention metrics
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

            # Optional: build token-level weights from attention (for loss weighting)
            try:
                if getattr(self.args, "token_weights", False):
                    tw_list, _tw_debug = build_token_vgr_weights_for_batch(
                        outputs_attentions=outputs.attentions,
                        input_ids=input_ids,
                        sequences=sequences,
                        processor=self.processing_class,
                        image_grid_thw=image_grid_thw_cpu,
                        exclude_special=True,
                        smooth_sigma=float(getattr(self.args, "token_weights_smooth_sigma", 0.0)),
                        clip_range=tuple(getattr(self.args, "token_weights_clip", (0.2, 3.0))),
                    )
                    if isinstance(self._logs.get("token_weights"), deque) and tw_list:
                        # Extend per-sample to keep alignment with later slicing by latest B items
                        self._logs["token_weights"].extend(tw_list)
            except Exception:
                pass

            # Free attention tensors quickly to avoid memory bloat
            outputs.attentions = None
            attention_context["outputs"] = None
            attention_context["inputs"] = None

            if not sample_results:
                return

            # Log and store metrics
            self._log_attention_metrics(sample_results, mode, skip_reasons)
        except Exception as e:
            # Do not fail training on diagnostics, but log the error
            logger.warning(f"Failed to compute attention metrics: {e}")
            import traceback
            logger.debug(f"Attention metrics error traceback:\n{traceback.format_exc()}")

    def _log_attention_metrics(
        self,
        sample_results: List[Optional[AttentionSampleResult]],
        mode: str,
        skip_reasons: List[Optional[str]],
    ) -> None:
        """Aggregate and log attention metrics (aligned with old repo logic)."""
        device = self.accelerator.device
        segments = ["early", "middle", "late", "all"]

        if not sample_results:
            return

        valid_results = [(idx, res) for idx, res in enumerate(sample_results) if res is not None]
        if not valid_results:
            # still extend internal buffers for completeness
            if isinstance(self._logs.get("attention"), deque):
                self._logs["attention"].extend(sample_results)
            if isinstance(self._attention_skip_reasons, deque):
                self._attention_skip_reasons.extend(skip_reasons)
            return

        for segment in segments:
            vgr_vals = []
            aei_text_vals = []
            aei_vision_vals = []
            for _, result in valid_results:
                seg = result.segments.get(segment)
                if seg is None:
                    continue
                vgr_vals.append(seg.vgr)
                aei_text_vals.append(seg.aei_text)
                aei_vision_vals.append(seg.aei_vision)

            if vgr_vals:
                vgr_tensor = torch.tensor(vgr_vals, device=device, dtype=torch.float32)
                vgr_tensor = torch.where(torch.isfinite(vgr_tensor), vgr_tensor, torch.full_like(vgr_tensor, float("nan")))
                gathered_vgr = self.accelerator.gather(vgr_tensor)
                self._metrics[mode][f"attention/{segment}/vgr"].append(torch.nanmean(gathered_vgr).item())

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
                    torch.isfinite(aei_vision_tensor), aei_vision_tensor, torch.full_like(aei_vision_tensor, float("nan"))
                )
                gathered_aei_vision = self.accelerator.gather(aei_vision_tensor)
                self._metrics[mode][f"attention/{segment}/aei_vision"].append(torch.nanmean(gathered_aei_vision).item())

        # Persist sample-level results for downstream logging and rewards
        if isinstance(self._logs.get("attention"), deque):
            self._logs["attention"].extend(sample_results)
        if isinstance(self._attention_skip_reasons, deque):
            self._attention_skip_reasons.extend(skip_reasons)
