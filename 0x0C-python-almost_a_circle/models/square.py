#!/usr/bin/python3
"""Square Class module"""


from multiprocessing.sharedctypes import Value
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ for Square
        Attributes:
        size (int): The size of the new Square.
        y (int): The y coordinate of the new Square.
        id (int): The identity of the new Square.
        """
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, super().x, super().y, super().width)

    @property
    def size(self):
        """Square size getter"""
        return super().width

    @size.setter
    def size(self, size):
        """Square size setter"""
        self.width = size
        self.height = size
