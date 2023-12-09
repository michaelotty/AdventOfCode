"""Advent of code 2020 day 1"""

import numpy as np
import pandas as pd

data = pd.read_csv("question.txt", header=None)
data = np.array(data[0])

for point in data:
    sums = data + point
    if any(np.in1d(sums, 2020)):
        mask = np.in1d(sums, 2020)
        answer = point * data[mask]

print(answer[0])
