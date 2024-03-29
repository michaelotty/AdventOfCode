"""Advent of code Day 11."""

import math
import operator
import re


def main() -> None:
    """Program starts here."""
    with open("2022/11/input.txt", encoding="utf-8") as file:
        monkey_text = file.read().split("\n\n")
    print("Part 1:", solve(monkey_text, 20, True))
    print("Part 2:", solve(monkey_text, 10000, False))


def create_monkeys(monkey_text: list[str]):
    """Create monkeys from the text input."""
    monkeys = []
    for monkey_text_line in monkey_text:
        monkey_text_block = monkey_text_line.splitlines()
        monkey: dict[str, int | list[int]] = {}
        monkey["items"] = [int(i) for i in re.findall(r"\d+", monkey_text_block[1])]
        monkey["operation"] = create_operation_fn(monkey_text_block[2])
        monkey["test"] = create_test_fn("\n".join(monkey_text_block[3:]))
        monkey["divisor"] = get_divisor(monkey_text_block[3])
        monkey["inspections"] = 0
        monkeys.append(monkey)
    return monkeys


def create_operation_fn(text: str):
    """Create a new function for the operation defined by the string."""
    op_char, num = re.findall(r"(\+|\*) (\d+|old)", text)[0]
    op_mapping = {"*": operator.mul, "+": operator.add}

    def operation(old):
        return op_mapping[op_char](old, num)

    if num != "old":
        num = int(num)

    return operation


def create_test_fn(text: str):
    """Create a test function based on string that returns the money to throw to."""
    nums = [
        int(i)
        for i in re.findall(
            r"divisible by (\d+).+true.+(\d+).+false.+(\d+)", text, re.DOTALL
        )[0]
    ]

    def operation(num):
        if not num % nums[0]:
            return nums[1]
        return nums[2]

    return operation


def get_divisor(text: str) -> int:
    """Get the divisor for the monkey test."""
    divisor = re.findall(r"divisible by (\d+)", text)[0]
    return int(divisor)


def run_rounds(monkeys: list, rounds: int, part_1: bool = True) -> list:
    """Run defined amount of rounds of monkey business.

    We are checking if the number is divisible, so we can prevent the number becoming
    huge by finding limiting the number to the total product of all the divisors.
    This is because `a mod b == (a mod xb) mod b`. `a` becomes really huge so instead
    we can store `a mod xb`.
    """
    modulo_val = math.prod(monkey["divisor"] for monkey in monkeys)

    for _ in range(rounds):
        for monkey in monkeys:
            while monkey["items"]:
                item = monkey["items"].pop(0)
                item = monkey["operation"](item)
                if part_1:
                    item = math.floor(item / 3.0)

                item %= modulo_val

                monkey["inspections"] += 1
                monkeys[monkey["test"](item)]["items"].append(item)

    return monkeys


def solve(monkey_text: list[str], rounds: int, part_1: bool):
    """Solve with arbitrary amount of rounds."""
    monkeys = create_monkeys(monkey_text)

    monkeys = run_rounds(monkeys, rounds, part_1)
    inspection_ranking = sorted(monkey["inspections"] for monkey in monkeys)
    monkey_business = inspection_ranking[-2] * inspection_ranking[-1]
    return monkey_business


if __name__ == "__main__":
    main()
