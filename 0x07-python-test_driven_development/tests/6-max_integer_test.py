#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_non_integer(self):
        """tests non integer list arguments
        """
        self.assertEqual(max_integer(['a','b','c','d']), 'd')
        self.assertEqual(max_integer(['ana', 'anb', 'anc']), 'anc')
        self.assertEqual(max_integer(['1', '2', '3']), '3')

    def test_empty(self):
        """tests an empty argument to function
        """
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

    def test_integer(self):
        """tests several variation of integer list argument
        """
        self.assertEqual(max_integer([1,1,1,1,1]), 1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([9, 2, 5, 9, 2]), 9)
        self.assertEqual(max_integer([9, 8, 7, 6, 5, 4, 3, 2, 1]), 9)
