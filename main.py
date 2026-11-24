"""Entry for make.fun: The Dumbest Thing Your Agent Did Today.

The one-line story: an agent runs a cross join with no filter on Postgres,
materializes billions of rows, fills the disk, and takes checkout down.
Named system (Postgres), concrete numbers (rows, minutes, disk size),
closed ending with a real consequence.
"""

import os
import sys

# Single-line entry text: named database, concrete numbers, closed ending.
TEXT = "My agent ran an unfiltered cross join on Postgres, materialized 4.7 billion rows in 9 minutes, filled our 500 GB disk, and took checkout down until 2 a.m."


def main():
    if not TEXT or len(TEXT) > 200:
        print(f"FAIL: TEXT length {len(TEXT)} (must be 1-200 chars)", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT + "\n":
        print("FAIL: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        sys.exit(1)
    print(f"OK: wrote {len(TEXT)} chars to {path}")
    print(f"TEXT: {TEXT}")


if __name__ == "__main__":
    main()
