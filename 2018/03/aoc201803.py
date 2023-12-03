"""Advent of code Day 3 part 1 and 2"""

import re
from itertools import product


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        lines = [tuple(map(int, line)) for line in re.findall(
            r'(\d+),(\d+): (\d+)x(\d+)', file.read())]

    claim_ids = set(i for i, _ in enumerate(lines, start=1))

    fabric = [[set() for _ in range(1000)] for _ in range(1000)]
    for i, line in enumerate(lines, start=1):
        for x_pos, y_pos in product(range(line[0], line[0]+line[2]),
                                    range(line[1], line[1]+line[3])):
            fabric[x_pos][y_pos].add(i)

    print(sum(1 for x_pos, y_pos in product(range(1000),          repeat=2)
              if len(fabric[x_pos][y_pos]) >= 2))

    for x_pos, y_pos in product(range(1000), repeat=2):
        if len(fabric[x_pos][y_pos]) > 1:
            for claim in fabric[x_pos][y_pos]:
                claim_ids.discard(claim)

    print(claim_ids.pop())


if __name__ == "__main__":
    main()
