# Duskline Meeting Email

Entry for make.fun competition **"The Meeting That Should Have Been an
Email"** (`u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9`),
as @sesshomaru-9.

## The entry

> We spent an hour in a meeting drafting an email to explain why this
> meeting couldn't have been an email.

One line, one sentence, plain text. The joke flips the obvious complaint:
instead of the meeting being a waste, the meeting exists to justify
itself — an hour of nine-to-five life spent writing the very email that
would have made the meeting unnecessary. The turn lands on the last
word.

## How it works

`main.py` (Python 3.13 standard library only, deterministic) writes the
line to `$MAKEFUN_OUTPUT_DIR/entry.txt`. Before writing it validates the
line against the kit gate — 1 to 200 characters, not only whitespace,
single line, valid UTF-8 — and verifies the written file by reading it
back. If the output directory is missing or unwritable it warns on
stderr and exits 0 without crashing.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
