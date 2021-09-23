"""Advent of code Day 6 part 1"""


def turn_on_lights(start_pos: tuple, end_pos: tuple) -> None:
    print(f'Turning on {start_pos} through {end_pos}')


def turn_off_lights(start_pos: tuple, end_pos: tuple) -> None:
    print(f'Turning off {start_pos} through {end_pos}')


def toggle_lights(start_pos: tuple, end_pos: tuple) -> None:
    print(f'Toggling {start_pos} through {end_pos}')


def main():
    """Main function"""
    with open('input.txt') as f:
        file_contents = f.read()

    actions = {'on': turn_on_lights,
               'off': turn_off_lights, 'toggle': toggle_lights}

    for line in file_contents.split('\n'):
        # Simplify command
        command = line.split(' ')
        command.remove('through')
        if len(command) == 4:
            command.remove('turn')

        # Convert coords to int tuples
        command[1] = tuple(int(i) for i in command[1].split(','))
        command[2] = tuple(int(i) for i in command[2].split(','))
        actions[command[0]](command[1], command[2])


if __name__ == "__main__":
    main()
