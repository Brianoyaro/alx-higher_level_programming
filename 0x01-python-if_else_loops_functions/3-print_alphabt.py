#!/usr/bin/python3
for letter in range(97, 123):
    latter = chr(letter)
    if latter not in "qe":
        print(latter, end = "")
