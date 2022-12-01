"""Advent of code Day 1."""


def main():
    """Main function."""
    with open("aoc2022/01/input.txt", encoding="utf-8") as file:
        numbers = [
            [int(num) for num in item.split()] for item in file.read().split("\n\n")
        ]
    print(numbers)
    print(f"Part 1: {part_1(numbers)}")
    print(f"Part 2: {part_2(numbers)}")


def part_1(numbers):
    """Solve part 1."""
    return max(sum(items) for items in numbers)


def part_2(numbers):
    """Solve part 1."""
    return sum(sorted(sum(items) for items in numbers)[-3:])


if __name__ == "__main__":
    main()
