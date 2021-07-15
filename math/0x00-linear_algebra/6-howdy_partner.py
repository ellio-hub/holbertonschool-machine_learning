#!/usr/bin/env python3
def cat_arrays(arr1, arr2):
    """function that concatenates two arrays

    Args:
        arr1 ([list]): lists of ints/floats
        arr2 ([list]): lists of ints/floats

    Returns:
        [list]: the concatenation of 2 arrays
    """
    new = []
    new.extend(arr1)
    new.extend(arr2)
    return new
