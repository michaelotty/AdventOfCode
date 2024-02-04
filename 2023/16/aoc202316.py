"""Advent of code day 16."""

from typing import Literal


def main() -> None:
    """Program starts here."""
    with open("2023/16/input.txt", encoding="utf-8") as file:
        grid = [list(line) for line in file.read().splitlines()]

    print("Part 1:", part_1(grid))
    print("Part 2:", part_2(grid))


def part_1(grid: list[list[str]]) -> int:
    """Solve part 1."""
    return run_energisation_sequence(grid, position=(0, -1), direction_char="r")


def part_2(grid: list[list[str]]) -> int:
    """Solve part 2."""
    width = len(grid[0])
    height = len(grid)

    starting_points = []

    # Add top and bottom
    for i in range(width):
        starting_points.append(((-1, i), "d"))
        starting_points.append(((height, i), "u"))

    # Add left and right
    for i in range(width):
        starting_points.append(((i, -1), "r"))
        starting_points.append(((i, height), "l"))

    return max(
        run_energisation_sequence(grid, position, direction_char)
        for position, direction_char in starting_points
    )


def run_energisation_sequence(
    grid: list[list[str]],
    position: tuple[int, int],
    direction_char: Literal["u", "d", "l", "r"] | str,
) -> int:
    """Energise the grid from a starting position and direction."""
    directions: dict[str, tuple[int, int]] = {
        "u": (-1, 0),
        "d": (1, 0),
        "l": (0, -1),
        "r": (0, 1),
    }

    direction = directions[direction_char]

    def in_bounds(pos: tuple[int, int]) -> bool:
        width = len(grid[0])
        height = len(grid)
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

        position_ch = grid[position[0]][position[1]]

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

    return len({position for position, _ in visited})


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
