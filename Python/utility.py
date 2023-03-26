import numpy as np
from datetime import datetime


DATEMAP = {
    0 : "mandag" ,
    1 : "tirsdag",
    2 : "onsdag" ,
    3 : "torsdag",
    4 : "fredag" ,
    5 : "lørdag" ,
    6 : "søndag"
}

def try_parsing_date(text):
    """
    Retrieved from 
    https://stackoverflow.com/questions/23581128/how-to-format-date-string-via-multiple-formats-in-python 
    """
    for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError("Date input is invalid")


def get_weekday_from_date(date: str) -> str:
    """
    Given a date string, returns weekday (in Norwegian)
    """
    dt = try_parsing_date(date)
    weekday_nr = dt.isoweekday()
    return DATEMAP[weekday_nr-1]


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


def get_valid_input(input_prompt: str, error_message: str, input_transform = None, valid_inputs: list = None, invalid_inputs: list = None) -> str:
    """
    Ensures and returns valid input from user.
    Takes either valid inputs OR invalid inputs.

    Args:
        input_prompt       (string)
        error_message      (string)
        input_transform  (Callable): Potential transform of input
        valid_inputs (list or type)
        invalid      (list or type)
    Returns:
        input (string)
    """
    assert (valid_inputs is None) ^ (invalid_inputs is None)

    input_is_valid = False
    print(input_prompt)

    while not input_is_valid:

        user_in = input()
        if not input_transform is None:
            # try:
            user_in = input_transform(user_in)
            # except:
            #     print(error_message)
            #     continue
        
        # Checking instance:
        if isinstance(valid_inputs, type) or isinstance(invalid_inputs, type):
            if (valid_inputs is None and isinstance(user_in, invalid_inputs)) or (invalid_inputs is None and not isinstance(user_in, valid_inputs)):
                print(error_message)
            else:
                input_is_valid = True
        
        # Checking membership:
        else:
            if (valid_inputs is None and user_in in invalid_inputs) or (invalid_inputs is None and not user_in in valid_inputs):
                print(error_message)
            else:
                input_is_valid = True
        
    return user_in