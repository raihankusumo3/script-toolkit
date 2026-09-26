#!/usr/bin/env python3
"""Batch rename files with preview support."""

import argparse
from pathlib import Path

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory", type=Path)
    p.add_argument("--prefix", default="")
    p.add_argument("--suffix", default="")
    p.add_argument("--start", type=int, default=1)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    files = sorted(x for x in args.directory.iterdir() if x.is_file())
    plan = [(f, f.with_name(f"{args.prefix}{i:03d}{args.suffix}{f.suffix}"))
            for i, f in enumerate(files, args.start)]
    targets = [new for _, new in plan]
    if len(set(targets)) != len(targets):
        p.error("Generated names are not unique")
    for old, new in plan:
        print(f"{'[DRY] ' if args.dry_run else ''}{old.name} -> {new.name}")
        if not args.dry_run and old != new:
            if new.exists():
                p.error(f"Target exists: {new}")
            old.rename(new)

if __name__ == "__main__":
    main()
