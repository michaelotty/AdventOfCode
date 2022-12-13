"""Advent of code Day 13."""


def main():
    """Main function."""
    with open("aoc2022/13/input.txt", encoding="utf-8") as file:
        packet_pairs = [pair.split() for pair in file.read().split("\n\n")]

    print(packet_pairs)
    print("Part 1:", part_1(packet_pairs))
    print("Part 2:", part_2(packet_pairs))


def part_1(packet_pairs):
    """Solve part 1."""
    return 0


def part_2(packet_pairs):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
