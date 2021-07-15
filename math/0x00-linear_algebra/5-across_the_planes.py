#!/usr/bin/env python3
def add_matrices2D(mat1, mat2):
    """ function that adds two matrices element-wise

    Args:
        mat1 (list): 2D matrices containing ints/floats
        mat2 (list): 2D matrices containing ints/floats

    Returns:
        list: the sum of 2 matrices
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    new = []
    for i in range(len(mat1)):
        x = []
        for j in range(len(mat1[0])):
            x.append(mat1[i][j] + mat2[i][j])
        new.append(x)
    return new
