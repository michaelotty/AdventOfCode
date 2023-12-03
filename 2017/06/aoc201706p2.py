"""Advent of code Day 6 part 2"""

from collections import OrderedDict


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        puzzle = [int(x) for x in file.read().split()]

    solved_puzzles = OrderedDict()
    iterations = 0

    while True:
        solved_puzzles[tuple(puzzle)] = iterations
        max_index = puzzle.index(max(puzzle))
        divider = puzzle[max_index] // len(puzzle)
        remainder = puzzle[max_index] % len(puzzle)
        puzzle[max_index] = 0

        for j, _ in enumerate(puzzle):
            index = j + max_index + 1
            if index >= len(puzzle):
                index -= len(puzzle)
            puzzle[index] += divider
            if remainder > 0:
                puzzle[index] += 1
                remainder -= 1

        iterations += 1

        if tuple(puzzle) in solved_puzzles:
            break

    print(iterations - solved_puzzles[tuple(puzzle)])


if __name__ == "__main__":
    main()
