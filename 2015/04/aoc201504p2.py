"""Advent of code Day 4 part 2"""

import hashlib


def main() -> None:
    """Main function"""
    with open("2015/04/input.txt", encoding="utf-8") as f:
        file_contents = f.read()

    found = False
    i = 0

    while not found:
        i += 1
        hash_val = hashlib.md5(
            "".join((file_contents, str(i))).encode("utf-8")
        ).hexdigest()
        found = hash_val[0:6] == "000000"

    print(i)


if __name__ == "__main__":
    main()
