"""Advent of code Day 12 part 1"""

import json


def main():
    """Main function"""
    with open("input.txt", encoding="utf-8") as f:
        data = json.load(f)
    print(sum_of_elements(data))


def sum_of_elements(data) -> int:
    """Sums all the numbers in the data"""
    try:
        return int(data)
    except TypeError:
        pass
    except ValueError:
        return 0

    sum_val = 0
    for i in data:
        if isinstance(data, dict):
            sum_val += sum_of_elements(data[i])
        else:
            sum_val += sum_of_elements(i)

    return sum_val


if __name__ == "__main__":
    main()
