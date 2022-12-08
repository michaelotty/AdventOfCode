"""Advent of code Day 8."""


def main():
    """Main function."""
    with open("aoc2022/08/test.txt", encoding="utf-8") as file:
        number_grid = [[int(num) for num in line] for line in file.read().splitlines()]
    print(number_grid)
    print("Part 1:", part_1(number_grid))
    print("Part 2:", part_2(number_grid))


def part_1(number_grid):
    """Solve part 1."""
    return 0


def part_2(number_grid):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
