"""Advent of code day 5 part 1 and 2, derived from day 2"""

from enum import IntEnum, unique


@unique
class Opcode(IntEnum):
    """Opcodes"""
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    END = 99


@unique
class ParameterMode(IntEnum):
    """Parameter modes"""
    POSITION = 0
    IMMEDIATE = 1


def solve_puzzle(file_input: tuple[int], input_val: int) -> int:
    """Solve the puzzle with corrected input"""
    numbers = list(file_input)
    address = 0
    return_val = None

    while True:
        opcode = f'{numbers[address]:05d}'
        parameter_modes = [int(i) for i in opcode[2::-1]]
        opcode = int(opcode[-2:])
        address += 1

        if opcode == Opcode.ADD:
            value = 0
            for parameter_mode in parameter_modes[:2]:
                if parameter_mode == ParameterMode.POSITION:
                    value += numbers[numbers[address]]
                elif parameter_mode == ParameterMode.IMMEDIATE:
                    value += numbers[address]
                address += 1

            numbers[numbers[address]] = value
            address += 1

        elif opcode == Opcode.MULTIPLY:
            values = []
            for parameter_mode in parameter_modes[:2]:
                if parameter_mode == ParameterMode.POSITION:
                    values.append(numbers[numbers[address]])
                elif parameter_mode == ParameterMode.IMMEDIATE:
                    values.append(numbers[address])
                address += 1

            numbers[numbers[address]] = values[0] * values[1]
            address += 1

        elif opcode == Opcode.END:
            return return_val

        elif opcode == Opcode.INPUT:
            if parameter_modes[0] == ParameterMode.POSITION:
                numbers[numbers[address]] = input_val
            elif parameter_modes[0] == ParameterMode.IMMEDIATE:
                numbers[address] = input_val
            address += 1

        elif opcode == Opcode.OUTPUT:
            if parameter_modes[0] == ParameterMode.POSITION:
                value = numbers[numbers[address]]
            elif parameter_modes[0] == ParameterMode.IMMEDIATE:
                value = numbers[address]

            if value != 0:
                return_val = value
            address += 1

        else:
            raise ValueError(f'Opcode: {opcode} not supported')


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        file_input = tuple(int(i) for i in file.read().split(','))

    print(f'Part 1: {solve_puzzle(file_input, 1)}')


if __name__ == "__main__":
    main()
