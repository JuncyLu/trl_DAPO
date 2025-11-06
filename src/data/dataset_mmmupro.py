#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Convert MMMU/MMMU_Pro (Standard: 4 or 10 options) to parquet with embedded images.
Output columns: image, problem, solution.

python src/data/dataset_mmmupro.py \
  --subset "standard (4 options)" \
  --out_dir ./dataset/mmmu_pro_4opt_openr1
"""

import os
import argparse
import ast
from typing import Any, List

from datasets import load_dataset, Dataset, Features, Value, Image
from tqdm import tqdm

DS_NAME = "MMMU/MMMU_Pro"

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

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

def parse_options(x: Any) -> List[str]:
    if x is None:
        return []
    if isinstance(x, list):
        return [str(i).strip() for i in x if str(i).strip()]
    if isinstance(x, str):
        s = x.strip()
        if s.startswith("[") and s.endswith("]"):
            try:
                parsed = ast.literal_eval(s)
                if isinstance(parsed, list):
                    return [str(i).strip() for i in parsed if str(i).strip()]
            except Exception:
                pass
        return [s] if s else []
    return [str(x).strip()] if str(x).strip() else []

def pick_solution(answer: str, choices: List[str]) -> str:
    if not answer:
        return ""
    ans = answer.strip().upper()
    if len(ans) == 1 and "A" <= ans <= "Z":
        return ans
    ans_lower = ans.lower()
    for i, c in enumerate(choices):
        if ans_lower == c.lower().strip():
            return chr(65 + i)
    return answer.strip()

def convert_split(subset: str, split: str, out_dir: str) -> int:
    print(f"[INFO] Loading {DS_NAME} (subset={subset}, split={split})")
    ds = load_dataset(DS_NAME, subset, split=split)

    parquet_dir = os.path.join(out_dir, "train")
    ensure_dir(parquet_dir)

    records = []
    written = 0

    for ex in tqdm(ds, desc=f"Converting {subset}/{split}"):
        img = None
        for k in [f"image_{i}" for i in range(1, 8)] + ["image"]:
            if k in ex and ex[k] is not None:
                img = ex[k]
                break
        if img is None:
            continue

        question = ex.get("question", "")
        options = parse_options(ex.get("options", []))
        answer = ex.get("answer", "")

        problem = format_problem(question, options)
        solution = pick_solution(answer, options)

        records.append({
            "image": img,
            "problem": problem,
            "solution": solution
        })
        written += 1

    if not records:
        print(f"[WARN] No valid records for subset={subset}, split={split}")
        return 0

    features = Features({
        "image": Image(),
        "problem": Value("string"),
        "solution": Value("string"),
    })
    ds_out = Dataset.from_list(records, features=features)

    safe_subset = subset.replace("/", "_").replace(" ", "_").replace("(", "").replace(")", "")
    parquet_path = os.path.join(parquet_dir, f"{safe_subset}_{split}-00000-of-00001.parquet")
    ds_out.to_parquet(parquet_path)

    print(f"[OK] Wrote {written} examples to {parquet_path}")
    return written

def main():
    parser = argparse.ArgumentParser(description="Convert MMMU-Pro to parquet with embedded images.")
    parser.add_argument("--subset", type=str, required=True,
                        choices=["standard (4 options)", "standard (10 options)"],
                        help="MMMU_Pro subset name.")
    parser.add_argument("--split", type=str, default="test", help="Split name (default: test).")
    parser.add_argument("--out_dir", type=str, required=True, help="Output directory.")
    args = parser.parse_args()

    ensure_dir(args.out_dir)
    total = convert_split(subset=args.subset, split=args.split, out_dir=args.out_dir)
    print(f"[DONE] Total written: {total}")

if __name__ == "__main__":
    main()
