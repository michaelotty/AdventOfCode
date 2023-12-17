"""Advent of code day 4."""

import re


def main() -> None:
    """Program starts here."""
    with open("2023/04/input.txt", encoding="utf-8") as file:
        raw_data = [
            re.split(r"(?:: )|(?: \| )", line)[1:] for line in file.read().splitlines()
        ]

    data = [
        (
            {int(num) for num in re.findall(r"\d+", left_str)},
            {int(num) for num in re.findall(r"\d+", right_str)},
        )
        for left_str, right_str in raw_data
    ]

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


def part_1(data: list[tuple[set[int], set[int]]]) -> int:
    """Solve part 1."""
    points = 0
    for nums_to_win, scratch_card in data:
        won_nums = len(nums_to_win & scratch_card)
        if not won_nums:
            continue
        points += 2 ** (won_nums - 1)

    return points


def part_2(data: list[tuple[set[int], set[int]]]) -> int:
    """Solve part 2."""
    # wins: list[set] = []
    scratch_card_copies = [1 for _ in data]
    for i, (nums_to_win, scratch_card) in enumerate(data):
        wins = len(nums_to_win & scratch_card)
        for j in range(i + 1, i + 1 + wins):
            scratch_card_copies[j] += scratch_card_copies[i]

    return sum(scratch_card_copies)


if __name__ == "__main__":
    main()
