"""Advent of code Day 1 part 2"""


def find_frequency(numbers: tuple[int]) -> int:
    """Finds the frequency"""
    result = 0
    numbers_reached = set()

    while True:
        for number in numbers:
            numbers_reached.add(result)
            result += number
            if result in numbers_reached:
                return result


def main():
    """Main function"""
    with open("input.txt", encoding="utf-8") as file:
        numbers = tuple(int(i) for i in file.readlines())

    print(find_frequency(numbers))


if __name__ == "__main__":
    main()
