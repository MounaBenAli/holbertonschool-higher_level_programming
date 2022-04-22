#!/usr/bin/python3
"""
 that takes in a URL,
 sends a request to the URL
 and displays the body of the response (decoded in utf-8)."""

from urllib import request, parse
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf8', 'strict'))
    except HTTPError as err:
        print('Error code: {}'.format(err.code))
