#!/usr/bin/env python3
"""Generate cryptographically secure random passwords."""

import argparse
import secrets
import string

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("-l", "--length", type=int, default=20)
    p.add_argument("-n", "--count", type=int, default=1)
    args = p.parse_args()
    if args.length < 8:
        p.error("Minimum length is 8")
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    for _ in range(args.count):
        print("".join(secrets.choice(alphabet) for _ in range(args.length)))

if __name__ == "__main__":
    main()
