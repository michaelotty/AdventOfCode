"""Advent of code Day 4."""

import re


def main():
    """Main function."""
    with open("aoc2022/04/input.txt", encoding="utf-8") as file:
        nums = [
            [int(num) for num in line]
            for line in re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", file.read())
        ]
        ranges = [
            (set(range(num[0], num[1] + 1)), set(range(num[2], num[3] + 1)))
            for num in nums
        ]

    print(f"Part 1: {part_1(ranges)}")
    print(f"Part 2: {part_2(ranges)}")


def part_1(ranges):
    """Solve part 1."""
    return sum(
        1 for left, right in ranges if len(left & right) in (len(left), len(right))
    )


def part_2(ranges):
    """Solve part 2."""
    return sum(1 for left, right in ranges if left & right)


if __name__ == "__main__":
    main()
