"""Advent of code Day 1."""

from turtle import Screen, Turtle, Vec2D


def part_1(instructions: list[str]) -> int:
    """Program starts here."""
    turtle = Turtle()

    turtle.setposition((0, 0))
    turtle.speed(0)

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])

        if direction == "R":
            turtle.right(90)
        elif direction == "L":
            turtle.left(90)
        else:
            raise ValueError

        turtle.forward(steps)

    x, y = turtle.position()
    return round(x + y)


def find_position(instructions: list[str]) -> Vec2D | None:
    """Find position."""
    turtle = Turtle()

    turtle.setposition((0, 0))
    turtle.speed(0)

    visited_locations = {turtle.position()}

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])

        if direction == "R":
            turtle.right(90)
        elif direction == "L":
            turtle.left(90)
        else:
            raise ValueError

        for _ in range(steps):
            turtle.forward(1)
            if turtle.position() in visited_locations:
                return turtle.position()
            visited_locations.add(turtle.position())

    return None


def part_2(instructions: list[str]) -> int:
    """Solve part 2."""
    vec = find_position(instructions)
    assert vec
    x, y = vec

    return round(x + y)


if __name__ == "__main__":
    with open("2016/01/input.txt", encoding="utf-8") as f:
        instructions_text = f.read().split(", ")

    screen = Screen()
    screen.mode("logo")
    print(f"Part 1: {part_1(instructions_text)}")
    print(f"Part 2: {part_2(instructions_text)}")
    screen.mainloop()
