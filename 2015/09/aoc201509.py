"""Advent of code Day 9 part 1 and 2."""

import sys
from itertools import permutations


def main() -> None:
    """Program starts here."""
    places: set[str] = set()
    distances: dict[str, dict[str, int]] = {}

    with open("2015/09/input.txt", encoding="utf-8") as fp:
        data = fp.read()

    for line in data.splitlines():
        source, _, destination, _, distance_str = line.split()
        places.add(source)
        places.add(destination)
        distance = int(distance_str)

        distances.setdefault(source, {})[destination] = distance
        distances.setdefault(destination, {})[source] = distance

    shortest = sys.maxsize
    longest = 0
    for items in permutations(places):
        distance = sum(distances[edge[0]][edge[1]] for edge in zip(items, items[1:]))
        shortest = min(shortest, distance)
        longest = max(longest, distance)

    print(f"Shortest: {shortest}")
    print(f"Longest: {longest}")


if __name__ == "__main__":
    main()
