"""Advent of code day 3."""

import re


def main() -> None:
    """Program starts here."""
    with open("2024/03/input.txt", encoding="utf-8") as file:
        data = file.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


def part_1(data) -> int:
    """Solve part 1."""
    data = [(int(x), int(y)) for x, y in re.findall(r"mul\((\d+),(\d+)\)", data)]
    return sum(x * y for x, y in data)


def part_2(data) -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
