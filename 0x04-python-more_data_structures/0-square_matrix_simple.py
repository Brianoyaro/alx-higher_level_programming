#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    column = len(matrix[0])
    row = len(matrix)
    return [[matrix[i][j] ** 2 for j in range(column)] for i in range(row)]
