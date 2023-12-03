"""Advent of code 2020 day 2"""

import re
import pandas as pd

data = pd.read_csv('question.txt', header=None, delimiter=' ')
data[1] = data[1].str.strip(':')
data[[0, 3]] = data[0].str.split('-', expand=True)
data[4] = False

for i, string in enumerate(data[2]):
    num_chars = len([a.start()
                     for a in re.finditer(data[1][i], f'(?={data[2][i]})')])
    data[4][i] = int(data[0][i]) <= num_chars <= int(data[3][i])

print(len(data[data[4] is True]))
