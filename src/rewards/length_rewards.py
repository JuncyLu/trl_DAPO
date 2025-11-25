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


from collections.abc import Callable


def get_soft_overlong_punishment(
    max_completion_len: int,
    soft_punish_cache: int | None = None,
) -> Callable:
    # docstyle-ignore
    r"""
    Reward function that penalizes overlong completions. It is used to penalize overlong completions, but not to reward
    shorter completions. Reference: Eq. (13) from the DAPO paper (https://huggingface.co/papers/2503.14476)

    $$
    R_{\text{length}}(y) = \begin{cases}
    0, & |y| \le L_{\max} - L_{\text{cache}} \\
    \dfrac{(L_{\max} - L_{\text{cache}}) - |y|}{L_{\text{cache}}}, & L_{\max} - L_{\text{cache}} < |y| \le L_{\max} \\
    -1, & L_{\max} < |y|
    \end{cases}
    $$

    Args:
        max_completion_len (`int`):
            Maximum completion length \(L_{\max}\).
        soft_punish_cache (`int`, *optional*):
            Minimum completion length \(L_{\text{cache}}\). If `None`, defaults to `round(0.7 * max_completion_len)`.
            If set to `0`, the intermediate linear penalty segment is removed.

    Example:
        ```python
        from trl.rewards import get_soft_overlong_punishment

        soft_overlong_punishment = get_soft_overlong_punishment(
            max_completion_len=100,
            soft_punish_cache=20,
        )
        completion_ids = [[1] * 90]
        rewards = soft_overlong_punishment(completion_ids)
        print(rewards)  # [-0.5]
        ```
    """

    L_max = int(max(1, max_completion_len))
    if soft_punish_cache is None:
        soft_punish_cache = max(1, int(round(0.7 * L_max)))
    else:
        soft_punish_cache = max(0, int(soft_punish_cache))

    threshold = L_max - soft_punish_cache if soft_punish_cache > 0 else L_max
    denom = float(soft_punish_cache) if soft_punish_cache > 0 else 1.0

    def soft_overlong_punishment_reward(completion_ids: list[list[int]], **kwargs) -> list[float]:
        """Reward function that penalizes overlong completions."""
        rewards: list[float] = []
        for ids in completion_ids:
            completion_length = len(ids)
            if completion_length <= threshold:
                rewards.append(0.0)
            elif threshold < completion_length <= L_max:
                rewards.append((threshold - completion_length) / denom)
            else:
                rewards.append(-1.0)
        return rewards

    soft_overlong_punishment_reward.__name__ = "length_reward"
    return soft_overlong_punishment_reward
