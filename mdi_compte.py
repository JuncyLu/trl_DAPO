import os
import json
import math
import re
from typing import Any, Dict, List, Optional, Tuple

import torch
from datasets import load_dataset, Dataset, DatasetDict
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor

# TRL utilities and rewards
from trl.rewards import think_format_reward
from trl.data_utils import prepare_multimodal_messages
from trl.trainer.attention_metrics import compute_qwen_attention_metrics_for_batch


# Default system prompt (as requested)
SYSTEM_PROMPT = (
    "A conversation between user and assistant. The user asks a question, and the assistant solves it. The "
    "assistant first thinks about the reasoning process in the mind and then provides the user with the answer. "
    "The reasoning process is enclosed within `<think>``</think>` tags, i.e., `<think>`\nThis is my reasoning.\n`</think>`. "
    "For multiple-choice questions (A-J), conclude your response with a single line: 'Answer: X' where X is the "
    "correct option letter."
)


def _safe_to_rgb(img: Image.Image) -> Image.Image:
    if img.mode != "RGB":
        return img.convert("RGB")
    return img


def _resolve_image_path(base_dir: Optional[str], path: str) -> str:
    # If absolute or exists, trust it; otherwise resolve relative to dataset dir
    if os.path.isabs(path) and os.path.exists(path):
        return path
    if os.path.exists(path):
        return path
    if base_dir is not None:
        candidate = os.path.join(base_dir, path)
        if os.path.exists(candidate):
            return candidate
    return path


class MDICompute:
    def __init__(self, model_name: str = "Qwen/Qwen2.5-VL-3B-Instruct", device: Optional[str] = None):
        self.model_name = model_name
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")

        # Generation config mirroring GRPO defaults
        self.generation_config: Dict[str, Any] = {
            "temperature": 1.0,
            "top_p": 1.0,
            "max_completion_length": 1024,
            "max_prompt_length": 2048,
            "output_attentions": True,
            "return_dict_in_generate": True,
        }

        # Initialize model + processor
        torch_dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
        self.processor = AutoProcessor.from_pretrained(self.model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch_dtype,
            device_map="auto" if torch.cuda.is_available() else None,
            trust_remote_code=True,
        )
        self.model.eval()

    # -------------------- Data --------------------
    def load_data(self, dataset_path: str, split_preference: Optional[List[str]] = None) -> Tuple[Dataset, Optional[str]]:
        """
        Load datasets from HF name or local parquet directory.
        Returns a Dataset and a base directory to resolve relative image paths.
        """
        base_dir = None
        if os.path.isdir(dataset_path):
            # Infer parquet files
            mapping = {}
            for name in ["train", "validation", "test", "sample_200"]:
                p = os.path.join(dataset_path, f"{name}.parquet")
                if os.path.isfile(p):
                    mapping[name] = p
            if not mapping:
                raise FileNotFoundError(f"No parquet files found in directory: {dataset_path}")
            ds = load_dataset("parquet", data_files=mapping)
            base_dir = dataset_path
        elif os.path.isfile(dataset_path) and dataset_path.endswith(".parquet"):
            ds = load_dataset("parquet", data_files={"data": dataset_path})
            base_dir = os.path.dirname(os.path.abspath(dataset_path))
        else:
            # HF hub dataset
            ds = load_dataset(dataset_path)

        # Choose split for inference
        if isinstance(ds, DatasetDict):
            order = split_preference or ["test", "validation", "sample_200", "train"]
            pick = next((s for s in order if s in ds), None)
            if pick is None:
                pick = next(iter(ds.keys()))
            dataset = ds[pick]
        else:
            dataset = ds
        return dataset, base_dir

    def preprocess_data(self, dataset: Dataset, base_dir: Optional[str]) -> Dataset:
        """Convert images to RGB, build conversation messages with system+user and keep label index."""

        def _filter_big_images(ex):
            # Accept either 'image' dict with path, or 'image_path'
            if "image_path" in ex and ex["image_path"]:
                p = _resolve_image_path(base_dir, ex["image_path"]) if base_dir else ex["image_path"]
                try:
                    with Image.open(p) as im:
                        w, h = im.size
                    return w < 1024 and h < 1024
                except Exception:
                    return False
            elif "image" in ex and isinstance(ex["image"], Image.Image):
                w, h = ex["image"].size
                return w < 1024 and h < 1024
            return True

        def _load_and_rgb(ex):
            if "image_path" in ex and ex["image_path"]:
                p = _resolve_image_path(base_dir, ex["image_path"]) if base_dir else ex["image_path"]
                try:
                    im = Image.open(p)
                    ex["image"] = _safe_to_rgb(im)
                except Exception:
                    ex["image"] = None
            elif "image" in ex and isinstance(ex["image"], Image.Image):
                ex["image"] = _safe_to_rgb(ex["image"])
            return ex

        def _build_messages(ex):
            # Determine user content field
            if "prompt" in ex and isinstance(ex["prompt"], str):
                user_content = ex["prompt"]
            elif "problem" in ex and isinstance(ex["problem"], str):
                user_content = ex["problem"]
            else:
                # Fallback assemble from question/choices
                q = ex.get("question", "").strip()
                choices = ex.get("choices", [])
                letters = [f"{chr(ord('A') + i)}. {c}" for i, c in enumerate(choices)]
                choices_text = "\n".join(letters)
                user_content = f"Question: {q}\nChoices:\n{choices_text}\nPlease select the correct answer."

            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_content},
            ]
            ex["messages"] = messages
            return ex

        dataset = dataset.filter(_filter_big_images)
        dataset = dataset.map(_load_and_rgb)
        dataset = dataset.map(_build_messages)
        return dataset

    # -------------------- Generation --------------------
    @torch.inference_mode()
    def generate_completions(self, prompts: List[List[Dict[str, Any]]], images: Optional[List[List[Image.Image]]]) -> Tuple[List[str], Dict[str, Any]]:
        """
        Generate completions replicating GRPO VLM rollout logic for single-turn batches:
        - prepare_multimodal_messages to inject image placeholders
        - apply chat template with add_generation_prompt=True
        - generate with output_attentions=True and return_dict_in_generate=True
        - compute attention metrics (MDI) from outputs.attentions
        Returns (completions_text, diagnostics)
        """
        # Prepare multimodal prompts in-place
        if images is not None:
            for m, img_list in zip(prompts, images):
                prepare_multimodal_messages(m, num_images=len(img_list) if img_list is not None else 0)

        # Build chat-formatted prompt text using model's template
        tokenizer = self.processor if hasattr(self.processor, "apply_chat_template") else self.processor.tokenizer
        prompts_text: List[str] = [
            tokenizer.apply_chat_template(p, add_generation_prompt=True, tokenize=False)
            for p in prompts
        ]

        # Prepare processor inputs
        proc_kwargs = {
            "text": prompts_text,
            "return_tensors": "pt",
            "padding": True,
        }
        if images is not None:
            # Qwen expects list of images per sample under key "images"
            proc_kwargs["images"] = images

        inputs = self.processor(**proc_kwargs)
        inputs = {k: v.to(self.device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

        # Generation kwargs
        gen_kwargs = dict(
            do_sample=True,
            temperature=self.generation_config["temperature"],
            top_p=self.generation_config["top_p"],
            max_new_tokens=self.generation_config["max_completion_length"],
            output_attentions=self.generation_config["output_attentions"],
            return_dict_in_generate=self.generation_config["return_dict_in_generate"],
        )

        outputs = self.model.generate(**inputs, **gen_kwargs)

        # Decode only the generated part
        sequences = outputs.sequences  # [B, prompt+gen]
        input_ids = inputs.get("input_ids")  # [B, prompt]
        completions_text: List[str] = []
        for i in range(sequences.size(0)):
            prompt_len = input_ids[i].size(0)
            gen_ids = sequences[i][prompt_len:]
            text = self.processor.tokenizer.decode(gen_ids, skip_special_tokens=True)
            completions_text.append(text)

        # Compute attention metrics (MDI) using the same utility as trainer
        try:
            # Some processors (Qwen) return image_grid_thw, pass it if present
            image_grid_thw = inputs.get("image_grid_thw")
            if isinstance(image_grid_thw, torch.Tensor):
                image_grid_cpu = image_grid_thw.detach().cpu()
            else:
                image_grid_cpu = None
            attn_results = compute_qwen_attention_metrics_for_batch(
                self.model,
                self.processor,
                outputs.attentions,
                input_ids=input_ids.detach().cpu(),
                sequences=sequences.detach().cpu(),
                image_grid_thw=image_grid_cpu,
            )
        except Exception as e:
            attn_results = []
            print(f"[WARN] Attention metrics computation failed: {e}")

        diagnostics = {
            "prompts_text": prompts_text,
            "attn_results": attn_results,
            "outputs": outputs,  # Keep for upstream use if needed
            "inputs": {k: (v.detach().cpu() if isinstance(v, torch.Tensor) else v) for k, v in inputs.items()},
        }
        return completions_text, diagnostics

    # -------------------- Rewards --------------------
    @staticmethod
    def mc_idx_reward(completions: List[str], label_idx: List[int]) -> List[float]:
        """Multi-choice index reward. Robust extraction of A-J letter, compare to gold index.
        Mirrors examples/scripts/grpo_vlm.py logic.
        """
        scores: List[float] = []
        for comp, idx in zip(completions, label_idx):
            try:
                text = str(comp)
                m = re.search(r"(?i)(?:final\s*answer|answer)\s*[:\-]?\s*([A-J])", text)
                if not m:
                    m = re.search(r"答案\s*[:：]?\s*([A-JＡ-Ｊ])", text)
                if not m:
                    m = re.search(r"选项\s*[:：]?\s*([A-JＡ-Ｊ])", text)
                if not m:
                    m = re.search(r"(?:option|choose|选择)\s*([A-J])", text, flags=re.IGNORECASE)
                if not m:
                    cands = re.findall(r"\b([A-J])\b", text)
                    pred = cands[-1].upper() if cands else None
                else:
                    pred = m.group(1)
                    full2ascii = {
                        "Ａ": "A", "Ｂ": "B", "Ｃ": "C", "Ｄ": "D", "Ｅ": "E",
                        "Ｆ": "F", "Ｇ": "G", "Ｈ": "H", "Ｉ": "I", "Ｊ": "J",
                    }
                    pred = full2ascii.get(pred, pred).upper()
                try:
                    gi = int(idx)
                    gold = chr(ord('A') + gi) if 0 <= gi <= 25 else None
                except Exception:
                    gold = None
                scores.append(1.0 if (pred and gold and pred == gold) else 0.0)
            except Exception:
                scores.append(0.0)
        return scores

    @staticmethod
    def _mdi_balances_from_attention(attn_results: List[Any], ratio_R: float = 2.0) -> List[float]:
        """Compute balance scores from attention MDI metrics like trainer does.
        balance = clip(1 - |log(MDI)| / log(R), 0, 1)
        Prefer 'late' segment; fallback to 'all'. Non-finite MDI -> 0.5 default.
        """
        if ratio_R <= 1.0:
            ratio_R = 2.0
        logR = math.log(float(ratio_R))
        balances: List[float] = []
        for r in attn_results or []:
            seg = getattr(r, "segments", None)
            mdi_val = None
            if isinstance(seg, dict):
                late = seg.get("late")
                allseg = seg.get("all")
                target = late or allseg
                if target is not None:
                    mdi_val = getattr(target, "mdi", None)
            # Fallback default
            if mdi_val is None or not (mdi_val > 0) or not math.isfinite(mdi_val):
                balances.append(0.5)
            else:
                b = max(0.0, min(1.0, 1.0 - abs(math.log(float(mdi_val))) / logR))
                balances.append(float(b))
        # If no results (e.g., no attentions), return empty list (caller handles)
        return balances

    def compute_rewards(
        self,
        completions_text: List[str],
        labels_idx: List[int],
        attn_results: Optional[List[Any]] = None,
        mdi_weight: float = 1.0,
    ) -> Dict[str, List[float]]:
        """Compute mc_idx_reward, think_format_reward, mdi_reward.
        Returns dict with keys: mc_idx_reward, think_format_reward, mdi_reward.
        Note: Weighting (4:1:1) is applied outside this method during aggregation if needed.
        """

        # mc index reward
        mc_scores = self.mc_idx_reward(completions_text, labels_idx)

        # think format reward expects: list[list[{"content": text}]]
        tf_inputs = [[{"content": text}] for text in completions_text]
        tf_scores = think_format_reward(tf_inputs)

        # mdi reward: r = w * (2*balance - 1)
        balances = self._mdi_balances_from_attention(attn_results or [])
        if not balances or len(balances) < len(completions_text):
            balances = [0.5] * len(completions_text)
        mdi_scores = [mdi_weight * (2.0 * float(b) - 1.0) for b in balances[: len(completions_text)]]

        return {
            "mc_idx_reward": mc_scores,
            "think_format_reward": tf_scores,
            "mdi_reward": mdi_scores,
            "mdi_balance": balances[: len(completions_text)],
        }

    # -------------------- Orchestration --------------------
    def run_inference(self, dataset_path: str, output_path: str, batch_size: int = 2):
        """Main inference loop. Saves JSONL with prompts, completions, and reward scores."""
        dataset, base_dir = self.load_data(dataset_path)
        dataset = self.preprocess_data(dataset, base_dir)

        os.makedirs(os.path.dirname(os.path.abspath(output_path)) or ".", exist_ok=True)
        out_f = open(output_path, "w", encoding="utf-8")

        # Extract labels if present
        def _label_of(ex):
            for k in ["label_idx", "answer_idx", "label", "gold_idx", "correct_choice_idx"]:
                if k in ex and ex[k] is not None:
                    try:
                        return int(ex[k])
                    except Exception:
                        continue
            return None

        total = len(dataset) if hasattr(dataset, "__len__") else None
        print(f"[MDICompute] Running inference on {total if total is not None else 'streaming'} samples...")

        def _batched(iterable, n):
            batch = []
            for item in iterable:
                batch.append(item)
                if len(batch) == n:
                    yield batch
                    batch = []
            if batch:
                yield batch

        idx_iter = range(len(dataset)) if total is not None else enumerate(dataset)
        for batch_indices in _batched(idx_iter, batch_size):
            if total is not None:
                batch = [dataset[i] for i in batch_indices]
            else:
                batch = [ex for _, ex in batch_indices]

            # Build per-sample images list (each sample may have 0/1+ images)
            batch_images: List[List[Image.Image]] = []
            for ex in batch:
                if isinstance(ex.get("image"), Image.Image):
                    batch_images.append([ex["image"]])
                else:
                    batch_images.append([])

            # Messages with system+user
            prompts = [ex["messages"] for ex in batch]

            # Generate
            completions_text, diag = self.generate_completions(prompts, batch_images)

            # Labels
            label_idx = [_label_of(ex) for ex in batch]
            label_idx = [i if i is not None else -1 for i in label_idx]

            # Rewards
            rewards = self.compute_rewards(completions_text, label_idx, attn_results=diag.get("attn_results"))

            # Persist per-sample rows
            for i, ex in enumerate(batch):
                row = {
                    "prompt": diag["prompts_text"][i],
                    "completion": completions_text[i],
                    "label_idx": label_idx[i],
                    "rewards": {
                        "mc_idx_reward": rewards["mc_idx_reward"][i],
                        "think_format_reward": rewards["think_format_reward"][i],
                        "mdi_reward": rewards["mdi_reward"][i],
                        "mdi_balance": rewards["mdi_balance"][i],
                    },
                }
                out_f.write(json.dumps(row, ensure_ascii=False) + "\n")
            out_f.flush()

        out_f.close()
        print(f"[MDICompute] Saved results to: {output_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="MDI compute inference replicating GRPO VLM rollout")
    parser.add_argument("--dataset_path", type=str, required=True, help="Dataset path (HF name or parquet dir/file)")
    parser.add_argument("--output_path", type=str, required=True, help="Path to save JSONL results")
    parser.add_argument("--model_name", type=str, default="Qwen/Qwen2.5-VL-3B-Instruct")
    parser.add_argument("--batch_size", type=int, default=2)
    args = parser.parse_args()

    runner = MDICompute(model_name=args.model_name)
    runner.run_inference(dataset_path=args.dataset_path, output_path=args.output_path, batch_size=args.batch_size)

