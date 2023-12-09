"""Advent of code day 2."""

import math


def main() -> None:
    """Main function."""
    with open("2023/02/input.txt", encoding="utf-8") as file:
        data = [line.split(": ")[1].split("; ") for line in file.read().split("\n")]

    games = []

    for line in data:
        game = []
        for subset in line:
            subset = subset.split(", ")
            new_subset = {}
            for cubes in subset:
                val, key = cubes.split()
                new_subset[key] = int(val)

            game.append(new_subset)
        games.append(game)

    print("Part 1:", part_1(games))
    print("Part 2:", part_2(games))


def part_1(games: list[list[dict[str, int]]]):
    """Solve part 1."""
    max_cubes = {"red": 12, "green": 13, "blue": 14}

    id_sum = 0

    for i, game in enumerate(games, start=1):
        is_possible = True
        for subset in game:
            for key in subset:
                if subset[key] > max_cubes[key]:
                    is_possible = False

        if is_possible:
            id_sum += i

    return id_sum


def part_2(games: list[list[dict[str, int]]]):
    """Solve part 2."""
    powers = []
    for game in games:
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        for subset in game:
            for key in subset:
                if subset[key] > min_cubes[key]:
                    min_cubes[key] = subset[key]
        powers.append(math.prod(min_cubes.values()))

    return sum(powers)


if __name__ == "__main__":
    main()
