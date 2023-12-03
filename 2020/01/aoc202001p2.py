"""Advent of code 2020 day 1"""

import itertools
from math import prod

import pandas as pd

data = pd.read_csv("question.txt", header=None)[0]

for subset in itertools.combinations(data, 3):
    if sum(subset) == 2020:
        answer = prod(subset)
        break

print(answer)
