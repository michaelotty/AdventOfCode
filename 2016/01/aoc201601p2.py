"""Advent of code Day 1 part 2"""

from turtle import Screen, Turtle, Vec2D


def find_position(instructions) -> Vec2D | None:
    """Find position."""
    screen = Screen()
    turtle = Turtle()

    turtle.setposition((0, 0))
    screen.mode("logo")
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
                screen.mainloop()
                return turtle.position()
            visited_locations.add(turtle.position())

    return None


def main() -> None:
    """Main function"""
    with open("2016/01/input.txt", encoding="utf-8") as f:
        instructions = f.read().split(", ")

    x, y = find_position(instructions)

    print(round(x + y))


if __name__ == "__main__":
    main()
