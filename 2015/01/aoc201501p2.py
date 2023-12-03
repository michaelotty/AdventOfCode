"""Advent of Code 2015 day 1 part 2"""


def main():
    """Start of program"""

    with open('input.txt') as f:
        text = str(f.read())

    floor = 0
    basement_floor = -1

    for i, char in enumerate(text):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == basement_floor:
            break

    print(f'basement steps: {i+1}')


if __name__ == "__main__":
    main()
