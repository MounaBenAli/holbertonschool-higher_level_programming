#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastDigit = number % -10
else:
    lastDigit = number % 10

str = ('Last digit of {:d}'.format(number))
str1 = ('is {:d}'.format(lastDigit))
str += (" " + str1)

if lastDigit > 5:
    print(str + (' and is greater than 5 '))
elif lastDigit == 0:
    print(str + ' and is 0')
elif lastDigit < 6:
    print(str + ' and is less than 6 and not 0')
