"""Advent of code Day 4 part 1 and 2"""


def valid_password(password: int) -> bool:
    """Returns true if password is valid"""
    password = str(password)
    return contains_pair(password) and ascending_numbers(password)


def contains_pair(password: str) -> bool:
    """Returns true if password contains a pair"""
    for i, digit in enumerate(password):
        if i == len(password) - 1:
            return False

        if digit == password[i+1]:
            return True


def ascending_numbers(password: str) -> bool:
    """Returns true if each number ascends the next"""
    highest_digit = 0
    for digit in password:
        digit = int(digit)
        if digit < highest_digit:
            return False
        highest_digit = digit
    return True


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        password_range = tuple(int(i) for i in file.read().split('-'))

    valid_passwords = [password for password in range(
        password_range[0], password_range[1]) if valid_password(password)]

    print(len(valid_passwords))


if __name__ == "__main__":
    main()
