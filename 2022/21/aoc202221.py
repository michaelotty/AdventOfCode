"""Advent of code Day 21."""

import re

from sympy.parsing import sympy_parser
import sympy

monkeys = {}


def main():
    """Main function."""
    global monkeys
    with open("aoc2022/21/input.txt", encoding="utf-8") as file:
        monkeys = dict(line.split(": ") for line in file.read().splitlines())
    print("Part 1:", part_1())
    print("Part 2:", part_2())


def part_1() -> int:
    """Solve part 1."""
    global monkeys

    return find_value("root")


def find_value(key: str):
    """Find the value of a monkey given by key."""
    global monkeys

    val = monkeys[key]
    try:
        return int(val)
    except ValueError:
        pass

    left, op, right = val.split()

    left = find_value(left)
    right = find_value(right)

    match op:
        case "+":
            return left + right
        case "-":
            return left - right
        case "*":
            return left * right
        case "/":
            return left // right


def part_2():
    """Solve part 2."""
    global monkeys

    left, _, right = monkeys["root"].split()
    monkeys["root"] = left + " - " + right

    algebra = find_path_to_humn()
    algebra.pop(0)

    last_expression = algebra.pop(0)

    for expression in algebra:
        word = re.findall(r"[a-z]+", expression)[0]
        last_expression = expression.replace(word, f"({last_expression})")

    last_expression = last_expression.replace("humn", "x")
    last_expression = sympy_parser.parse_expr(last_expression)
    last_expression = sympy.solve(last_expression)

    return last_expression[0]


def find_path_to_humn(key="root") -> list[str]:
    """Find the path to humn."""
    global monkeys

    if key == "humn":
        return ["humn"]

    val = monkeys[key]
    try:
        int(val)
        return None
    except ValueError:
        pass

    left, op, right = val.split()

    left_val = find_path_to_humn(left)
    right_val = find_path_to_humn(right)

    if left_val:
        left_val.append(f"{left} {op} {find_value(right)}")
        return left_val
    if right_val:
        right_val.append(f"{find_value(left)} {op} {right}")
        return right_val


if __name__ == "__main__":
    main()
