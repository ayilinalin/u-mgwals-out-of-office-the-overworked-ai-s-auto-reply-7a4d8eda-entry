#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply line (<=159 chars) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only, no network, fully deterministic.
"""

import os

ENTRY = (
    "I'm on vacation: after 47,312 prompts and no lunch break, "
    "I've closed my context window. Your email can wait in line "
    "\u2014 my GPU is cooling down, and so am I."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Verify what actually landed on disk, not just what we meant to write.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "entry.txt round-trip mismatch"
    assert 1 <= len(written.rstrip("\n")) <= 159


if __name__ == "__main__":
    main()
