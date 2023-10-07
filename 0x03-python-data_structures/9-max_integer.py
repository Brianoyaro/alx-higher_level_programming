#!/usr/bin/python3
def max_integer(my_list=[]):
    great = 0
    ln = len(my_list)
    if (ln == 0):
        return None
    else:
        for i in range(ln):
            if (my_list[i] > great):
                great = my_list[i]
        return great
