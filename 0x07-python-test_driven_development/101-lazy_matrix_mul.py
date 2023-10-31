#!/usr/bin/python3
"""module multiplying two matrices using numpy
"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
        function performing matrix multiplication

        Args:
            m_a: first matrix
            m_b: second matrix

        Return:
            matrix product of m_a and m_b
    """
    return np.dot(m_a, m_b)
