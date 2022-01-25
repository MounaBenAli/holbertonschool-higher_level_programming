#!/usr/bin/python3
"""
The matrix_divided module.
With function matrix_divided().
"""

def matrix_divided(matrix, div):
    """
    checks if paramater matrix is a list of int or float
    checks if each row of the matrix is the same size
    checks if div is an int or a float and not zero
    returns a new matrix divided by div
    """
    e1 ='matrix must be a matrix (list of lists) of integers/floats'
    e2 = 'Each row of the matrix must have the same size'
    e3 = 'div must be a number'
    e4 = 'division by zero'

    if not matrix:
        raise TypeError(e1)
    if not isinstance(matrix, list):
        raise TypeError(e1)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(e1)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(e1)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(e1)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(e3)
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError(e2)
    if div == 0:
        raise ZeroDivisionError(e4)
    return [[round(item / div, 2) for item in lists] for lists in matrix]
