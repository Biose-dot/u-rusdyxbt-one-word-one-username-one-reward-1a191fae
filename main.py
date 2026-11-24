#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes the entry text (no trailing newline, nothing else) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The entrant's own make.fun username, one word and nothing else, exactly as the brief requires. The entrypoint now self-checks the gate (one word, 1-30 characters, no whitespace) before writing.
"""
import os

ENTRY = 'biose-dot'


def main() -> None:
    # Gate self-check (brief: one word, 1-30 chars, no whitespace).
    assert 1 <= len(ENTRY) <= 30 and ENTRY.split() == [ENTRY], "entry fails the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
