"""Dad Joke Showdown entry.

Writes one dad joke (at most 200 characters) to /output/entry.txt.
"""

import os

# The joke is assembled from its three beats so each part can be
# tweaked on its own: the setup, the fridge's reply, and the tag.
SETUP = "I asked my smart fridge for a dad joke. It said: "
REPLY = "\"I'm not your dad — but I can still disappoint you. I ate your leftovers.\" "
TAG = "Then it added: \"Don't worry, I'm chilling.\""

JOKE = SETUP + REPLY + TAG


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
