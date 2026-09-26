#!/usr/bin/env python3
"""Check HTTP/HTTPS URLs and report status and response time."""

import argparse
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("urls", nargs="+")
    p.add_argument("--timeout", type=float, default=10)
    args = p.parse_args()
    for url in args.urls:
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        start = time.perf_counter()
        try:
            req = Request(url, headers={"User-Agent": "script-toolkit/1.0"})
            with urlopen(req, timeout=args.timeout) as response:
                elapsed = time.perf_counter() - start
                print(f"OK   {response.status:3}  {elapsed:.2f}s  {url}")
        except HTTPError as e:
            print(f"HTTP {e.code:3}  {time.perf_counter()-start:.2f}s  {url}")
        except URLError as e:
            print(f"ERR       {time.perf_counter()-start:.2f}s  {url} ({e.reason})")

if __name__ == "__main__":
    main()
