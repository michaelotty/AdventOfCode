"""Advent of code day 4."""


def main() -> None:
    """Program starts here."""
    with open("2024/04/input.txt", encoding="utf-8") as file:
        data = [list(line) for line in file.read().splitlines()]

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


def part_1(data) -> int:
    """Solve part 1."""
    count = 0

    for i in range(len(data[0])):
        for j in range(len(data)):
            count += count_words(data, i, j)
    return count


def count_words(data, i, j):
    """Count the number of words starting from this location."""
    WORD = "XMAS"
    directions = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )
    count = 0
    for direction in directions:
        matches = 0
        for k, letter in enumerate(WORD):
            coord_i, coord_j = i + k * direction[0], j + k * direction[1]
            if not (0 <= coord_i < len(data[0]) and 0 <= coord_j < len(data)):
                # Out of bounds
                break

            if letter == data[coord_i][coord_j]:
                matches += 1

        if matches == len(WORD):
            count += 1

    return count


def part_2(data) -> int:
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
