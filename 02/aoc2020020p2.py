"""Advent of code 2020 day 2"""

import pandas as pd

data = pd.read_csv('question.txt', header=None, delimiter=' ')
data[1] = data[1].str.strip(':')
data[[0, 3]] = data[0].str.split('-', expand=True)
data[4] = False

for i, string in enumerate(data[2]):
    data[4][i] = (string[int(data[0][i]) - 1] == data[1][i]
                  ) ^ (string[int(data[3][i]) - 1] == data[1][i])

print(len(data[data[4] is True]))
