#!/usr/bin/python3
"""module that multiplies two matrices
"""
def matrix_mul(m_a, m_b):
    """
        function that multiplies two matrices

        Args:
            m_a: first matrix
            m_b: second matrix

        Return:
            matrix composed of m_a * m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    elif not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")
    elif len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for i in range(len(m_a)):
        for j in range(len(m_a[0])):
            if not (isinstance(m_a[i][j], int) or isinstance(m_a[i][j], float)):
                raise TypeError("m_a should contain only integers or floats")
    for i in range(len(m_b)):
        for j in range(len(m_b[0])):
            if not (isinstance(m_b[i][j], int) or isinstance(m_b[i][j], float)):
                raise TypeError("m_b should contain only integers or floats")
    for i in range(len(m_a)):
        if len(m_a[i]) != len(m_a[0]):
                raise TypeError("each row of m_a must be of the same size")
    for i in range(len(m_b)):
        if len(m_b[i]) != len(m_b[0]):
                raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    ls = [[sum(a * b for a, b in zip(x_row, y_col)) for y_col in zip(*m_b)] for x_row in m_a]
    return ls
