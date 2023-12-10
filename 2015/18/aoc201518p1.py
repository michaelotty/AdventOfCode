"""Advent of code Day 18 part 1."""

import copy


def main() -> None:
    """Program starts here."""
    with open("2015/18/input.txt", encoding="utf-8") as file:
        lines = file.read().split()

    gol = GameOfLife(lines)

    for _ in range(100):
        next(gol)

    print(gol.num_of_lights_on)


class GameOfLife:
    """Game of life grid."""

    def __init__(self, lines: list) -> None:
        """Create a game of life grid."""
        self._text_file_contents = lines
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = [
            [self._extract_cell(i, j) for i in range(self.height)]
            for j in range(self.width)
        ]

    def __repr__(self) -> str:
        """Return a string representation."""
        return (
            "\n".join(
                "".join("#" if item else "." for item in line) for line in self.grid
            )
            + "\n"
        )

    @property
    def num_of_lights_on(self) -> int:
        """Get the total number of lights switched on."""
        return sum(sum(line) for line in self.grid)

    def __next__(self) -> None:
        """Update the game of life."""
        new_grid = copy.deepcopy(self.grid)

        for i in range(self.height):
            for j in range(self.width):
                neighbour_sum = 0
                for x in range(i - 1, i + 2):
                    if not 0 <= x < self.height:
                        continue
                    for y in range(j - 1, j + 2):
                        if not 0 <= y < self.width:
                            continue
                        if x == i and y == j:
                            continue
                        if self.grid[x][y]:
                            neighbour_sum += 1
                new_grid[i][j] = self._process_cell(self.grid[i][j], neighbour_sum)

        self.grid = new_grid.copy()

    def _extract_cell(self, i: int, j: int) -> bool:
        """Convert character map into bool map."""
        if self._text_file_contents[j][i] == "#":
            return True
        return False

    @staticmethod
    def _process_cell(prev_value: bool, sum_of_neighbors: int) -> bool:
        """Process the cell's next value."""
        if prev_value:
            return sum_of_neighbors in (2, 3)
        return sum_of_neighbors == 3


if __name__ == "__main__":
    main()
