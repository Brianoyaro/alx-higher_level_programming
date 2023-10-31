#!/usr/bin/python3
"""module handling matrix division
"""


def matrix_divided(matrix, div):
    """
        function handling matrix division
        Args:
            matrix: matrix to divide
            div(int/float): divisor

        Return:
            matrix whose elements have been divided by div
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not (isinstance(matrix[i][j], int) or isinstance(matrix[i][j], float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    ls = [[round((matrix[x][y] / div), 2) for y in range(len(matrix[x]))] for x in range(len(matrix))]
    return ls
