"""Advent of code Day 3 part 2."""

from typing import Literal


def move_location(
    location: tuple[int, int], char: Literal["^", ">", "v", "<"] | str
) -> tuple[int, int]:
    """Move the location tuple using instruction from the char."""
    if char == "^":
        return (location[0], location[1] + 1)
    if char == ">":
        return (location[0] + 1, location[1])
    if char == "v":
        return (location[0], location[1] - 1)
    if char == "<":
        return (location[0] - 1, location[1])
    return location


def main() -> None:
    """Program starts here."""
    with open("2015/03/input.txt", encoding="utf-8") as f:
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
