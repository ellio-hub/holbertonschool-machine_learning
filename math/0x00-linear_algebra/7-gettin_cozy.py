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
    new = []
    for i in range(len(mat1)):
        if len(mat1[i]) == 0:
            return None
        new.append(mat1[i])
    if axis == 1:
        for i in range(len(mat2)):
            for j in range(len(mat2[0])):
                new[i].append(mat2[i][j])
        print(hex(id(new)))
        print(hex(id(mat1)))
    else:
        new.extend(mat2)
    print(new)
    print(mat1)
    return new
