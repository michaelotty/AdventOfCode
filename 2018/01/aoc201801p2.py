"""Advent of code Day 1 part 2."""


def find_frequency(numbers: tuple[int, ...]) -> int:
    """Find the frequency."""
    result = 0
    numbers_reached = set()

    while True:
        for number in numbers:
            numbers_reached.add(result)
            result += number
            if result in numbers_reached:
                return result


def main() -> None:
    """Program starts here."""
    with open("2018/01/input.txt", encoding="utf-8") as file:
        numbers = tuple(int(i) for i in file.readlines())

    print(find_frequency(numbers))


if __name__ == "__main__":
    main()
