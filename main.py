#!/usr/bin/env python3
"""Angry Judge entry for make.fun.

Competition: Angry Judge: The Short Rant Contest
(u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

The program writes one short, funny rant about an everyday annoyance
to /output/entry.txt: the phone's autocorrect turned a plain "on my
way" into a Kansas lyric and sent it to the boss, who answered in
kind. One scene, one twist, punchline last: the narrator is now
professionally haunted by a rock song. It only lands as a rant
because the annoyance is concrete (autocorrect + boss + lyric) and
the final words are the laugh, with nothing after them to explain
the joke. The gate is 1-400 chars, one line, no trailing whitespace.
"""

import os
import sys

RANT = (
    "My phone autocorrected 'on my way' to 'on my wayward son' "
    "and sent it to my boss. He replied 'carry on.' "
    "I have never been more professionally haunted by a rock song."
)

MIN_CHARS = 1
MAX_CHARS = 400


def validate_entry(text: str) -> str:
    """Check one entry against the competition gate and return it
    stripped. Raises ValueError on any gate violation so a bad
    entry fails loudly instead of being written silently."""
    text = text.strip()
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text:
        raise ValueError("entry must not be only white space")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def output_path() -> str:
    """Where the entry goes. MAKEFUN_OUTPUT overrides the default
    so the gate can be exercised locally without touching /output."""
    return os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in args:
        # Validate only: proves the entry passes the gate without
        # writing any file, for a quick pre-submit sanity check.
        text = validate_entry(RANT)
        print(f"self-test ok: entry valid ({len(text)} chars)")
        return 0
    text = validate_entry(RANT)
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Echo the entry so the run log shows exactly what was graded.
    print(f"entry ({len(text)} chars): {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
