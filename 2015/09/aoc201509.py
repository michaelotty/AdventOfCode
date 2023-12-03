"""Advent of code Day 9 part 1 and 2"""

import sys
from itertools import permutations


def main():
    """Main function"""
    places = set()
    distances = {}

    for line in open("input.txt", encoding="utf-8"):
        source, _, destination, _, distance = line.split()
        places.add(source)
        places.add(destination)
        distance = int(distance)

        distances.setdefault(source, dict())[destination] = distance
        distances.setdefault(destination, dict())[source] = distance

    shortest = sys.maxsize
    longest = 0
    for items in permutations(places):
        distance = sum([distances[edge[0]][edge[1]] for edge in zip(items, items[1:])])
        shortest = min(shortest, distance)
        longest = max(longest, distance)

    print(f"Shortest: {shortest}")
    print(f"Longest: {longest}")


if __name__ == "__main__":
    main()
