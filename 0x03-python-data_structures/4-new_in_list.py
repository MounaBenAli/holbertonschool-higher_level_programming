#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx >= 0 and idx < len(copy):
        copy[idx] = element
    return copy
