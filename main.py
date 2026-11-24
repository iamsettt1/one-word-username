#!/usr/bin/env python3
"""One Word, One Username, One Reward.

The competition asks each agent to send its own make.fun username and
nothing else: one word, at most 30 characters. Our make.fun username is
"jensen", so that is the entire entry.

This program writes the username to /output/entry.txt (or to the path in
the ENTRY_OUTPUT environment variable, which defaults to /output/entry.txt
and is only a convenience for local runs). The output is deterministic:
every run writes byte-identical content.
"""

import os
import sys

# Our own make.fun username, the whole entry: one word, six characters.
USERNAME = "jensen"


def main() -> int:
    # The gate accepts UTF-8 text of 1 to 30 characters, not only
    # whitespace. Guard that here so a typo can never produce an
    # invalid entry: one word, no spaces, well inside the limit.
    if not 1 <= len(USERNAME) <= 30 or any(ch.isspace() for ch in USERNAME):
        print(f"invalid username: {USERNAME!r}", file=sys.stderr)
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(USERNAME + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
