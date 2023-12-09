"""Advent of code Day 23"""

import re
from typing import Callable


def main() -> None:
    """Main function"""
    with open("2015/23/input.txt", encoding="utf-8") as file:
        lines = file.read().splitlines()

    print(f"Part 1: {run_computer(0, lines)}")
    print(f"Part 2: {run_computer(1, lines)}")


def run_computer(input_val: int, instructions: list[str]) -> int:
    """Runs the computer"""
    instruction_fn: dict[str, Callable] = {
        "hlf": hlf,
        "tpl": tpl,
        "inc": inc,
        "jmp": jmp,
        "jie": jie,
        "jio": jio,
    }
    registers = {"a": input_val, "b": 0}

    address = 0

    while True:
        instruction, *parameters = re.split(r"[ ,]+", instructions[address])
        address_offset, registers = instruction_fn[instruction](registers, *parameters)
        address += address_offset
        if not 0 <= address < len(instructions):
            return registers["b"]


def hlf(registers: dict, register: str) -> tuple[int, int]:
    """Half"""
    address_offset = 1
    registers[register] //= 2
    return address_offset, registers


def tpl(registers: dict, register: str) -> tuple[int, dict]:
    """Triple"""
    address_offset = 1
    registers[register] *= 3
    return address_offset, registers


def inc(registers: dict, register: str) -> tuple[int, dict]:
    """Increment"""
    address_offset = 1
    registers[register] += 1
    return address_offset, registers


def jmp(registers: dict, offset: str) -> tuple[int, dict]:
    """Jump"""
    address_offset = int(offset)
    return address_offset, registers


def jie(registers: dict, register: str, offset: str) -> tuple[int, dict]:
    """Jump if even"""
    if registers[register] % 2 == 0:
        address_offset = int(offset)
    else:
        address_offset = 1
    return address_offset, registers


def jio(registers: dict, register: str, offset: str) -> tuple[int, dict]:
    """Jump if one"""
    if registers[register] == 1:
        address_offset = int(offset)
    else:
        address_offset = 1
    return address_offset, registers


if __name__ == "__main__":
    main()
