"""Advent of code Day 4 part 1 and 2"""

import re
from datetime import datetime
from operator import itemgetter


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        lines = [(datetime.fromisoformat(date_time), desc)
                 for date_time, desc in re.findall(r'\[(.+)\] (.+)\n', file.read())]

    lines = sorted(lines, key=itemgetter(0))

    for line in lines:
        print(f'{line[0].isoformat()} {line[1]}')


if __name__ == "__main__":
    main()
