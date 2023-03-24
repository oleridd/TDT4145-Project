import numpy as np


def get_smallest_elem_without_successor(arr: np.ndarray) -> int:
    """
    Given a numpy array of integers, returns the smallest element
    in the array which does not have a successor.
    If array is empty, returns 0.
    """

    if len(arr > 0):

        arr.sort()
        indicator = np.append(
            np.invert(arr[:-1] == (arr-1)[1:]), # Indexes elements without successors (except the last)
            [True]                              # Last element will never have a successor
        )
        return int(arr[indicator].min())
    
    return 0 # Array is empty


def is_member_of(arr: np.ndarray, lst: list) -> np.ndarray:
    """
    Iterates each element of arr and checks whether it is
    an element of lst. Returns the result as a boolean array.
    """
    arr = arr.flatten()
    result = np.zeros(len(arr), dtype=bool)
    for i, elem in enumerate(arr):
        result[i] = elem in lst
    return result


def list_in(lst: list, arr:np.ndarray) -> bool:
    """
    Given a size n list and a (mxn) array, checks whether the
    list is a member of arr.
    """
    for l in arr:
        if lst == list(l):
            return True
    return False