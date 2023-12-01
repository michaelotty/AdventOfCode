"""Advent of code day 1."""

from string import ascii_lowercase


def main():
    """Main function."""

    with open("aoc2023/01/input.txt", encoding="utf-8") as file:
        data = file.read()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


def part_1(data):
    """Solve part 1."""
    trans_table = str.maketrans({letter: "" for letter in ascii_lowercase})
    return sum(int(x[0] + x[-1]) for x in data.translate(trans_table).split())


def part_2(data):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
