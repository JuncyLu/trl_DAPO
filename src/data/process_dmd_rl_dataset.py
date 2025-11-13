#!/usr/bin/env python3
"""Filter and resize records in dataset/dmd_split/dmd_rl.parquet.
python process_dmd_rl_dataset.py --output dataset/dmd_split/dmd_rl_filtered.parquet
"""

from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path
from typing import Iterable

import pyarrow as pa
import pyarrow.parquet as pq

try:
    from PIL import Image
except ModuleNotFoundError as exc:  # pragma: no cover - pillow is required for resizing
    raise SystemExit("Pillow is required for this script: pip install Pillow") from exc


def default_input_path() -> Path:
    repo_root = Path(__file__).resolve().parent
    return repo_root / "dataset" / "dmd_split" / "dmd_rl.parquet"


def derive_output_path(input_path: Path) -> Path:
    return input_path.with_name(f"{input_path.stem}_filtered{input_path.suffix}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Filter long problems and resize oversized images in a Parquet file.")
    parser.add_argument("--input", type=Path, default=None, help="Path to the source Parquet file.")
    parser.add_argument("--output", type=Path, default=None, help="Path to write the processed Parquet file.")
    parser.add_argument(
        "--max-problem-length",
        type=int,
        default=500,
        help="Maximum allowed number of characters in problem field (inclusive).",
    )
    parser.add_argument(
        "--max-image-side",
        type=int,
        default=640,
        help="Scale images so that their longest side does not exceed this value.",
    )
    return parser.parse_args()


def infer_format_from_path(path: str | None, fallback: str = "PNG") -> str:
    if not path:
        return fallback
    suffix = Path(path).suffix.lower()
    mapping = {
        ".jpg": "JPEG",
        ".jpeg": "JPEG",
        ".png": "PNG",
        ".bmp": "BMP",
        ".webp": "WEBP",
    }
    return mapping.get(suffix, fallback)


def resize_image_bytes(
    image_bytes: bytes | None, image_path: str | None, max_side: int
) -> tuple[bytes | None, bool]:
    if image_bytes is None:
        return None, False

    with Image.open(io.BytesIO(image_bytes)) as img:
        width, height = img.size
        longest_side = max(width, height)
        if longest_side <= max_side:
            return image_bytes, False

        scale = max_side / float(longest_side)
        new_size = (
            max(1, int(round(width * scale))),
            max(1, int(round(height * scale))),
        )
        resampling = getattr(Image, "Resampling", Image).LANCZOS
        resized_img = img.resize(new_size, resampling)

        format_hint = (img.format or "").upper() or infer_format_from_path(image_path)
        if format_hint in {"JPEG", "JPG"} and resized_img.mode in {"RGBA", "LA", "P"}:
            resized_img = resized_img.convert("RGB")

        buffer = io.BytesIO()
        resized_img.save(buffer, format=format_hint)
        return buffer.getvalue(), True


def rows_to_arrow_table(
    rows: Iterable[dict],
    schema: pa.Schema,
    image_struct_type: pa.StructType,
    *,
    problem_idx: int,
    solution_idx: int,
) -> pa.Table:
    materialized = list(rows)
    if not materialized:
        return pa.Table.from_arrays([], schema=schema).slice(0, 0)

    image_bytes = [row["image_bytes"] for row in materialized]
    image_paths = [row["image_path"] for row in materialized]
    problems = [row["problem"] for row in materialized]
    solutions = [row["solution"] for row in materialized]

    struct_array = pa.StructArray.from_arrays(
        [
            pa.array(image_bytes, type=image_struct_type.field(0).type),
            pa.array(image_paths, type=image_struct_type.field(1).type),
        ],
        fields=image_struct_type,
    )

    return pa.Table.from_arrays(
        [
            struct_array,
            pa.array(problems, type=schema.field(problem_idx).type),
            pa.array(solutions, type=schema.field(solution_idx).type),
        ],
        schema=schema,
    )


def main() -> None:
    args = parse_args()
    input_path = (args.input or default_input_path()).expanduser()
    output_path = (args.output or derive_output_path(input_path)).expanduser()

    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    if output_path == input_path:
        print("Input and output paths are identical. Specify a different --output.", file=sys.stderr)
        sys.exit(1)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    parquet_file = pq.ParquetFile(input_path)
    schema = parquet_file.schema_arrow
    image_idx = schema.get_field_index("image")
    problem_idx = schema.get_field_index("problem")
    solution_idx = schema.get_field_index("solution")

    if -1 in {image_idx, problem_idx, solution_idx}:
        print("Schema does not contain expected fields: image, problem, solution.", file=sys.stderr)
        sys.exit(1)

    image_struct_type = schema.field(image_idx).type

    writer = pq.ParquetWriter(output_path, schema=schema, compression="snappy")

    total_rows = 0
    kept_rows = 0
    dropped_long_problem = 0
    resized_images = 0

    try:
        for row_group_idx in range(parquet_file.num_row_groups):
            table = parquet_file.read_row_group(row_group_idx)
            rows = table.to_pylist()
            chunk_buffer = []

            for row in rows:
                total_rows += 1
                problem = row.get("problem")
                if problem is not None and len(problem) > args.max_problem_length:
                    dropped_long_problem += 1
                    continue

                image = row.get("image") or {}
                image_bytes = image.get("bytes")
                image_path = image.get("path")
                processed_bytes, was_resized = resize_image_bytes(image_bytes, image_path, args.max_image_side)
                if was_resized:
                    resized_images += 1

                chunk_buffer.append(
                    {
                        "image_bytes": processed_bytes,
                        "image_path": image_path,
                        "problem": problem,
                        "solution": row.get("solution"),
                    }
                )

            if chunk_buffer:
                writer.write_table(
                    rows_to_arrow_table(
                        chunk_buffer,
                        schema,
                        image_struct_type,
                        problem_idx=problem_idx,
                        solution_idx=solution_idx,
                    )
                )
                kept_rows += len(chunk_buffer)
    finally:
        writer.close()

    print(f"Input rows: {total_rows}")
    print(f"Dropped (problem too long): {dropped_long_problem}")
    print(f"Kept rows: {kept_rows}")
    print(f"Resized images: {resized_images}")
    print(f"Written to: {output_path}")


if __name__ == "__main__":
    main()
