"""Advent of code Day 25."""


def main() -> None:
    """Main function."""
    with open("2022/25/input.txt", encoding="utf-8") as file:
        nums = file.read().splitlines()
    test_snafu()
    print("Part 1:", part_1(nums))
    print("Part 2:", part_2(nums))


def test_snafu() -> None:
    """Test the SNAFU converters."""
    test_cases = {
        "1": 1,
        "2": 2,
        "1=": 3,
        "1-": 4,
        "10": 5,
        "11": 6,
        "12": 7,
        "2=": 8,
        "2-": 9,
        "20": 10,
        "1=0": 15,
        "1-0": 20,
        "1=11-2": 2022,
        "1-0---0": 12345,
        "1121-1110-1=0": 314159265,
    }
    for key, val in test_cases.items():
        test = snafu_to_int(key)
        assert test == val, f"SNAFU to int unsuccessful: ({test} != {val})"
        test = int_to_snafu(val)
        assert test == key, f"int to SNAFU unsuccessful: ({test} != {key})"


def snafu_to_int(snafu: str) -> int:
    """Convert a SNAFU number to a normal number."""
    new_digit = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    return sum(
        5**base * new_digit[digit] for base, digit in enumerate(reversed(snafu))
    )


def int_to_snafu(num: int) -> str:
    """Convert a normal number to a SNAFU number."""
    if num == 0:
        return "0"

    new_digits = {4: "-", 3: "=", 2: "2", 1: "1", 0: "0"}

    digits = ""
    while num:
        remainder = num % 5
        num = num // 5
        new_digit = new_digits[remainder]
        digits += new_digit
        if remainder > 2:
            num += 1

    return digits[::-1]


def part_1(nums):
    """Solve part 1."""
    return int_to_snafu(sum(snafu_to_int(num) for num in nums))


def part_2(nums):
    """Solve part 2."""
    return nums


if __name__ == "__main__":
    main()
