#!/usr/bin/python3
"""BaseGeometry module
"""


class BaseGeometry:
    """BaseGeometry class
    """
    def area(self):
        """raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        """
        if not isinstance(value, int):
            err1 = "{} must be an integer".format(name)
            raise TypeError(err1)

        if value <= 0:
            err2 = "{} must be greater than 0".format(name)
            raise ValueError(err2)
