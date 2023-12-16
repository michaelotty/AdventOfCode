"""Advent of code day 11."""

import itertools


class GalaxyMap:
    """Galaxy map."""

    def __init__(self, text: str) -> None:
        """Create a galaxy map."""
        self.galaxy_coords = set()
        grid = [list(line) for line in text.splitlines()]
        self.width = len(grid[0])
        self.height = len(grid)

        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char == "#":
                    self.galaxy_coords.add((i, j))

    def expand_universe(self, amount: int = 2) -> None:
        """Expand the universe."""
        amount -= 1
        # Expand the rows first
        for i in reversed(range(self.height)):
            # Handle not empty row early
            if any((i, j) in self.galaxy_coords for j in range(self.width)):
                continue

            self.height += amount

            for coord in self.galaxy_coords.copy():
                if coord[0] > i:
                    self.galaxy_coords.remove(coord)
                    self.galaxy_coords.add((coord[0] + amount, coord[1]))

        # Then columns
        for j in reversed(range(self.width)):
            # Handle not empty col early
            if any((i, j) in self.galaxy_coords for i in range(self.height)):
                continue

            self.width += amount

            for coord in self.galaxy_coords.copy():
                if coord[1] > j:
                    self.galaxy_coords.remove(coord)
                    self.galaxy_coords.add((coord[0], coord[1] + amount))

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
        grid = [["." for _ in range(self.width)] for _ in range(self.height)]
        for coord in self.galaxy_coords:
            grid[coord[0]][coord[1]] = "#"
        return "\n".join("".join(line) for line in grid)


def manhattan_distance(from_coord: tuple[int, int], to_coord: tuple[int, int]) -> int:
    """Calculate the manhattan distances between coordinates."""
    return sum(abs(left - right) for left, right in zip(from_coord, to_coord))


def main() -> None:
    """Program starts here."""
    with open("2023/11/input.txt", encoding="utf-8") as file:
        text = file.read()

    print("Part 1:", part_1(GalaxyMap(text)))
    print("Part 2:", part_2(GalaxyMap(text)))


def part_1(galaxy_map) -> int:
    """Solve part 1."""
    galaxy_map.expand_universe()
    return galaxy_map.solve()


def part_2(galaxy_map) -> int:
    """Solve part 2."""
    galaxy_map.expand_universe(1000000)
    return galaxy_map.solve()


if __name__ == "__main__":
    main()
