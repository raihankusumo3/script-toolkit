#!/usr/bin/env python3
"""Count lines, words, characters, and bytes in a UTF-8 text file."""

import argparse
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("file", type=Path)
args = p.parse_args()
text = args.file.read_text(encoding="utf-8")
print(f"Lines:      {len(text.splitlines()):,}")
print(f"Words:      {len(text.split()):,}")
print(f"Characters: {len(text):,}")
print(f"Bytes:      {len(text.encode('utf-8')):,}")
