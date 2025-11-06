#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Upload Parquet dataset to Hugging Face Hub.

python src/data/upload_to_hf.py \
  --dataset_path DDM/train/train-00000-of-00001.parquet \
  --repo_id lujunxi57/DDM \
  --split train
"""

import argparse
from datasets import load_dataset, DatasetDict
from huggingface_hub import create_repo

def main():
    parser = argparse.ArgumentParser(description="Upload parquet dataset to Hugging Face Hub")
    parser.add_argument("--dataset_path", type=str, required=True,
                        help="Path to the parquet file or directory containing parquet files")
    parser.add_argument("--repo_id", type=str, required=True,
                        help="Hugging Face repository ID (e.g., 'username/dataset-name')")
    parser.add_argument("--split", type=str, default="train",
                        help="Dataset split name (default: 'train')")
    parser.add_argument("--private", action="store_true",
                        help="Make the repository private")
    parser.add_argument("--commit_message", type=str, default="Upload dataset",
                        help="Commit message for the upload")
    args = parser.parse_args()

    print(f"[INFO] Loading dataset from {args.dataset_path}...")
    dataset = load_dataset("parquet", data_files=args.dataset_path)[args.split]
    print(f"[INFO] Dataset loaded: {len(dataset)} examples")

    create_repo(repo_id=args.repo_id, repo_type="dataset", private=args.private, exist_ok=True)
    print(f"[INFO] Uploading to https://huggingface.co/datasets/{args.repo_id}...")

    DatasetDict({args.split: dataset}).push_to_hub(
        repo_id=args.repo_id,
        commit_message=args.commit_message,
        private=args.private
    )

    print(f"[OK] Dataset uploaded successfully!")
    print(f"[OK] View at: https://huggingface.co/datasets/{args.repo_id}")

if __name__ == "__main__":
    main()

