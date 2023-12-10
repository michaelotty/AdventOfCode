"""Advent of code Day 19 part 1"""

import re


def main() -> None:
    """Main function"""
    with open("2015/19/input.txt", encoding="utf-8") as file:
        file_contents = file.read()

    data, formula = file_contents.split("\n\n")
    replacements = [tuple(re.split(r" => ", line)) for line in data.split("\n")]

    distinct_molecules = set()

    for replacement in replacements:
        for i in range(len(formula)):
            left_formula, right_formula = formula[:i], formula[i:]
            molecule = left_formula + right_formula.replace(
                replacement[0], replacement[1], 1
            )
            distinct_molecules.add(molecule)
    distinct_molecules.remove(formula)

    print(len(distinct_molecules))


if __name__ == "__main__":
    main()
