"""Advent of code day 2."""


def main():
    """Main function."""
    with open("aoc2023/02/input.txt", encoding="utf-8") as file:
        data = [line.split(": ")[1].split("; ") for line in file.read().split("\n")]

    print("Part 1:", part_1(data))
    print("Part 2:", part_2())


def part_1(data: list[list[str]]):
    """Solve part 1."""
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


def part_2():
    """Solve part 2."""


if __name__ == "__main__":
    main()
