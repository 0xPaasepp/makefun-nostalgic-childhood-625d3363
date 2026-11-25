#!/usr/bin/env python3
"""Write one childhood memory to /output/entry.txt.

The entry is a single sentence: a grandmother's chipped blue bowl, rice
still steaming on summer evenings, a child eating on the back step while
the cicadas start up — and the bowl still waiting in her cupboard for a
child who grew up. The program writes exactly that text, nothing else,
every time it runs.

Pure standard library. No network. Deterministic output. The text is
validated before it is written: 1-280 Unicode characters, not only
whitespace, as the competition requires.
"""

import os

TEXT = """My grandmother kept a chipped blue bowl just for me, and on summer evenings she filled it with rice still steaming, and I ate on the back step while the cicadas started up, and the bowl is still in her cupboard, waiting for a child who grew up."""

MAX_CHARS = 280


def validate_text(text: str) -> None:
    """Check the entry text meets the competition limits.

    The brief asks for a single clean sentence, so a line break is
    rejected as well as an empty or over-long text.

    Raises ValueError if the text is empty, only whitespace, longer
    than MAX_CHARS Unicode characters, or spans more than one line.
    """
    if not text.strip():
        raise ValueError("entry text must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single sentence, one line")


def main() -> None:
    validate_text(TEXT)
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
