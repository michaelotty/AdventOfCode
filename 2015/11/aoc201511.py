"""Advent of code Day 11 part 1 and 2"""

import string


def main():
    """Main function"""
    with open("input.txt", encoding="utf-8") as file:
        passwords = [file.read()]

    passwords.append(find_next_password(passwords[0]))
    passwords.append(find_next_password(increment_password(passwords[1])))
    print(passwords)


def find_next_password(password: str) -> str:
    """Finds the next valid password given the rules"""
    while not is_password_valid(password):
        password = increment_password(password)
    return password


def is_password_valid(password: str) -> bool:
    """Finds if a password if valid"""
    valid_password = (
        contains_straight_letters(password)
        and not contains_illegal_characters(password)
        and contains_two_non_overlapping_character_pairs(password)
    )
    return valid_password


def contains_straight_letters(password: str) -> bool:
    """Includes a straight set of letters"""
    straight_sets = {
        string.ascii_lowercase[i : i + 3]
        for i in range(len(string.ascii_lowercase) - 2)
    }
    return any(x in password for x in straight_sets)


def contains_illegal_characters(password: str) -> bool:
    """Finds if a password includes illegal characters"""
    illegal_characters = {"i", "o", "l"}
    return any(x in password for x in illegal_characters)


def contains_two_non_overlapping_character_pairs(password: str) -> bool:
    """Pair like 'aa', 'cc'"""
    character_pairs = set(x + x for x in string.ascii_lowercase)
    return sum(x in password for x in character_pairs) >= 2


def increment_password(password: str) -> str:
    """Increments the password"""
    shifted_alphabet = string.digits + string.ascii_lowercase[: -len(string.digits)]
    trans_down = str.maketrans(string.ascii_lowercase, shifted_alphabet)
    trans_up = str.maketrans(shifted_alphabet, string.ascii_lowercase)
    password = str.translate(password, trans_down)
    password_as_int = int(password, base=26)
    password_as_int += 1
    password = int_to_base26(password_as_int)
    password = str.translate(password, trans_up)
    while len(password) < 8:
        password = "a" + password

    return password


def int_to_base26(x: int, base: int = 26) -> str:
    """Converts an integer to base26. Opposite of int('abc', base=26)"""
    shifted_alphabet = string.digits + string.ascii_lowercase[: -len(string.digits)]
    digits: list[str] = []
    while x:
        digits.append(shifted_alphabet[x % base])
        x = x // base
    digits.reverse()
    return "".join(digits)


if __name__ == "__main__":
    main()
