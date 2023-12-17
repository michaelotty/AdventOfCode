"""Advent of code day 8."""

import itertools
import re


def main() -> None:
    """Program starts here."""
    with open("2023/08/input.txt", encoding="utf-8") as file:
        steps, mapping_text = file.read().split("\n\n")

    mapping = create_mapping(mapping_text)

    print("Part 1:", part_1(steps, mapping))
    print("Part 2:", part_2())


def create_mapping(mapping_text: str) -> dict[str, tuple[str, str]]:
    """Create a mapping from the text input."""
    mapping = {}

    for line in mapping_text.splitlines():
        key, left, right = re.findall(r"\w+", line)
        mapping[key] = (left, right)

    return mapping


def part_1(steps, mapping) -> int:
    """Solve part 1."""
    position = "AAA"
    distance_travelled = 0
    for direction in itertools.cycle(steps):
        distance_travelled += 1
        if direction == "L":
            position = mapping[position][0]
        else:
            position = mapping[position][1]

        if position == "ZZZ":
            return distance_travelled

    return 0


def part_2() -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
