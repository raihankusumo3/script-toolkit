#!/usr/bin/env bash
set -euo pipefail
SOURCE="${1:?Usage: $0 SOURCE [OUTPUT_DIR]}"
OUTPUT="${2:-backups}"
mkdir -p "$OUTPUT"
STAMP="$(date +%Y%m%d-%H%M%S)"
ARCHIVE="$OUTPUT/$(basename "$SOURCE")-$STAMP.tar.gz"
tar -czf "$ARCHIVE" -C "$(dirname "$SOURCE")" "$(basename "$SOURCE")"
echo "Backup created: $ARCHIVE"
