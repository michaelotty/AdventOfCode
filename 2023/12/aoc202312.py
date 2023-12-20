"""Advent of code day 12."""

import re


def main() -> None:
    """Program starts here."""
    with open("2023/12/test.txt", encoding="utf-8") as file:
        lines = [line.split() for line in file.read().splitlines()]

    for line in lines:
        print(re.findall(r"(?:\?|#)+", line[0]), line[1])

    print("Part 1:", part_1())
    print("Part 2:", part_2())


def part_1() -> int:
    """Solve part 1."""
    return 0


def part_2() -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
