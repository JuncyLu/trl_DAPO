#!/usr/bin/env python3
"""
Split DMD dataset into SFT and RL training sets and store them as Parquet files.

This script loads the lujunxi57/DMD dataset from HuggingFace and splits it into:
- 30% for SFT (supervised fine-tuning)
- 70% for RL (reinforcement learning) training

python split_dmd_dataset.py \
  --dataset_name lujunxi57/DMD \
  --sft_ratio 0.3 \
  --output_dir ./dataset/dmd_split \
  --seed 42

"""

import argparse
import shutil
from datasets import load_dataset
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Split DMD dataset into SFT and RL sets")
    parser.add_argument(
        "--dataset_name",
        type=str,
        default="lujunxi57/DMD",
        help="HuggingFace dataset name or path"
    )
    parser.add_argument(
        "--sft_ratio",
        type=float,
        default=0.3,
        help="Ratio of data for SFT (default: 0.3)"
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="./dataset/dmd_split",
        help="Output directory to save the split datasets"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility (default: 42)"
    )
    parser.add_argument(
        "--split_name",
        type=str,
        default="train",
        help="Name of the split to load from dataset (default: 'train')"
    )
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Loading dataset: {args.dataset_name}")
    print(f"Split: {args.split_name}")
    print(f"SFT ratio: {args.sft_ratio}")
    print(f"RL ratio: {1 - args.sft_ratio}")
    print(f"Random seed: {args.seed}")
    print(f"Output directory: {output_dir}")
    print("-" * 60)
    
    # Load dataset
    try:
        dataset = load_dataset(args.dataset_name, split=args.split_name)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        print("Trying to load without specifying split...")
        dataset_dict = load_dataset(args.dataset_name)
        if args.split_name in dataset_dict:
            dataset = dataset_dict[args.split_name]
        else:
            # Use the first available split
            available_splits = list(dataset_dict.keys())
            print(f"Available splits: {available_splits}")
            if available_splits:
                dataset = dataset_dict[available_splits[0]]
                print(f"Using split: {available_splits[0]}")
            else:
                raise ValueError(f"No splits found in dataset {args.dataset_name}")
    
    total_size = len(dataset)
    print(f"Total dataset size: {total_size} samples")
    
    # Split dataset
    sft_size = int(total_size * args.sft_ratio)
    rl_size = total_size - sft_size
    
    print(f"\nSplitting dataset:")
    print(f"  SFT set: {sft_size} samples ({args.sft_ratio * 100:.1f}%)")
    print(f"  RL set: {rl_size} samples ({(1 - args.sft_ratio) * 100:.1f}%)")
    
    # Split with train_test_split
    split_result = dataset.train_test_split(
        test_size=args.sft_ratio,
        seed=args.seed,
        shuffle=True
    )
    
    # Note: train_test_split returns 'train' and 'test'
    # We want: 'test' -> SFT, 'train' -> RL
    sft_dataset = split_result['test']  # Smaller portion for SFT
    rl_dataset = split_result['train']  # Larger portion for RL
    
    print(f"\nActual split sizes:")
    print(f"  SFT set: {len(sft_dataset)} samples")
    print(f"  RL set: {len(rl_dataset)} samples")
    
    # Save datasets as parquet for downstream consumption
    sft_path = output_dir / "dmd_sft.parquet"
    rl_path = output_dir / "dmd_rl.parquet"
    
    # Remove old Arrow directories if they exist to avoid confusion
    for path in (sft_path, rl_path):
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
    
    print(f"\nSaving datasets as Parquet...")
    sft_dataset.to_parquet(str(sft_path))
    print(f"  SFT dataset saved to: {sft_path}")
    
    rl_dataset.to_parquet(str(rl_path))
    print(f"  RL dataset saved to: {rl_path}")
    
    # Print dataset info
    print(f"\nDataset structure:")
    print(f"  SFT dataset features: {sft_dataset.features}")
    print(f"  RL dataset features: {rl_dataset.features}")
    
    # Print sample from each split
    print(f"\nSample from SFT dataset:")
    print(sft_dataset[0])
    
    print(f"\nSample from RL dataset:")
    print(rl_dataset[0])
    
    print("\n" + "=" * 60)
    print("Dataset splitting completed successfully!")
    print("=" * 60)
    print(f"\nTo use the datasets in Python:")
    print(f"  from datasets import Dataset")
    print(f"  sft_dataset = Dataset.from_parquet('{sft_path}')")
    print(f"  rl_dataset = Dataset.from_parquet('{rl_path}')")


if __name__ == "__main__":
    main()
