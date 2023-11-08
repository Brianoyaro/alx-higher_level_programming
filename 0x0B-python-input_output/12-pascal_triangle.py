#!/usr/bin/python3
"""pascal triangle technical interview question
"""


def pascal_triangle(n):
    """returns a list of lists of integers\
            representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = [1]
    ls = [1]
    for i in range(n - 1):
        temp = [1]
        for j in range(len(ls) - 1):
            left = ls[j]
            right = ls[j + 1]
            temp.append(right + left)

        temp.append(1)
        ls = temp.copy()
        triangle.append(temp)

    return triangle
