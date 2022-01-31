#!/usr/bin/python3
"""Defines a direct/ indirect inheritance-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a given class
    Attributes:
    obj: the object to check.
    a_class: the class to check within for a match
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
