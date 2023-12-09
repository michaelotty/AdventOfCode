"""Advent of code Day 24 part 1"""

from itertools import permutations


def main() -> None:
    """Main function"""
    with open("2015/24/input.txt", encoding="utf-8") as file:
        present_weights = tuple(int(i) for i in file.read().split())

    presents_in_group_1 = 2

    # present_weights = (1, 2, 3, 4, 5, 7, 8, 9, 10, 11)
    valid_combos = set()
    searching_for_solution = True
    while searching_for_solution:
        for permutation in permutations(present_weights):
            group_1 = permutation[:presents_in_group_1]
            group_2_and_3 = permutation[presents_in_group_1:]
            for i in range(2, len(group_2_and_3) - 2):
                group_2 = group_2_and_3[:i]
                group_3 = group_2_and_3[i:]

                if sum(group_1) == sum(group_2) == sum(group_3):
                    searching_for_solution = False
                    valid_combos.add((group_1, group_2, group_3))
        presents_in_group_1 += 1

    print(min(multiply(i[0]) for i in valid_combos))


def multiply(*iterable) -> int:
    """Multiply all elements and sub-elements"""
    multiple = 1
    for i in iterable:
        if isinstance(i, int):
            multiple *= i
        else:
            multiple *= multiply(*i)
    return multiple


if __name__ == "__main__":
    main()
