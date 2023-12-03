"""Advent of code day 3."""

import re
from itertools import product


def main():
    """Main function."""
    with open("2023/03/test.txt", encoding="utf-8") as file:
        rows = file.read().splitlines()

    print("Part 1:", part_1(rows))
    print("Part 2:", part_2(rows))


def part_1(rows: list[str]):
    """Solve part 1."""
    symbol_coords = set()
    height = len(rows)
    width = len(rows[0])

    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if re.match(r"[^\.\d]", char):
                symbol_coords |= {
                    (i + x, j + y)
                    for x, y in product(range(-1, 2), range(-1, 2))
                    if 0 <= i + x < height and 0 <= j + y < width
                }

    part_numbers = []

    for i, row in enumerate(rows):
        number = []
        is_part_number = False

        for j, char in enumerate(row):
            if re.match(r"\d", char):
                number.append(char)
                if (i, j) in symbol_coords:
                    is_part_number = True
            elif number and is_part_number:
                part_numbers.append(int("".join(number)))
                number = []
                is_part_number = False
            else:
                number = []

        if number and is_part_number:
            part_numbers.append(int("".join(number)))

    return sum(part_numbers)


def part_2(rows):
    """Solve part 2."""
    height = len(rows)
    width = len(rows[0])

    gear_coords = set()
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == "*":
                adjacent_coords = [
                    (i + x, j + y)
                    for x, y in product(range(-1, 2), range(-1, 2))
                    if 0 <= i + x < height and 0 <= j + y < width and not x == y == 0
                ]

                # for row_id, col_id in adjacent_coords:
                #     if re.match(r"\d", rows[row_id][col_id]):

                print(adjacent_coords)
                gear_coords.add((i, j))
    return gear_coords


if __name__ == "__main__":
    main()
