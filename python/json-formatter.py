#!/usr/bin/env python3
"""Validate and pretty-print JSON."""
import argparse,json
from pathlib import Path
def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("input",type=Path); p.add_argument("-o","--output",type=Path); a=p.parse_args()
    try: data=json.loads(a.input.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e: p.error(f"Invalid JSON at line {e.lineno}, column {e.colno}: {e.msg}")
    text=json.dumps(data,indent=2,ensure_ascii=False)+"\n"
    if a.output: a.output.write_text(text,encoding="utf-8"); print(f"Wrote {a.output}")
    else: print(text,end="")
if __name__=="__main__": main()
