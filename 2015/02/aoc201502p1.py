"""Advent of code Day 2 part 1"""


def area_of_cuboid(length: int, width: int, height: int) -> tuple[int, int]:
    """Finds the surface area of a cuboid

    Also finds the size of the smallest side"""
    side_1 = length * width
    side_2 = length * height
    side_3 = height * width
    area = 2 * side_1 + 2 * side_2 + 2 * side_3
    smallest_side = min(side_1, side_2, side_3)
    return (area, smallest_side)


def main() -> None:
    """Main function"""
    with open("2015/02/input.txt", encoding="utf-8") as f:
        file_contents = f.read()

    data = file_contents.split()

    amount_of_wrapping_paper = 0

    for line in data:
        length, width, height = tuple(int(i) for i in line.split("x"))
        area, smallest_side = area_of_cuboid(length, width, height)
        amount_of_wrapping_paper += area + smallest_side

    print(amount_of_wrapping_paper)


if __name__ == "__main__":
    main()
