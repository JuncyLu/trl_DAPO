import pytest


torch = pytest.importorskip("torch")


def test_segment_metrics_are_length_normalized():
    from src.utils.attention_metrics import _compute_segment_metrics

    instruction_mask = torch.tensor([True, True, False, False], dtype=torch.bool)
    vision_mask = torch.tensor([False, False, True, True], dtype=torch.bool)
    actual_prompt_length = 4
    num_prompt_queries = 3
    layer_indices = [0, 1]

    def run(generated_tokens: int):
        total_queries = num_prompt_queries + generated_tokens
        attn = torch.zeros(total_queries, actual_prompt_length, dtype=torch.float32)
        if generated_tokens > 0:
            attn[num_prompt_queries:, :] = torch.tensor([0.5, 0.0, 0.5, 0.0], dtype=torch.float32)
        per_layer_attn = {0: attn.clone(), 1: attn.clone()}
        return _compute_segment_metrics(
            per_layer_attn=per_layer_attn,
            instruction_mask=instruction_mask,
            vision_mask=vision_mask,
            layer_indices=layer_indices,
            num_prompt_queries=num_prompt_queries,
            actual_prompt_length=actual_prompt_length,
        )

    seg_1 = run(generated_tokens=1)
    seg_3 = run(generated_tokens=3)

    assert seg_1.attention_text == seg_3.attention_text
    assert seg_1.attention_vision == seg_3.attention_vision

    assert abs(seg_1.attention_text - 0.5) < 1e-6
    assert abs(seg_1.attention_vision - 0.5) < 1e-6
