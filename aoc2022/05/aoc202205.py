"""Advent of code Day 5."""

import re


def main():
    """Main function."""
    with open("aoc2022/05/input.txt", encoding="utf-8") as file:
        stacks, instructions = file.read().split("\n\n")
        stacks = stacks.split("\n")
        instructions = instructions.split("\n")

    # Extract stack data from file into useful
    indexes = range(1, len(stacks[0]), 4)
    stacks = stacks[:-1]
    stacks = [[line[i] for line in reversed(stacks) if line[i] != " "] for i in indexes]

    # Simplify instructions
    instructions = [
        tuple(int(i) for i in re.findall(r"\d+", line)) for line in instructions
    ]

    print(f"Part 1: {part_1(stacks, instructions)}")
    print(f"Part 2: {part_2(stacks, instructions)}")


def part_1(stacks: list[list[str]], instructions):
    """Solve part 1."""
    for amount, from_stack, to_stack in instructions:
        for _ in range(amount):
            stacks[to_stack - 1].append(stacks[from_stack - 1].pop())
    return "".join(stack[-1] for stack in stacks)


def part_2(stacks, instructions):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
