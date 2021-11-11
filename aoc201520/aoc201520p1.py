"""Advent of code Day 20 part 1"""

from collections import Counter
from functools import reduce
from math import sqrt
from operator import mul


def factors(n: int) -> int:
    j = 2
    while n > 1:
        for i in range(j, int(sqrt(n+0.05)) + 1):
            if n % i == 0:
                n //= i
                j = i
                yield i
                break
        else:
            if n > 1:
                yield n
                break


def presents_at_house(house_number: int) -> int:
    """Works out the number of presents delivered to a house"""
    presents = 0
    for elf_id in range(1, house_number + 1):
        if not (house_number % elf_id):
            presents += elf_id
    return presents * 10


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        puzzle_input = int(file.read())
    # facts = tuple(int(i) for i in factors(puzzle_input//10))
    facts = tuple(factors(puzzle_input//10))
    reduced_facts = tuple(a**b for a, b in Counter(facts).most_common())
    print(facts)
    print(reduced_facts)
    print(reduce(mul, facts))
    # for i in range(500000, puzzle_input//10):
    #     x = presents_at_house(i)
    #     if x >= puzzle_input:
    #         presents = (i, x)
    #         break
    #     if not (i % 1000):
    #         print(f'{i}: {x}')
    # print(presents)

# 900480 too high


if __name__ == "__main__":
    main()
