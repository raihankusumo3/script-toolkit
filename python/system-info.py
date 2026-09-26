#!/usr/bin/env python3
"""Display useful cross-platform system information."""

import platform
import shutil
import socket
import sys
from pathlib import Path

print("Script Toolkit - System Info")
print("=" * 40)
print(f"OS:         {platform.system()} {platform.release()}")
print(f"Machine:    {platform.machine()}")
print(f"Python:     {sys.version.split()[0]}")
print(f"Hostname:   {socket.gethostname()}")
print(f"CPU:        {platform.processor() or 'unknown'}")
disk = shutil.disk_usage(Path.home())
print(f"Disk total: {disk.total / 1024**3:.1f} GB")
print(f"Disk free:  {disk.free / 1024**3:.1f} GB")
