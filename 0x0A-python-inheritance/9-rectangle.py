#!/usr/bin/python3
"""Define a derived class Rectangle from the base BaseGeomtry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle derived from BaseGeomtry class.
    Attributes:
        width: must be an int , Rectangle's width
        height: must be an int , Rectangle's height
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Define area Rectangle"""
        return(self.__height * self.__width)

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
