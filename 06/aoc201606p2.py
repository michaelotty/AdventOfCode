"""Advent of code Day 6 part 2"""

from collections import Counter


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        content = file.read().splitlines()
    transposed_content = [''.join(x[y] for x in content)
                          for y in range(len(content[0]))]

    counters = [Counter(x) for x in transposed_content]
    print(''.join(x.most_common()[-1][0] for x in counters))


if __name__ == "__main__":
    main()
