"""Advent of code Day 3 part 2"""

from itertools import product


def move(position: tuple[int, int], direction: str) -> tuple:
    """Move coordinate in indicated direction"""
    if direction == 'right':
        position = (position[0] + 1, position[1])
    elif direction == 'up':
        position = (position[0], position[1] + 1)
    elif direction == 'left':
        position = (position[0] - 1, position[1])
    elif direction == 'down':
        position = (position[0], position[1] - 1)
    else:
        raise ValueError(f'{direction} is not a valid direction')

    return position


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        puzzle_input = int(file.read())

    position = (0, 0)
    position_grid = {position: 1}

    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0

    direction = 'right'
    while True:
        position = move(position, direction)
        if position[0] > max_x:
            direction = 'up'
            max_x = position[0]
        elif position[1] > max_y:
            direction = 'left'
            max_y = position[1]
        elif position[0] < min_x:
            direction = 'down'
            min_x = position[0]
        elif position[1] < min_y:
            direction = 'right'
            min_y = position[1]

        value = 0
        for x in product(range(-1, 2), range(-1, 2)):
            value += position_grid.get((position[0]+x[0], position[1]+x[1]), 0)
        position_grid[position] = value

        if value > puzzle_input:
            print(value)
            break


if __name__ == "__main__":
    main()
