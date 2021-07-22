#!/usr/bin/env python3
"""
    17-integrate module
"""


def poly_integral(poly, C=0):
    """
        function that calculates the integral of a polynomial
    """
    if type(poly) != list or len(poly) == 0 or type(C) != int:
        return None
    x = []
    x.append(C)
    if len(poly) ==1 and poly[0] == 0:
        return x
    for i in range(len(poly)):
        if type(poly[i]) != int:
            return None
        if (poly[i] / (i + 1)) % 1 == 0:
            x.append(int(poly[i] / (i + 1)))
        else:
            x.append(poly[i] / (i + 1))
    return x
