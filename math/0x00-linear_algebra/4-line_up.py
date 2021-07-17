#!/usr/bin/env python3
"""
    4-line_up module
"""


def add_arrays(arr1, arr2):
    """ function that adds two arrays element-wise

    Args:
        arr1 (list): list of integers or floats
        arr2 (list): list of integers or floats

    Returns:
        [list]: list of the sum of elemnts of 2 arrays
    """
    if len(arr1) != len(arr2):
        return None
    new = []
    for i in range(len(arr1)):
        new.append(arr1[i] + arr2[i])
    return new
