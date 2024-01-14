"""Advent of code day 13."""

import logging
from collections.abc import Iterator


def main() -> None:
    """Program starts here."""
    with open("2023/13/input.txt", encoding="utf-8") as file:
        patterns = [pattern.splitlines() for pattern in file.read().split("\n\n")]

    print("Part 1:", part_1(patterns))
    print("Part 2:", part_2(patterns))


def part_1(patterns: list[list[str]]) -> int:
    """Solve part 1."""
    return sum(find_reflection_score(pattern) for pattern in patterns)


def part_2(patterns: list[list[str]]) -> int:
    """Solve part 2."""
    return sum(
        find_smudged_reflection_score(pattern) for pattern in patterns
    )  # 41350 too low, 41494 too low


def find_reflection_score(pattern: list[str]) -> int:
    """Find the score for a pattern."""
    # Check rows first
    for i in range(len(pattern) - 1):
        if all(up == down for up, down in zip(pattern[i::-1], pattern[i + 1 :])):
            logging.debug("Reflection between row %d and %d", i + 1, i + 2)
            return 100 * (i + 1)

    cols = ["".join(x) for x in zip(*pattern)]

    # Then columns
    for i in range(len(cols) - 1):
        if all(left == right for left, right in zip(cols[i::-1], cols[i + 1 : -1])):
            logging.debug("Reflection between col %d and %d", i + 1, i + 2)
            return i + 1

    logging.debug("No reflections found")
    return 0


def find_smudged_reflection_score(pattern: list[str]) -> int:
    """Find the score for a pattern that has a smudge."""
    # Check rows first
    for i in range(len(pattern) - 1):
        if calculate_difference(zip(pattern[i::-1], pattern[i + 1 :])) == 1:
            logging.debug("Reflection between row %d and %d", i + 1, i + 2)
            return 100 * (i + 1)

    cols = ["".join(x) for x in zip(*pattern)]

    # Then columns
    for i in range(len(cols) - 1):
        if calculate_difference(zip(cols[i::-1], cols[i + 1 : -1])) == 1:
            logging.debug("Reflection between col %d and %d", i + 1, i + 2)
            return i + 1

    logging.debug("No reflections found")
    return 0


def calculate_difference(rows: Iterator[tuple[str, str]]) -> int:
    """Calculate the number of character differences between rows."""
    differences = 0
    for left, right in rows:
        for left_char, right_char in zip(left, right):
            if left_char != right_char:
                differences += 1
    return differences


if __name__ == "__main__":
    logging.basicConfig(filename="output.log", filemode="w", level=logging.DEBUG)
    main()
