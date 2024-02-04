"""Advent of code day 17."""


def main() -> None:
    """Program starts here."""
    with open("2023/17/test.txt", encoding="utf-8") as file:
        grid = [list(map(int, line)) for line in file.read().splitlines()]

    print("Part 1:", part_1(grid))
    print("Part 2:", part_2(grid))


def part_1(grid: list[list[int]]) -> int:
    """Solve part 1."""
    return grid[0][0]


def part_2(grid: list[list[int]]) -> int:
    """Solve part 2."""
    return grid[0][0]


if __name__ == "__main__":
    main()
