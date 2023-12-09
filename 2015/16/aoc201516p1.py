"""Advent of code Day 16 part 1"""


def main() -> None:
    """Main function"""
    with open("2015/16/input.txt", encoding="utf-8") as file:
        data = file.readlines()

    matches = (
        "children: 3",
        "cats: 7",
        "samoyeds: 2",
        "pomeranians: 3",
        "akitas: 0",
        "vizslas: 0",
        "goldfish: 5",
        "trees: 3",
        "cars: 2",
        "perfumes: 1",
    )

    for match in matches:
        data = [line for line in data if match_or_missing(match, line)]

    for line in data:
        print(line[0:-1])


def match_or_missing(match: str, line: str) -> bool:
    """Returns true if the string matches or if it isn't there at all"""
    if match.split()[0] in line:
        return match in line
    return True


if __name__ == "__main__":
    main()
