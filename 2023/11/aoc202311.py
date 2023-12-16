"""Advent of code day 11."""

import itertools


class GalaxyMap:
    """Galaxy map."""

    def __init__(self, text: str) -> None:
        """Create a galaxy map."""
        self.grid = [list(line) for line in text.splitlines()]

    def expand_universe(self):
        """Expand the universe."""
        empty_rows = [len(set(line)) == 1 for line in self.grid]
        empty_cols = [len(set(col)) == 1 for col in zip(*self.grid)]

        empty_row = ["." for _ in self.grid[0]]

        for i, is_empty in reversed(list(enumerate(empty_rows))):
            if is_empty:
                self.grid.insert(i, empty_row.copy())

        for i, is_empty in reversed(list(enumerate(empty_cols))):
            if is_empty:
                for row in self.grid:
                    row.insert(i, ".")

    @property
    def galaxy_coords(self) -> set[tuple[int, int]]:
        """Get the galaxy coordinates."""
        galaxy_coords = set()
        for i, row in enumerate(self.grid):
            for j, char in enumerate(row):
                if char == "#":
                    galaxy_coords.add((i, j))
        return galaxy_coords

    @property
    def galaxy_routes(self):
        """Find the routes between galaxies."""
        galaxy_coords = self.galaxy_coords
        galaxy_routes = list(itertools.combinations(galaxy_coords, 2))
        return galaxy_routes

    def solve(self) -> int:
        """Solve puzzle."""
        return sum(
            manhattan_distance(left, right) for left, right in self.galaxy_routes
        )

    def __repr__(self) -> str:
        """Return a string representation."""
        return "\n".join("".join(line) for line in self.grid)


def manhattan_distance(from_coord: tuple[int, int], to_coord: tuple[int, int]) -> int:
    """Calculate the manhattan distances between coordinates."""
    return sum(abs(left - right) for left, right in zip(from_coord, to_coord))


def main() -> None:
    """Program starts here."""
    with open("2023/11/input.txt", encoding="utf-8") as file:
        text = file.read()

    data = GalaxyMap(text)

    print("Part 1:", part_1(data))
    print("Part 2:", part_2())


def part_1(data) -> int:
    """Solve part 1."""
    data.expand_universe()
    return data.solve()


def part_2() -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
