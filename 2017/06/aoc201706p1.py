"""Advent of code Day 6 part 1"""


def main():
    """Main function"""
    with open("input.txt", encoding="utf-8") as file:
        puzzle = [int(x) for x in file.read().split()]

    solved_puzzles = set()
    iterations = 0

    while True:
        solved_puzzles.add(tuple(puzzle))
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

    print(iterations)


if __name__ == "__main__":
    main()
