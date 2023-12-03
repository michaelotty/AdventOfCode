"""Advent of code 2020 day 10"""

from collections import Counter
from typing import Generator, Iterable


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        file_input = tuple(sorted(int(i) for i in file.read().split()))

    print(f'Part 1: {solve_part_1(file_input)}')
    print(f'Part 2: {solve_part_2(file_input)}')


def solve_part_1(file_input: tuple[int, ...]) -> int:
    """Solve part 1 of the puzzle"""
    adapters = (0, *file_input, file_input[-1] + 3)
    diffs = Counter(diff(adapters))
    return diffs[1] * diffs[3]


def solve_part_2(file_input: tuple[int, ...]) -> int:
    """Solve part 2 of the puzzle"""
    adapters = (*file_input, file_input[-1] + 3)
    counter = {0: 1}

    for adapter in adapters:
        counter[adapter] = sum(counter.get(adapter - i, 0)
                               for i in range(1, 4))
    return counter[adapters[-1]]


def diff(list_of_numbers: Iterable[int]) -> Generator:
    """Creates a diff generator"""
    return (j - i for i, j in zip(list_of_numbers[:-1], list_of_numbers[1:]))


if __name__ == "__main__":
    main()
