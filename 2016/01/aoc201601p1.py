"""Advent of code Day 1 part 1"""

from turtle import Screen, Turtle


def main() -> None:
    """Main function"""
    with open("2016/01/input.txt", encoding="utf-8") as f:
        instructions = f.read().split(", ")

    screen = Screen()
    turtle = Turtle()

    turtle.setposition((0, 0))
    screen.mode("logo")
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
    print(round(x + y))

    screen.mainloop()


if __name__ == "__main__":
    main()
