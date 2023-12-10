"""Advent of code Day 16 part 2."""

import re


def main() -> None:
    """Program starts here."""
    with open("2015/16/input.txt", encoding="utf-8") as file:
        data = file.readlines()

    greaters = ("cats: 7", "trees: 3")

    fewers = (
        "pomeranians: 3",
        "goldfish: 5",
    )

    matches = (
        "children: 3",
        "samoyeds: 2",
        "akitas: 0",
        "vizslas: 0",
        "cars: 2",
        "perfumes: 1",
    )

    for match in matches:
        data = [line for line in data if match_or_missing(match, line)]

    for greater in greaters:
        data = [line for line in data if greater_or_missing(greater, line)]

    for fewer in fewers:
        data = [line for line in data if fewer_or_missing(fewer, line)]

    for line in data:
        print(line[0:-1])


def match_or_missing(match: str, line: str) -> bool:
    """Return true if the string matches or if it isn't there at all."""
    if match.split()[0] in line:
        return match in line
    return True


def greater_or_missing(match: str, line: str) -> bool:
    """Return true if the value is greater than or if it isn't there at all."""
    regex_match = re.search(match.split()[0] + r" (\d+)", line)
    if regex_match is not None:
        return int(regex_match.group(1)) > int(match.split()[1])
    return True


def fewer_or_missing(match: str, line: str) -> bool:
    """Return true if the value is less than or if it isn't there at all."""
    regex_match = re.search(match.split()[0] + r" (\d+)", line)
    if regex_match is not None:
        return int(regex_match.group(1)) < int(match.split()[1])
    return True


if __name__ == "__main__":
    main()
