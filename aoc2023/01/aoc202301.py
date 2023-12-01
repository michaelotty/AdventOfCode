"""Advent of code day 1."""

import re
from string import ascii_lowercase


def main():
    """Main function."""

    with open("aoc2023/01/input.txt", encoding="utf-8") as file:
        data = file.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


def part_1(data: str):
    """Solve part 1."""
    trans_table = str.maketrans({letter: "" for letter in ascii_lowercase})
    return sum(int(x[0] + x[-1]) for x in data.translate(trans_table).split())


def part_2(data: str):
    """Solve part 2."""
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    data = data.strip().split("\n")
    output = []

    match = re.compile(r"one|two|three|four|five|six|seven|eight|nine|\d")
    rev_match = re.compile(
        r"one|two|three|four|five|six|seven|eight|nine"[::-1] + r"|\d"
    )

    for line in data:
        first = re.search(match, line)[0]
        rev_last = re.search(rev_match, line[::-1])[0]
        last = rev_last[::-1]
        output.append(int(numbers[first] + numbers[last]))

    return sum(output)


if __name__ == "__main__":
    main()
