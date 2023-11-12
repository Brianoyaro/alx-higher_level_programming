#!/usr/bin/python3
"""test module for Rectangle class
"""
from models.square import Square
import unittest


class TectRectangle(unittest.TestCase):
    """class that contains test cases for Rectangle
    """
    def test_width_gettter(self):
        """tests the getter of width
        """
        r1 = Square(5)
        r2 = Square(10, 10, 10, 10)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r2.width, 10)

    def test_height_getter(self):
        """tests the getter of height
        """
        r1 = Square(13)
        r2 = Square(10, 10, 10, 10)
        self.assertEqual(r1.height, 13)
        self.assertEqual(r2.height, 10)

    def test_x_getter(self):
        """tests the getter of x
        """
        r1 = Square(1, 2)
        r2 = Square(10, 10, 10, 10)
        r3 = Square(8)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r2.x, 10)

    def test_y_getter(self):
        """tests the getter of y
        """
        r1 = Square(1)
        r2 = Square(10, 10, 10, 10)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 10)

    def test_width_setter(self):
        """tests the width setter method
        """
        r1 = Square(1)
        self.assertEqual(r1.width, 1)
        with self.assertRaises(TypeError):
            r1.width = 'h'
        r1.width = 75
        self.assertEqual(r1.width, 75)
        with self.assertRaises(ValueError):
            r1.width = 0

    def test_height_setter(self):
        """tests the height setter method
        """
        r1 = Square(2)
        self.assertEqual(r1.height, 2)
        r1.height = 13
        self.assertEqual(r1.height, 13)
        with self.assertRaises(TypeError):
            r1.height = 'brian'
        with self.assertRaises(ValueError):
            r1.height = -127

    def test_x_setter(self):
        """tests the seeter method of x
        """
        r1 = Square(1)
        self.assertEqual(r1.x, 0)
        r1.x = 99
        self.assertEqual(r1.x, 99)
        with self.assertRaises(TypeError):
            r1.x = 's'
        r1.x = 5
        self.assertEqual(r1.x, 5)
        with self.assertRaises(ValueError):
            r1.x = -1

    def test_y_setter(self):
        """tests the setter method for y attribute
        """
        r1 = Square(1, 2, 3, 4)
        self.assertEqual(r1.y, 3)
        r1.y = 7
        self.assertEqual(r1.y, 7)
        with self.assertRaises(TypeError):
            r1.y = 't'
        with self.assertRaises(ValueError):
            r1.y = -9

    def test_id_setter(self):
        """tests the setter method for id attribute
        """
        r1 = Square(1)
        r1.id = 80
        self.assertEqual(r1.id, 80)
        r1.id = 9
        self.assertEqual(r1.id, 9)

    def test_area(self):
        """tests area method
        """
        r1 = Square(10)
        self.assertEqual(r1.area(), 100)
        with self.assertRaises(TypeError):
            r2 = Square('h')
        with self.assertRaises(ValueError):
            r2 = Square(-9)

    def test_update_args(self):
        """tests update method with args as parameter
        """
        r1 = Square(1, 1, 1, 1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)

        arguments = (5, 12, 21, 5)
        r1.update(*arguments)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.x, 21)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 12)

        arguments2 = (1, '2', 2, 2)
        with self.assertRaises(TypeError):
            r1.update(*arguments2)

    def test_udate_kwargs(self):
        """tests update method with **kwargs as parameter
        """
        r1 = Square(7)

        r1.update(size=9, id=6, x=1, y=2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.width, 9)
        self.assertEqual(r1.height, 9)
        self.assertEqual(r1.id, 6)

        update = {'size': 'h', 'id': 5}
        with self.assertRaises(TypeError):
            r1.update(**update)

    def test_to_dictionary(self):
        """tests the to_dictionary method
        """
        r1 = Square(1, 4, 6, 5)
        val = r1.to_dictionary()
        self.assertEqual(val, {'id': 5, 'x': 4, 'size': 1, 'y': 6})
