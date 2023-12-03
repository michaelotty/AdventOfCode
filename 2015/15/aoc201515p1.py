"""Advent of code Day 15 part 1"""

import re
from itertools import combinations_with_replacement


def main():
    """Main function"""
    with open("2015/15/input.txt", encoding="utf-8") as file:
        data = file.readlines()

    ingredients = []
    best_score = 0

    for line in data:
        numbers = re.findall(r"[+-]?\d", line)
        ingredients.append(tuple(int(i) for i in numbers))

    for comb in combinations_with_replacement(ingredients, 100):
        capacity = 0
        durability = 0
        flavour = 0
        texture = 0

        for ingredient in comb:
            capacity += ingredient[0]
            durability += ingredient[1]
            flavour += ingredient[2]
            texture += ingredient[3]

        capacity = max(capacity, 0)
        durability = max(durability, 0)
        flavour = max(flavour, 0)
        texture = max(texture, 0)

        score = capacity * durability * flavour * texture
        if score > best_score:
            best_score = score

    print(best_score)


if __name__ == "__main__":
    main()
