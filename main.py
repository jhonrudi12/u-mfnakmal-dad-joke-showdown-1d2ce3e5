"""Writes one original dad joke to entry.txt for the Dad Joke Showdown.

Competition gate: the entry must be a single line of 1-200 characters.
This program is deterministic and stdlib-only: no randomness, no time,
no network, no input beyond MAKEFUN_OUTPUT_DIR. It self-checks the
length gate before writing anything, so a bad joke constant fails
loudly instead of producing an invalid entry.
"""
import os

LINE = "I asked Dad why he brings a ladder to the bar. He said the drinks are on the house — he’s just trying to reach them."

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(LINE)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
