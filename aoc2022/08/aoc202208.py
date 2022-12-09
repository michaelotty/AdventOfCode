"""Advent of code Day 8."""


def main():
    """Main function."""
    with open("aoc2022/08/input.txt", encoding="utf-8") as file:
        number_grid = [[int(num) for num in line] for line in file.read().splitlines()]
    print("Part 1:", part_1(number_grid))
    print("Part 2:", part_2(number_grid))


def part_1(number_grid: list[list[int]]) -> int:
    """Solve part 1."""
    width = len(number_grid[0])
    height = len(number_grid)
    coords = set()
    directions = {
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1),
        "up": (-1, 0),
    }
    for direction in directions.values():
        for start_row in range(height):
            for start_col in range(width):
                row = start_row
                col = start_col
                tree_height = number_grid[row][col]
                blocked = False
                row, col = row + direction[0], col + direction[1]

                while 0 <= row < height and 0 <= col < width:
                    if number_grid[row][col] >= tree_height:
                        blocked = True
                        break
                    row, col = row + direction[0], col + direction[1]

                if not blocked:
                    coords.add((start_row, start_col))

    # debug_coords = coords
    # debug_coords.remove((0, 0))
    # debug_coords.remove((1, 0))
    # debug_coords.remove((2, 0))
    # debug_coords.remove((3, 0))

    # debug_coords.remove((4, 0))
    # debug_coords.remove((4, 1))
    # debug_coords.remove((4, 2))
    # debug_coords.remove((4, 3))

    # debug_coords.remove((4, 4))
    # debug_coords.remove((3, 4))
    # debug_coords.remove((2, 4))
    # debug_coords.remove((1, 4))

    # debug_coords.remove((0, 4))
    # debug_coords.remove((0, 3))
    # debug_coords.remove((0, 2))
    # debug_coords.remove((0, 1))
    # print(*sorted(debug_coords))

    return len(coords)


def part_2(number_grid: list[list[int]]) -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
