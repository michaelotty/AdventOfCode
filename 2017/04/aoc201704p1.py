"""Advent of code Day 4 part 1."""


def main() -> None:
    """Program starts here."""
    with open("2017/04/input.txt", encoding="utf-8") as file:
        puzzle_input = [x.split() for x in file.readlines()]

    valid_passphrases = [line for line in puzzle_input if len(set(line)) == len(line)]
    print(len(valid_passphrases))


if __name__ == "__main__":
    main()
