"""Dad Joke Showdown entry.

Writes exactly one original dad joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when the harness sets it).
Deterministic: no network, no randomness, no timestamps.
The joke is 95 characters, inside the gate's 1-200 range.
"""

import os

JOKE = "My daughter said my jokes were getting stale. I said, 'That's just the yeast of your problems.'"

assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
