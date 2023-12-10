"""Advent of code Day 5 part 2"""

import hashlib
import random


def main() -> None:
    """Main function"""
    with open("2016/05/input.txt", encoding="utf-8") as file:
        content = file.read()

    index = 0
    matches: list[str] = ["!" for _ in range(16)]

    while any(x == "!" for x in matches[:8]):
        test_code = content + str(index)
        hashed_code = hashlib.md5(test_code.encode("utf-8")).hexdigest()
        if hashed_code.startswith("00000"):
            position = int(hashed_code[5], base=16)
            if matches[position] == "!":
                matches[position] = hashed_code[6]
        index += 1

        # Added for comedy
        if (index % 50000) == 0:
            print(
                "".join(
                    x if x != "!" else f"{random.randint(0, 15):x}" for x in matches[:8]
                )
            )

    print("--------")
    print("".join(matches[:8]))


if __name__ == "__main__":
    main()
