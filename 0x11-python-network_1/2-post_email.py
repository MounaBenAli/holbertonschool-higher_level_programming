#!/usr/bin/python3
"""
takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

from urllib import request, parse
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email}).encode()
    # this will make the method "POST"
    req = request.Request(url=url, data=data)

    with request.urlopen(req) as f:
        print(f.read().decode('utf-8'))
