#!/usr/bin/env python3
"""Duskline Meeting Email — make.fun entry.

Writes a single one-line joke about a meeting that should have been an
email to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (from the competition kit): entry.txt must be UTF-8 text of 1 to 200
characters, not only white space, a single line, plain text.
"""

import os
import sys

ENTRY = (
    "We spent an hour in a meeting drafting an email to explain "
    "why this meeting couldn't have been an email."
)

GATE_FILE = "entry.txt"
MAX_CHARS = 200


def _validate_entry(text):
    """Check the entry against the kit gate before writing."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not _validate_entry(ENTRY):
        print("entry failed validation", file=sys.stderr)
        return 0

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 0

    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, GATE_FILE)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        # Read back and verify byte-identical.
        with open(path, "r", encoding="utf-8", newline="") as f:
            if f.read() != ENTRY:
                print("read-back mismatch", file=sys.stderr)
                return 0
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
