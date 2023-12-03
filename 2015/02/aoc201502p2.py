"""Advent of code Day 2 part 2"""


def volume_of_cuboid(length, width, height):
    """Finds the volume of a cuboid"""
    return length * width * height


def find_shortest_perimeter(length, width, height):
    """Finds the shortest perimeter for a bow for a cuboid"""
    dimensions = [length, width, height]
    dimensions.sort()
    dimensions.pop()
    return 2 * dimensions[0] + 2 * dimensions[1]


def main():
    """Main function"""
    with open("input.txt", encoding="utf-8") as f:
        file_contents = f.read()

    file_contents = file_contents.split()

    length_of_ribbon = 0

    for line in file_contents:
        length, width, height = tuple(int(i) for i in line.split("x"))
        length_of_ribbon += find_shortest_perimeter(
            length, width, height
        ) + volume_of_cuboid(length, width, height)

    print(length_of_ribbon)


if __name__ == "__main__":
    main()
