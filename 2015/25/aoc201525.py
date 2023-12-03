"""Advent of code Day 25"""


def part_1() -> int:
    """Solve part 1 of the puzzle"""
    for val, row, col in diagonal_sequence(20151125):
        if (row, col) == (2947, 3029):
            return val
    raise RuntimeError("Solution not found")


def part_2() -> int:
    """Solve part 2 of the puzzle"""
    return 0


def diagonal_sequence(starting_val):
    """Diagonal sequence"""
    row = 1
    col = 1
    while True:
        row -= 1
        col += 1
        if row == 0:
            row, col = col, 1
        starting_val = (starting_val * 252533) % 33554393
        yield starting_val, row, col


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
