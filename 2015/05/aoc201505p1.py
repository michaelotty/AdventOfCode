"""Advent of code Day 5 part 1"""


def has_double_letter(string: str) -> bool:
    """Finds if the string has a repeated letter"""
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False


def count_vowels(string: str) -> int:
    """Counts the amount of vowels in a string"""
    vowels = ("a", "e", "i", "o", "u")
    num_of_vowels = 0
    for vowel in vowels:
        num_of_vowels += string.count(vowel)

    return num_of_vowels


def is_banned_string(string: str) -> bool:
    """Finds if the string contains at least one banned string"""
    banned_strings = ("ab", "cd", "pq", "xy")
    for banned_string in banned_strings:
        if banned_string in string:
            return True
    return False


def is_nice_string(string: str) -> bool:
    """Finds if a string is nice"""
    condition_1 = count_vowels(string) >= 3
    condition_2 = has_double_letter(string)
    condition_3 = not is_banned_string(string)

    return condition_1 and condition_2 and condition_3


def main() -> None:
    """Main function"""
    with open("2015/05/input.txt", encoding="utf-8") as f:
        file_contents = f.read()

    nice_strings = []

    file_contents = file_contents.split()

    for line in file_contents:
        if is_nice_string(line):
            nice_strings.append(line)

    print(len(nice_strings))


if __name__ == "__main__":
    main()
