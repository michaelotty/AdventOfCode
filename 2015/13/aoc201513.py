"""Advent of code Day 13"""

from itertools import permutations
from pathlib import Path


def solve(path: Path) -> int:
    """Solve single part of day 13."""
    with open(path, encoding="utf-8") as file:
        data = file.readlines()
    operations = {"gain": 1, "lose": -1}
    names: dict[str, dict[str, int]] = {}

    for line in data:
        first, _, operator, num, *_, last = line.split()
        first = first[0]
        last = last[0]
        names.setdefault(first, {})[last] = operations[operator] * int(num)

    best_happiness = 0
    for arrangement in set(permutations(names, len(names))):
        happiness = 0
        for i, arr in enumerate(arrangement):
            happiness += names[arr][arrangement[i - 1]]
            happiness += names[arrangement[i - 1]][arr]
        if happiness > best_happiness:
            best_happiness = happiness

    return best_happiness


if __name__ == "__main__":
    base_path = Path("2015/13")
    print("Part 1:", solve(base_path / "input.txt"))
    print("Part 2:", solve(base_path / "input_part_2.txt"))
