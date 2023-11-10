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

    def update(self,*args, **kwargs):
        """reassigns attributes to an instance
        """
        if args and len(args) > 0:
            for i, val in enumerate(args):
                if i == 0:
                    self.id = val
                elif i == 1:
                    self.width = val
                    self.height = val
                elif i == 2:
                    self.x = val
                elif i == 3:
                    self.y = val

        else:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                elif key == 'size':
                    self.width = val
                    self.height = val
                elif key == 'x':
                    self.x = val
                elif key == 'y':
                    self.y = val

    def to_dictionary(self):
        """returns a dictionary of Square instance
        """
        #return self.__dict__
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
