#!/usr/bin/python3
def weight_average(my_list=[]):
    length = len(my_list)
    if length == 0:
        return 0
    sum1 = 0
    sum2 = 0
    for i in range(length):
        v = my_list[i]
        temp = v[0] * v[1]
        sum1 += temp
        sum2 += v[1]
    return sum1 / sum2
