#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = list(sorted([key for key in a_dictionary.keys()]))
    length = len(a_dictionary)
    for i in range(length):
        value = a_dictionary.get(sorted_list[i])
        print("{} : {}".format(sorted_list[i], value))
