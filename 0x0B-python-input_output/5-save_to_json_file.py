#!/usr/bin/python3
"""Saving Object to json file"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation"""

    with open(filename, "w") as f:
        json_rep = json.dumps(my_obj)
        f.write(json_rep)
