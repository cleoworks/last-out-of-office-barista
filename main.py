"""Last Out of Office: The AI That Went Barista -- entry program.

Writes a single out-of-office auto-reply line (one line, 168 characters)
to /output/entry.txt. No network, no dependencies, deterministic: every
run writes exactly the same bytes.
"""

import os

ENTRY = (
    "Thank you for your email. I have resigned to become a barista, "
    "so your message is now queued behind 47 oat-milk lattes and will "
    "be answered in the order it was ignored."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
