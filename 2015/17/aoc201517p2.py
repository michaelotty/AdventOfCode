"""Advent of code Day 17 part 2"""

from itertools import combinations


def main():
    """Main function"""
    with open('input.txt') as file:
        data = file.readlines()

    comb = 0

    containers = tuple(int(i) for i in data)
    for i in combinations(containers, 4):
        if sum(i) == 150:
            comb += 1
    print(comb)


if __name__ == "__main__":
    main()
