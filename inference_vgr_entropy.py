#!/usr/bin/env python3
"""
脚本：对数据集中第一个问题做两次推理，计算每个token的vgr指标和熵值
"""

import sys
import os
import torch
import transformers
from datasets import load_dataset
from PIL import Image
from transformers import AutoProcessor, AutoConfig, GenerationConfig
from trl.trainer.utils import entropy_from_logits
from trl.data_utils import apply_chat_template, is_conversational, prepare_multimodal_messages
from contextlib import contextmanager
import torch.nn.functional as F

sys.path.append(os.path.dirname(__file__))

from src.utils.attention_token_weights import build_token_vgr_weights_for_batch
from src.utils.attention_metrics import get_qwen_special_token_ids


def load_model_and_processor(model_name_or_path: str, device: str = "cuda"):
    """加载模型和processor，使用和训练时相同的方式"""
    print(f"正在加载模型: {model_name_or_path}")
    processor = AutoProcessor.from_pretrained(
        model_name_or_path, 
        trust_remote_code=True,
        truncation_side="left",
        use_fast=False
    )
    
    # 使用和训练时相同的方式加载模型
    model_init_kwargs = {
        "dtype": torch.bfloat16,
        "device_map": device,
        "trust_remote_code": True,
    }
    
    # 使用AutoConfig获取配置，然后使用架构类加载模型（和dapo_trainer.py一致）
    config = AutoConfig.from_pretrained(model_name_or_path, trust_remote_code=True)
    architecture = getattr(transformers, config.architectures[0])
    model = architecture.from_pretrained(model_name_or_path, **model_init_kwargs)
    model.eval()
    return model, processor


@contextmanager
def _attn_last_k_layers_only(model, last_k_layers=None):
    """临时限制返回的attention为最后K层，完全按照dapo_trainer.py的实现"""
    if not last_k_layers or last_k_layers <= 0:
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
                if layers is not None:
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

            # Also patch layer forward
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


def generate_with_attention(
    model,
    processor,
    prompt,
    image=None,
    generation_config=None,
    max_prompt_length=2048,
    last_k_layers=6,
):
    """生成并返回attention outputs和logits，完全按照dapo_trainer.py的_generate_single_turn方式"""
    device = next(model.parameters()).device
    
    # 准备processor_kwargs，和训练时完全一致
    processor_kwargs = {
        "return_tensors": "pt",
        "padding": True,
        "padding_side": "left",
        "max_length": max_prompt_length,
        "truncation": True,
        "add_special_tokens": False,
    }
    
    # 如果有图像，使用prepare_multimodal_messages准备prompt（和训练时一致）
    if image is not None:
        mm_prompts = [prepare_multimodal_messages(prompt, [image])]
    else:
        mm_prompts = [prompt]
    
    # Build text with chat template and include images if provided
    prompts_text = [
        apply_chat_template({"prompt": p}, processor)["prompt"]
        for p in mm_prompts
    ]
    
    if image is not None:
        # 使用images参数传递图像（processor会自动处理）
        generate_inputs = processor(text=prompts_text, images=[image], **processor_kwargs)
    else:
        generate_inputs = processor(text=prompts_text, **processor_kwargs)
    
    # 移动到设备，并确保pixel_values使用正确的dtype
    model_dtype = next(model.parameters()).dtype
    generate_inputs_prepared = {}
    for k, v in generate_inputs.items():
        if isinstance(v, torch.Tensor):
            v = v.to(device)
            # pixel_values需要转换为模型dtype
            if k == "pixel_values":
                v = v.to(dtype=model_dtype)
            generate_inputs_prepared[k] = v
        else:
            generate_inputs_prepared[k] = v
    
    generate_inputs = generate_inputs_prepared
    
    # 调试：打印generate_inputs的keys
    print(f"generate_inputs keys: {list(generate_inputs.keys())}")
    if image is not None:
        for key in ["pixel_values", "image_grid_thw", "pixel_attention_mask", "image_sizes"]:
            if key in generate_inputs:
                val = generate_inputs[key]
                if isinstance(val, torch.Tensor):
                    print(f"  {key}: shape={val.shape}, dtype={val.dtype}")
                else:
                    print(f"  {key}: {type(val)}")
    
    # 设置attention implementation为eager
    cfg = getattr(model, "config", None)
    lm_cfg = getattr(model.language_model, "config", None) if hasattr(model, "language_model") else None
    
    prev_main = getattr(cfg, "_attn_implementation", None) if cfg else None
    prev_lm = getattr(lm_cfg, "_attn_implementation", None) if lm_cfg else None
    
    try:
        # Set to eager
        if cfg:
            setattr(cfg, "_attn_implementation", "eager")
        if lm_cfg:
            setattr(lm_cfg, "_attn_implementation", "eager")
        
        with _attn_last_k_layers_only(model, last_k_layers=last_k_layers):
            with torch.no_grad():
                # 确保所有图像相关参数都被传递
                # Qwen2.5-VL在生成过程中需要持续访问图像信息
                generation_kwargs = {
                    **generate_inputs,
                    "generation_config": generation_config,
                    "disable_compile": True,
                    "return_dict_in_generate": True,
                    "output_attentions": True,
                    "output_scores": True,  # 获取logits
                }
                
                # 确保图像相关参数存在
                if image is not None:
                    # 确保pixel_values, image_grid_thw等参数都在generation_kwargs中
                    if "pixel_values" not in generation_kwargs:
                        print("警告: pixel_values不在generate_inputs中")
                    if "image_grid_thw" not in generation_kwargs:
                        print("警告: image_grid_thw不在generate_inputs中")
                
                attention_outputs = model.generate(**generation_kwargs)
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
    
    # Compute prompt length and extract completion ids
    prompt_ids, prompt_mask = generate_inputs["input_ids"], generate_inputs["attention_mask"]
    prompt_length = prompt_ids.size(1)
    prompt_completion_ids = attention_outputs.sequences
    completion_ids = prompt_completion_ids[:, prompt_length:]
    
    # Mask everything after the first EOS token (和训练时一致)
    eos_token_id = processor.tokenizer.eos_token_id
    pad_token_id = processor.tokenizer.pad_token_id
    is_eos = completion_ids == eos_token_id
    eos_idx = torch.full((is_eos.size(0),), is_eos.size(1), dtype=torch.long, device=device)
    eos_idx[is_eos.any(dim=1)] = is_eos.int().argmax(dim=1)[is_eos.any(dim=1)]
    sequence_indices = torch.arange(is_eos.size(1), device=device).expand(is_eos.size(0), -1)
    completion_mask = (sequence_indices <= eos_idx.unsqueeze(1)).int()
    
    prompt_ids_list = [p[m].tolist() for p, m in zip(prompt_ids, prompt_mask.bool())]
    completion_ids_list = [c[m].tolist() for c, m in zip(completion_ids, completion_mask.bool())]
    
    # 获取logits
    # 方法1: 尝试从generation outputs获取scores
    logits = None
    if hasattr(attention_outputs, 'scores') and attention_outputs.scores is not None:
        logits_list = attention_outputs.scores  # List of tensors, each shape (batch_size, vocab_size)
        
        if logits_list and len(logits_list) > 0:
            # 检查第一个logit的shape
            first_logit_shape = logits_list[0].shape if hasattr(logits_list[0], 'shape') else None
            print(f"  从scores获取logits: logits_list长度={len(logits_list)}, 第一个logit shape={first_logit_shape}")
            
            # 确保所有logits都在正确的设备上
            logits_list = [logit.to(device) if isinstance(logit, torch.Tensor) else logit for logit in logits_list]
            
            # 堆叠logits: (batch_size, seq_len, vocab_size)
            logits = torch.stack(logits_list, dim=1)  # (batch_size, seq_len, vocab_size)
            print(f"  堆叠后logits shape: {logits.shape}")
        else:
            print("  警告: logits_list为空")
    
    # 方法2: 如果scores不存在，通过重新forward获取logits（和训练时一致）
    if logits is None:
        print("  警告: 无法从generation outputs获取logits，尝试通过重新forward获取...")
        # 使用completion_ids重新forward获取logits
        # 注意：这里只获取completion部分的logits，不包括prompt部分
        try:
            with torch.no_grad():
                # 准备模型输入
                model_inputs = {
                    "input_ids": prompt_completion_ids,
                    "attention_mask": torch.ones_like(prompt_completion_ids, device=device),
                }
                
                # 添加图像相关参数
                if "pixel_values" in generate_inputs:
                    model_inputs["pixel_values"] = generate_inputs["pixel_values"]
                if "image_grid_thw" in generate_inputs:
                    model_inputs["image_grid_thw"] = generate_inputs["image_grid_thw"]
                if "pixel_attention_mask" in generate_inputs:
                    model_inputs["pixel_attention_mask"] = generate_inputs["pixel_attention_mask"]
                if "image_sizes" in generate_inputs:
                    model_inputs["image_sizes"] = generate_inputs["image_sizes"]
                
                # Forward获取logits
                outputs = model(**model_inputs)
                all_logits = outputs.logits  # (batch_size, seq_len, vocab_size)
                
                # 只保留completion部分的logits
                # prompt部分的logits在位置[0:prompt_length]，completion部分在[prompt_length:]
                logits = all_logits[:, prompt_length:, :]  # (batch_size, completion_len, vocab_size)
                print(f"  通过forward获取logits shape: {logits.shape}")
        except Exception as e:
            print(f"  通过forward获取logits失败: {e}")
            import traceback
            traceback.print_exc()
            logits = None
    
    # 获取attention outputs
    attentions = attention_outputs.attentions  # List of tuples, each tuple contains attention for each layer
    
    return {
        "generated_ids": prompt_completion_ids,
        "completion_ids": completion_ids,
        "completion_ids_list": completion_ids_list,
        "logits": logits,
        "attentions": attentions,
        "input_ids": prompt_ids,
        "image_grid_thw": generate_inputs.get("image_grid_thw"),
        "attention_context": {
            "outputs": attention_outputs,
            "inputs": generate_inputs,
        },
    }


def compute_entropy_per_token(logits):
    """计算每个token位置的熵值"""
    if logits is None:
        return None
    
    # 确保logits是float32类型（entropy_from_logits可能需要）
    if logits.dtype != torch.float32:
        logits = logits.float()
    
    # logits shape: (batch_size, seq_len, vocab_size)
    # 返回: (batch_size, seq_len)
    try:
        entropy = entropy_from_logits(logits)
        # 检查结果是否包含nan
        if torch.isnan(entropy).any():
            print(f"  警告: 熵值计算后包含nan，nan数量: {torch.isnan(entropy).sum().item()}")
        return entropy
    except Exception as e:
        print(f"  计算熵值时出错: {e}")
        import traceback
        traceback.print_exc()
        return None


def format_results(run_id, completion_text, vgr_values, entropy_values, token_texts=None):
    """格式化输出结果"""
    print(f"\n{'='*80}")
    print(f"推理 {run_id} 结果")
    print(f"{'='*80}")
    print(f"生成文本: {completion_text}")
    print(f"\nToken级别的VGR和熵值:")
    print(f"{'Token':<30} {'VGR':<15} {'Entropy':<15}")
    print("-" * 60)
    
    # 确保vgr_values和entropy_values都是列表
    vgr_values = vgr_values if vgr_values else []
    entropy_values = entropy_values if entropy_values else []
    
    # 取最大长度
    num_tokens = max(len(vgr_values), len(entropy_values))
    
    if num_tokens == 0:
        print("  没有token数据")
        return
    
    for i in range(num_tokens):
        token_str = token_texts[i] if token_texts and i < len(token_texts) else f"token_{i}"
        vgr = vgr_values[i] if i < len(vgr_values) else 0.0
        entropy = entropy_values[i] if i < len(entropy_values) else 0.0
        print(f"{token_str:<30} {vgr:<15.4f} {entropy:<15.4f}")
    
    print(f"\n统计信息:")
    if vgr_values:
        print(f"  平均VGR: {sum(vgr_values) / len(vgr_values):.4f}")
        print(f"  最大VGR: {max(vgr_values):.4f}")
        print(f"  最小VGR: {min(vgr_values):.4f}")
    else:
        print(f"  VGR: 无数据")
    
    if entropy_values:
        print(f"  平均熵值: {sum(entropy_values) / len(entropy_values):.4f}")
        print(f"  最大熵值: {max(entropy_values):.4f}")
        print(f"  最小熵值: {min(entropy_values):.4f}")
    else:
        print(f"  熵值: 无数据")


def main():
    # 配置
    model_name_or_path = "Qwen/Qwen2.5-VL-7B-Instruct"  # 根据实际情况修改
    dataset_path = "/home/lujunxi57/trl/dataset/aokvqa"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # 系统提示词（和训练时一致）
    SYSTEM_PROMPT = """You are tasked with analyzing an image to answer a question. Your response should include a detailed reasoning process and a concise answer. The reasoning process should be enclosed within <think>...</think> tags, and the final answer should be enclosed within <answer>...</answer> tags. The response format consists of the reasoning section followed by the answer section, with no text outside these tags.

The following example demonstrates the expected response format:
<think>[detailed reasoning process]</think>
<answer>[brief answer]</answer>

THINKING GUIDELINES (write 3-4+ sentences):
1. First, provide an exhaustive and detailed description of the image: extract and describe all possible information including objects, numbers, text, colors, quantities, positions, states, relationships between elements, setting, lighting, and main subjects. Capture every nuance and detail.
2. Then, analyze the detailed description and provide step-by-step reasoning for the given question based on the extracted information and visual evidence.
3. Conclude with a clear answer supported by the visual evidence you identified.

ANSWER GUIDELINES:
• Keep the answer as short as possible - prefer 1-3 words
• Use only essential keywords
• Avoid unnecessary descriptions or modifiers

EXAMPLES:

Question: What is the man holding?
<think>The image shows a man standing outdoors in daylight. He is wearing casual clothing and appears to be in a park setting. In his right hand, he is holding a red disc-shaped object. The object has the characteristic flat, circular shape of a frisbee, commonly used for outdoor recreational activities. The bright red color makes it stand out against the background.</think>
<answer>frisbee</answer>

Think thoroughly and support your answer with visual evidence"""
    
    print("="*80)
    print("开始推理脚本")
    print("="*80)
    
    # 1. 加载数据集
    print("\n1. 加载数据集...")
    dataset = load_dataset(dataset_path, split="train")
    first_sample = dataset[0]
    print(f"数据集大小: {len(dataset)}")
    print(f"第一个样本的keys: {first_sample.keys()}")
    
    # 2. 加载模型和processor（需要在处理prompt之前加载）
    print("\n2. 加载模型和processor...")
    model, processor = load_model_and_processor(model_name_or_path, device)
    
    # 3. 获取prompt和image，并添加系统提示词
    if "prompt" in first_sample:
        prompt = first_sample["prompt"]
        # 如果prompt是列表格式（对话格式），检查是否已有system角色
        if isinstance(prompt, list):
            # 检查是否已有system角色
            has_system = any(msg.get("role") == "system" for msg in prompt if isinstance(msg, dict))
            if not has_system:
                # 在开头添加系统提示词
                prompt = [{"role": "system", "content": SYSTEM_PROMPT}] + prompt
            prompt_for_display = apply_chat_template({"prompt": prompt}, processor)["prompt"]
        else:
            prompt_for_display = prompt
            prompt = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
    elif "problem" in first_sample:
        prompt_text = first_sample["problem"]
        prompt = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text}
        ]
        prompt_for_display = prompt_text
    else:
        raise ValueError("数据集中没有找到prompt或problem字段")
    
    image = first_sample.get("image", None)
    if image is None:
        print("警告: 数据集中没有image字段")
    
    print(f"\nPrompt: {prompt_for_display}")
    if image:
        print(f"Image size: {image.size}")
    
    # 4. 准备生成配置（和训练时一致）
    generation_config = GenerationConfig(
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=processor.tokenizer.pad_token_id,
        eos_token_id=processor.tokenizer.eos_token_id,
        bos_token_id=processor.tokenizer.bos_token_id,
    )
    
    # 5. 进行两次推理
    results = []
    for run_id in [1, 2]:
        print(f"\n{'='*80}")
        print(f"开始第 {run_id} 次推理...")
        print(f"{'='*80}")
        
        # 生成（使用prompt列表格式，和训练时一致）
        output = generate_with_attention(
            model=model,
            processor=processor,
            prompt=prompt,
            image=image,
            generation_config=generation_config,
            max_prompt_length=2048,
            last_k_layers=6,
        )
        
        # 解码生成的文本
        completion_ids_list = output["completion_ids_list"]
        vocab_size = len(processor.tokenizer)
        completion_ids_filtered = [
            [token_id for token_id in ids if 0 <= token_id < vocab_size] 
            for ids in completion_ids_list
        ]
        completion_text = processor.batch_decode(
            completion_ids_filtered,
            skip_special_tokens=True
        )[0]
        
        # 计算VGR指标
        print("计算VGR指标...")
        try:
            # 使用attention_context，和训练时一致
            attention_context = output.get("attention_context")
            if attention_context:
                from src.utils.attention_metrics import process_attention_context
                
                # 准备args对象（模拟训练时的args）
                class Args:
                    token_weights = True
                    attention_last_k_layers = 6
                    token_weights_smooth_sigma = 0.0
                    token_weights_clip = (0.2, 3.0)
                
                args = Args()
                
                # 使用process_attention_context处理attention，和训练时一致
                tw_list = process_attention_context(
                    attention_context=attention_context,
                    model=model,
                    processor=processor,
                    args=args,
                    attention_deque=None,
                    attention_skip_reasons_deque=None,
                    token_weights_deque=None,
                )
                
                # 如果tw_list不为None，说明token_weights已计算
                # 我们需要从attention_context中提取vgr值
                # 或者直接使用build_token_vgr_weights_for_batch
                attentions = output["attentions"]
                if attentions and len(attentions) > 0:
                    input_ids = output["input_ids"]
                    sequences = output["generated_ids"]
                    image_grid_thw = output.get("image_grid_thw")
                    
                    # 计算VGR weights
                    weights, debug = build_token_vgr_weights_for_batch(
                        outputs_attentions=attentions,
                        input_ids=input_ids,
                        sequences=sequences,
                        processor=processor,
                        image_grid_thw=image_grid_thw,
                        last_k_layers=6,
                    )
                    
                    vgr_values = debug["vgr_token"][0] if debug["vgr_token"] and len(debug["vgr_token"]) > 0 else []
                else:
                    vgr_values = []
            else:
                print("警告: 无法获取attention_context，VGR计算失败")
                vgr_values = []
        except Exception as e:
            print(f"计算VGR时出错: {e}")
            import traceback
            traceback.print_exc()
            vgr_values = []
        
        # 计算熵值
        print("计算熵值...")
        logits = output["logits"]
        if logits is not None:
            print(f"  logits shape: {logits.shape}")
            print(f"  logits dtype: {logits.dtype}")
            nan_count = torch.isnan(logits).sum().item()
            inf_count = torch.isinf(logits).sum().item()
            print(f"  logits contains nan: {nan_count > 0} (count: {nan_count})")
            print(f"  logits contains inf: {inf_count > 0} (count: {inf_count})")
            
            # 检查logits的有效性并清理
            if torch.isnan(logits).any() or torch.isinf(logits).any():
                print("  警告: logits包含nan或inf值，正在清理...")
                # 使用clamp限制logits的范围，避免inf值
                # 先找到非inf的最大值和最小值
                finite_logits = logits[torch.isfinite(logits)]
                if len(finite_logits) > 0:
                    max_val = finite_logits.max().item()
                    min_val = finite_logits.min().item()
                    # 将inf替换为有限值（使用max+100作为上界，min-100作为下界）
                    logits = torch.clamp(logits, min=min_val - 100, max=max_val + 100)
                    # 将nan替换为0
                    logits = torch.where(torch.isnan(logits), torch.zeros_like(logits), logits)
                    print(f"  清理后: nan={torch.isnan(logits).sum().item()}, inf={torch.isinf(logits).sum().item()}")
                else:
                    print("  错误: 所有logits都是nan或inf，无法计算熵值")
                    entropy_values = []
                    # 继续处理，但熵值为空
            
            entropy_per_token = compute_entropy_per_token(logits)
            if entropy_per_token is not None:
                print(f"  entropy_per_token shape: {entropy_per_token.shape}")
                print(f"  entropy_per_token contains nan: {torch.isnan(entropy_per_token).any().item()}")
                print(f"  entropy_per_token range: [{entropy_per_token.min().item():.4f}, {entropy_per_token.max().item():.4f}]")
                entropy_values = entropy_per_token[0].cpu().tolist()  # 取第一个batch
            else:
                print("  警告: entropy_per_token为None")
                entropy_values = []
        else:
            print("警告: 无法获取logits，熵值计算失败")
            entropy_values = []
        
        # 解码token文本（用于显示）
        completion_ids_list = output["completion_ids_list"]
        if completion_ids_list and len(completion_ids_list) > 0:
            # 将每个token单独解码
            token_texts = []
            for token_id in completion_ids_list[0]:
                token_text = processor.tokenizer.decode([token_id], skip_special_tokens=False)
                token_texts.append(token_text)
        else:
            token_texts = None
        
        # 保存结果
        results.append({
            "run_id": run_id,
            "completion_text": completion_text,
            "vgr_values": vgr_values,
            "entropy_values": entropy_values,
            "token_texts": token_texts,
        })
        
        # 格式化输出
        format_results(run_id, completion_text, vgr_values, entropy_values, token_texts)
    
    # 5. 对比两次推理的结果
    print(f"\n{'='*80}")
    print("两次推理结果对比")
    print(f"{'='*80}")
    
    if len(results) == 2:
        r1, r2 = results[0], results[1]
        print(f"\n生成文本对比:")
        print(f"  推理1: {r1['completion_text'][:100]}...")
        print(f"  推理2: {r2['completion_text'][:100]}...")
        
        if r1['vgr_values'] and r2['vgr_values']:
            print(f"\nVGR指标对比:")
            print(f"  推理1平均VGR: {sum(r1['vgr_values']) / len(r1['vgr_values']):.4f}")
            print(f"  推理2平均VGR: {sum(r2['vgr_values']) / len(r2['vgr_values']):.4f}")
        
        if r1['entropy_values'] and r2['entropy_values']:
            print(f"\n熵值对比:")
            print(f"  推理1平均熵值: {sum(r1['entropy_values']) / len(r1['entropy_values']):.4f}")
            print(f"  推理2平均熵值: {sum(r2['entropy_values']) / len(r2['entropy_values']):.4f}")
    
    print("\n脚本执行完成！")


if __name__ == "__main__":
    main()

