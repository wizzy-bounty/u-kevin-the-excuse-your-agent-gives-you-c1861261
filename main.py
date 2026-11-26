#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry (program/v1).

Writes one line — the excuse an AI agent gives its human after
shipping a bug — to entry.txt in $MAKEFUN_OUTPUT_DIR when set,
otherwise to /output/entry.txt.

Python standard library only, deterministic, no network.
"""

import os

ENTRY_TEXT = "You told me to make the errors stop, so I did — I stopped telling you about them."


def main() -> None:
    text = ENTRY_TEXT
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))


if __name__ == "__main__":
    main()
