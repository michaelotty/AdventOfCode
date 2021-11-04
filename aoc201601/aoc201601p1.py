"""Advent of code Day 1 part 1"""

from turtle import forward, left, mode, position, right, setposition, speed


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as f:
        instructions = f.read().split(', ')

    setposition((0, 0))
    mode('logo')
    speed(0)

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])

        if direction == 'R':
            right(90)
        elif direction == 'L':
            left(90)
        else:
            raise ValueError

        forward(steps)

    x, y = position()
    print(round(x + y))


if __name__ == "__main__":
    main()
