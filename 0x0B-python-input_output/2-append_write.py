#!/usr/bin/python3
""" Append file Module"""


def append_write(filename="", text=""):
    """ appends a string at the end of file returns num of chars appended"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
