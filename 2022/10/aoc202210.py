"""Advent of code Day 10."""


def main():
    """Main function."""
    with open("2022/10/input.txt", encoding="utf-8") as file:
        instructions = file.read().splitlines()
    part_1_solution, x_register = part_1(instructions)
    print("Part 1:", part_1_solution)
    print("Part 2:", part_2(x_register), sep="\n")


def part_1(instructions: list[str]):
    """Solve part 1."""
    ops = {"noop": noop, "addx": addx}
    x_register = [1]
    for instruction in instructions:
        op, *amount = instruction.split()
        if amount:
            amount = int(amount[0])
        else:
            amount = 0
        x_register = ops[op](x_register, amount)

    indexes = list(range(20, 220 + 1, 40))
    signal_strength = sum(i * x_register[i - 1] for i in indexes)
    return signal_strength, x_register


def noop(x_register: list[int], value: int):
    """Execute the no op operation."""
    x_register.append(x_register[-1])
    return x_register


def addx(x_register: list[int], value: int):
    """Execute the add X operation."""
    x_register.append(x_register[-1])
    x_register.append(x_register[-1] + value)
    return x_register


def part_2(x_register: list[int]):
    """Solve part 2."""
    x_register_rows = [x_register[i : i + 40] for i in range(0, len(x_register), 40)]
    crt_rows = []
    for x_register_row in x_register_rows:
        crt_row = []
        for pixel_idx, sprite_pos in enumerate(x_register_row):
            if pixel_idx in [sprite_pos - 1, sprite_pos, sprite_pos + 1]:
                crt_row.append("#")
            else:
                crt_row.append(" ")
        crt_row = "".join(crt_row)
        crt_rows.append(crt_row)
    crt_rows = "\n".join(crt_rows)

    return crt_rows


if __name__ == "__main__":
    main()
