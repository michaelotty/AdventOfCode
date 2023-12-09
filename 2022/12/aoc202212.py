"""Advent of code Day 12."""

import queue


def main() -> None:
    """Main function."""
    with open("2022/12/input.txt", encoding="utf-8") as file:
        height_map = file.read().splitlines()
        height_map = [list(map(ord, line)) for line in height_map]

    print("Part 1:", part_1(height_map))
    print("Part 2:", part_2(height_map))


def part_1(height_map: list[list[int]]) -> int:
    """Solve part 1."""
    return solve(height_map, find("S", height_map))


def part_2(height_map: list[list[int]]) -> int:
    """Solve part 2."""
    return min(
        solve(height_map, starting_coord)
        for starting_coord in find_all("a", height_map)
    )


def solve(height_map: list[list[int]], start_coord: tuple[int, int] | None) -> int:
    """Solve the path length for a given starting position up to E marker."""
    end_coord = find("E", height_map)

    frontier: queue.PriorityQueue = queue.PriorityQueue()
    frontier.put((0, start_coord))
    came_from: dict[tuple[int, int] | None, tuple[int, int] | None] = {}
    cost_so_far = {}
    came_from[start_coord] = None
    cost_so_far[start_coord] = 0

    while not frontier.empty():
        _, current_coord = frontier.get()

        if current_coord == end_coord:
            break

        for next_coord in get_neighbors(current_coord, height_map):
            new_cost = cost_so_far[current_coord] + 1
            if (next_coord not in cost_so_far) or (new_cost < cost_so_far[next_coord]):
                cost_so_far[next_coord] = new_cost
                priority = new_cost + heuristic(next_coord, end_coord)
                frontier.put((priority, next_coord))
                came_from[next_coord] = current_coord

    if current_coord != end_coord:
        return len(height_map) * len(height_map[0])

    current_coord = end_coord
    path = []
    while current_coord != start_coord:
        path.append(current_coord)
        current_coord = came_from[current_coord]

    return len(path)


def find(char_to_find: str, height_map: list[list[int]]) -> tuple[int, int] | None:
    """Find the first coordinate of a character in height map grid."""
    char_code_to_find = ord(char_to_find)
    for i, line in enumerate(height_map):
        for j, char_to_search in enumerate(line):
            if char_to_search == char_code_to_find:
                return (i, j)

    return None


def find_all(char_to_find: str, height_map: list[list[int]]) -> list[tuple[int, int]]:
    """Find the first coordinate of a character in height map grid."""
    char_code_to_find = ord(char_to_find)
    coords = []

    for i, line in enumerate(height_map):
        coords.extend(
            [
                (i, j)
                for j, char_to_search in enumerate(line)
                if char_to_search == char_code_to_find
            ]
        )

    return coords


def get_neighbors(
    from_coord: tuple[int, int], height_map: list[list[int]]
) -> list[tuple[int, int]]:
    """Find all the squares we can move to from our location."""
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    frontier = []

    for row, col in directions:
        to_coord = (from_coord[0] + row, from_coord[1] + col)
        if not 0 <= to_coord[0] < len(height_map):
            continue
        if not 0 <= to_coord[1] < len(height_map[0]):
            continue

        from_height = height_map[from_coord[0]][from_coord[1]]
        to_height = height_map[to_coord[0]][to_coord[1]]

        # Remap S and E to a and z
        remapping = {ord("S"): ord("a"), ord("E"): ord("z")}
        from_height = remapping.get(from_height, from_height)
        to_height = remapping.get(to_height, to_height)

        if to_height - from_height <= 1:
            frontier.append(to_coord)

    return frontier


def heuristic(coord_a: tuple[int, int] | None, coord_b: tuple[int, int] | None) -> int:
    """Manhattan distance."""
    if coord_a is None or coord_b is None:
        return 0
    x1, y1 = coord_a
    x2, y2 = coord_b
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    main()
