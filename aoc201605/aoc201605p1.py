"""Advent of code Day 5 part 1"""

import hashlib


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        content = file.read()
    index = 0
    matches = []

    while len(matches) < 8:
        test_code = content + str(index)
        hash = hashlib.md5(test_code.encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            matches.append(hash[5])
        index += 1

    print(''.join(matches))


if __name__ == "__main__":
    main()
