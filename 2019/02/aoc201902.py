"""Advent of code Day 2 part 1 and 2"""

from enum import IntEnum, unique


@unique
class Opcode(IntEnum):
    """Opcodes"""

    ADD = 1
    MULTIPLY = 2
    END = 99


def init_puzzle_input(file_input: tuple[int], noun: int, verb: int) -> list[int]:
    """Inits the puzzle input"""
    numbers = list(file_input)
    numbers[1] = noun
    numbers[2] = verb
    return numbers


def solve_puzzle(file_input: tuple[int], noun: int, verb: int) -> int:
    """Solve the puzzle with corrected input"""
    numbers = init_puzzle_input(file_input=file_input, noun=noun, verb=verb)
    i = 0
    while True:
        opcode, *parameters = numbers[i : i + 4]
        if opcode == Opcode.ADD:
            numbers[parameters[2]] = numbers[parameters[0]] + numbers[parameters[1]]
        elif opcode == Opcode.MULTIPLY:
            numbers[parameters[2]] = numbers[parameters[0]] * numbers[parameters[1]]
        elif opcode == Opcode.END:
            return numbers[0]
        else:
            raise ValueError(f"Opcode: {opcode} not supported")
        i += 4


def main():
    """Main function"""
    with open("2019/02/input.txt", encoding="utf-8") as file:
        file_input = tuple(int(i) for i in file.read().split(","))

    print(f"Part 1: {solve_puzzle(file_input, 12, 2)}")

    noun = 0
    while True:
        for verb in range(noun + 1):
            if solve_puzzle(file_input, noun, verb) == 19690720:
                print(f"Part 2: {100 * noun + verb}")
                return
        noun += 1


if __name__ == "__main__":
    main()
