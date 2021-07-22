#!/usr/bin/env python3
"""
    10-matisse
"""


def poly_derivative(poly):
    """
        function that calculates the derivative of a polynomial
    """
    if type(poly) != list or len(poly) == 0:
        return None
    x = []
    for i in range(1, len(poly)):
        if type(poly[i]) != int:
            return None
        x.append(poly[i] * i)
    if len(x) == 0:
        x.append(0)
    return x
