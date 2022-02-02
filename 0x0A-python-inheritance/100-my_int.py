#!/usr/bin/python3
class MyInt(int):
    """The inheritance from int class.
    MyInt has == and != operators inverted
    """


class MyInt(int):
    """Define a MyInt."""

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
