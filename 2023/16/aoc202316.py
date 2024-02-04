"""Advent of code day 16."""


def main() -> None:
    """Program starts here."""
    with open("2023/16/input.txt", encoding="utf-8") as file:
        data = [list(line) for line in file.read().splitlines()]

    print("Part 1:", part_1(data))
    print("Part 2:", part_2())


def part_1(data: list[list[str]]) -> int:
    """Solve part 1."""
    directions: dict[str, tuple[int, int]] = {
        "u": (-1, 0),
        "d": (1, 0),
        "l": (0, -1),
        "r": (0, 1),
    }
    position = (0, -1)
    direction_char = "r"
    direction = directions[direction_char]

    def in_bounds(pos: tuple[int, int]) -> bool:
        width = len(data[0])
        height = len(data)
        return 0 <= pos[0] < height and 0 <= pos[1] < width

    visited: set[tuple[tuple[int, int], str]] = set()
    frontier: set[tuple[tuple[int, int], str]] = set()

    next_position = (position[0] + direction[0], position[1] + direction[1])
    frontier.add((next_position, direction_char))

    mirrors = {
        "\\": {"u": "l", "d": "r", "l": "u", "r": "d"},
        "/": {"u": "r", "d": "l", "l": "d", "r": "u"},
    }

    while frontier:
        position, direction_char = frontier.pop()
        if (position, direction_char) in visited:
            continue
        visited.add((position, direction_char))

        position_ch = data[position[0]][position[1]]

        if (
            position_ch == "."
            or (direction_char in ("l", "r") and position_ch == "-")
            or (direction_char in ("u", "d") and position_ch == "|")
        ):
            direction = directions[direction_char]

        elif position_ch in ("\\", "/"):
            direction_char = mirrors[position_ch][direction_char]
            direction = directions[direction_char]

        elif direction_char in ("u", "d") and position_ch == "-":
            # Add left now, and right later
            direction = directions["l"]
            next_position = (position[0] + direction[0], position[1] + direction[1])
            if in_bounds(next_position):
                frontier.add((next_position, "l"))

            direction_char = "r"
            direction = directions[direction_char]

        elif direction_char in ("l", "r") and position_ch == "|":
            # Add up now, and down later
            direction = directions["u"]
            next_position = (position[0] + direction[0], position[1] + direction[1])
            if in_bounds(next_position):
                frontier.add((next_position, "u"))

            direction_char = "d"
            direction = directions[direction_char]

        else:
            raise RuntimeError("Unrecognised grid position")

        next_position = (position[0] + direction[0], position[1] + direction[1])
        if in_bounds(next_position):
            frontier.add((next_position, direction_char))

    visited_tiles = {position for position, _ in visited}

    return len(visited_tiles)


def part_2() -> int:
    """Solve part 2."""
    return 0


def print_debug(
    width: int,
    height: int,
    visited: set[tuple[tuple[int, int], str]],
) -> None:
    """Print the light beams for debugging."""
    grid = [["." for _ in range(width)] for _ in range(height)]

    for position, direction_char in visited:
        printable_direction = {"u": "^", "d": "v", "l": "<", "r": ">"}
        direction_char = printable_direction[direction_char]
        if grid[position[0]][position[1]] == ".":
            grid[position[0]][position[1]] = direction_char
        else:
            grid[position[0]][position[1]] = "2"

    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    main()
