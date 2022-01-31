#!/usr/bin/python3
"""
This is the look up module.

This module contains the lookup function that returns a list object
"""


def lookup(obj):
    """
    returns a list that list of available attributes and method of an object
    """
    return (dir(obj))
