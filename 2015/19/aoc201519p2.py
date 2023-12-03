"""Advent of code Day 19 part 2"""

import re
from random import shuffle


def gen_sequence(X, replacements):
    """Ngl, stole this from reddit"""
    for j, i in replacements:
        for k in range(len(X)):
            if X[k:k+len(i)] == i:
                y = X[:k] + j + X[k+len(i):]
                yield y


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        lines = file.read().splitlines()

    replacements = []
    for i in lines[:-2]:
        molecule = re.findall(r'(\S+) => (\S+)', i)
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
