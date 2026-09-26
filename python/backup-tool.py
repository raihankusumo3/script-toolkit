#!/usr/bin/env python3
"""Create a timestamped ZIP archive from a directory."""

import argparse
import shutil
from datetime import datetime
from pathlib import Path

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("source", type=Path)
    p.add_argument("-o", "--output", type=Path, default=Path("backups"))
    args = p.parse_args()
    source = args.source.expanduser().resolve()
    if not source.is_dir():
        p.error(f"Not a directory: {source}")
    args.output.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    target = args.output / f"{source.name}-{stamp}"
    archive = shutil.make_archive(str(target), "zip", root_dir=source)
    print(f"Backup created: {archive}")

if __name__ == "__main__":
    main()
