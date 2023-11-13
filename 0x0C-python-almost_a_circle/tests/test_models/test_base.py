#!/usr/bin/python3
"""test module for Base class
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestBase(unittest.TestCase):
    """class containing test cases
    """
    def test_base_id(self):
        """tests base id instance.
        """
        b1 = Base()
        b2 = Base(90)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 90)
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        """tests the to_json_string method
        """
        r1 = Rectangle(1, 1, 1, 1, 1)
        temp_val = r1.to_dictionary()
        val = Base.to_json_string(temp_val)
        ans = '{"x": 1, "y": 1, "id": 1, "height": 1, "width": 1}'
        self.assertEqual(val, ans)

        r2 = Square(2, 2, 2, 2)
        temp_val = r2.to_dictionary()
        val = Square.to_json_string(temp_val)
        self.assertEqual(val, '{"id": 2, "x": 2, "size": 2, "y": 2}')

        self.assertEqual(Square.to_json_string(None), '[]')

    def test_from_json_string(self):
        """tests the from_json_string method
        """
        r1 = Rectangle(1, 1, 1, 1, 1)
        temp_val = Base.to_json_string(r1.to_dictionary())
        val = r1.from_json_string(temp_val)
        ans = {"x": 1, "y": 1, "id": 1, "height": 1, "width": 1}
        self.assertEqual(val, ans)

        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string('[]'), [])

    def test_create(self):
        """tests the create method
        """
        r1 = Square(2, 2, 2, 2)
        r1_dictionary = r1.to_dictionary()
        val = Square.create(**r1_dictionary)
        self.assertEqual(val.id, 2)

    def test_load_from_file_csv(self):
        """tests the load_from_file_csv method
        """
        r1 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file_csv([r1])
        val = Rectangle.load_from_file_csv()
        self.assertEqual(val[0].id, 1)

    def test_load_from_file(self):
        """test the load_from_file method
        """
        r1 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([r1])
        val = Rectangle.load_from_file()
        self.assertEqual(val[0].id, 1)

    def test_save_to_file(self):
        """tests the save_to_file method
        """
        r1 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([r1])
        with open('Rectangle.json', mode='r', encoding='utf-8') as f:
            temp = f.read()
        ans = '[{"x": 1, "y": 1, "id": 1, "height": 1, "width": 1}]'
        self.assertEqual(temp, ans)

    def test_save_to_file_csv(self):
        """tests the save_to_file_csv method
        """
        r1 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file_csv([r1])
        with open('Rectangle.csv', mode='r', encoding='utf-8') as f:
            temp = f.read()
        ans = '[{"id": 1, "width": 1, "height": 1, "x": 1, "y": 1}]'
        self.assertEqual(temp, ans)
