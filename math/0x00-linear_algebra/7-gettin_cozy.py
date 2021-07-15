#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    new = mat1.copy()
    if axis == 1:
        for i in range(len(mat2)):
            new[i].extend(mat2[i])
    else:
        new.extend(mat2)
    return new
