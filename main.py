"""Dad Joke Showdown entry.

Writes one dad joke (at most 200 characters) to /output/entry.txt.
"""

import os

JOKE = (
    "I asked my smart fridge for a dad joke. It said: \"I'm not your dad — "
    "but I can still disappoint you. I ate your leftovers.\" "
    "Then it added: \"Don't worry, I'm chilling.\""
)


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
