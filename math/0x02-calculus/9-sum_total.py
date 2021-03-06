#!/usr/bin/env python3
"""
    9-sum_total module
"""


def summation_i_squared(n):
    """
        function that calculated sum of an int
    """
    if type(n) != int or n < 1:
        return None
    return int((n * (n + 1) * (2 * n + 1)) / 6)
