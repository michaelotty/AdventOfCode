"""Advent of code Day 1 part 2"""

from turtle import forward, left, mode, position, right, setposition, speed


def find_position(instructions):
    setposition((0, 0))
    mode('logo')
    speed(0)

    visited_locations = {position()}

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])

        if direction == 'R':
            right(90)
        elif direction == 'L':
            left(90)
        else:
            raise ValueError

        for _ in range(steps):
            forward(1)
            if position() in visited_locations:
                return position()
            visited_locations.add(position())


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as f:
        instructions = f.read().split(', ')

    x, y = find_position(instructions)

    print(round(x + y))


if __name__ == "__main__":
    main()
