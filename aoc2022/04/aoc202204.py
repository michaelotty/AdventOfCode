"""Advent of code Day 4."""


def main():
    """Main function."""
    with open("aoc2022/04/input.txt", encoding="utf-8") as file:
        expressions = [
            [tuple(int(num) for num in nums.split("-")) for nums in line.split(",")]
            for line in file.read().split()
        ]
    print(f"Part 1: {part_1(expressions)}")
    print(f"Part 2: {part_2(expressions)}")


def part_1(expressions):
    """Solve part 1."""
    count = 0
    for expr1, expr2 in expressions:
        left_range = set(range(expr1[0], expr1[1] + 1))
        right_range = set(range(expr2[0], expr2[1] + 1))
        if len(left_range & right_range) in (len(left_range), len(right_range)):
            count += 1

    return count


def part_2(expressions):
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
