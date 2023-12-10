"""Advent of code Day 1 part 1 and 2."""


def main() -> None:
    """Program starts here."""
    with open("2019/01/input.txt", encoding="utf-8") as file:
        numbers = [int(i) for i in file.readlines()]
    print(f"Part 1: {sum(max(num // 3 - 2, 0) for num in numbers)}")

    part_2_answer = 0
    for num in numbers:
        while True:
            num = num // 3 - 2
            if num > 0:
                part_2_answer += num
            else:
                break

    print(f"Part 2: {part_2_answer}")


if __name__ == "__main__":
    main()
