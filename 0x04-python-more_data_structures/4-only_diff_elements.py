#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    inter = set_1.intersection(set_2)
    union = set.union(set_1, set_2)
    new = union - inter
    return new
