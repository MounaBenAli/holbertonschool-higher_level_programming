#!/usr/bin/python3
"""
 takes in my GitHub credentials (username and password)
 and uses the GitHub API to display my id
"""

import requests
from sys import argv

if __name__ == "__main__":

    api_url = "https://api.github.com/users/"
    response = requests.get(api_url, auth=(argv[1], argv[2]))
    data = response.json()
    try:
        print(data.get("id"))
    except Exception:
        print(None)
