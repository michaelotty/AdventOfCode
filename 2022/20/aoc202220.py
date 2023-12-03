"""Advent of code Day 20."""


def main():
    """Main function."""
    with open("aoc2022/20/input.txt", encoding="utf-8") as file:
        nums = list(map(int, file.read().split()))
    print("Part 1:", part_1(nums))
    print("Part 2:", part_2(nums))


def part_1(nums: list[int]):
    """Solve part 1."""
    indexes = list(range(len(nums)))
    for i in indexes.copy():
        from_index = indexes.index(i)
        indexes.pop(from_index)
        to_index = (from_index + nums[i] - 1) % len(indexes) + 1
        indexes.insert(to_index, i)
    mixed = [nums[i] for i in indexes]
    zero_index = mixed.index(0)
    return sum(
        (
            mixed[(1000 + zero_index) % len(mixed)],
            mixed[(2000 + zero_index) % len(mixed)],
            mixed[(3000 + zero_index) % len(mixed)],
        )
    )


def part_2(nums: list[int]):
    """Solve part 2."""
    decrypt_key = 811589153
    nums = [num * decrypt_key for num in nums]

    indexes = list(range(len(nums)))
    for i in indexes.copy() * 10:
        from_index = indexes.index(i)
        indexes.pop(from_index)
        to_index = (from_index + nums[i] - 1) % len(indexes) + 1
        indexes.insert(to_index, i)
    mixed = [nums[i] for i in indexes]
    zero_index = mixed.index(0)
    return sum(
        (
            mixed[(1000 + zero_index) % len(mixed)],
            mixed[(2000 + zero_index) % len(mixed)],
            mixed[(3000 + zero_index) % len(mixed)],
        )
    )


if __name__ == "__main__":
    main()
