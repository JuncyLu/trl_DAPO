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


def get_soft_overlong_punishment(max_completion_len: int, soft_punish_cache: int) -> Callable:
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
            Maximum length of the completion,  \( L_{\max} \).
        soft_punish_cache (`int`):
            Minimum length of the completion,  \( L_{\text{cache}} \). If set to `0`, no minimum length is applied.

    Example:
    ```python
    from src.rewards import get_soft_overlong_punishment

    soft_overlong_punishment = get_soft_overlong_punishment(max_completion_len=100, soft_punish_cache=20)
    completion_ids = [[1] * 90]  # simulating a completion with 90 tokens. 90 is between 80 and 100.
    rewards = soft_overlong_punishment(completion_ids)
    print(rewards)  # [-0.5]
    ```
    """

    def soft_overlong_punishment_reward(completion_ids: list[list[int]], **kwargs) -> list[float]:
        """Reward function that penalizes overlong completions."""
        rewards = []
        for ids in completion_ids:
            completion_length = len(ids)
            if completion_length <= max_completion_len - soft_punish_cache:
                rewards.append(0.0)
            elif max_completion_len - soft_punish_cache < completion_length <= max_completion_len:
                rewards.append((max_completion_len - soft_punish_cache - completion_length) / soft_punish_cache)
            else:
                rewards.append(-1.0)
        return rewards

    return soft_overlong_punishment_reward


def get_accuracy_conditioned_length_reward(
    max_completion_len: int,
    lower_ratio: float = 0.2,
    upper_ratio: float = 0.5,
    alpha: float = 0.5,
) -> Callable:
    # docstyle-ignore
    r"""
    长度奖励函数：答对则返回 1；答错时按响应长度惩罚，长度超过阈值越多惩罚越大。

    .. math::
        R_{\text{len}} =
        \begin{cases}
            1, & \text{correct} \\
            1 - \alpha \cdot \mathrm{clamp}\left(\dfrac{|y| - L_0}{L_{\max} - L_0}, 0, 1\right), & \text{incorrect}
        \end{cases}

    其中 \( |y| \) 为生成 token 数。默认 \( L_0 = 0.2 \cdot L_{\text{max}} \)，\( L_{\max} = 0.5 \cdot L_{\text{max}} \)。

    Args:
        max_completion_len (`int`):
            Maximum allowed completion length.
        lower_ratio (`float`, *optional*, defaults to `0.2`):
            Ratio used to derive \( L_0 = \text{lower\_ratio} \times L_{\text{max}} \).
        upper_ratio (`float`, *optional*, defaults to `0.5`):
            Ratio used to derive \( L_{\max} = \text{upper\_ratio} \times L_{\text{max}} \).
        alpha (`float`, *optional*, defaults to `0.5`):
            Penalty factor applied when the answer is wrong, constrained to `[0, 1]`.
    """

    lower_ratio = max(0.0, min(lower_ratio, 1.0))
    upper_ratio = max(lower_ratio + 1e-6, min(upper_ratio, 1.0))
    alpha = max(0.0, min(alpha, 1.0))

    # 依据 ratio 计算阈值，并确保 L_max > L_0
    L0 = max(1, int(round(max_completion_len * lower_ratio)))
    Lmax = max(L0 + 1, int(round(max_completion_len * upper_ratio)))
    denom = max(1, Lmax - L0)

    def accuracy_conditioned_length_reward(
        completion_ids: list[list[int]],
        accuracies: list[float] | None = None,
        **kwargs,
    ) -> list[float]:
        rewards: list[float] = []

        for idx, ids in enumerate(completion_ids):
            completion_len = len(ids)

            if accuracies is None or idx >= len(accuracies):
                # 缺少准确率信息时视为中性奖励
                rewards.append(1.0)
                continue

            is_correct = float(accuracies[idx]) >= 0.5
            if is_correct:
                rewards.append(1.0)
                continue

            penalty = max(0.0, completion_len - L0) / denom
            penalty = min(1.0, penalty)
            rewards.append(1.0 - alpha * penalty)

        return rewards

    accuracy_conditioned_length_reward.__name__ = "length_reward"
    return accuracy_conditioned_length_reward
