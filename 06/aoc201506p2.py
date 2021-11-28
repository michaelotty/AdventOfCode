"""Advent of code Day 6 part 2"""


def main():
    """Main function"""
    with open('input.txt') as f:
        file_contents = f.read()

    actions = {'on': turn_on_lights,
               'off': turn_off_lights,
               'toggle': toggle_lights}

    grid_width = 1000
    grid_height = grid_width

    lights = [[0 for i in range(grid_height)] for j in range(grid_width)]

    for line in file_contents.split('\n'):
        # Simplify command
        command = line.split(' ')
        command.remove('through')
        if len(command) == 4:
            command.remove('turn')

        # Convert coords to int tuples
        command[1] = tuple(int(i) for i in command[1].split(','))
        command[2] = tuple(int(i) for i in command[2].split(','))
        lights = actions[command[0]](command[1], command[2], lights)

    print(sum([sum(line) for line in lights]))


def turn_on_lights(start_pos: tuple, end_pos: tuple, lights: list) -> list:
    """Turns on lights in range"""
    for i in range(start_pos[0], end_pos[0]+1):
        for j in range(start_pos[1], end_pos[1]+1):
            lights[i][j] += 1
    return lights


def turn_off_lights(start_pos: tuple, end_pos: tuple, lights: list) -> list:
    """Turns off lights in range"""
    for i in range(start_pos[0], end_pos[0]+1):
        for j in range(start_pos[1], end_pos[1]+1):
            if lights[i][j] > 0:
                lights[i][j] -= 1
    return lights


def toggle_lights(start_pos: tuple, end_pos: tuple, lights: list) -> list:
    """Toggles all lights in range"""
    for i in range(start_pos[0], end_pos[0]+1):
        for j in range(start_pos[1], end_pos[1]+1):
            lights[i][j] += 2
    return lights


if __name__ == "__main__":
    main()
