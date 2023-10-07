#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    ln1 = len(matrix)
    if (ln1 == 1):
        print()
    ln2 = len(matrix[0])
    for i in range(ln1):
        for j in range(ln2):
            length = ln2 - 1
            if (j < length):
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]))
