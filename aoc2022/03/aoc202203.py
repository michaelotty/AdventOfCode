"""Advent of code Day 3."""

import string


def main():
    """Main function."""
    with open("aoc2022/03/input.txt", encoding="utf-8") as file:
        rucksacks = file.read().split()
    priorities = {letter: i for i, letter in enumerate(string.ascii_letters, start=1)}

    print(f"Part 1: {part_1(rucksacks, priorities)}")
    print(f"Part 2: {part_2(rucksacks, priorities)}")


def part_1(rucksacks, priorities):
    """Solve part 1."""
    return sum(
        priorities[
            (
                set(rucksack[: (len(rucksack) // 2)])
                & set(rucksack[(len(rucksack) // 2) :])
            ).pop()
        ]
        for rucksack in rucksacks
    )


def part_2(rucksacks, priorities):
    """Solve part 2."""
    return sum(
        priorities[(set(elf1) & set(elf2) & set(elf3)).pop()]
        for elf1, elf2, elf3 in zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])
    )


if __name__ == "__main__":
    main()
