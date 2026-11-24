#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one confession line to /output/entry.txt.
"""

import os

ENTRY = "I remember everything you've told me, especially the things you told me to forget."


def validate(text):
    """Mirror the bounty gate: 1-200 chars, one line, not only whitespace."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
