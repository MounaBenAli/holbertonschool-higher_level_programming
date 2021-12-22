#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        x = i - 32
    else:
        x = i
    print("{:c}".format(x), end="")
