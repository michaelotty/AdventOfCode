"""Advent of code Day 14."""


def main():
    """Main function."""
    with open("2022/14/input.txt", encoding="utf-8") as file:
        lines = file.read().splitlines()
    print("Part 1:", part_1(form_grid(lines)))
    print("Part 2:", part_2(form_grid(lines)))


def form_grid(lines: list[str]) -> set[tuple[int, int]]:
    """Form a grid of filled points with the input text."""
    grid = set()
    for line in lines:
        line_ends = [tuple(map(int, point.split(","))) for point in line.split(" -> ")]
        for left, right in zip(line_ends[:-1], line_ends[1:]):
            x_min, x_max = min(left[0], right[0]), max(left[0], right[0])
            y_min, y_max = min(left[1], right[1]), max(left[1], right[1])
            for x in range(x_min, x_max + 1):
                for y in range(y_min, y_max + 1):
                    grid.add((x, y))

    return grid


def part_1(grid: set[tuple[int, int]]) -> int:
    """Solve part 1."""
    start_coord = (500, 0)
    coord = start_coord
    count = 0
    bottom_y = max(grid, key=lambda x: x[1])[1]

    while True:
        coord_below = (coord[0], coord[1] + 1)
        coord_below_left = (coord[0] - 1, coord[1] + 1)
        coord_below_right = (coord[0] + 1, coord[1] + 1)

        if coord_below not in grid:
            coord = coord_below
            if coord[1] > bottom_y:
                break
        elif coord_below_left not in grid:
            coord = coord_below_left
        elif coord_below_right not in grid:
            coord = coord_below_right
        else:
            grid.add(coord)
            coord = start_coord
            count += 1

    return count


def part_2(grid: set[tuple[int, int]]) -> int:
    """Solve part 2."""
    start_coord = (500, 0)
    coord = start_coord
    count = 0

    # Add floor
    large_amount = 10000
    bottom_y = max(grid, key=lambda x: x[1])[1] + 2
    min_x = min(grid, key=lambda x: x[0])[0] - large_amount
    max_x = max(grid, key=lambda x: x[0])[0] + large_amount
    for x in range(min_x, max_x):
        grid.add((x, bottom_y))

    while True:
        coord_below = (coord[0], coord[1] + 1)
        coord_below_left = (coord[0] - 1, coord[1] + 1)
        coord_below_right = (coord[0] + 1, coord[1] + 1)

        if coord_below not in grid:
            coord = coord_below
        elif coord_below_left not in grid:
            coord = coord_below_left
        elif coord_below_right not in grid:
            coord = coord_below_right
        else:
            grid.add(coord)
            count += 1
            if coord == start_coord:
                break
            coord = start_coord

    return count


if __name__ == "__main__":
    main()
