#!/usr/bin/env python3
"""Trim CSV cells and optionally remove duplicate rows."""

import argparse
import csv
from pathlib import Path

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("output", type=Path)
    p.add_argument("--dedupe", action="store_true")
    args = p.parse_args()
    with args.input.open(newline="", encoding="utf-8-sig") as src:
        reader = csv.DictReader(src)
        fields = reader.fieldnames or []
        rows, seen = [], set()
        for row in reader:
            clean = {k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
            key = tuple(clean.get(k, "") for k in fields)
            if args.dedupe and key in seen:
                continue
            seen.add(key)
            rows.append(clean)
    with args.output.open("w", newline="", encoding="utf-8") as dst:
        writer = csv.DictWriter(dst, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows):,} rows to {args.output}")

if __name__ == "__main__":
    main()
