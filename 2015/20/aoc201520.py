"""Advent of code Day 20 part 1 and 2"""


def find_lowest_house(houses: list[int], value: int) -> tuple[int, int]:
    """Finds the house id and amount of presents for the first house that contains
    the presents that exceeds the value"""
    for house_num, presents in enumerate(houses):
        if presents >= value:
            return house_num, presents
    raise ValueError(f"Could not find lowest house for {value} in list given")


def main():
    """Main function"""
    with open("input.txt", encoding="utf-8") as file:
        puzzle_input = int(file.read())

    # Part 1
    print("Allocating...")
    houses = [0 for _ in range(puzzle_input // 10)]
    print("Populating...")
    for i in range(1, puzzle_input // 10):
        for j in range(i, puzzle_input // 10, i):
            houses[j] += i * 10
    print("Finding...")
    house_num, presents = find_lowest_house(houses, puzzle_input)
    print(f"{house_num}: {presents}")
    print("Done\n\n")

    # Part 2
    print("Allocating...")
    houses = [0 for _ in range(puzzle_input // 10)]
    print("Populating...")
    for i in range(1, puzzle_input // 10):
        for j in range(i, i * 50 + 1, i):
            if j >= puzzle_input // 10:
                break
            houses[j] += i * 11
    print("Finding...")
    house_num, presents = find_lowest_house(houses, puzzle_input)
    print(f"{house_num}: {presents}")
    print("Done")


if __name__ == "__main__":
    main()
