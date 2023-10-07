#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ln = len(my_list)
    tmp = []
    for i in range(ln):
        tmp.append(my_list[i] % 2 == 0)
    return tmp
