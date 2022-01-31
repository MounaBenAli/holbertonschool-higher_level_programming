#!/usr/bin/python3


class MyInt(int):
    """The inheritance from int class.
    MyInt has == and != operators inverted
    """

    def negation_of_equals(inst1, inst2):
        """always should return same as not_equals(inst1, inst2)"""
        return not inst1 == inst2

    def not_equals(inst1, inst2):
        """always should return same as negation_of_equals(inst1, inst2)"""
        return inst1 != inst2
