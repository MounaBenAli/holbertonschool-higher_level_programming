#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = 0
    y = 0
    for i in (tuple_a, tuple_b):
        if len(i) >= 2:
            x += i[0]
            y += i[1]
        elif len(i) == 1:
            x += i[0]
            y += 0
    return(x, y)
