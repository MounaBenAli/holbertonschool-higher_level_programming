#!/usr/bin/python3
"""
 takes in a letter
 and sends a POST request to http://0.0.0.0:5000/search_user
 with the letter as a parameter.
"""

import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    resp = requests.post(url='http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r = resp.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
