"""Advent of code Day 3 part 1"""


def main():
    """Main function"""
    with open("2015/03/input.txt", encoding="utf-8") as f:
        file_contents = f.read()

    location = (0, 0)
    visited_locations = set()
    visited_locations.add(location)

    for char in file_contents:
        if char == "^":
            location = (location[0], location[1] + 1)
        elif char == ">":
            location = (location[0] + 1, location[1])
        elif char == "v":
            location = (location[0], location[1] - 1)
        elif char == "<":
            location = (location[0] - 1, location[1])
        visited_locations.add(location)

    print(len(visited_locations))


if __name__ == "__main__":
    main()
