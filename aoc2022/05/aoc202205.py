"""Advent of code Day 5."""

import copy
import re


def main():
    """Main function."""
    with open("aoc2022/05/input.txt", encoding="utf-8") as file:
        stacks, instructions = file.read().split("\n\n")
        stacks = stacks.split("\n")
        instructions = instructions.split("\n")

    # Structure stacks as list of lists
    indexes = range(1, len(stacks[0]), 4)
    stacks = stacks[:-1]  # Remove the line with the stack IDs
    stacks = [[line[i] for line in reversed(stacks) if line[i] != " "] for i in indexes]

    # Convert "move a from b to c" to (a, b, c)
    instructions = [
        tuple(int(num) for num in re.findall(r"\d+", line)) for line in instructions
    ]

    # Copy so we can use again for part 2
    print(f"Part 1: {part_1(copy.deepcopy(stacks), instructions)}")
    print(f"Part 2: {part_2(stacks, instructions)}")


def part_1(stacks: list[list[str]], instructions: list[tuple[int, int, int]]):
    """Solve part 1."""
    for amount, from_stack, to_stack in instructions:
        for _ in range(amount):
            stacks[to_stack - 1].append(stacks[from_stack - 1].pop())

    return "".join(stack[-1] for stack in stacks)


def part_2(stacks: list[list[str]], instructions: list[tuple[int, int, int]]):
    """Solve part 2."""
    for amount, from_stack, to_stack in instructions:
        stacks[to_stack - 1].extend(stacks[from_stack - 1][-amount:])
        for _ in range(amount):
            stacks[from_stack - 1].pop()

    return "".join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    main()
