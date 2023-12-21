"""Advent of code Day 1 part 2."""


def main() -> None:
    """Program starts here."""
    with open("2017/01/input.txt", encoding="utf-8") as file:
        numbers = [int(x) for x in file.read()]

    answer = 0

    for i, _ in enumerate(numbers):
        if numbers[i] == numbers[(i + len(numbers) // 2) % len(numbers)]:
            answer += numbers[i]

    print(answer)


if __name__ == "__main__":
    main()
