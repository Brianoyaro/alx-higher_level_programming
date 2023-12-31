#!/usr/bin/python3
"""rectangle class module
"""
import models.base as base


class Rectangle(base.Base):
    """rectangle class which inherits from Base
    """
    filename_json = 'Rectangle.json'
    filename_csv = 'Rectangle.csv'

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
                    self.width = val
                elif i == 2:
                    self.height = val
                elif i == 3:
                    self.x = val
                elif i == 4:
                    self.y = val
        else:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                elif key == 'width':
                    self.width = val
                elif key == 'height':
                    self.height = val
                elif key == 'x':
                    self.x = val
                elif key == 'y':
                    self.y = val

    def to_dictionary(self):
        """returns dictionary representation of Rectangle instance
        """
        dict_temp = {}
        dict_temp['x'] = self.__x
        dict_temp['y'] = self.__y
        dict_temp['id'] = self.id
        dict_temp['height'] = self.__height
        dict_temp['width'] = self.__width
        return dict_temp

    def to_dictionary_csv(self):
        """returns the csv dictionary representation
        """
        dict_temp = {}
        dict_temp['id'] = self.id
        dict_temp['width'] = self.__width
        dict_temp['height'] = self.__height
        dict_temp['x'] = self.__x
        dict_temp['y'] = self.__y
        return dict_temp
