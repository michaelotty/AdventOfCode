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
        return {(0, x) for x in range(3)} | {(x, 2) for x in range(3)}


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

    def __init__(self, file_name) -> None:
        """Create a grid."""
        self.grid = set()

        with open(file_name, encoding="utf-8") as file:
            self.directions_string = file.read()

        self.direction_generator = self._direction_generator()
        self.shape_generator = self._shape_generator()

    def _direction_generator(self):
        """Generate the infinite looping directions from the file."""
        for i, char in itertools.cycle(enumerate(self.directions_string)):
            # print(i, char)
            yield char

    def _shape_generator(self):
        """Generate the shape to use infinitely."""
        shapes = (MinusShape, PlusShape, LShape, IShape, BoxShape)

        for shape in itertools.cycle(shapes):
            yield shape()

    def get_max_row(self, grid):
        if not grid:
            grid = self.grid

        return max(row for row, _ in grid)

    def _move_shape(self, shape, direction):
        direction_mapping = {"right": (0, 1), "left": (0, -1), "down": (-1, 0)}
        direction = direction_mapping[direction]
        return {(row + direction[0], col + direction[1]) for row, col in shape}

    def _str_of_grid(self, grid) -> str:
        """String representation of a grid."""
        rows_to_print = []

        for row in range(self.get_max_row(grid) + 1):
            row_line = []
            for col in range(7):
                if (row, col) in grid:
                    row_line.append("#")
                else:
                    row_line.append(".")

            rows_to_print.append("".join(row_line))

        rows_to_print.reverse()

        return "\n".join(rows_to_print)

    def __next__(self):
        """Add a shape to the grid, then iterate the movement until it stops."""
        shape = next(self.shape_generator)

        height = 0

        if self.grid:
            height = self.get_max_row(self.grid) + 1

        active_shape = {(row + height + 3, col + 2) for row, col in shape.coords}

        next_active_shape = active_shape.copy()

        direction_mapping = {">": "right", "<": "left"}

        falling = True

        while falling:
            next_active_shape = self._move_shape(
                next_active_shape, direction_mapping[next(self.direction_generator)]
            )

            # print(self._str_of_grid(next_active_shape))
            # print()

            for row, col in next_active_shape:
                if not 0 <= col < 7:
                    next_active_shape = active_shape.copy()
                    break

                if (row, col) in self.grid:
                    next_active_shape = active_shape.copy()
                    break

            active_shape = next_active_shape.copy()

            next_active_shape = self._move_shape(next_active_shape, "down")

            for row, col in next_active_shape:
                if (row, col) in self.grid or row < 0:
                    next_active_shape = active_shape.copy()
                    falling = False
                    break

            active_shape = next_active_shape.copy()

        self.grid |= active_shape

    def __repr__(self) -> str:
        """String representation of grid."""
        return self._str_of_grid(self.grid)


def part_1():
    """Solve part 1."""
    grid = Grid("aoc2022/17/input.txt")
    for _ in range(2022):
        next(grid)

    return grid.get_max_row(grid.grid) + 1


def part_2():
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
