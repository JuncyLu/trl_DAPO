 - 启用 token 级权重到损失（修正现有“计算未使用”问题）
      - 问题：adv_matrix 已计算但未参与 per_token_loss；且该段出现在损失计算之后（逻辑顺序错误）（src/trainer/
        dapo_trainer.py:2321）。
      - 建议：
          - 将“Token-level weighting integration”代码块上移到计算 per_token_loss 之前（约 src/trainer/dapo_trainer.py:2230
            附近），并以 adv_matrix 替代 advantages.unsqueeze(1)：
              - 替换 src/trainer/dapo_trainer.py:2248-2253
                  - 现状：per_token_loss1/2 = coef_* advantages.unsqueeze(1)
                  - 建议：先构造 adv_mat = 使用 token_weights 后的矩阵；再 per_token_loss1/2 = coef_* adv_mat
          - 同步在生成阶段产出 token_weights 并随 batch 传入 inputs：
              - 位置 A（推荐）：在 _process_attention_metrics 内部、清理 attentions 之前，调用
                build_token_vgr_weights_for_batch（src/utils/attention_token_weights.py:33），将结果暂存到
                self._logs 或一个环形缓冲，然后在 _generate_and_score_completions 组装 output 时按顺序对齐并填充到
                inputs["token_weights"]。
              - 位置 B：在 _generate_single_turn 返回 attention_context 后，紧跟构造 token_weights，再返回给 _generate（需
                要调整数据通路）。
          - 细节：将权重对齐到 completion_mask 的右侧长度（padding 到 logits_to_keep），并在优势为负处将权重折叠回 1（与现
            有 top-k 放大逻辑一致）。
  - 生成路径与注意力度量的兼容提示与兜底
      - 问题：vLLM 与 paged 生成不产出 attentions，VGR 奖励退化为中性 0.5（符合代码，但容易误用）。
      - 建议：当 compute_attention_metrics=True 且 attention_context=None 时，显式记录告警并建议关闭 vLLM/paged 或将 VGR
        权重置零；或自动在日志中标注“VGR 为中性奖励”（src/trainer/dapo_trainer.py:1434, 1499, 1540）。
  - 注意力度量的性能控制
      - 问题：常规 transformers.generate + output_attentions=True 代价较高。
      - 建议：新增配置如 attention_metrics_ratio（例如仅对 10% batch 计算）、或 attention_metrics_steps 间隔抽
        样；在 _process_attention_metrics 前做随机采样与 early return（src/trainer/dapo_config.py，src/trainer/
        dapo_trainer.py:2600 附近）。
  - 默认更符合实践的截断屏蔽
      - 建议：将 mask_truncated_completions 默认为 True，或在实验脚本中显式开启，避免截断样本影响稳定性（src/trainer/
        dapo_config.py:602，src/trainer/dapo_trainer.py:1601）。
  - 日志体量节制
      - 建议：增加 rollout_logging_steps 或 sample_n 机制，只在特定步数写 Markdown 明细，避免日志过大（现有
        realtime_rollout_logging=True；src/trainer/dapo_trainer.py:2060、src/utils/dapo_logging.py）。
  - 适配更多 VLM 的视觉 token 识别
      - 问题：extract_vision_token_spans_qwen 假设 Qwen 特殊符号（src/utils/attention_metrics.py:468）。
      - 建议：抽象视觉 token span 提取接口，为不同模型注册解析器或做 tokenizer 特殊符号自适应探测，提升通用性。

  如果你希望，我可以直接提交一版“最小可用”的 token_weights 接入补丁（计算→注入 inputs→替换损失优势项），并同时加上选项开关
  与基础告警。