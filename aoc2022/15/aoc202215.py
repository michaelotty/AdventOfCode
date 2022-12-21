"""Advent of code Day 15."""

import re


def main():
    """Main function."""
    regex = r"Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)"

    with open("aoc2022/15/test1.txt", encoding="utf-8") as file:
        coords = [map(int, nums) for nums in re.findall(regex, file.read())]
        coords = {(x1, y1): (x2, y2) for x1, y1, x2, y2 in coords}

    print("Part 1:", part_1(coords, 10))
    print("Part 2:", part_2(coords))


def part_1(coords: dict[tuple[int, int], tuple[int, int]], y_to_check: int) -> int:
    """Solve part 1."""
    beacon_no_go_zone = set()

    for sensor, beacon in coords.items():
        distance = manhattan_distance(sensor, beacon)
        for x in range(-distance, distance + 1):
            pos = (x, y_to_check)
            if manhattan_distance(pos, sensor) <= distance:
                beacon_no_go_zone.add(pos)

    return beacon_no_go_zone


def manhattan_distance(start: tuple[int, int], end: tuple[int, int]) -> int:
    """Calculate the manhattan distance between two points."""
    return abs(end[0] - start[0]) + abs(end[1] - start[1])


def part_2(coords: dict[tuple[int, int], tuple[int, int]]) -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
