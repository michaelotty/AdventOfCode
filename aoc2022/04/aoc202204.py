"""Advent of code Day 4."""


def main():
    """Main function."""
    with open("aoc2022/04/input.txt", encoding="utf-8") as file:
        expressions = [
            [tuple(int(num) for num in nums.split("-")) for nums in line.split(",")]
            for line in file.read().split()
        ]
    expressions = [
        (set(range(num1[0], num1[1] + 1)), set(range(num2[0], num2[1] + 1)))
        for num1, num2 in expressions
    ]

    print(f"Part 1: {part_1(expressions)}")
    print(f"Part 2: {part_2(expressions)}")


def part_1(expressions):
    """Solve part 1."""
    return sum(
        1
        for expr1, expr2 in expressions
        if len(expr1 & expr2) in (len(expr1), len(expr2))
    )


def part_2(expressions):
    """Solve part 2."""
    return sum(1 for expr1, expr2 in expressions if len(expr1 & expr2))


if __name__ == "__main__":
    main()
