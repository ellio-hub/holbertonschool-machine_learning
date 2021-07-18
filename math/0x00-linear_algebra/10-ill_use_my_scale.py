#!/usr/bin/env python3
"""
    10-ill_use_my_scale module
"""


def np_shape(matrix):
    """ function that calculates the shape of a numpy.ndarray

    Returns:
        [tuple]: shape of an array
    """
    a = []
    x = matrix
    a.append(x.size)
    
    while x.size > 0 or not isinstance(x[0], list):
        print(x[0])
        x = x[0]
        a.append(x.size)
    return tuple(a)
