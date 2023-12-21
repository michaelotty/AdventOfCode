"""Advent of Code 2020 day 5."""

with open("question.txt", encoding="utf-8") as f:
    text = f.read()
    text = text.replace("F", "0")
    text = text.replace("B", "1")

    text = text.replace("L", "0")
    text = text.replace("R", "1")

    data = text.split("\n")
    IDs = []
    for line in data:
        ID = int(line, 2)
        IDs.append(ID)
    print(max(IDs))
