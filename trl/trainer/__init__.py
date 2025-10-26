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

from typing import TYPE_CHECKING

from ..import_utils import _LazyModule


_import_structure = {
    "callbacks": [
        "LogCompletionsCallback",
        "SyncRefModelCallback",
    ],
    "judges": [
        "BasePairwiseJudge",
    ],
    "model_config": ["ModelConfig"],
    "utils": [
        "RunningMoments",
        "compute_accuracy",
        "disable_dropout_in_model",
        "empty_cache",
        "peft_module_casting_to_bf16",
    ],
}

if TYPE_CHECKING:
    from .callbacks import (
        LogCompletionsCallback,
        SyncRefModelCallback,
    )
    from .judges import (
        BasePairwiseJudge,
    )
    from .model_config import ModelConfig
    from .utils import (
        RunningMoments,
        compute_accuracy,
        disable_dropout_in_model,
        empty_cache,
        peft_module_casting_to_bf16,
    )
else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)
