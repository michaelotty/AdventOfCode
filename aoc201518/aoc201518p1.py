"""Advent of code Day 18 part 1"""


def main():
    """Main function"""
    with open('test.txt') as file:
        lines = file.read().split()

    height = len(lines)
    width = len(lines[0])

    grid = [[extract_cell(i, j, lines) for i in range(height)] for j in range(width)]

    print(sum([sum(line) for line in grid]))


def extract_cell(i: int, j: int, lines: str) -> bool:
    """Convert character map into bool map"""
    if lines[j][i] == '#':
        return True
    return False


if __name__ == "__main__":
    main()
