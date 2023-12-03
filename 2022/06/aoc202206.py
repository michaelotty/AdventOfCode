"""Advent of code Day 6."""


def main():
    """Main function."""
    with open("aoc2022/06/input.txt", encoding="utf-8") as file:
        packet = file.read()

    print("Part 1:", solve(packet, 4))
    print("Part 2:", solve(packet, 14))


def solve(packet: str, length: int):
    """Solve for any given distict character length."""
    uniques = [
        len(set(zip(packet[i + j : length + i + j])))
        for i in range(length)
        for j in range(len(packet) - length)
    ]

    return uniques.index(length) + length


if __name__ == "__main__":
    main()
