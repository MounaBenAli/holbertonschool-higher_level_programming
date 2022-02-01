#!/usr/bin/python3
"""Student Module
"""


class Student:
    """Define Class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        for JSON serialization of an object.
        """
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for elements in attrs:
            if hasattr(self, elements):
                my_dict[elements] = getattr(self, elements)
        return my_dict

    def reload_from_json(self, json):
        """ replaces all attributes of Student"""
        self.__dict__.update(json)
