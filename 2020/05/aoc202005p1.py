"""Advent of Code 2020 day 5"""

with open('question.txt', 'rt') as f:
    text = f.read()
    text = text.replace('F', '0')
    text = text.replace('B', '1')

    text = text.replace('L', '0')
    text = text.replace('R', '1')

    text = text.split('\n')
    IDs = list()
    for line in text:
        ID = int(line, 2)
        IDs.append(ID)
    print(max(IDs))
