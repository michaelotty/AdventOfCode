"""Advent of code Day 2 part 1 and 2"""

from enum import IntEnum, unique


@unique
class Opcode(IntEnum):
    """Opcodes"""
    ADD = 1
    MULTIPLY = 2
    END = 99


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        numbers = [int(i) for i in file.read().split(',')]

    numbers[1] = 12
    numbers[2] = 2

    i = 0
    while True:
        opcode, *address = numbers[i:i+4]
        if opcode == Opcode.ADD:
            numbers[address[2]] = numbers[address[0]] + numbers[address[1]]
        elif opcode == Opcode.MULTIPLY:
            numbers[address[2]] = numbers[address[0]] * numbers[address[1]]
        elif opcode == Opcode.END:
            print(f'Part 1: {numbers[0]}')
            break
        else:
            raise ValueError(f'Opcode: {opcode} not supported')
        i += 4


if __name__ == "__main__":
    main()
