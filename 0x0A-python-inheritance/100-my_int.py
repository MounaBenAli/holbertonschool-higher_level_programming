#!/usr/bin/python3
class MyInt(int):
    """The inheritance from int class.
    MyInt has == and != operators inverted
    """


class MyInt(int):
    """Define a MyInt."""

    def __eq__(self, other):
        """ Swaping behavior of `==` and `!=`"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ Swaping behavior of `==` and `!=`"""
        return super().__eq__(other)
