#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Convert openbmb/VisRAG-Ret-Test-ArxivQA to parquet with embedded images.
Output columns: image, problem, solution.

python src/data/dataset_visrag_arxivqa.py \
  --out_dir ./dataset/visrag_arxivqa_openr1 \
  --split train
"""

import os
import argparse
import re
from typing import Any, List

from datasets import load_dataset, Dataset, Features, Value, Image
from PIL import Image as PILImage
from tqdm import tqdm

DS_NAME = "openbmb/VisRAG-Ret-Test-ArxivQA"

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def to_list(x: Any) -> List[str]:
    if x is None:
        return []
    if isinstance(x, list):
        return [str(i) for i in x]
    return [str(x)]

def clean_choices(choices: List[str]) -> List[str]:
    cleaned = []
    for c in choices:
        s = str(c).strip()
        if not s or s == "-" or s.startswith("##"):
            continue
        s = re.sub(r'^[A-Z][\)\.]\s+', '', s)
        s = re.sub(r'^[A-Z]\s+', '', s)
        s = s.strip()
        if not s or s == "-" or s.startswith("##"):
            continue
        cleaned.append(s)
    return cleaned

def format_problem(question: str, choices: List[str]) -> str:
    if not choices:
        return (question or "").strip()
    labels = [chr(65 + i) for i in range(len(choices))]
    parts = [question.strip()] + [f"{lbl}: {c}" for lbl, c in zip(labels, choices)]
    return "\n".join(parts)

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

def resize_image(img, max_size=1024):
    if img is None:
        return None
    if isinstance(img, PILImage.Image):
        pil_img = img
    elif hasattr(img, 'convert'):
        pil_img = img.convert('RGB')
    else:
        return None
    width, height = pil_img.size
    if max(width, height) <= max_size:
        return pil_img
    if width > height:
        new_width = max_size
        new_height = int(height * max_size / width)
    else:
        new_height = max_size
        new_width = int(width * max_size / height)
    return pil_img.resize((new_width, new_height), PILImage.Resampling.LANCZOS)

def convert_split(split: str, out_dir: str) -> int:
    print(f"[INFO] Loading {DS_NAME} (split={split})")
    corpus = load_dataset(DS_NAME, name="corpus", split=split)
    queries = load_dataset(DS_NAME, name="queries", split=split)
    qrels = load_dataset(DS_NAME, name="qrels", split=split)

    pid2img = {}
    for ex in tqdm(corpus, desc="Indexing corpus"):
        pid = str(ex.get("corpus-id", ""))
        if pid:
            pid2img[pid] = ex.get("image", None)

    qid2pids = {}
    for ex in qrels:
        qid = str(ex.get("query-id", ""))
        pid = str(ex.get("corpus-id", ""))
        score = ex.get("score", 0)
        if qid and pid and isinstance(score, (int, float)) and score > 0:
            qid2pids.setdefault(qid, []).append(pid)

    parquet_dir = os.path.join(out_dir, "train")
    ensure_dir(parquet_dir)

    records = []
    written = 0

    for ex in tqdm(queries, desc=f"Converting {split}"):
        qid = str(ex.get("query-id", ""))
        pos_pids = qid2pids.get(qid, [])
        if not pos_pids or len(pos_pids) > 1:
            continue
        img = pid2img.get(pos_pids[0], None)
        if img is None:
            continue
        
        img = resize_image(img)
        if img is None:
            continue

        question = ex.get("query", "")
        answer = ex.get("answer", "")
        choices = clean_choices(to_list(ex.get("options", [])))

        problem = format_problem(question, choices)
        if len(problem) > 700:
            continue
        
        solution = pick_solution(answer, choices)

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
    parser = argparse.ArgumentParser(description="Convert VisRAG-Ret-Test-ArxivQA to parquet with embedded images.")
    parser.add_argument("--out_dir", type=str, required=True, help="Output directory.")
    parser.add_argument("--split", type=str, default="train", help="Split name (default: train).")
    args = parser.parse_args()

    ensure_dir(args.out_dir)
    total = convert_split(split=args.split, out_dir=args.out_dir)
    print(f"[DONE] Total written: {total}")

if __name__ == "__main__":
    main()
