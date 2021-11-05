"""Advent of code Day 7 part 2"""

import re


def has_abba(test_string: str) -> bool:
    """An ABBA is any four-character sequence which consists
    of a pair of two DIFFERENT characters followed by the
    reverse of that pair, such as xyyx or abba.
    Not aaaa or tttt."""
    num_of_substr = len(test_string) - 3
    for i in range(num_of_substr):
        if (test_string[i] != test_string[i+1]) and (test_string[i:i+2] == test_string[i+3:i+1:-1]):
            return True
    return False


def has_aba(test_string: str) -> list[tuple[str, str]]:
    """An ABA is any three-character sequence which
    consists of the same character twice with a
    different character between them, such as xyx
    or aba."""
    chars = []
    num_of_substr = len(test_string) - 2

    for i in range(num_of_substr):
        if (test_string[i] != test_string[i+1]) and (test_string[i] == test_string[i+2]):
            chars.append((test_string[i], test_string[i+1]))
    return chars


def has_bab(test_string: str, bab_chars: tuple[str, str]) -> bool:
    """A corresponding BAB is the same characters
    but in reversed positions: yxy and bab,
    respectively."""
    return bool(re.search(f'{bab_chars[1]}{bab_chars[0]}{bab_chars[1]}', test_string))


def supports_tls(supernets: list[str], hypernets: list[str]) -> bool:
    """An IP supports TLS if it has an Autonomous Bridge
    Bypass Annotation, or ABBA.
    However, the IP also must not have an ABBA within any
    hypernet sequences, which are contained by square
    brackets."""
    return any(map(has_abba, supernets)) and not any(map(has_abba, hypernets))


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
    with open('input.txt', encoding='utf-8') as file:
        lines = file.read().splitlines()

    ips_that_support_tls = []
    ips_that_support_ssl = []

    inside_brackets = re.compile(r'\[(\w+)\]')
    outside_brackets = re.compile(r'\w+\[|\]\w+')
    word_only = re.compile(r'\w+')

    for line in lines:
        hypernet_sequences = inside_brackets.findall(line)
        ip_sequences = outside_brackets.findall(line)
        ip_sequences = [
            word_only.search(ip_sequence).group()
            for ip_sequence in ip_sequences]

        ips_that_support_tls.append(
            supports_tls(ip_sequences, hypernet_sequences))

        ips_that_support_ssl.append(
            supports_ssl(ip_sequences, hypernet_sequences))

    print(sum(ips_that_support_ssl))


if __name__ == "__main__":
    main()
