"""Advent of code day 10."""


def main() -> None:
    """Program starts here."""
    with open("2023/10/input.txt", encoding="utf-8") as file:
        data = file.read()

    data = data.replace("|", "\u2502")
    data = data.replace("-", "\u2500")
    data = data.replace("L", "\u2514")
    data = data.replace("J", "\u2518")
    data = data.replace("7", "\u2510")
    data = data.replace("F", "\u250C")
    data = data.replace(".", " ")

    print(data)

    print("Part 1:", part_1())
    print("Part 2:", part_2())


def part_1() -> int:
    """Solve part 1."""
    return 0


def part_2() -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
