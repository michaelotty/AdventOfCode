"""Advent of code Day 5 part 2."""


def main() -> None:
    """Program starts here."""
    with open("2017/05/input.txt", encoding="utf-8") as file:
        puzzle_input = list(map(int, file.read().split()))

    steps = 0
    index = 0
    while 0 <= index < len(puzzle_input):
        value = puzzle_input[index]
        if value >= 3:
            puzzle_input[index] -= 1
        else:
            puzzle_input[index] += 1
        index += value
        steps += 1
    print(steps)


if __name__ == "__main__":
    main()
