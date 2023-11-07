#!/usr/bin/python3
"""pascal triangle technical interview question
"""


def pascal_triangle(n):
    """returns a list of lists of integers\
            representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [[1],[1, 1]]
    else:
        final_list = [[1], [1, 1]]
        lis = [1, 1]
        for y in range(n - 2):
            new = [1]
            for i in range(len(lis) - 1):
                left = les[i]
                right = lis[i + 1]
                new.append(left + right)
            new.append(1)
            lis = new
            final_list.append(lis)
        return final_list

