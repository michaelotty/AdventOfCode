"""Advent of Code 2015 day 1 part 1"""


def main():
    """Start of program"""

    with open('input.txt') as f:
        text = str(f.read())

    up = text.count("(")
    down = text.count(")")

    print(f'up: {up}')
    print(f'down: {down}')
    print(f'up - down: {up-down}')


if __name__ == "__main__":
    main()
