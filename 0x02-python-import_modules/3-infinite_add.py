#!/usr/bin/python3
import sys
args = sys.argv
summ = 0
for i, value in enumerate(args):
    if (i == 0):
        continue
    summ += int(value)
print(summ)
