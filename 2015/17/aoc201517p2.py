"""Advent of code Day 17 part 2."""

from itertools import combinations


def main() -> None:
    """Program starts here."""
    with open("2015/17/input.txt", encoding="utf-8") as file:
        data = file.readlines()

    comb = 0

    containers = tuple(int(i) for i in data)
    for i in combinations(containers, 4):
        if sum(i) == 150:
            comb += 1
    print(comb)


if __name__ == "__main__":
    main()
