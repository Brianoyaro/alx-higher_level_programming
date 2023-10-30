#!/usr/bin/python3
"""N queens program
"""
import sys
args = sys.argv
#Usage: nqueens N
if len(args) != 2:
    print("Usage: nqueens N")
    exit(1)
#where N must be an integer greater or equal to 4
for i in args[1]:
    if ord(i) not in range(48, 58):
        print("N must be a number")
        exit(1)
#check if N is greater the 4
if int(args[1]) < 4:
    print("N must be at least 4")
    exit(1)
#Handle rest of code here

