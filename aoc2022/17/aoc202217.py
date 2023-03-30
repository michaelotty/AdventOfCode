"""Advent of code Day 17."""

import itertools
from abc import ABC, abstractmethod


def main():
    """Main function."""
    print("Part 1:", part_1())
    print("Part 2:", part_2())


class Shape(ABC):
    """Abstract shape."""

    @abstractmethod
    def __repr__(self) -> str:
        """Get the ascii version of the shape."""

    @property
    @abstractmethod
    def coords(self) -> set[tuple[int, int]]:
        """Get the starting coords for a shape."""


class MinusShape(Shape):
    """Minus shape."""

    def __repr__(self) -> str:
        """Get the ascii version of the shape."""
        return "####"

    @property
    def coords(self) -> set[tuple[int, int]]:
        """Get the starting coords for a shape."""
        return {(0, x) for x in range(4)}


class PlusShape(Shape):
    """Plus shape."""

    def __repr__(self) -> str:
        """Get the ascii version of the shape."""
        return " #\n###\n #"

    @property
    def coords(self) -> set[tuple[int, int]]:
        """Get the starting coords for a shape."""
        return {(1, x) for x in range(3)} | {(0, 1), (2, 1)}


class LShape(Shape):
    """L shape."""

    def __repr__(self) -> str:
        """Get the ascii version of the shape."""
        return "  #\n  #\n###"

    @property
    def coords(self) -> set[tuple[int, int]]:
        """Get the starting coords for a shape."""
        return {(0, x) for x in range(3)} | {(x, 0) for x in range(3)}


class IShape(Shape):
    """I shape."""

    def __repr__(self) -> str:
        """Get the ascii version of the shape."""
        return "#\n#\n#\n#"

    @property
    def coords(self) -> set[tuple[int, int]]:
        """Get the starting coords for a shape."""
        return {(x, 0) for x in range(4)}


class BoxShape(Shape):
    """Box shape."""

    def __repr__(self) -> str:
        """Get the ascii version of the shape."""
        return "##\n##"

    @property
    def coords(self) -> set[tuple[int, int]]:
        """Get the starting coords for a shape."""
        return {(x, y) for x in range(2) for y in range(2)}


class Grid:
    """A grid."""

    def __init__(self) -> None:
        """Create a grid."""
        self.grid = set()

        self.direction_generator = self._direction_generator()
        self.shape_generator = self._shape_generator()

    def _direction_generator(self):
        """Generate the infinite looping directions from the file."""
        with open("aoc2022/17/test1.txt", encoding="utf-8") as file:
            directions = file.read()

        for char in itertools.cycle(directions):
            yield char

    def _shape_generator(self):
        """Generate the shape to use infinitely."""
        shapes = (MinusShape, PlusShape, LShape, IShape, BoxShape)[4:]

        for shape in itertools.cycle(shapes):
            yield shape()

    def __next__(self):
        """Add a shape to the grid, then iterate the movement until it stops."""
        shape = next(self.shape_generator)

        height = 0

        if self.grid:
            height = self._get_max_row()

        active_shape = {(row + height + 3, col + 2) for row, col in shape.coords}

        self.grid |= active_shape

    def _get_max_row(self):
        return max(row for row, _ in self.grid)

    def __repr__(self) -> str:
        """String representation of grid."""
        rows_to_print = []

        for row in range(self._get_max_row() + 1):
            row_line = []
            for col in range(7):
                if (row, col) in self.grid:
                    row_line.append("#")
                else:
                    row_line.append(".")

            rows_to_print.append("".join(row_line))

        rows_to_print.reverse()

        return "\n".join(rows_to_print)


def print_grid(grid):
    """Print the grid representation."""
    grid = zip(*grid)
    print("\n".join("".join(line) for line in grid))


def part_1():
    """Solve part 1."""
    grid = Grid()
    next(grid)

    print(grid)

    return 0


def part_2():
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
