"""Advent of code Day 23."""


def main():
    """Main function."""
    with open("aoc2022/23/test1.txt", encoding="utf-8") as file:
        grid = [
            [1 if char == "#" else 0 for char in line]
            for line in file.read().splitlines()
        ]
    print("Part 1:", part_1(grid), sep="\n")
    print("Part 2:", part_2(grid))


def part_1(grid):
    """Solve part 1."""
    return "\n".join(str(line) for line in grid)


def part_2(grid):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
