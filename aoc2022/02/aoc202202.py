"""Advent of code Day 2."""


def main():
    """Main function."""
    with open("input.txt", encoding="utf-8") as file:
        puzzle = [tuple(line.split()) for line in file.read().split("\n")]
    print(f"Part 1: {part_1(puzzle)}")
    print(f"Part 2: {part_2(puzzle)}")


def part_1(puzzle):
    """Solve part 1."""
    win = 6
    draw = 3
    loss = 0
    scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
        ("A", "X"): draw,
        ("A", "Y"): win,
        ("A", "Z"): loss,
        ("B", "X"): loss,
        ("B", "Y"): draw,
        ("B", "Z"): win,
        ("C", "X"): win,
        ("C", "Y"): loss,
        ("C", "Z"): draw,
    }
    totals = []
    for them, us in puzzle:
        totals.append(scores[us] + scores[(them, us)])

    return sum(totals)


def part_2(puzzle):
    """Solve part 2."""
    win = 6
    draw = 3
    loss = 0
    scores = {
        ("A", "X"): 3,
        ("A", "Y"): 1,
        ("A", "Z"): 2,
        ("B", "X"): 1,
        ("B", "Y"): 2,
        ("B", "Z"): 3,
        ("C", "X"): 2,
        ("C", "Y"): 3,
        ("C", "Z"): 1,
        "X": loss,
        "Y": draw,
        "Z": win,
    }
    totals = []
    for them, us in puzzle:
        totals.append(scores[(them, us)] + scores[us])

    return sum(totals)


if __name__ == "__main__":
    main()
