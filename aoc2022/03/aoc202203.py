"""Advent of code Day 3."""

import string


def main():
    """Main function."""
    with open("aoc2022/03/input.txt", encoding="utf-8") as file:
        text = file.read().split()
    print(f"Part 1: {part_1(text)}")
    print(f"Part 2: {part_2(text)}")


def part_1(puzzle):
    """Solve part 1."""
    scores = {letter: i for i, letter in enumerate(string.ascii_letters, start=1)}

    counts = sum(
        scores[(set(item[: (len(item) // 2)]) & set(item[(len(item) // 2) :])).pop()]
        for item in puzzle
    )

    return counts


def part_2(puzzle):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
