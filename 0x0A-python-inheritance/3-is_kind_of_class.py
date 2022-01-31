#!/usr/bin/python3
"""Defines a class-checking and inheritance-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class.
    Checks if an object is an inheritance of a given class
    Attributes:
    obj: the object to check.
    a_class: the class to check within for a match
    """
    if isinstance(obj, a_class):
        return True
    return False
