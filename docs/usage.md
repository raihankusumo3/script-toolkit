# Usage Guide

Run any Python utility with `python path/to/script.py --help`.

## Safe file organization
```bash
python python/file-organizer.py ~/Downloads --dry-run
python python/file-organizer.py ~/Downloads
```

## Duplicate detection
```bash
python python/duplicate-finder.py ~/Documents
```
Files are grouped by size before SHA-256 hashing.

## Backups
```bash
python python/backup-tool.py ~/Documents --output ./backups
```

## URL checks
```bash
python python/url-checker.py https://example.com https://github.com
```

## Development
The toolkit prefers Python's standard library. Keep scripts small, readable, safe by default, and documented.
