#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class handling unit testing of module max_integer"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1,2,3,4]), 4)
        self.assertEqual(max_integer([1,1,1,1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1,2,4,2,6,9,9,6]), 9)
        self.assertEqual(max_integer(["1","2","3"]), '3')
        self.assertEqual(max_integer(["a", "b", "c"]), 'c')
        self.assertEqual(max_integer(["ana", "anb", "anc"]), 'anc')

