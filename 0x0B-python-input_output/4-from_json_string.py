#!/usr/bin/python3
""" Object From JSON Representation Module """


import json


def from_json_string(my_str):
    """ retuns an object  represented by a JSON string"""

    # Deserializing
    return json.loads(my_str)
