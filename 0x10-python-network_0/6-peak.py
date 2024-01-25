#!/usr/bin/python3
""" Find a peak module"""


def find_peak(list_of_integers):
    """function that finds the peak in a list of numbers"""
    max_ = None
    for i in range(len(list_of_integers) - 1):
        j = i + 1
        max_ = list_of_integers[i]
        if list_of_integers[j] > list_of_integers[i]:
            max_ = list_of_integers[j]
    return max_
