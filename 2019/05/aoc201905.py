"""Advent of code day 5 part 1 and 2, derived from day 2."""

from enum import IntEnum, unique
from typing import Callable


@unique
class Opcode(IntEnum):
    """Opcodes."""

    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JMP_IF_TRUE = 5
    JMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    END = 99


@unique
class ParameterMode(IntEnum):
    """Parameter modes."""

    POSITION = 0
    IMMEDIATE = 1


def main() -> None:
    """Program starts here."""
    with open("2019/05/input.txt", encoding="utf-8") as file:
        file_input = tuple(int(i) for i in file.read().split(","))

    print(f"Part 1: {solve_puzzle(file_input, 1)}")
    print(f"Part 2: {solve_puzzle(file_input, 5)}")


def solve_puzzle(file_input: tuple[int, ...], input_val: int) -> int | None:
    """Solve the puzzle with corrected input."""
    numbers = list(file_input)
    address = 0
    return_val = None
    opcode_fns: dict[int, Callable] = {
        Opcode.ADD: add_op,
        Opcode.MULTIPLY: multiply_op,
        Opcode.JMP_IF_TRUE: jmp_if_true_op,
        Opcode.JMP_IF_FALSE: jmp_if_false_op,
        Opcode.LESS_THAN: less_than_op,
        Opcode.EQUALS: equals_op,
    }

    while True:
        opcode_str = f"{numbers[address]:05d}"
        parameter_modes = [int(i) for i in opcode_str[2::-1]]
        opcode = int(opcode_str[-2:])
        address += 1

        if opcode == Opcode.END:
            return return_val

        if opcode == Opcode.INPUT:
            address, numbers = input_op(address, numbers, parameter_modes, input_val)
        elif opcode == Opcode.OUTPUT:
            address, numbers, return_val = output_op(address, numbers, parameter_modes)
        else:
            try:
                address, numbers = opcode_fns[opcode](address, numbers, parameter_modes)
            except KeyError:
                raise ValueError(f"Opcode: {opcode} not supported") from KeyError


def add_op(
    address: int, numbers: list[int], parameter_modes: list[int]
) -> tuple[int, list[int]]:
    """Add operator."""
    value = 0
    for parameter_mode in parameter_modes[:2]:
        if parameter_mode == ParameterMode.POSITION:
            value += numbers[numbers[address]]
        elif parameter_mode == ParameterMode.IMMEDIATE:
            value += numbers[address]
        address += 1

    numbers[numbers[address]] = value
    address += 1

    return address, numbers


def multiply_op(
    address: int, numbers: list[int], parameter_modes: list[int]
) -> tuple[int, list[int]]:
    """Multiply operator."""
    values = []
    for parameter_mode in parameter_modes[:2]:
        if parameter_mode == ParameterMode.POSITION:
            values.append(numbers[numbers[address]])
        elif parameter_mode == ParameterMode.IMMEDIATE:
            values.append(numbers[address])
        address += 1

    numbers[numbers[address]] = values[0] * values[1]
    address += 1
    return address, numbers


def input_op(
    address: int, numbers: list[int], parameter_modes: list[int], input_val: int
) -> tuple[int, list[int]]:
    """Input operator."""
    if parameter_modes[0] == ParameterMode.POSITION:
        numbers[numbers[address]] = input_val
    elif parameter_modes[0] == ParameterMode.IMMEDIATE:
        numbers[address] = input_val
    address += 1
    return address, numbers


def output_op(
    address: int, numbers: list[int], parameter_modes: list[int]
) -> tuple[int, list[int], int]:
    """Output operator."""
    if parameter_modes[0] == ParameterMode.POSITION:
        return_val = numbers[numbers[address]]
    elif parameter_modes[0] == ParameterMode.IMMEDIATE:
        return_val = numbers[address]
    address += 1
    return address, numbers, return_val


def jmp_if_true_op(
    address: int, numbers: list[int], parameter_modes: list[int]
) -> tuple[int, list[int]]:
    """Jump if true operator."""
    if parameter_modes[0] == ParameterMode.POSITION:
        value = bool(numbers[numbers[address]])
    elif parameter_modes[0] == ParameterMode.IMMEDIATE:
        value = bool(numbers[address])
    address += 1

    if value:
        if parameter_modes[1] == ParameterMode.POSITION:
            address = numbers[numbers[address]]
        elif parameter_modes[1] == ParameterMode.IMMEDIATE:
            address = numbers[address]
    else:
        address += 1
    return address, numbers


def jmp_if_false_op(
    address: int, numbers: list[int], parameter_modes: list[int]
) -> tuple[int, list[int]]:
    """Jump if false operator."""
    if parameter_modes[0] == ParameterMode.POSITION:
        value = bool(numbers[numbers[address]])
    elif parameter_modes[0] == ParameterMode.IMMEDIATE:
        value = bool(numbers[address])
    address += 1

    if not value:
        if parameter_modes[1] == ParameterMode.POSITION:
            address = numbers[numbers[address]]
        elif parameter_modes[1] == ParameterMode.IMMEDIATE:
            address = numbers[address]
    else:
        address += 1
    return address, numbers


def less_than_op(
    address: int, numbers: list[int], parameter_modes: list[int]
) -> tuple[int, list[int]]:
    """Less than operator."""
    values = []
    for parameter_mode in parameter_modes[:2]:
        if parameter_mode == ParameterMode.POSITION:
            values.append(numbers[numbers[address]])
        elif parameter_mode == ParameterMode.IMMEDIATE:
            values.append(numbers[address])
        address += 1

    numbers[numbers[address]] = int(values[0] < values[1])
    address += 1
    return address, numbers


def equals_op(
    address: int, numbers: list[int], parameter_modes: list[int]
) -> tuple[int, list[int]]:
    """Equals operator."""
    values = []
    for parameter_mode in parameter_modes[:2]:
        if parameter_mode == ParameterMode.POSITION:
            values.append(numbers[numbers[address]])
        elif parameter_mode == ParameterMode.IMMEDIATE:
            values.append(numbers[address])
        address += 1

    numbers[numbers[address]] = int(values[0] == values[1])
    address += 1
    return address, numbers


if __name__ == "__main__":
    main()
