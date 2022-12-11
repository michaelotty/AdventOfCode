"""Advent of code Day 9."""


def main():
    """Main function."""
    with open("aoc2022/09/input.txt", encoding="utf-8") as file:
        instructions = [line.split() for line in file.read().splitlines()]
        instructions = [(direction, int(amount)) for direction, amount in instructions]
    print("Part 1:", part_1(instructions))
    print("Part 2:", part_2(instructions))


def part_1(instructions):
    """Solve part 1."""
    head_pos = (0, 0)
    tail_pos = (0, 0)
    coords = {tail_pos}
    directions = {
        "U": (0, 1),
        "R": (1, 0),
        "D": (0, -1),
        "L": (-1, 0),
        "UR": (1, 1),
        "DR": (1, -1),
        "DL": (-1, -1),
        "UL": (-1, 1),
    }
    for direction, amount in instructions:
        head_direction = directions[direction]
        for _ in range(amount):
            head_pos = move_coord(head_pos, head_direction)
            if distance(head_pos, tail_pos) > 1:
                tail_direction = directions[tail_move_direction(head_pos, tail_pos)]
                tail_pos = move_coord(tail_pos, tail_direction)
                coords.add(tail_pos)
    return len(coords)


def tail_move_direction(head_pos, tail_pos):
    """Work out what direction the tail needs to move to catchup with the head."""
    directions = {
        (0, 2): "U",
        (2, 0): "R",
        (0, -2): "D",
        (-2, 0): "L",
        (2, 2): "UR",
        (1, 2): "UR",
        (2, 1): "UR",
        (2, -2): "DR",
        (1, -2): "DR",
        (2, -1): "DR",
        (-2, -2): "DL",
        (-1, -2): "DL",
        (-2, -1): "DL",
        (-2, 2): "UL",
        (-1, 2): "UL",
        (-2, 1): "UL",
    }
    x_change = head_pos[0] - tail_pos[0]
    y_change = head_pos[1] - tail_pos[1]
    return directions[(x_change, y_change)]


def move_coord(coord: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    """Move the coordinate in the specified direction."""
    return (
        coord[0] + direction[0],
        coord[1] + direction[1],
    )


def part_2(instructions):
    """Solve part 2."""
    return 0


def distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    """The distance on with the puzzle distance definition."""
    return max(abs(b[0] - a[0]), abs(b[1] - a[1]))


if __name__ == "__main__":
    main()
