"""Advent of code day 6."""


def main() -> None:
    """Program starts here."""
    with open("2023/06/input.txt", encoding="utf-8") as file:
        text = file.read()

    first_line, second_line = text.splitlines()

    _, *time_strs = first_line.split()
    _, *distance_strs = second_line.split()

    times = [int(x) for x in time_strs]
    distances = [int(x) for x in distance_strs]

    print("Part 1:", part_1(times, distances))
    print("Part 2:", part_2())


def part_1(times: list[int], distances: list[int]) -> int:
    """Solve part 1."""
    print(times)
    print(distances)
    return 0


def part_2() -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
