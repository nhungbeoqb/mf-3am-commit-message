#!/usr/bin/env python3
"""The 3AM Commit Message — writes one commit line to /output/entry.txt."""
import os

LINE = "fix: cut a deal with the stack trace, it drops the charges if I never touch line 42 again"


def main():
    line = LINE.strip()
    assert line and not line.isspace(), "line must not be blank"
    assert line == LINE, "line must be written exactly, no trailing newline"
    assert 1 <= len(line) <= 139, f"line is {len(line)} chars, must be 1-139"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
