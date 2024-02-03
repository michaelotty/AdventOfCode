"""Advent of code day 15."""


def main() -> None:
    """Program starts here."""
    with open("2023/15/input.txt", encoding="utf-8") as file:
        data = file.read().replace("\n", "").split(",")

    print("Part 1:", part_1(data))
    print("Part 2:", part_2())


def part_1(data: list[str]) -> int:
    """Solve part 1."""
    return sum(hash_algorithm(item) for item in data)


def hash_algorithm(string: str) -> int:
    """Return the HASH of a string."""
    output = 0
    for char in string:
        output += ord(char)
        output *= 17
        output %= 256

    return output


def part_2() -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
