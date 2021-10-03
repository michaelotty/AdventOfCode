"""Advent of code Day 11 part 1"""

from itertools import combinations_with_replacement
from string import ascii_lowercase

allowed_letters = list(ascii_lowercase)
allowed_letters.remove('i')
allowed_letters.remove('o')
allowed_letters.remove('l')
allowed_letters = ''.join(allowed_letters)

possible_combiniations = tuple(
    ''.join(i) for i in combinations_with_replacement(allowed_letters, 8))


def main():
    """Main function"""
    with open('input.txt') as f:
        current_password = f.read()

    # Test
    # current_password = 'hijklmmn'
    current_password = 'abcdefgh'

    print(find_next_password(current_password))


def find_next_password(password: str) -> str:
    """Finds the next valid password given the rules"""
    while not is_password_valid(password):
        password = increment_password(password)
    return password


def is_password_valid(password: str) -> bool:
    """Finds if a password if valid"""
    valid_password = contains_straight_letters(password) and not contains_illegal_characters(
        password) and contains_two_non_overlapping_character_pairs(password)
    return valid_password


def contains_straight_letters(password: str) -> bool:
    """Includes a straight set of letters"""
    straight_sets = set(ascii_lowercase[i:i+3]
                        for i in range(len(ascii_lowercase)-2))
    return any(x in password for x in straight_sets)


def contains_illegal_characters(password: str) -> bool:
    """Finds if a password includes illegal characters"""
    illegal_characters = {'i', 'o', 'l'}
    return any(x in password for x in illegal_characters)


def contains_two_non_overlapping_character_pairs(password: str) -> bool:
    """Pair like 'aa', 'cc'"""
    character_pairs = set(x + x for x in ascii_lowercase)
    return sum(x in password for x in character_pairs) >= 2


def increment_password(password: str) -> str:
    """Increments the password"""
    global possible_combiniations
    found_pw = False

    for x in possible_combiniations:
        if found_pw:
            return x
        elif x == password:
            found_pw = True
        else:
            possible_combiniations.remove(x)
        if len(possible_combiniations) % 1000 == 0:
            print(len(possible_combiniations))

    return password


if __name__ == "__main__":
    main()
