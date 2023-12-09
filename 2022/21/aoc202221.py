"""Advent of code Day 21."""

import re

import sympy
from sympy.parsing import sympy_parser


def main():
    """Main function."""
    with open("2022/21/input.txt", encoding="utf-8") as file:
        monkeys = dict(line.split(": ") for line in file.read().splitlines())
    print("Part 1:", part_1(monkeys))
    print("Part 2:", part_2(monkeys))


def part_1(monkeys) -> int:
    """Solve part 1."""
    return find_value("root", monkeys)


def find_value(key: str, monkeys):
    """Find the value of a monkey given by key."""
    val = monkeys[key]
    try:
        return int(val)
    except ValueError:
        pass

    left, op, right = val.split()

    left = find_value(left, monkeys)
    right = find_value(right, monkeys)

    match op:
        case "+":
            return left + right
        case "-":
            return left - right
        case "*":
            return left * right
        case "/":
            return left // right


def part_2(monkeys):
    """Solve part 2."""
    left, _, right = monkeys["root"].split()
    monkeys["root"] = left + " - " + right

    algebra = find_path_to_humn(monkeys)
    algebra.pop(0)

    last_expression = algebra.pop(0)

    for expression in algebra:
        word = re.findall(r"[a-z]+", expression)[0]
        last_expression = expression.replace(word, f"({last_expression})")

    last_expression = last_expression.replace("humn", "x")
    last_expression = sympy_parser.parse_expr(last_expression)
    last_expression = sympy.solve(last_expression)

    return last_expression[0]


def find_path_to_humn(monkeys, key="root") -> list[str] | None:
    """Find the path to humn."""
    if key == "humn":
        return ["humn"]

    val = monkeys[key]
    try:
        int(val)
        return None
    except ValueError:
        pass

    left, op, right = val.split()

    left_val = find_path_to_humn(monkeys, left)
    right_val = find_path_to_humn(monkeys, right)

    if left_val:
        left_val.append(f"{left} {op} {find_value(monkeys, right)}")
        return left_val
    if right_val:
        right_val.append(f"{find_value(monkeys, left)} {op} {right}")
        return right_val
    return None


if __name__ == "__main__":
    main()
