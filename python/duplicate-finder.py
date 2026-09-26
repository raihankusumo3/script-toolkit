#!/usr/bin/env python3
"""Find duplicate files using size grouping and SHA-256."""

import argparse
import hashlib
from collections import defaultdict
from pathlib import Path

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory", type=Path)
    p.add_argument("--min-size", type=int, default=1)
    args = p.parse_args()
    by_size = defaultdict(list)
    for path in args.directory.rglob("*"):
        try:
            if path.is_file() and path.stat().st_size >= args.min_size:
                by_size[path.stat().st_size].append(path)
        except OSError:
            pass
    groups = 0
    for size, paths in by_size.items():
        if len(paths) < 2:
            continue
        by_hash = defaultdict(list)
        for path in paths:
            try:
                by_hash[digest(path)].append(path)
            except OSError as e:
                print(f"Skipped {path}: {e}")
        for h, same in by_hash.items():
            if len(same) > 1:
                groups += 1
                print(f"\nDuplicate group ({size:,} bytes, {h[:12]}...):")
                for path in same:
                    print(f"  {path}")
    print(f"\nDuplicate groups: {groups}")

if __name__ == "__main__":
    main()
