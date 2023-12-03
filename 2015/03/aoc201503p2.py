"""Advent of code Day 3 part 2"""


def move_location(location, char):
    """Move the location stored in the tuple depending on the instruction from the char"""
    if char == '^':
        location = (location[0], location[1]+1)
    elif char == '>':
        location = (location[0]+1, location[1])
    elif char == 'v':
        location = (location[0], location[1]-1)
    elif char == '<':
        location = (location[0]-1, location[1])

    return location


def main():
    """Main function"""
    with open('input.txt') as f:
        file_contents = f.read()

    santa_location = (0, 0)
    robot_location = (0, 0)

    visited_locations = set()
    visited_locations.add(santa_location)
    visited_locations.add(robot_location)

    select_santa = True

    for char in file_contents:
        if select_santa:
            select_santa = False
            santa_location = move_location(santa_location, char)
            visited_locations.add(santa_location)
        else:
            select_santa = True
            robot_location = move_location(robot_location, char)
            visited_locations.add(robot_location)

    print(len(visited_locations))


if __name__ == "__main__":
    main()
