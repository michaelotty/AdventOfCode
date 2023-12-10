"""Advent of code 2020 day 6."""

with open("question.txt", encoding="utf-8") as f:
    text = f.read()
    groups = text.split("\n\n")

    TOTAL = 0

    for string in groups:
        entries = string.split()
        sets = [set(a) for a in entries]

        if len(sets) == 1:
            TOTAL += len(sets[0])
            continue

        intersected_set = sets[0]
        for i in range(1, len(sets)):
            intersected_set &= sets[i]
        TOTAL += len(intersected_set)

print(TOTAL)
