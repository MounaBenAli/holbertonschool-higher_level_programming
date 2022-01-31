#!/usr/bin/python3


class MyInt(int):
    """The inheritance from int class.
    MyInt has == and != operators inverted
    """

    def __eq__(self, other):
        """eq magic method"""
        if isinstance(other, MyInt):
            return False

    def __ne__(self, other):
        """ne magic method"""
        if isinstance(other, MyInt):
            return True