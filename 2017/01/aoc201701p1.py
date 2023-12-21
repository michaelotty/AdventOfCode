"""Advent of code Day 1 part 1."""


def main() -> None:
    """Program starts here."""
    with open("2017/01/input.txt", encoding="utf-8") as file:
        numbers = tuple(int(x) for x in file.read())

    answer = 0

    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            answer += numbers[i]
    if numbers[-1] == numbers[0]:
        answer += numbers[-1]

    print(answer)


if __name__ == "__main__":
    main()
