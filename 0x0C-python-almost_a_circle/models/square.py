#!/usr/bin/python3
"""square module
"""
import models.rectangle as rectangle


class Square(rectangle.Rectangle):
    """square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a nice, printable form of square instance
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """size getter method
        """
        return self.width

    @size.setter
    def size(self, val):
        """size setter method
        """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        else:
            if (val <= 0):
                raise ValueError("width must be > 0")
            else:
                self.width = val
                self.height = val
