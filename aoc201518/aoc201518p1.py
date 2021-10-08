"""Advent of code Day 18 part 1"""


def main():
    """Main function"""
    with open('test.txt') as file:
        lines = file.read().split()

    gol = GameOfLife(lines)

    for _ in range(3):
        print(gol)
        print()
        gol.update()

    print(gol.num_of_lights_on)


class GameOfLife:
    """Creates a game of life grid"""

    def __init__(self, lines: list) -> None:
        self._text_file_contents = lines
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = [[self._extract_cell(i, j) for i in range(
            self.height)] for j in range(self.width)]

    def __str__(self) -> str:
        return '\n'.join(''.join('#' if item else '.' for item in line) for line in self.grid)

    @property
    def num_of_lights_on(self) -> int:
        """Gets the total number of lights switched on"""
        return sum([sum(line) for line in self.grid])

    def update(self) -> None:
        """Update the game of life"""
        new_grid = self.grid.copy()

        height = len(self.grid)
        width = len(self.grid[0])

        # Corners
        top_left = sum((self.grid[0][1], self.grid[1][0], self.grid[1][1]))
        top_right = sum((self.grid[width-2][0], self.grid[width-2][1], self.grid[width-1][1]))
        bottom_left = sum((self.grid[0][height-2], self.grid[1][height-2], self.grid[1][height-1]))
        bottom_right = sum((self.grid[width-2][height-2], self.grid[width-1][height-2], self.grid[width-2][height-1]))

        new_grid[0][0] = True if top_left == 2 else 
        new_grid[width-1][0] = sum((self.grid[width-2][0], self.grid[width-2][1], self.grid[width-1][1]))
        new_grid[0][height-1] = sum((self.grid[0][height-2], self.grid[1][height-2], self.grid[1][height-1]))
        new_grid[width-1][height-1] = sum((self.grid[width-2][height-2], self.grid[width-1][height-2], self.grid[width-2][height-1]))

        # Edges
        # for i

        for i in range(1, height - 1):
            for j in range(1, width - 1):
                neighbours = (self.grid[i-1][j-1], self.grid[i-1][j], self.grid[i-1][j+1],
                              self.grid[i][j-1], self.grid[i][j+1],
                              self.grid[i+1][j-1], self.grid[i+1][j], self.grid[i+1][j+1])
                total = sum(neighbours)
                if total == 3:
                    new_grid[i][j] = True
                elif total != 2:
                    new_grid[i][j] = False

        self.grid = new_grid.copy()

    def _extract_cell(self, i: int, j: int) -> bool:
        """Convert character map into bool map"""
        if self._text_file_contents[j][i] == '#':
            return True
        return False


if __name__ == "__main__":
    main()
