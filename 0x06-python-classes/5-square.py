#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square

    Attributes: __size
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """retreiver or getter property."""
        return self.__size

    @size.setter
    def size(self, value):
        """setter property."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """square area"""
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print()

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
