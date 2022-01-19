#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square

    Attributes: __size + __position
    """
    
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retreiver or getter property for __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """setter property for __size ."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """retreiver or getter property for __position."""
        return self.__position

    @position.setter
    def position(self, value):
        """setter property for __position."""
        
        if type(value) is not tuple:  
        
            raise TypeError("position must be a tuple of 2 positive integers")
        
        else:
            self.__position = position

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
        