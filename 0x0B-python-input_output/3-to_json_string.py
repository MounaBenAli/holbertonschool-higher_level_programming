#!/usr/bin/python3
""" Object To JSON Representation Module """


import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object(str)"""

    # Serializing
    return json.dumps(my_obj)
