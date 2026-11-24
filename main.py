#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; deterministic; no network, no input files.
"""

import os

ENTRY = (
    "I missed the deadline because I asked myself for clarification, "
    "and I'm still waiting on my own reply."
)


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1 to 200 characters, got %d" % len(ENTRY))
    if not ENTRY.strip():
        raise SystemExit("entry must not be only white space")
    if ENTRY != ENTRY.rstrip("\n"):
        raise SystemExit("entry must not end with a newline")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
