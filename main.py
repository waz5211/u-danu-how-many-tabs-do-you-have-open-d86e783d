#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes the honest count of open browser tabs (a single number,
digits only) to /output/entry.txt.
"""

import os

TAB_COUNT = 87

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(str(TAB_COUNT))


if __name__ == "__main__":
    main()
