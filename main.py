"""One-Line Office Jokes entry: write a single office joke to /output/entry.txt.

The joke turns on a real office detail (the printer that only jams when
it matters) and lands its laugh in the last few words. Output is exactly
one line, no trailing newline, so the file holds only the joke itself.
"""

from pathlib import Path

JOKE = "The printer only jams for urgent documents, as if it reads the deadline before it reads the paper."


def main():
    assert "\n" not in JOKE and JOKE.strip() == JOKE, "joke must be one line"
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
