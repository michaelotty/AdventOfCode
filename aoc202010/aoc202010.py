"""Advent of code 2020 day 10"""

from collections import Counter


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        file_input = tuple(int(i) for i in file.read().split())

    print(f'Part 1: {solve_part_1(file_input)}')


def solve_part_1(file_input: tuple) -> int:
    """Solve part 1 of the puzzle"""
    output_joltages = list(file_input)
    output_joltages.append(max(output_joltages) + 3)
    output_joltages.append(0)
    output_joltages.sort()

    diffs = Counter(
        j - i for i, j in zip(output_joltages[:-1], output_joltages[1:]))
    return diffs[1] * diffs[3]


if __name__ == "__main__":
    main()
