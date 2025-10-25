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


from trl.rewards import accuracy_reward, get_soft_overlong_punishment, think_format_reward

from .testing_utils import TrlTestCase, require_math_latex


class TestThinkFormatReward(TrlTestCase):
    def test_valid_format(self):
        completions = [
            "<think>This is my reasoning.</think>Answer: A",  # Simple, one-line reasoning
            "<think>\nThis is my reasoning.\n</think>\nAnswer: B",  # Multiline reasoning
            "<think>\nThis is\nmy reasoning.\n</think>\nAnswer: C",  # Multiline reasoning
            "<think>\nThis is my reasoning.</think>\nAnswer: D",  # Reasoning with answer
            "<think>Short reasoning.</think>Answer: E",  # Short reasoning
        ]
        completions = [[{"content": completion}] for completion in completions]
        rewards = think_format_reward(completions)
        # 软格式奖励应该给这些格式良好的文本高分
        assert all(reward >= 0.8 for reward in rewards), f"Expected high rewards, got {rewards}"

    def test_invalid_format(self):
        completions = [
            "<think>\nThis is my reasoning.\nThis is my answer.",  # No closing </think>
            "<think>This is my reasoning.\nThis is my answer.",  # No closing </think>
            "This is my reasoning. This is my answer.",  # No <think> tags
            "This is my reasoning.\nThis is my answer.",  # No <think> tags
            "This is my reasoning.</think>\nThis is my answer.",  # No opening <think>
            "This is my reasoning.</think>This is my answer.",  # No opening <think>
            "This<think>is my reasoning.</think>\nThis is my answer.",  # <think> tag in the middle
            "<think>This is<think>my reasoning.</think></think>This is my answer.",  # Nested <think> tags
            "<think>This is</think>\nmy\n<think>reasoning.</think>\nThis is my answer.",  # Multiline <think>
        ]
        completions = [[{"content": completion}] for completion in completions]
        rewards = think_format_reward(completions)
        # 软格式奖励应该给这些格式不完整的文本相对低分
        # 注意：软格式奖励会给部分匹配的格式一些分数
        assert all(reward < 0.8 for reward in rewards), f"Expected relatively low rewards, got {rewards}"

    def test_mixed_format(self):
        completions = [
            "<think>This is my reasoning.</think>Answer: A",  # Valid
            "<think>\nThis is my reasoning.\n</think>\nAnswer: B",  # Valid
            "<think>This is my reasoning.\nThis is my answer.",  # Invalid
            "This is my reasoning. This is my answer.",  # Invalid
        ]
        completions = [[{"content": completion}] for completion in completions]
        rewards = think_format_reward(completions)
        # 前两个应该有高分，后两个应该有低分
        assert rewards[0] >= 0.8, f"Expected high reward for valid format, got {rewards[0]}"
        assert rewards[1] >= 0.8, f"Expected high reward for valid format, got {rewards[1]}"
        assert rewards[2] < 0.5, f"Expected low reward for invalid format, got {rewards[2]}"
        assert rewards[3] < 0.5, f"Expected low reward for invalid format, got {rewards[3]}"


class TestSoftOverlongPunishmentReward:
    def test_soft_overlong_punishment_short_completion(self):
        """Test soft overlong punishment reward function with a short completion."""
        # length 50, with max=100 and soft cache=20, reward should be 0.
        reward_fn = get_soft_overlong_punishment(max_completion_len=100, soft_punish_cache=20)
        completion_ids = [[1] * 50]  # 50 <= 80
        rewards = reward_fn(completion_ids=completion_ids)
        assert rewards == [0]

    def test_soft_overlong_punishment_long_completion(self):
        """Test soft overlong punishment reward function with a longer than max completion."""
        # 110 > 100, reward should be -1.
        reward_fn = get_soft_overlong_punishment(max_completion_len=100, soft_punish_cache=20)
        completion_ids = [[1] * 110]
        rewards = reward_fn(completion_ids)
        assert rewards == [-1]

    def test_soft_overlong_punishment_intermediate_completion(self):
        """Test soft overlong punishment reward function for intermediate length completion."""
        reward_fn = get_soft_overlong_punishment(max_completion_len=100, soft_punish_cache=20)
        completion_ids = [[1] * 90]  # 90 is between 80 and 100
        rewards = reward_fn(completion_ids)
        assert round(abs(rewards[0] - -0.5), 4) == 0


class TestAccuracyReward:
    @require_math_latex
    def test_accuracy_reward_correct_answer(self):
        """Test accuracy_reward with a correct answer."""
        completion = [[{"content": r"\boxed{\frac{63}{400}}"}], [{"content": r"\boxed{\frac{63}{400}}"}]]
        solution = [r"\frac{63}{400}", "63/400"]
        rewards = accuracy_reward(completion, solution)
        assert rewards[0] == 1.0
        assert rewards[1] == 1.0

    @require_math_latex
    def test_accuracy_reward_wrong_answer(self):
        """Test accuracy_reward with an incorrect answer."""
        completion = [[{"content": r"\boxed{\frac{64}{400}}"}]]
        solution = [r"\frac{63}{400}"]
        rewards = accuracy_reward(completion, solution)
        assert rewards[0] == 0.0

    @require_math_latex
    def test_accuracy_reward_wrong_answer_no_latex(self):
        """Test accuracy_reward with an incorrect answer and gold solution with no latex."""
        completion = [[{"content": r"\boxed{3}"}]]
        solution = ["6"]
        rewards = accuracy_reward(completion, solution)
        assert rewards[0] == 0.0

    @require_math_latex
    def test_accuracy_reward_unparseable_gold(self):
        """Test accuracy_reward with an unparseable gold solution."""
        completion = [
            [{"content": "Answer is forty two."}],
            [{"content": "Some other content."}],
            [{"content": r"Answer is \boxed{42}."}],
            [{"content": r"Answer is \boxed{\mathbf{42}}."}],  # Make response bold
            [{"content": r"Answer is \boxed{\textbf{42}}."}],  # Different latex command for bold
            [{"content": r"Answer is \boxed{42}."}],
            [{"content": r"Answer is \boxed{42.3456}."}],
        ]
        solution = [
            "Answer is forty two.",
            "Answer is forty three.",
            "Answer is 42.0",  # Decimal point
            "Answer is 42 43 okay?",  # Extra space
            "Answer is 42",
            r"Answer is \n\boxed{42}",  # Newline in gold solution
            "Answer is 42.34560",  # Extra trailing zero
        ]
        rewards = accuracy_reward(completion, solution)
        assert rewards[0] == 1.0  # Should revert to exact text match
        assert rewards[1] == 0.0
        assert rewards[2] == 1.0
        assert rewards[3] == 1.0
        assert rewards[4] == 1.0
        assert rewards[5] == 1.0
        assert rewards[6] == 1.0  # Should ignore trailing zeros
