#!/usr/bin/python3
"""Define a class Rectangle ."""


class Rectangle:
    """Represents a square

    Attributes: __width + __height
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """retreiver or getter property for __height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter property for __height."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        else:
            self.__height = value
        if value < 0:
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        """retreiver or getter property for __width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter property for __width."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        else:
            self.__width = value
        if value < 0:
            raise ValueError('width must be >= 0')

    def area(self):
        """rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
