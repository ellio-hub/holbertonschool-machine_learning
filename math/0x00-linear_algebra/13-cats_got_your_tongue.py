#!/usr/bin/env python3
"""
    13-cats_got_your_tongue
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
        function that concatenates two matrices
    """
    return np.concatenate((mat1, mat2), axis=axis)
