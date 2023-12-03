"""Advent of code Day 13 part 2"""

from itertools import permutations


def main():
    """Main function"""
    with open("2015/13/input_part_2.txt", encoding="utf-8") as file:
        data = file.readlines()

    operations = {"gain": 1, "lose": -1}
    names = {}

    for i in data:
        first, _, operator, num, _, _, _, _, _, _, last = i.split()
        first = first[0]
        last = last[0]
        names.setdefault(first, {})[last] = operations[operator] * int(num)

    perms = set(i for i in permutations(names, len(names)))

    best_happiness = 0
    for arrangement in perms:
        happiness = 0
        for i, arr in enumerate(arrangement):
            happiness += names[arr][arrangement[i - 1]]
            happiness += names[arrangement[i - 1]][arr]
        if happiness > best_happiness:
            best_happiness = happiness
            best_combination = arrangement

    print(best_combination)
    print(best_happiness)


if __name__ == "__main__":
    main()
