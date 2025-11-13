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


import sys
from typing import TYPE_CHECKING

from ..import_utils import _LazyModule


_import_structure = {
    "accuracy_rewards": ["accuracy_reward"],
    "format_rewards": ["think_format_reward", "tag_count_reward"],
    "length_rewards": ["get_soft_overlong_punishment"],
    "attention_rewards": ["vgr_reward", "vgr_hard_negative"],
    "reward_utils": [
        "RewardWeightManager", 
        "RewardWeightConfig", 
        "create_reward_weight_manager",
        "calculate_reward_metrics"
    ],
}


if TYPE_CHECKING:
    from .accuracy_rewards import accuracy_reward
    from .format_rewards import think_format_reward, tag_count_reward
    from .length_rewards import get_soft_overlong_punishment
    from .attention_rewards import vgr_reward, vgr_hard_negative
    from .reward_utils import (
        RewardWeightManager, 
        RewardWeightConfig, 
        create_reward_weight_manager,
        calculate_reward_metrics
    )


else:
    sys.modules[__name__] = _LazyModule(__name__, __file__, _import_structure, module_spec=__spec__)
