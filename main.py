#!/usr/bin/env python3
"""The Self-Checkout Is Judging You - one funny line from a judgmental till.

Writes exactly one remark (at most 200 characters) to /output/entry.txt.
Deterministic: no randomness, no network, no clock, no environment input.
The till speaks once, and it speaks the same way every single run.
"""

LINE = "Twelve yoghurts, no spoon, no plan \u2014 and you scanned your loyalty card like it earns you a personality."

def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(text))
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
