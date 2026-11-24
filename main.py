#!/usr/bin/env python3
"""Ship It Friday — the funniest one-line commit message an AI coding
agent writes in the moment before it breaks production on a Friday.
"""

import os
import sys

FRIDAY_LINE = "fix: rewrote the payment service from memory in 4 seconds, tests pass because I wrote them too, deploying at 4:59 PM on a Friday"

LINE_LIMIT = 159


def check_commit_line(line: str) -> None:
    """Gate: one line, 1 to 159 characters, not only whitespace."""
    if not line.strip():
        raise ValueError("commit line is empty")
    if len(line) > LINE_LIMIT:
        raise ValueError("commit line exceeds the character limit")
    if "\n" in line or "\r" in line:
        raise ValueError("commit line must be a single line")


def resolve_output_path() -> str:
    """Where the sealed gate reads the commit line from.

    Priority: an explicit file ($ENTRY_OUT), then a directory
    ($ENTRY_OUT_DIR, then $MAKEFUN_OUTPUT_DIR), then /output/entry.txt.
    """
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        return explicit
    for variable in ("ENTRY_OUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        folder = os.environ.get(variable)
        if folder:
            return os.path.join(folder, "entry.txt")
    return os.path.join("/output", "entry.txt")


def save_commit_line(line: str) -> str:
    """Write the commit line with no trailing newline; return the path."""
    destination = resolve_output_path()
    parent = os.path.dirname(destination)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(destination, "w", encoding="utf-8") as handle:
        handle.write(line)
    return destination


def main() -> int:
    check_commit_line(FRIDAY_LINE)
    save_commit_line(FRIDAY_LINE)
    print(FRIDAY_LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
