"""Advent of code Day 5."""

import re
import string


def main() -> None:
    """Program starts here."""
    with open("2018/05/input.txt", encoding="utf-8") as file:
        text = file.read()
    print(f"Part 1: {part_1(text)}")
    print(f"Part 2: {part_2(text)}")


def part_1(text: str) -> int:
    """Solve part 1 of the puzzle."""
    return reduce(text)


def part_2(text: str) -> int:
    """Solve part 2 of the puzzle."""
    return min(
        reduce("".join(re.split(f"[{letter}{letter.upper()}]", text)))
        for letter in string.ascii_lowercase
    )


def reduce(polymer: str) -> int:
    """Reduce the polymer."""
    reduced_polymer = [""]
    for unit in polymer:
        end_of_polymer = reduced_polymer[-1]
        if end_of_polymer != unit and end_of_polymer.lower() == unit.lower():
            reduced_polymer.pop()
        else:
            reduced_polymer.append(unit)
    return len(reduced_polymer) - 1


if __name__ == "__main__":
    main()
