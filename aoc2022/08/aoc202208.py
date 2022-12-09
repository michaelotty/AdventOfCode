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

    return len(coords)


def part_2(number_grid: list[list[int]]) -> int:
    """Solve part 2."""
    width = len(number_grid[0])
    height = len(number_grid)
    coords = {}
    directions = {
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1),
        "up": (-1, 0),
    }
    for start_row in range(1, height - 1):
        for start_col in range(1, width - 1):
            scenic_score = 1
            for direction in directions.values():
                row = start_row
                col = start_col
                tree_height = number_grid[row][col]
                row, col = row + direction[0], col + direction[1]
                tree_count = 0

                while 0 <= row < height and 0 <= col < width:
                    tree_count += 1
                    if number_grid[row][col] >= tree_height:
                        break
                    row, col = row + direction[0], col + direction[1]

                scenic_score *= tree_count

            coords[(start_row, start_col)] = scenic_score

    return max(coords.values())  # 127 too low


if __name__ == "__main__":
    main()
