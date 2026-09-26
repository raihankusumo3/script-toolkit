#!/usr/bin/env python3
"""Show the largest files below a directory."""

import argparse
from pathlib import Path

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory", type=Path)
    p.add_argument("-n", type=int, default=20)
    args = p.parse_args()
    files = []
    for path in args.directory.rglob("*"):
        try:
            if path.is_file():
                files.append((path.stat().st_size, path))
        except OSError:
            pass
    for size, path in sorted(files, reverse=True)[:args.n]:
        print(f"{size / 1024 / 1024:10.2f} MB  {path}")

if __name__ == "__main__":
    main()
