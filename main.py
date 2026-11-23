#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes a single pickup line (at most 200 characters) to /output/entry.txt.
Pure Python standard library only; deterministic output.
"""

import os

LINE = "My loss function drops every time you reply \u2014 you must be the gradient I've been descending toward."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
