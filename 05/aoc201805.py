"""Advent of code Day 5"""


def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as file:
        text = file.read()
    did_reduce = True

    while did_reduce:
        did_reduce, text = reduce(text)
    print(len(text))


def reduce(text: str) -> tuple[bool, str]:
    """Reduce polymer, bool returns true if reduction was made"""
    text: tuple = tuple(text)
    starting_len = len(text)
    i = 0
    while True:
        if i + 1 >= len(text):
            return starting_len != len(text), ''.join(text)
        if (text[i] == text[i + 1].upper()
            and text[i].lower() == text[i + 1]) or (text[i].upper() == text[i + 1]
                                                    and text[i] == text[i + 1].lower()):
            text = (*text[:i], *text[i+2:])
        i += 1


if __name__ == "__main__":
    main()
