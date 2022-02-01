#!/usr/bin/python3
""" Write file Module"""


def write_file(filename="", text=""):
    """writes a string in file and returns the number of chars written"""

    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
