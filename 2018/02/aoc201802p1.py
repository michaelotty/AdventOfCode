"""Advent of code Day 2 part 1."""

from collections import Counter


def calculate_checksum(lines: list[str]) -> int:
    """Calculate checksum."""
    count_of_twos = 0
    count_of_threes = 0
    sorted_lines = [Counter(line).most_common() for line in lines]

    for line in sorted_lines:
        count_of_letters = set(i for _, i in line)
        if 2 in count_of_letters:
            count_of_twos += 1
        if 3 in count_of_letters:
            count_of_threes += 1

    return count_of_twos * count_of_threes


def main() -> None:
    """Program starts here."""
    with open("2018/02/input.txt", encoding="utf-8") as file:
        lines = file.read().split()

    print(calculate_checksum(lines))


if __name__ == "__main__":
    main()
