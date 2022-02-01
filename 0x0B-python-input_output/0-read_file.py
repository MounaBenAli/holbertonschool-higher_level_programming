#!/usr/bin/python3
""" Read file Module"""


def read_file(filename=""):
    """reads a test file and prints to stdout"""

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
