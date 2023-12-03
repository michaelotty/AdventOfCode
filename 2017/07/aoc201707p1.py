"""Advent of code Day 7 part 1"""

import re


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        lines = file.readlines()

    weights = {}
    tree = {}

    for line in lines:
        label, weight, *extra = re.findall(r'\w+', line)
        weights[label] = int(weight)
        tree[label] = tuple(extra)

    print((set(weights) - {child for children in tree.values()
          for child in children}).pop())


if __name__ == "__main__":
    main()
