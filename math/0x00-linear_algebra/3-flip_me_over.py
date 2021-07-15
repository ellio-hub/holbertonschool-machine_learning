#!/usr/bin/env python3

def matrix_transpose(matrix):
    """ function that returns the transpose of a 2D matrix

    Args:
        matrix (list): list of lists forming a 2 dimensional matrices

    Returns:
        [list]: transposed matix
    """    
    new = []
    i = 0
    for i in range(len(matrix[0])):
        j = 0
        w = []
        for j in range(len(matrix)):
            w.append(matrix[j][i])
        new.append(w)
    return new
