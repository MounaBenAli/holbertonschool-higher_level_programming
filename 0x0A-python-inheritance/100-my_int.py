#!/usr/bin/python3


class MyInt(int):
    """The inheritance from int class.
    MyInt has == and != operators inverted
    """
    def __eq__(self, other):
        """magic method __eq__"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """ Super Call to Equal """
        return not super().__ne__(other)
