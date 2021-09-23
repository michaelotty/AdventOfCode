"""Advent of Code 2020 Day 3"""

with open('question.txt', "rt") as f:
    col = 0
    answer = 0
    lines = f.readlines()

    for line in lines:
        line = line.replace('\n', '')
        if col >= len(line):
            col -= len(line)

        if line[col] == '#' or line[col] == 'O':
            answer += 1
        col += 3

    print(answer)
