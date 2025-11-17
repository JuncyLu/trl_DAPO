#!/usr/bin/env python3
"""
将 A-OKVQA 数据集转换成与 DMD 数据集相同 schema 的 Parquet（image/problem/solution）。

特点：
- 直接使用 HuggingFaceM4/A-OKVQA 中自带的图像字段（无需本地 COCO 路径）
- image 列输出 struct { bytes, path }，与 dmd_rl.parquet 对齐
- solution 取 direct_answers 的首个非空答案
python3 src/data/convert_aokvqa_to_parquet.py \
    --split train \
    --out_path dataset/aokvqa/train/aokvqa_dmd.parquet \
    --question_id_path A-OKVQA_question_id.txt
"""

from __future__ import annotations

import argparse
import ast
from pathlib import Path
from typing import Dict, List, Optional, Set

from datasets import Dataset, Features, Image, Value, load_dataset
from tqdm import tqdm


def read_image_bytes(path: Optional[str]) -> Optional[bytes]:
    """如果路径存在则读取图片二进制，否则返回 None。"""
    if not path:
        return None
    try:
        with open(path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        return None


def normalize_answers(value) -> List[str]:
    """将 direct_answers 字段整理成字符串列表。"""
    if isinstance(value, list):
        answers = value
    elif isinstance(value, str):
        text = value.strip()
        if text.startswith("[") and text.endswith("]"):
            try:
                parsed = ast.literal_eval(text)
                if isinstance(parsed, list):
                    answers = parsed
                else:
                    answers = [text]
            except Exception:
                answers = [text]
        else:
            answers = [value]
    else:
        answers = []

    cleaned = []
    for ans in answers:
        if isinstance(ans, str):
            ans = ans.strip()
            if ans:
                cleaned.append(ans)
    return cleaned


def load_question_ids(path: Optional[Path]) -> Optional[Set[str]]:
    """读取需要保留的 question_id 列表，返回 set。"""
    if not path:
        return None
    path = path.expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"question_id 列表不存在: {path}")

    ids: Set[str] = set()
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                ids.add(line)
    if not ids:
        raise ValueError(f"question_id 文件为空: {path}")
    return ids


def convert_split(
    split: str,
    dataset_name: str,
    dataset_config: Optional[str],
    keep_ids: Optional[Set[str]],
) -> List[Dict[str, object]]:
    """拉取一个 split 并构造成 DMD schema."""
    if dataset_config:
        ds = load_dataset(dataset_name, dataset_config, split=split)
    else:
        ds = load_dataset(dataset_name, split=split)

    ds = ds.cast_column("image", Image(decode=False))

    rows: List[Dict[str, object]] = []
    for item in tqdm(ds, desc=split):
        question_id = item.get("question_id")
        if keep_ids is not None and question_id not in keep_ids:
            continue

        image_field = item["image"]  # dict: {path, bytes}
        image_bytes = image_field.get("bytes")
        image_path = image_field.get("path")
        if image_bytes is None:
            image_bytes = read_image_bytes(image_path)

        answers = normalize_answers(item.get("direct_answers"))
        # A-OKVQA 有 10 个可接受答案，全部保存用于 VQA 评分
        # 如果不足 10 个，用空字符串填充
        while len(answers) < 10:
            answers.append("")
        # 只保留前 10 个
        solution = answers[:10]

        rows.append({
            "image": {
                "bytes": image_bytes,
                "path": str(Path(image_path).resolve()) if image_path else "",
            },
            "problem": item.get("question", ""),
            "solution": solution,  # list[str] with 10 answers
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert A-OKVQA to DMD-compatible Parquet",
    )
    parser.add_argument(
        "--split",
        nargs="+",
        default=["train"],
        help="要导出的 split，例如 train val test",
    )
    parser.add_argument(
        "--out_path",
        type=Path,
        default=Path("aokvqa_dmd.parquet"),
        help="输出 Parquet 文件路径",
    )
    parser.add_argument(
        "--dataset_name",
        default="HuggingFaceM4/A-OKVQA",
        help="datasets.load_dataset 的数据集名称",
    )
    parser.add_argument(
        "--dataset_config",
        default="",
        help="可选配置名称（默认使用官方 default 配置）",
    )
    parser.add_argument(
        "--question_id_path",
        default="A-OKVQA_question_id.txt",
        help="需要保留的 question_id 列表路径；留空字符串表示使用全部数据",
    )
    args = parser.parse_args()

    dataset_config = args.dataset_config or None
    question_id_path = (
        Path(args.question_id_path.strip()).expanduser()
        if args.question_id_path and args.question_id_path.strip()
        else None
    )
    keep_ids = load_question_ids(question_id_path) if question_id_path else None

    all_rows: List[Dict[str, object]] = []
    for split in args.split:
        rows = convert_split(split, args.dataset_name, dataset_config, keep_ids)
        all_rows.extend(rows)

    # solution 是包含 10 个答案的列表（VQA 标准）
    from datasets import Sequence
    features = Features({
        "image": Image(decode=True),
        "problem": Value("string"),
        "solution": Sequence(Value("string"), length=10),
    })
    hf_dataset = Dataset.from_list(all_rows, features=features)
    hf_dataset.to_parquet(str(args.out_path))
    print(f"写入完成：{len(hf_dataset):,} 条 -> {args.out_path}")


if __name__ == "__main__":
    main()
