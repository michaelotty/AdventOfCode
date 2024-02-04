"""Advent of code day 17."""


def main() -> None:
    """Program starts here."""
    with open("2023/17/test.txt", encoding="utf-8") as file:
        grid = [list(map(int, line)) for line in file.read().splitlines()]

    print("Part 1:", part_1(grid))
    print("Part 2:", part_2(grid))


def part_1(grid: list[list[int]]) -> int:
    """Solve part 1."""
    start: tuple[int, int] = (0, 0)
    # end: tuple[int, int] = (len(grid), len(grid[0]))
    directions: dict[str, tuple[int, int]] = {
        "u": (-1, 0),
        "d": (1, 0),
        "l": (0, -1),
        "r": (0, 1),
    }

    frontier: list[tuple[int, int]] = [start]
    reached: set[tuple[int, int]] = {start}

    def in_bounds(pos: tuple[int, int]) -> bool:
        width = len(grid[0])
        height = len(grid)
        return 0 <= pos[0] < height and 0 <= pos[1] < width

    def get_neighbors(pos: tuple[int, int]) -> list[tuple[int, int]]:
        new_neighbors = []
        for i in range(3):
            for direction in directions.values():
                new_neighbor = (
                    pos[0] + direction[0] * (i + 1),
                    pos[1] + direction[1] * (i + 1),
                )
                if in_bounds(new_neighbor):
                    new_neighbors.append(new_neighbor)
        return new_neighbors

    while frontier:
        position = frontier.pop()
        for neighbour in get_neighbors(position):
            if neighbour not in reached:
                frontier.insert(0, neighbour)
                reached.add(neighbour)

    return grid[0][0]


def part_2(grid: list[list[int]]) -> int:
    """Solve part 2."""
    return grid[0][0]


if __name__ == "__main__":
    main()
