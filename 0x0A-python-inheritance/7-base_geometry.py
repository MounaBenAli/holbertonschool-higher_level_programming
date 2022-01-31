#!/usr/bin/python3
"""Define a base geomtry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value type int
        Attributes:
        name: is always a string
        value: the int to be validated 
        """

        if type(value) is not int: 
            raise TypeError ('{} must be an integer'.format(name))
        else:
            self.__value = value
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
