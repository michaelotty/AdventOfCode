#!/bin/python3

"""Advent of Code 2020 Day 3"""


def part_1(lines, horizontal_step=3):
    """Solve part 1"""
    width = len(lines[0])
    x_pos = 0
    trees = 0

    for line in lines:
        if x_pos >= width:
            x_pos -= width
        trees += line[x_pos] == "#"
        x_pos += horizontal_step

    return trees


def part_2(lines):
    """Solve part 2"""
    nums = [part_1(lines, i) for i in range(1, 8, 2)]
    nums.append(part_1(lines[::2], 1))
    val = 1
    for num in nums:
        val *= num
    return val


def main():
    """Start of program execution"""
    with open("question.txt", encoding="utf-8") as file:
        lines = file.read().splitlines()

    print(f"Part 1: {part_1(lines)}")
    print(f"Part 2: {part_2(lines)}")


if __name__ == "__main__":
    main()
