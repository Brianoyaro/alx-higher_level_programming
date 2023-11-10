#!/usr/bin/python3
"""rectangle class module
"""
import models.base as base


class Rectangle(base.Base):
    """rectangle class which inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        else:
            if (width <= 0):
                raise ValueError("width must be > 0")
            else:
                self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        else:
            if (height <= 0):
                raise ValueError("height must be > 0")
            else:
                self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        else:
            if (x < 0):
                raise ValueError("x must be >= 0")
            else:
                self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        else:
            if (y < 0):
                raise ValueError("y must be >= 0")
            else:
                self.__y = y

    @property
    def width(self):
        """width getter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if (value <= 0):
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @property
    def height(self):
        """height property getter mothod
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if (value <= 0):
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    @property
    def x(self):
        """x getter method
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        else:
            if (value < 0):
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    @property
    def y(self):
        """y getter method
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        else:
            if (value < 0):
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        """area method. Returns with * height
        """
        return self.__width * self.__height

    def display(self):
        """prints Rectangle instance with #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print((' ' * self.__x), end='')
            print('#' * self.__width)

    def __str__(self):
        """returns a nicely printable string representing the instance
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if args and len(args) > 0:
            for i, val in enumerate(args):
                if i == 0:
                    self.id = val
                elif i == 1:
                    self.__width = val
                elif i == 2:
                    self.__height = val
                elif i == 3:
                    self.__x = val
                elif i == 4:
                    self.__y = val
        else:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                elif key == 'width':
                    self.__width = val
                elif key == 'height':
                    self.__height = val
                elif key == 'x':
                    self.__x = val
                elif key == 'y':
                    self.__y = val

    def to_dictionary(self):
        """returns dictionary representation of Rectangle instance
        """
        return self.__dict__
