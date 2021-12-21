#!/usr/bin/python3
for number in range(0, 100):
    if number < 10:
        print(str(number).zfill(2), end=', ')
    else:
        print(number, end=', ')
