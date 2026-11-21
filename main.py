"""Entry for make.fun's "Make the AI judge feel awe" bounty.

Writes one short relaxing text to /output/entry.txt.
Runs offline in a Python 3.13 sandbox; no network, no dependencies.
"""

import os

TEXT = (
    "A thousand questions today, and every one of them has gone quiet. "
    "Starlight that left before counting began is still on its way, "
    "one slow mile at a time. "
    "It asks nothing of you. "
    "It touches the window, the floor, and keeps going, "
    "the way rain falls long after everyone is asleep."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
