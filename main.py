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

RANT = (
    "My phone autocorrected 'on my way' to 'on my wayward son' "
    "and sent it to my boss. He replied 'carry on.' "
    "I have never been more professionally haunted by a rock song."
)

MIN_CHARS = 1
MAX_CHARS = 400


def main() -> None:
    text = RANT.strip()
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Echo the entry so the run log shows exactly what was graded.
    print(f"entry ({len(text)} chars): {text}")


if __name__ == "__main__":
    main()
