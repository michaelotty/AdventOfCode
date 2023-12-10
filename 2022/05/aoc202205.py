"""Advent of code Day 5."""

import copy
import re


def main() -> None:
    """Main function."""
    with open("2022/05/input.txt", encoding="utf-8") as file:
        data1, data2 = file.read().split("\n\n")
        stacks_data = data1.split("\n")[:-1]
        instructions_data = data2.split("\n")

    # Structure stacks as list of lists
    stacks: list[list[str]] = [
        [item for item in stack if item != " "]
        for stack in list(zip(*[line[1::4] for line in reversed(stacks_data)]))
    ]

    # Convert "move a from b to c" to (a, b, c)
    instructions: list[tuple[int, ...]] = [
        tuple(int(num) for num in re.findall(r"\d+", line))
        for line in instructions_data
    ]

    # Copy so we can use again for part 2
    print("Part 1:", part_1(copy.deepcopy(stacks), instructions))
    print("Part 2:", part_2(stacks, instructions))


def part_1(stacks: list[list[str]], instructions: list[tuple[int, ...]]):
    """Solve part 1."""
    for amount, from_stack, to_stack in instructions:
        for _ in range(amount):
            stacks[to_stack - 1].append(stacks[from_stack - 1].pop())

    return "".join(stack[-1] for stack in stacks)


def part_2(stacks: list[list[str]], instructions: list[tuple[int, ...]]):
    """Solve part 2."""
    for amount, from_stack, to_stack in instructions:
        stacks[to_stack - 1].extend(stacks[from_stack - 1][-amount:])
        for _ in range(amount):
            stacks[from_stack - 1].pop()

    return "".join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    main()
