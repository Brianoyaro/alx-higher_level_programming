#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    val = 0
    for i in range(x):
        try:
            my_list[i] / 1
            print("{:d}".format(my_list[i]), end='')
            val += 1
        except TypeError:
            pass
    print()
    return val
