#!/usr/bin/env bash
set -euo pipefail
DIR="${1:-.}"
DAYS="${DAYS:-30}"
find "$DIR" -type f -name "*.log" -mtime +"$DAYS" -print
if [[ "${DELETE:-0}" == "1" ]]; then
  find "$DIR" -type f -name "*.log" -mtime +"$DAYS" -delete
  echo "Old logs deleted."
fi
