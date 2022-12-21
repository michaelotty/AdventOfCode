"""Advent of code Day 21."""


def main():
    """Main function."""
    with open("aoc2022/21/input.txt", encoding="utf-8") as file:
        monkeys = dict(line.split(": ") for line in file.read().splitlines())
    print("Part 1:", part_1(monkeys))
    print("Part 2:", part_2())


def part_1(monkeys: dict[str, str]) -> int:
    """Solve part 1."""
    return find_value("root", monkeys)


def find_value(key: str, monkeys: dict[str, str]):
    """Find the value of a monkey given by key."""
    val = monkeys[key]
    try:
        return int(val)
    except ValueError:
        pass

    left, op, right = val.split()

    match op:
        case "+":
            return find_value(left, monkeys) + find_value(right, monkeys)
        case "-":
            return find_value(left, monkeys) - find_value(right, monkeys)
        case "*":
            return find_value(left, monkeys) * find_value(right, monkeys)
        case "/":
            return find_value(left, monkeys) // find_value(right, monkeys)


def part_2():
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
