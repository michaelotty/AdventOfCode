"""Advent of code day 2."""


def main() -> None:
    """Program starts here."""
    with open("2024/02/test.txt", encoding="utf-8") as file:
        data = [[int(x) for x in line.split()] for line in file]

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


def part_1(data) -> int:
    """Solve part 1."""
    return sum(all_increasing(line) or all_decreasing(line) for line in data)


def all_increasing(line) -> bool:
    """Check all numbers increase."""
    return all(1 <= (y - x) <= 3 for x, y in zip(line[:-1], line[1:]))


def all_decreasing(line) -> bool:
    """Check all numbers decrease."""
    return all(-3 <= (y - x) <= -1 for x, y in zip(line[:-1], line[1:]))


def part_2(data) -> int:
    """Solve part 2."""
    count = 0
    for line in data:
        if all_increasing(line) or all_decreasing(line):
            count += 1
        else:
            for i in range(len(line)):
                new_line = [*line[:i], *line[i + 1 :]]
                if all_increasing(new_line) or all_decreasing(new_line):
                    count += 1
                    break

    return count


if __name__ == "__main__":
    main()
