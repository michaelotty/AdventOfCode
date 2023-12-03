"""Advent of code Day 5 part 1"""


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        puzzle_input = list(map(int, file.read().split()))

    steps = 0
    index = 0
    while 0 <= index < len(puzzle_input):
        value = puzzle_input[index]
        puzzle_input[index] += 1
        index += value
        steps += 1
    print(steps)


if __name__ == "__main__":
    main()
