"""Advent of Code 2015 day 1 part 2"""


def main():
    """Start of program"""

    with open("2015/01/input.txt", encoding="utf-8") as f:
        text = f.read()

    floor = 0
    basement_floor = -1

    for i, char in enumerate(text):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == basement_floor:
            print(f"basement steps: {i+1}")
            break


if __name__ == "__main__":
    main()
