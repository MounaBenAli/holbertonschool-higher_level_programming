#!/usr/bin/python3
"""Create an Object from "JSON file" Module"""


import json


def load_from_json_file(filename):
    """creates and Object from a "JSON file"."""

    with open(filename, "r") as f:
        content = f.read()
        return json.loads(content)
