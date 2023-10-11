#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    great = 0
    for value in a_dictionary.values():
        if value > great:
            great = value
    for key,value in a_dictionary.items():
        if value == great:
            return key
