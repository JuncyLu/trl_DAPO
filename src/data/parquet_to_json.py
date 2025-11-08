#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Convert parquet file to JSON for viewing prompts.

Usage:
    python src/data/parquet_to_json.py \
        --input ./dataset/visrag_arxivqa_openr1/train/train-00000-of-00001.parquet \
        --output ./visrag_arxivqa_prompts.json
"""

import os
import json
import argparse
import base64
from io import BytesIO
from typing import Any, Dict

from datasets import load_dataset
from PIL import Image as PILImage
from tqdm import tqdm

def image_to_base64(img: Any) -> str:
    """Convert PIL Image to base64 string."""
    if img is None:
        return ""
    if isinstance(img, PILImage.Image):
        pil_img = img
    elif hasattr(img, 'convert'):
        pil_img = img.convert('RGB')
    else:
        return ""
    
    buffer = BytesIO()
    pil_img.save(buffer, format='PNG')
    img_bytes = buffer.getvalue()
    return base64.b64encode(img_bytes).decode('utf-8')

def image_to_metadata(img: Any) -> Dict[str, Any]:
    """Extract metadata from PIL Image."""
    if img is None:
        return {"width": 0, "height": 0, "mode": "unknown"}
    if isinstance(img, PILImage.Image):
        pil_img = img
    elif hasattr(img, 'convert'):
        pil_img = img.convert('RGB')
    else:
        return {"width": 0, "height": 0, "mode": "unknown"}
    
    return {
        "width": pil_img.width,
        "height": pil_img.height,
        "mode": pil_img.mode,
        "format": pil_img.format or "unknown"
    }

def convert_parquet_to_json(
    parquet_path: str,
    output_path: str,
    include_image_base64: bool = False,
    include_image_metadata: bool = True
) -> int:
    """Convert parquet file to JSON."""
    print(f"[INFO] Loading parquet file: {parquet_path}")
    ds = load_dataset("parquet", data_files=parquet_path, split="train")
    
    print(f"[INFO] Converting {len(ds)} examples to JSON...")
    records = []
    
    for i, ex in enumerate(tqdm(ds, desc="Converting")):
        record = {
            "index": i,
            "problem": ex.get("problem", ""),
            "solution": ex.get("solution", "")
        }
        
        if include_image_metadata:
            img = ex.get("image", None)
            record["image_metadata"] = image_to_metadata(img)
        
        if include_image_base64:
            img = ex.get("image", None)
            record["image_base64"] = image_to_base64(img)
        
        records.append(record)
    
    print(f"[INFO] Writing {len(records)} records to {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] Wrote {len(records)} examples to {output_path}")
    return len(records)

def main():
    parser = argparse.ArgumentParser(description="Convert parquet file to JSON for viewing prompts.")
    parser.add_argument("--input", type=str, required=True, help="Input parquet file path.")
    parser.add_argument("--output", type=str, required=True, help="Output JSON file path.")
    parser.add_argument("--include_image_base64", action="store_true", 
                        help="Include image as base64 string (makes file large).")
    parser.add_argument("--no_image_metadata", action="store_true",
                        help="Don't include image metadata (width, height, etc.).")
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"[ERROR] Input file not found: {args.input}")
        return
    
    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    total = convert_parquet_to_json(
        parquet_path=args.input,
        output_path=args.output,
        include_image_base64=args.include_image_base64,
        include_image_metadata=not args.no_image_metadata
    )
    print(f"[DONE] Total converted: {total}")

if __name__ == "__main__":
    main()



