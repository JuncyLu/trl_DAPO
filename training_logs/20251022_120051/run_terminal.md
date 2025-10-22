# Training Logs

- Time: 2025-10-22 12:00:51
- Model: Qwen/Qwen2.5-VL-3B-Instruct
- Dataset: /home/lujunxi57/aokvqa_trl_data
- Output Dir: grpo-Qwen2.5-VL-3B-Instruct

---

```text
# Training Logs

- Time: 2025-10-22 12:00:51
- Model: Qwen/Qwen2.5-VL-3B-Instruct
- Dataset: /home/lujunxi57/aokvqa_trl_data
- Output Dir: grpo-Qwen2.5-VL-3B-Instruct

---

```text
Loaded train size: 9930
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|#####     | 1/2 [00:00<00:00,  5.65it/s]Loading checkpoint shards: 100%|##########| 2/2 [00:00<00:00,  8.39it/s]
📁 Training logs directory: /home/lujunxi57/trl/training_logs
📝 Rollout log file: /home/lujunxi57/trl/training_logs/20251022_120051/rollout_results.md
🧠 Attention diagnostics file: /home/lujunxi57/trl/training_logs/20251022_120051/attention_diagnostics.md
  0%|          | 0/29790 [00:00<?, ?it/s]  0%|          | 1/29790 [00:19<158:51:28, 19.20s/it]  0%|          | 2/29790 [00:25<95:48:39, 11.58s/it]   0%|          | 3/29790 [00:35<88:20:56, 10.68s/it]  0%|          | 4/29790 [00:41<73:44:54,  8.91s/it]  0%|          | 5/29790 [00:49<72:00:28,  8.70s/it]  0%|          | 6/29790 [00:55<64:07:56,  7.75s/it]Traceback (most recent call last):
  File "/home/lujunxi57/trl/examples/scripts/grpo_vlm.py", line 660, in <module>
    trainer.train()
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/trainer.py", line 2325, in train
    return inner_training_loop(
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/trainer.py", line 2674, in _inner_training_loop
    tr_loss_step = self.training_step(model, inputs, num_items_in_batch)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/trainer.py", line 4014, in training_step
    inputs = self._prepare_inputs(inputs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/trl/trl/extras/profiling.py", line 98, in wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/trl/trl/trainer/grpo_trainer.py", line 1185, in _prepare_inputs
    generation_batch = self._generate_and_score_completions(generation_batch)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/trl/trl/trainer/grpo_trainer.py", line 1977, in _generate_and_score_completions
    prompt_ids_list, completion_ids_list, num_items_in_batch, sampling_per_token_logps_list = self._generate(
                                                                                              ^^^^^^^^^^^^^^^
  File "/home/lujunxi57/trl/trl/trainer/grpo_trainer.py", line 1515, in _generate
    prompt_ids, completion_ids, logprobs, attention_context = self._generate_single_turn(prompts, images)
                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/trl/trl/trainer/grpo_trainer.py", line 1474, in _generate_single_turn
    attention_outputs = unwrapped_model.generate(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/generation/utils.py", line 2564, in generate
    result = decoding_method(
             ^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/generation/utils.py", line 2787, in _sample
    outputs = model_forward(**model_inputs, return_dict=True)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/accelerate/utils/operations.py", line 818, in forward
    return model_forward(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/accelerate/utils/operations.py", line 806, in __call__
    return convert_to_fp32(self.model_forward(*args, **kwargs))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/amp/autocast_mode.py", line 44, in decorate_autocast
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/utils/generic.py", line 918, in wrapper
    output = func(self, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py", line 1476, in forward
    outputs = self.model(
              ^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py", line 1305, in forward
    outputs = self.language_model(
              ^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py", line 891, in forward
    layer_outputs = decoder_layer(
                    ^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/modeling_layers.py", line 94, in __call__
    return super().__call__(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py", line 741, in forward
    hidden_states, self_attn_weights = self.self_attn(
                                       ^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py", line 654, in forward
    query_states, key_states = apply_multimodal_rotary_pos_emb(
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py", line 581, in apply_multimodal_rotary_pos_emb
    sin = torch.cat([m[i % 3] for i, m in enumerate(sin.split(mrope_section, dim=-1))], dim=-1).unsqueeze(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lujunxi57/miniconda3/envs/trl/lib/python3.11/site-packages/transformers/models/qwen2_5_vl/modeling_qwen2_5_vl.py", line 581, in <listcomp>
    sin = torch.cat([m[i % 3] for i, m in enumerate(sin.split(mrope_section, dim=-1))], dim=-1).unsqueeze(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

```

```
