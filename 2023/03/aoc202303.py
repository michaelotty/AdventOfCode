"""Advent of code day 3."""

import re
from itertools import product


def main() -> None:
    """Program starts here."""
    with open("2023/03/input.txt", encoding="utf-8") as file:
        rows = file.read().splitlines()

    print("Part 1:", part_1(rows))
    print("Part 2:", part_2(rows))


def part_1(rows: list[str]) -> int:
    """Solve part 1."""
    symbol_coords: set[tuple[int, int]] = set()
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

    part_numbers: list[int] = []

    for i, row in enumerate(rows):
        number: list[str] = []
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


def part_2(rows: list[str]) -> int:
    """Solve part 2."""
    height = len(rows)
    width = len(rows[0])

    gear_ratios: list[int] = []

    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == "*":
                adjacent_coords = [
                    (i + x, j + y)
                    for x, y in product(range(-1, 2), range(-1, 2))
                    if 0 <= i + x < height and 0 <= j + y < width and not x == y == 0
                ]
                digit_coords: list[tuple[int, int]] = []
                for row_id, col_id in adjacent_coords:
                    if re.match(r"\d", rows[row_id][col_id]):
                        digit_coords.append((row_id, col_id))

                number_coords: list[tuple[int, int]] = []
                for digit_coord in digit_coords:
                    if (
                        digit_coord[0],
                        digit_coord[1] - 1,
                    ) not in number_coords and (
                        digit_coord[0],
                        digit_coord[1] + 1,
                    ) not in number_coords:
                        number_coords.append(digit_coord)
                        continue

                if len(number_coords) == 2:
                    gear_ratios.append(
                        find_number_at_coord(rows, number_coords[0])
                        * find_number_at_coord(rows, number_coords[1])
                    )

    return sum(gear_ratios)  # 53923625 too low


def find_number_at_coord(grid: list[str], coord: tuple[int, int]) -> int:
    """Find the number located at coordinate"""
    width = len(grid[0])

    leftmost_col = coord[1]

    char = grid[coord[0]][coord[1]]

    while re.match(r"\d", char) and leftmost_col != 0:
        leftmost_col = min(max(leftmost_col - 1, 0), width - 1)
        char = grid[coord[0]][leftmost_col]

    return int(re.findall(r"\d+", grid[coord[0]][leftmost_col:])[0])


if __name__ == "__main__":
    main()
