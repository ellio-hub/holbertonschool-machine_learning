#!/usr/bin/env python3
"""
    8-ridin_bareback module
"""


def mat_mul(mat1, mat2):
    """ function that performs matrix multiplication

    Returns:
        [list]: multiplied matrices
    """
    if len(mat1[0]) != len(mat2):
        return None
    new = []
    for i in range(len(mat1)):
        new.append([])
        for j in range(len(mat2[0])):
            d = 0
            for x in range(len(mat1[0])):
                d = d + (mat1[i][x] * mat2[x][j])
            new[i].append(d)
    return new
