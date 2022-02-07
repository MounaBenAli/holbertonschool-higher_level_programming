#!/usr/bin/python3
"""Rectangle Class module"""

from models.base import Base


class Rectangle(Base):
    """Define class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ for Rectangle
        Attributes:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        x (int): The x coordinate of the new Rectangle.
        y (int): The y coordinate of the new Rectangle.
        id (int): The identity of the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Rectangle height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Rectangle Coordinate getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Rectangle Coordinate setter"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Rectangle Coordinate getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Rectangle Coordinate setter"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area of the Rectangle"""
        return self.height * self.width

    def display(self):
        """prints to stdout the Rectangle with `#` character"""
        lay_out = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(lay_out, end='')

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
