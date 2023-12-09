"""Advent of code Day 4 part 1 and 2"""

import string


def valid_password(password: int, is_part_2: bool) -> bool:
    """Returns true if password is valid according to part 1 rules"""
    password_str = str(password)
    return contains_pair(password_str, is_part_2) and ascending_numbers(password_str)


def contains_pair(password: str, exclusive: bool = False) -> bool:
    """Returns true if password contains a pair"""
    if exclusive:
        for digit in string.digits:
            if digit + digit in password and (digit + digit + digit) not in password:
                return True
        return False

    for i, digit in enumerate(password):
        if i == len(password) - 1:
            return False

        if digit == password[i + 1]:
            return True
    raise RuntimeError("How did we get here?")


def ascending_numbers(password: str) -> bool:
    """Returns true if each number ascends the next"""
    highest_digit = 0
    for digit_char in password:
        digit = int(digit_char)
        if digit < highest_digit:
            return False
        highest_digit = digit
    return True


def main() -> None:
    """Main function"""
    with open("2019/04/input.txt", encoding="utf-8") as file:
        password_range = tuple(int(i) for i in file.read().split("-"))

    print(
        "Part 1:",
        sum(
            1
            for _ in (
                password
                for password in range(password_range[0], password_range[1])
                if valid_password(password, False)
            )
        ),
    )
    print(
        "Part 2:",
        sum(
            1
            for _ in (
                password
                for password in range(password_range[0], password_range[1])
                if valid_password(password, True)
            )
        ),
    )


if __name__ == "__main__":
    main()
