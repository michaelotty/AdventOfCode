"""Advent of code Day 23."""

import io
import operator


def main():
    """Main function."""
    with open("aoc2022/23/test1.txt", encoding="utf-8") as file:
        grid = Grid(file)
    print(grid, "\n")
    print("Part 1:", part_1(grid))
    print("Part 2:", part_2(grid))


class Grid:
    """Grid class."""

    def __init__(self, file: io.TextIOWrapper) -> None:
        """Create a Grid from text file."""
        self.grid = {
            (x, y)
            for y, line in enumerate(file.read().splitlines())
            for x, char in enumerate(line)
            if char == "#"
        }

    def __repr__(self) -> str:
        """Grid as string."""
        min_x = min(self.grid, key=operator.index(0))
        max_x = max(self.grid, key=operator.index(0))
        min_y = min(self.grid, key=operator.index(1))
        max_y = max(self.grid, key=operator.index(1))

        lines = ("".join("#" if item else "." for item in line) for line in self.grid)
        return "\n".join(lines)

    def __iter__(self):
        return self

    def __next__(self):
        return self


def part_1(grid: Grid):
    """Solve part 1."""
    for i in range(10):
        next(grid)
        print(grid, "\n")
    return 0


def part_2(grid: Grid):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
