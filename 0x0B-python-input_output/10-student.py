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
        if isinstance(attrs, str):
            return self.first_name
        return self.__dict__
