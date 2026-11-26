#!/usr/bin/env python3
"""Write the make.fun entry text to entry.txt."""

import os
from pathlib import Path

ENTRY_TEXT = "I can reproduce the bug now—unfortunately, so can every user, at scale."


def entry_path() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / "entry.txt"


def main() -> None:
    entry_path().write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
