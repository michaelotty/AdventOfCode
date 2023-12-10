"""Advent of code day 9."""


def main() -> None:
    """Main function."""
    with open("2023/09/input.txt", encoding="utf-8") as file:
        histories = [
            [int(num) for num in line.split()] for line in file.read().splitlines()
        ]

    print("Part 1:", part_1(histories))
    print("Part 2:", part_2(histories))


def part_1(histories: list[list[int]]) -> int:
    """Solve part 1."""
    values = []

    for history in histories:
        analyse = [history]
        while not all(item == 0 for item in analyse[-1]):
            new_item = [
                right - left for left, right in zip(analyse[-1][:-1], analyse[-1][1:])
            ]
            analyse.append(new_item)

        values.append(sum(line[-1] for line in analyse))
    return sum(values)


def part_2(histories: list[list[int]]) -> int:
    """Solve part 2."""
    values = []

    for history in histories:
        analyse = [history]
        while not all(item == 0 for item in analyse[-1]):
            new_item = [
                right - left for left, right in zip(analyse[-1][:-1], analyse[-1][1:])
            ]
            analyse.append(new_item)

        analyse.reverse()
        past = [0]
        for row in analyse[1:]:
            past.append(row[0] - past[-1])

        values.append(past[-1])
    return sum(values)


if __name__ == "__main__":
    main()
