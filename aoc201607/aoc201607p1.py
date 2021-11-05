"""Advent of code Day 7 part 1"""

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


def supports_tls(ips: list[str], hypernets: list[str]) -> bool:
    """An IP supports TLS if it has an Autonomous Bridge
    Bypass Annotation, or ABBA.
    However, the IP also must not have an ABBA within any
    hypernet sequences, which are contained by square
    brackets."""
    return any(map(has_abba, ips)) and not any(map(has_abba, hypernets))


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        lines = file.read().splitlines()

    re_expr = re.compile(r'\[(\w+)\]')
    print(sum(supports_tls(x[::2], x[1::2]) for x in (re_expr.split(line) for line in lines)))


if __name__ == "__main__":
    main()
