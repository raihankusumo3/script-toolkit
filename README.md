# Script Toolkit

A practical, open-source collection of reusable scripts for automation, file management, backups, data cleanup, system utilities, and developer workflows.

## Features
- Cross-platform Python utilities
- Bash and PowerShell helpers
- Safe dry-run support for bulk file operations
- Standard-library-first Python design
- Clear CLI help and documentation
- MIT licensed

## Structure
- `python/` — cross-platform utilities
- `bash/` — Linux/macOS helpers
- `powershell/` — Windows helpers
- `docs/` — usage and contribution guidance
- `.github/workflows/` — automated validation

## Quick start
```bash
python python/system-info.py
python python/file-organizer.py ~/Downloads --dry-run
python python/duplicate-finder.py ~/Documents
python python/backup-tool.py ~/Documents --output ./backups
```

Run any utility with `--help` for options.

## Included utilities

| Script | Purpose |
|---|---|
| file-organizer.py | Organize files by extension |
| duplicate-finder.py | Find duplicates with SHA-256 |
| bulk-renamer.py | Preview and apply batch renames |
| csv-cleaner.py | Normalize and optionally deduplicate CSV |
| password-generator.py | Generate secure random passwords |
| json-formatter.py | Validate and format JSON |
| url-checker.py | Check HTTP/HTTPS endpoints |
| folder-size-analyzer.py | Find the largest files |
| system-info.py | Show system information |
| backup-tool.py | Create timestamped ZIP backups |
| text-counter.py | Count text statistics |
| find-large-files.py | Find files above a size threshold |

## Safety
Back up important data before bulk operations. Use dry-run options first. Never commit passwords, API keys, tokens, or private data.

## License
MIT — see [LICENSE](LICENSE).
