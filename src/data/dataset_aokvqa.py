#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Convert HuggingFaceM4/A-OKVQA to parquet with embedded images.
Output columns: image, problem, solution.

python src/dataset/dataset_aokvqa.py \
  --splits train \
  --out_dir ./aokvqa_openr1 \
  --question_id_file /home/lujunxi57/trl/A-OKVQA_question_id.txt
"""

import os
import argparse
from typing import List, Any, Optional, Set

from datasets import load_dataset, Dataset, Features, Value, Image
from tqdm import tqdm

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def load_question_ids(question_id_file: str) -> Set[str]:
    if not question_id_file or not os.path.exists(question_id_file):
        return set()
    question_ids = set()
    with open(question_id_file, 'r', encoding='utf-8') as f:
        for line in f:
            qid = line.strip()
            if qid:
                question_ids.add(qid)
    print(f"[INFO] Loaded {len(question_ids)} question_ids from {question_id_file}")
    return question_ids

def to_list(x: Any) -> List[str]:
    if x is None:
        return []
    if isinstance(x, list):
        return [str(i) for i in x]
    return [str(x)]

def format_problem(question: str, choices: List[str]) -> str:
    if not choices:
        return (question or "").strip()
    labels = [chr(65 + i) for i in range(len(choices))]
    parts = [question.strip()] + [f"{lbl}: {c}" for lbl, c in zip(labels, choices)]
    return "\n".join(parts)

def pick_solution(choices: List[str],
                  correct_idx: Optional[int],
                  direct_answers: Any) -> str:
    """
    Priority:
      1) letter option (A, B, C, D) based on correct_idx if valid
      2) first of direct_answers (list or str)
      3) ""
    """
    if choices and correct_idx is not None:
        try:
            idx = int(correct_idx)
            if 0 <= idx < len(choices):
                # 返回字母选项：0->A, 1->B, 2->C, 3->D
                return chr(65 + idx)  # 65 is ASCII for 'A'
        except Exception:
            pass
    das = to_list(direct_answers)
    if das:
        return das[0]
    return ""

# Minimal conversion for current dataset.

def convert_split(ds_name: str,
                  split: str,
                  out_dir: str,
                  question_ids: Optional[Set[str]] = None) -> int:
    """Convert a single split to parquet with embedded images."""
    
    print(f"[INFO] Loading dataset={ds_name} split={split}")
    ds = load_dataset(ds_name, split=split)

    parquet_dir = os.path.join(out_dir, "train")
    ensure_dir(parquet_dir)

    records = []
    written = 0

    for i, ex in enumerate(tqdm(ds, desc=f"Converting {split}")):
        if question_ids is not None and len(question_ids) > 0:
            qid = str(ex.get("question_id", ""))
            if qid not in question_ids:
                continue

        img = ex.get("image", None)
        question = ex.get("question", "")
        choices = ex.get("choices", [])
        correct_idx = ex.get("correct_choice_idx", None)
        direct_answers = ex.get("direct_answers", None)
        # rationale not used

        choices = to_list(choices)

        if img is None:
            continue

        problem = format_problem(question, choices)
        solution = pick_solution(choices, correct_idx, direct_answers)
        records.append({
            "image": img,
            "problem": problem,
            "solution": solution
        })
        written += 1

    if not records:
        print(f"[WARN] No valid records for split={split}")
        return 0

    features = Features({
        "image": Image(),
        "problem": Value("string"),
        "solution": Value("string"),
    })

    ds_out = Dataset.from_list(records, features=features)

    parquet_path = os.path.join(parquet_dir, f"{split}-00000-of-00001.parquet")
    ds_out.to_parquet(parquet_path)

    print(f"[OK] Wrote {written} examples to {parquet_path}")
    return written

def main():
    parser = argparse.ArgumentParser(description="Convert A-OKVQA to parquet with embedded images.")
    parser.add_argument("--dataset_name", type=str, default="HuggingFaceM4/A-OKVQA",
                        help="HF dataset name or local path.")
    parser.add_argument("--splits", type=str, default="train,validation,test",
                        help="Comma-separated splits to convert.")
    parser.add_argument("--out_dir", type=str, required=True,
                        help="Output directory for the Parquet files.")
    parser.add_argument("--question_id_file", type=str, default="",
                        help="Optional path to question_id filter file (one id per line).")
    args = parser.parse_args()

    ensure_dir(args.out_dir)

    # 加载 question_id 筛选列表（可选）
    question_ids = load_question_ids(args.question_id_file) if args.question_id_file else set()

    total = 0
    for split in [s.strip() for s in args.splits.split(",") if s.strip()]:
        total += convert_split(
            ds_name=args.dataset_name,
            split=split,
            out_dir=args.out_dir,
            question_ids=question_ids if question_ids else None,
        )
    print(f"[DONE] Total written: {total}")

if __name__ == "__main__":
    main()
