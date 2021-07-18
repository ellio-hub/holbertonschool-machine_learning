#!/usr/bin/env python3
"""
    7-getting_cozy
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """function that concatenates two matrices along a specific axis

    Returns:
        [list]: concatinated matrices
    """
    for i in range(len(mat1)):
        if mat1[i] == []:
            return None
    new = mat1.copy()
    if axis == 1:
        for i in range(len(mat2)):
            if mat2[i] == []:
                return None
            new[i].extend(mat2[i])
    else:
        new.extend(mat2)
    return new
