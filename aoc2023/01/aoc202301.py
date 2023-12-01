"""Advent of code day 1."""

import re
from string import ascii_lowercase


def main():
    """Main function."""

    with open("aoc2023/01/input.txt", encoding="utf-8") as file:
        data = file.read()

    print(data)

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


def part_1(data: str):
    """Solve part 1."""
    trans_table = str.maketrans({letter: "" for letter in ascii_lowercase})
    return sum(int(x[0] + x[-1]) for x in data.translate(trans_table).split())


def part_2(data: str):
    """Solve part 2."""

    data = data.strip().split("\n")
    output = []
    for line in data:
        matches = re.findall(r"one|two|three|four|five|six|seven|eight|nine|\d", line)
        print(matches)
        output.append(int(give_digit(matches[0]) + give_digit(matches[-1])))

    return sum(output)


# 54194 too low


def give_digit(in_word: str):
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
    return numbers[in_word]


if __name__ == "__main__":
    main()
