#!/usr/bin/env python3
"""
    10-matisse
"""


def poly_derivative(poly):
    """
        function that calculates the derivative of a polynomial
    """
    if type(poly) != list:
        return None
    x = []
    for i in range(1, len(poly)):
        if type(poly[i]) != int:
            return None
        x.append(poly[i] * i)
    return x
