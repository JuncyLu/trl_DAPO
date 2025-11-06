#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Merge multiple Parquet files (with embedded images) into a single Parquet.

python src/data/merge_parquet.py \
  --inputs dataset/aokvqa_openr1/train/train-00000-of-00001.parquet \
           dataset/visrag_arxivqa_openr1/train/train-00000-of-00001.parquet \
           dataset/mmmu_pro_4opt_openr1/train/standard_4_options_test-00000-of-00001.parquet \
  --output DDM/train/train-00000-of-00001.parquet
"""

import os
import argparse

from datasets import load_dataset, concatenate_datasets

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="Merge multiple parquet files into one.")
    parser.add_argument("--inputs", nargs="+", required=True, help="Input parquet file paths.")
    parser.add_argument("--output", required=True, help="Output parquet file path.")
    args = parser.parse_args()

    if not args.inputs:
        raise ValueError("No input parquet files provided.")

    base = load_dataset("parquet", data_files=args.inputs[0])["train"]
    ds_list = [base]

    for p in args.inputs[1:]:
        ds = load_dataset("parquet", data_files=p)["train"]
        if ds.features != base.features:
            ds = ds.cast(base.features)
        ds_list.append(ds)

    merged = concatenate_datasets(ds_list)

    out_dir = os.path.dirname(args.output) or "."
    ensure_dir(out_dir)
    merged.to_parquet(args.output)

    print(f"[OK] Wrote {len(merged)} rows to {args.output}")

if __name__ == "__main__":
    main()


