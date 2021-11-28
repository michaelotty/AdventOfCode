"""Advent of code Day 15 part 2"""

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
        ingredients.append(tuple(int(i) for i in numbers))

    for comb in combinations_with_replacement(ingredients, 100):
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0

        for ingredient in comb:
            capacity += ingredient[0]
            durability += ingredient[1]
            flavor += ingredient[2]
            texture += ingredient[3]
            calories += ingredient[4]

        if capacity < 0:
            capacity = 0
        if durability < 0:
            durability = 0
        if flavor < 0:
            flavor = 0
        if texture < 0:
            texture = 0

        score = capacity * durability * flavor * texture
        if score > best_score and calories == 500:
            best_score = score

    print(best_score)


if __name__ == "__main__":
    main()
