"""Advent of code Day 15 part 1"""

import re
from itertools import combinations_with_replacement


def main():
    """Main function"""
    with open('input.txt') as file:
        data = file.readlines()

    ingredients = []
    best_score = 0

    for line in data:
        numbers = re.findall(r'[+-]?\d', line)
        numbers = tuple(int(i) for i in numbers)
        props = numbers[0:-1]
        ingredient = (props, numbers[-1])
        ingredients.append(ingredient)

    for comb in combinations_with_replacement(ingredients, 100):
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0

        for ingredient in comb:
            capacity += ingredient[0][0]
            durability += ingredient[0][1]
            flavor += ingredient[0][2]
            texture += ingredient[0][3]

        if capacity < 0:
            capacity = 0
        if durability < 0:
            durability = 0
        if flavor < 0:
            flavor = 0
        if texture < 0:
            texture = 0

        score = capacity * durability * flavor * texture
        if score > best_score:
            best_score = score

    print(best_score)


if __name__ == "__main__":
    main()
