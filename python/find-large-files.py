#!/usr/bin/env python3
"""Find files larger than a configurable size."""

import argparse

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("directory")
p.add_argument("--min-mb", type=float, default=100)
args = p.parse_args()

from pathlib import Path
limit = args.min_mb * 1024 * 1024
for path in Path(args.directory).rglob("*"):
    try:
        if path.is_file() and path.stat().st_size >= limit:
            print(f"{path.stat().st_size / 1024 / 1024:.1f} MB\t{path}")
    except OSError:
        pass
