#!/usr/bin/env python3
"""
    7-getting_cozy
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """function that concatenates two matrices along a specific axis

    Returns:
        [list]: concatinated matrices
    """
    if axis == 0 and len(mat1) != len(mat2[0]):
        return None
    if axis == 1 and len(mat1) != len(mat2):
        return None
    for i in range(len(mat1)):
        if len(mat1[i]) == 0:
            return None
    new = mat1.copy()
    if axis == 1:
        for i in range(len(mat2)):
            new[i].extend(mat2[i])
    else:
        new.extend(mat2)
    return new
