#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class.
    Attributes:
    obj: the object to check.
    a_class: the class to check within for a match
    """
    if type(obj) == a_class:
        return True
    return False
