#!/usr/bin/python3
for alpha in range(ord('a'), ord('z')+1):
    letter = chr(alpha)
    if letter not in "qe":
        print(letter, end="")
