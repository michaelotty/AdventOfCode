"""Advent of code day 1."""


def main() -> None:
    """Program starts here."""
    with open("2024/01/input.txt", encoding="utf-8") as file:
        data = [tuple(map(int, x.split())) for x in file.read().splitlines()]

    print("Part 1:", part_1(data))
    print("Part 2:", part_2())


def part_1(data) -> int:
    """Solve part 1."""
    data = list(zip(*data))
    x = sorted(data[0])
    y = sorted(data[1])
    sums = []
    for i, j in zip(x, y):
        sums.append(abs(i - j))
    return sum(sums)


def part_2() -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
