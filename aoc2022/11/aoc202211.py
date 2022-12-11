"""Advent of code Day 11."""

import math
import operator
import re


def main():
    """Main function."""
    with open("aoc2022/11/input.txt", encoding="utf-8") as file:
        monkey_text = file.read().split("\n\n")
    monkeys = create_monkeys(monkey_text)
    print("Part 1:", part_1(monkeys))
    print("Part 2:", part_2())


def create_monkeys(monkey_text: list[str]):
    """Create monkeys from the text input."""
    monkeys = []
    for monkey_text_block in monkey_text:
        monkey_text_block = monkey_text_block.splitlines()
        monkey = {}
        monkey["items"] = [int(i) for i in re.findall(r"\d+", monkey_text_block[1])]
        monkey["operation"] = create_operation_fn(monkey_text_block[2])
        monkey["test"] = create_test_fn("\n".join(monkey_text_block[3:]))
        monkey["inspections"] = 0
        monkeys.append(monkey)
    return monkeys


def create_operation_fn(text: str):
    """Create a new function for the operation defined by the string."""
    op_char, num = re.findall(r"(\+|\*) (\d+|old)", text)[0]
    op_mapping = {"*": operator.mul, "+": operator.add}
    if num == "old":

        def operation(old):
            return op_mapping[op_char](old, old)

        return operation
    else:
        num = int(num)

        def operation(old):
            return op_mapping[op_char](old, num)

        return operation
    raise RuntimeError("No operators detected in string!")


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
        else:
            return nums[2]

    return operation


def run_rounds(monkeys, rounds):
    """Run defined amount of rounds of monkey business."""
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey["items"]:
                item = monkey["items"].pop(0)
                item = monkey["operation"](item)
                item = math.floor(item / 3.0)
                monkey["inspections"] += 1
                monkeys[monkey["test"](item)]["items"].append(item)

    return monkeys


def part_1(monkeys: list[dict]):
    """Solve part 1."""
    monkeys = run_rounds(monkeys, 20)
    inspection_ranking = sorted(monkey["inspections"] for monkey in monkeys)
    monkey_business = inspection_ranking[-2] * inspection_ranking[-1]
    return monkey_business


def part_2():
    """Solve part 2."""
    return 0


if __name__ == "__main__":
    main()
