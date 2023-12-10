"""Advent of code Day 5 part 2."""


def contains_repeated_pair(string: str) -> bool:
    """Finds if string contains a pair of letters which occurs twice."""
    for i in range(len(string) - 1):
        search_string = string[i : i + 2]
        string1_to_search = string[0:i]
        string2_to_search = string[i + 2 : -1]

        if search_string in string1_to_search or search_string in string2_to_search:
            return True

    return False


def contains_spaced_repeated_letter(string: str) -> bool:
    """Finds if a letter repeats after with a 1 letter jump."""
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    return False


def is_nice_string(string: str) -> bool:
    """Finds if a string is nice."""
    condition_1 = contains_repeated_pair(string)
    condition_2 = contains_spaced_repeated_letter(string)

    return condition_1 and condition_2


def main() -> None:
    """Program starts here."""
    with open("2015/05/input.txt", encoding="utf-8") as f:
        file_contents = f.read()

    nice_strings = []

    data = file_contents.split()

    for line in data:
        if is_nice_string(line):
            nice_strings.append(line)

    print(len(nice_strings))


if __name__ == "__main__":
    main()
