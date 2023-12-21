"""Advent of code Day 19 part 2."""

import re
from random import shuffle
from typing import Generator


def gen_sequence(x, replacements: list) -> Generator[str, None, None]:
    """Ngl, stole this from reddit."""
    for j, i in replacements:
        for k in range(len(x)):
            if x[k : k + len(i)] == i:
                y = x[:k] + j + x[k + len(i) :]
                yield y


def main() -> None:
    """Program starts here."""
    with open("2015/19/input.txt", encoding="utf-8") as file:
        lines = file.read().splitlines()

    replacements = []
    for i in lines[:-2]:
        molecule = re.findall(r"(\S+) => (\S+)", i)
        replacements.append(molecule[0])
    medicine_molecule = lines[-1]
    while True:
        shuffle(replacements)

        visited = {medicine_molecule}
        molecule = [medicine_molecule]

        count = 0
        while True:
            made_molecule = []
            for i in molecule:
                for j in gen_sequence(i, replacements):
                    if j in visited:
                        continue
                    made_molecule.append(j)
                    visited.add(j)
                    break
            molecule = made_molecule
            count += 1
            if molecule or made_molecule:
                reduced_len = min(map(len, molecule))
            else:
                break
        if reduced_len == 1:
            print(count)
            break


if __name__ == "__main__":
    main()
