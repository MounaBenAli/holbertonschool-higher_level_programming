#!/usr/bin/python3

"""Define a derived class Rectangle from the base BaseGeomtry."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square with multiple inheritance from class Rectangle
    Attributes:
        square: must be a positive int , Square's size
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Define area Rectangle"""
        return(self.__size * self.__size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
