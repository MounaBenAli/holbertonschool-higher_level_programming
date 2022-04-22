#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":

    response = requests.request(method='GET',
                                url='https://intranet.hbtn.io/status')
    html = str(requests.models.Response)
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(response.text))
