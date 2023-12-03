"""Advent of code 2020 day 6"""

with open("question.txt", encoding="utf-8") as f:
    text = f.read()
    groups = text.split("\n\n")

    TOTAL = 0

    for string in groups:
        string = string.replace("\n", "")  # Remove whitespace
        letters = set(string)
        TOTAL += len(letters)

    print(TOTAL)
