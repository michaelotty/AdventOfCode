"""Advent of code 2020 day 6"""

with open('question.txt', 'rt') as f:
    text = f.read()
    groups = text.split('\n\n')

    total = 0

    for string in groups:
        string = string.replace('\n', '')  # Remove whitespace
        letters = set(string)
        total += len(letters)
    
    print(total)
