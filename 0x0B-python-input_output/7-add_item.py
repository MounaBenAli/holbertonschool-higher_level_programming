#!/usr/bin/python3
"""Load Add Save Module"""

import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
args = sys.argv[1:]

if __name__ == '__main__':
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)
