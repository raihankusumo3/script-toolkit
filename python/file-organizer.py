#!/usr/bin/env python3
"""Organize files into folders based on file extension."""

import argparse
import shutil
from pathlib import Path

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory", type=Path)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    root = args.directory.expanduser().resolve()
    if not root.is_dir():
        p.error(f"Not a directory: {root}")
    for item in sorted(root.iterdir()):
        if not item.is_file() or item.name.startswith("."):
            continue
        folder = item.suffix.lower().lstrip(".") or "no-extension"
        dest = root / folder / item.name
        print(f"{'[DRY] ' if args.dry_run else ''}{item.name} -> {folder}/")
        if not args.dry_run:
            dest.parent.mkdir(exist_ok=True)
            if dest.exists():
                print(f"  skipped: {dest.name} already exists")
                continue
            shutil.move(str(item), str(dest))

if __name__ == "__main__":
    main()
