#!/usr/bin/python3
def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    x = len(list_of_integers)
    left = 0
    right = x - 1
    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and (
                mid == x - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return mid
        if mid == 0 or list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1
