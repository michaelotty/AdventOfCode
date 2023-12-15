"""Advent of code day 6."""

import math


def main() -> None:
    """Program starts here."""
    with open("2023/06/input.txt", encoding="utf-8") as file:
        text = file.read()

    first_line, second_line = text.splitlines()

    _, *time_strs = first_line.split()
    _, *distance_strs = second_line.split()

    data = [
        {"time": int(time), "distance": int(distance)}
        for time, distance in zip(time_strs, distance_strs)
    ]

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(time_strs, distance_strs))


def part_1(races: list[dict[str, int]]) -> int:
    """Solve part 1."""
    race_wins = []
    for race in races:
        winners = []
        for speed in range(1, race["time"]):
            time_left = race["time"] - speed
            distance = speed * time_left
            if distance > race["distance"]:
                winners.append(speed)

        race_wins.append(len(winners))

    return math.prod(race_wins)


def part_2(time_strs: list[str], distance_strs: list[str]) -> int:
    """Solve part 2."""
    time = int("".join(time_strs))
    distance = int("".join(distance_strs))

    winners = 0
    for speed in range(1, time):
        time_left = time - speed
        distance_travelled = speed * time_left
        if distance_travelled > distance:
            winners += 1

    return winners


if __name__ == "__main__":
    main()
