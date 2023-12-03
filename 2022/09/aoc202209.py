"""Advent of code Day 9."""


def main():
    """Main function."""
    with open("2022/09/input.txt", encoding="utf-8") as file:
        instructions = [line.split() for line in file.read().splitlines()]
        instructions = [(direction, int(amount)) for direction, amount in instructions]
    print("Part 1:", solve(instructions, 2))
    print("Part 2:", solve(instructions, 10))


def solve(instructions, length):
    """Solve for any rope length."""
    rope = [(0, 0) for _ in range(length)]
    tail_visited_coords = {rope[-1]}
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
    indexes = list(range(length))
    for direction, amount in instructions:
        for _ in range(amount):
            head_direction = directions[direction]
            rope[0] = move_coord(rope[0], head_direction)

            for head_idx, tail_idx in zip(indexes[:-1], indexes[1:]):
                if distance(rope[head_idx], rope[tail_idx]) > 1:
                    tail_direction = directions[
                        tail_move_direction(rope[head_idx], rope[tail_idx])
                    ]
                    rope[tail_idx] = move_coord(rope[tail_idx], tail_direction)
            tail_visited_coords.add(rope[-1])
    return len(tail_visited_coords)


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


def distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    """The distance on with the puzzle distance definition."""
    return max(abs(b[0] - a[0]), abs(b[1] - a[1]))


if __name__ == "__main__":
    main()
