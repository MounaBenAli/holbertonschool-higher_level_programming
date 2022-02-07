#!/usr/bin/python3
"""Base Class Module."""


import json


class Base():
    """Define a base model.
    Represents the "base" for all other classes in this project.
    Attributes:
    __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize new Base
        Args :
        id(int) : The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        dict = []
        if list_objs is None:
            return dict
        with open(filename, "w") as f:
            json_rep = cls.to_json_string(dict)
            f.write(json_rep)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)
