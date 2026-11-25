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
    """Check the entry against the kit gate before writing.

    Rejects empty/oversized text, line breaks, control characters, and
    anything that is not encodable as UTF-8, so the written file can only
    ever be one clean plain-text line.
    """
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    # Reject control characters (C0/C1 ranges and DEL): the gate wants a
    # single plain-text line, and stray control bytes would break it.
    if any(ord(ch) < 0x20 or 0x7F <= ord(ch) < 0xA0 for ch in text):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def _resolve_output_dir():
    """Return the harness output dir, or None with an error printed."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return None
    return out_dir


def main():
    if not _validate_entry(ENTRY):
        print("entry failed validation", file=sys.stderr)
        return 0

    out_dir = _resolve_output_dir()
    if out_dir is None:
        return 0

    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, GATE_FILE)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        # Read back and verify byte-identical, including byte length.
        with open(path, "r", encoding="utf-8", newline="") as f:
            if f.read() != ENTRY:
                print("read-back mismatch", file=sys.stderr)
                return 0
        if os.path.getsize(path) != len(ENTRY.encode("utf-8")):
            print("written byte length mismatch", file=sys.stderr)
            return 0
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
