"""Advent of code Day 6 part 2."""


def main(part2: bool) -> None:
    """Program starts here."""
    with open("2015/06/input.txt", encoding="utf-8") as f:
        file_contents = f.read()

    if part2:
        actions = {
            "on": turn_on_lights2,
            "off": turn_off_lights2,
            "toggle": toggle_lights2,
        }
    else:
        actions = {
            "on": turn_on_lights1,
            "off": turn_off_lights1,
            "toggle": toggle_lights1,
        }

    grid_width = 1000
    grid_height = grid_width

    if part2:
        lights = [[0 for i in range(grid_height)] for j in range(grid_width)]
    else:
        lights = [[False for i in range(grid_height)] for j in range(grid_width)]

    for line in file_contents.split("\n"):
        # Simplify command
        command = line.split(" ")
        command.remove("through")
        if len(command) == 4:
            command.remove("turn")

        # Convert coords to int tuples
        command_a = tuple(int(i) for i in command[1].split(","))
        command_b = tuple(int(i) for i in command[2].split(","))
        lights = actions[command[0]](command_a, command_b, lights)

    print(sum(sum(line) for line in lights))


def turn_on_lights1(start_pos: tuple, end_pos: tuple, lights: list) -> list:
    """Turn on lights in range."""
    for i in range(start_pos[0], end_pos[0] + 1):
        for j in range(start_pos[1], end_pos[1] + 1):
            lights[i][j] = True
    return lights


def turn_off_lights1(start_pos: tuple, end_pos: tuple, lights: list) -> list:
    """Turn off lights in range."""
    for i in range(start_pos[0], end_pos[0] + 1):
        for j in range(start_pos[1], end_pos[1] + 1):
            lights[i][j] = False
    return lights


def toggle_lights1(start_pos: tuple, end_pos: tuple, lights: list) -> list:
    """Toggle all lights in range."""
    for i in range(start_pos[0], end_pos[0] + 1):
        for j in range(start_pos[1], end_pos[1] + 1):
            lights[i][j] ^= True
    return lights


def turn_on_lights2(start_pos: tuple, end_pos: tuple, lights: list) -> list:
    """Turn on lights in range."""
    for i in range(start_pos[0], end_pos[0] + 1):
        for j in range(start_pos[1], end_pos[1] + 1):
            lights[i][j] += 1
    return lights


def turn_off_lights2(start_pos: tuple, end_pos: tuple, lights: list) -> list:
    """Turn off lights in range."""
    for i in range(start_pos[0], end_pos[0] + 1):
        for j in range(start_pos[1], end_pos[1] + 1):
            if lights[i][j] > 0:
                lights[i][j] -= 1
    return lights


def toggle_lights2(start_pos: tuple, end_pos: tuple, lights: list) -> list:
    """Toggle all lights in range."""
    for i in range(start_pos[0], end_pos[0] + 1):
        for j in range(start_pos[1], end_pos[1] + 1):
            lights[i][j] += 2
    return lights


if __name__ == "__main__":
    main(part2=False)
    main(part2=True)
