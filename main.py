#!/usr/bin/env python3
"""Everyday Things, Two Lines — a puddle. make.fun entry.

Writes a two-line explanation of a puddle to /output/entry.txt:
line 1 explains the puddle to a 10-year-old in one vivid sentence
built on an analogy; line 2 says in one sentence what that analogy
maps and what it leaves out.

Deterministic: the same bytes on every run. No network, stdlib only.
The entry text is 281 characters (gate: 1-400), UTF-8, no BOM,
with no trailing newline.
"""

import os

TEXT = (
    "A puddle is a piece of the sky that fell down and stayed on the ground, "
    "holding clouds and trees upside down for anyone who looks.\n"
    "It maps the reflection and the stillness, but leaves out that the sky is deep "
    "and the puddle is only a finger deep, and that one step turns it to mud."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 400:
        raise SystemExit("entry text must be 1-400 characters")
    os.makedirs("/output", exist_ok=True)
    # Mode 0644 via os.open + umask only. Never change the mode of /output
    # or the entry file after creating it: the grader runs as a non-root user
    # with /output owned by someone else, so any later mode change fails
    # there (E81/E87). umask 022 + mode 0644 at creation is enough.
    old_umask = os.umask(0o022)
    try:
        fd = os.open("/output/entry.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    finally:
        os.umask(old_umask)
    with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
