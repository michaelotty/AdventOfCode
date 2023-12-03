"""Advent of code Day 7 part 2"""

import re


def has_aba(test_string: str) -> list[tuple[str, str]]:
    """An ABA is any three-character sequence which
    consists of the same character twice with a
    different character between them, such as xyx
    or aba."""
    chars = []
    num_of_substr = len(test_string) - 2

    for i in range(num_of_substr):
        if (test_string[i] != test_string[i + 1]) and (
            test_string[i] == test_string[i + 2]
        ):
            chars.append((test_string[i], test_string[i + 1]))
    return chars


def has_bab(test_string: str, bab_chars: tuple[str, str]) -> bool:
    """A corresponding BAB is the same characters
    but in reversed positions: yxy and bab,
    respectively."""
    return bool(re.search(f"{bab_chars[1]}{bab_chars[0]}{bab_chars[1]}", test_string))


def supports_ssl(supernets: list[str], hypernets: list[str]) -> bool:
    """An IP supports SSL if it has an Area-Broadcast
    Accessor, or ABA, anywhere in the supernet sequences
    (outside any square bracketed sections), and a
    corresponding Byte Allocation Block, or BAB,
    anywhere in the hypernet sequences."""
    for aba_list in map(has_aba, supernets):
        for aba_item in aba_list:
            if any(has_bab(x, aba_item) for x in hypernets):
                return True
    return False


def main():
    """Main function"""
    with open("input.txt", encoding="utf-8") as file:
        lines = file.read().splitlines()

    re_expr = re.compile(r"\W+")
    print(
        sum(
            supports_ssl(x[::2], x[1::2])
            for x in (re_expr.split(line) for line in lines)
        )
    )


if __name__ == "__main__":
    main()
