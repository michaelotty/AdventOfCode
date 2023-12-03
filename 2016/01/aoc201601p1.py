"""Advent of code Day 1 part 1"""

import turtle


def main():
    """Main function"""
    with open("2016/01/input.txt", encoding="utf-8") as f:
        instructions = f.read().split(", ")

    turtle.setposition((0, 0))
    turtle.mode("logo")
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


if __name__ == "__main__":
    main()
