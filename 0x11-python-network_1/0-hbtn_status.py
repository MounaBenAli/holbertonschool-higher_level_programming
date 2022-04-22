#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""

import urllib.request as req


if __name__ == "__main__":

    url = 'https://intranet.hbtn.io/status'

    with req.urlopen(url) as response:
        body = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- conent: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode('UTF-8')))
