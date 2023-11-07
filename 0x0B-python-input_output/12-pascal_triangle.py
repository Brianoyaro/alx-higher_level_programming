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
    

