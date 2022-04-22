#!/usr/bin/python3
"""
takes in a URL,
sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response."""

import urllib.request as req
from sys import argv


if __name__ == "__main__":

    with req.urlopen(argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
