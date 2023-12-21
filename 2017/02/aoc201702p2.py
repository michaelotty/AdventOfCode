"""Advent of code Day 2 part 2."""

from itertools import combinations


def main() -> None:
    """Program starts here."""
    with open("2017/02/input.txt", encoding="utf-8") as file:
        rows = tuple(
            tuple(int(element) for element in row.split()) for row in file.readlines()
        )

    print(
        sum(
            comb[1] // comb[0]
            for row in rows
            for comb in combinations(sorted(row), 2)
            if comb[1] % comb[0] == 0
        )
    )


if __name__ == "__main__":
    main()
