#!/usr/bin/python3
"""N queens program
"""


import sys

args = sys.argv
if len(args) != 2:
    print("Usage: nqueens N")
    exit(1)

for i in args[1]:
    if ord(i) not in range(48, 58):
        print("N must be a number")
        exit(1)

if int(args[1]) < 4:
    print("N must be at least 4")
    exit(1)
#Handle rest of code here

