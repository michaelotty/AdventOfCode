"""Advent of code day 4."""

import re


def main() -> None:
    """Program starts here."""
    with open("2023/04/input.txt", encoding="utf-8") as file:
        raw_data = [
            re.split(r"(?:: )|(?: \| )", line)[1:] for line in file.read().splitlines()
        ]

    data = [
        (
            [int(num) for num in re.findall(r"\d+", left_str)],
            [int(num) for num in re.findall(r"\d+", right_str)],
        )
        for left_str, right_str in raw_data
    ]

    for line in data:
        print(line)

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
