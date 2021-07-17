#!/usr/bin/env python3
"""
    2-size_me_please module
"""


def matrix_shape(matrix):
    """ matrix_shape(matrix):
        function that calculates the shape of a matrix

    Args:
        matrix (list): list of lists forming a mono
        or multi-dimensional matrices

    Returns:
        [list]: list of integers defining the shape of a matrix
    """
    a = []
    x = matrix
    a.append(len(x))
    while isinstance(x[0], list):
        x = x[0]
        a.append(len(x))
    return a
