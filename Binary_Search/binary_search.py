# https://stackoverflow.com/questions/17141979/round-a-floating-point-number-down-to-the-nearest-integer

import math

def binary_search(sorted_list, target_value, verbose):
    """
    Performs a binary search.
    Binary search should be O(log n) for time and O(1) for space.

    Args:
        sorted_list: a sorted list to be searched.
        target_value: the target value to be found.
        verbose: Bool - if true, then print workings of search to console

    Returns:
        The index of the target_value in the sorted_list,
            or None if the target_value is not in the list

    Raises:
        IndexError: if passed an empty list
    """

    index_of_start_of_search_area = 0
    index_of_end_of_search_area = len(sorted_list) - 1

    if verbose:
        print("***** Starting a binary search")

    while True:
        if verbose:
            print("*** Start of loop")
            print("Start index:", index_of_start_of_search_area)
            print("End index", index_of_end_of_search_area)

        middle_index = math.floor(index_of_start_of_search_area + (
            (index_of_end_of_search_area - index_of_start_of_search_area) / 2))

        middle_value = sorted_list[middle_index]

        if verbose:
            print("Middle_index:", middle_index)
            print("Middle_value:", middle_value)

        if middle_value == target_value: 
            if verbose:
                print("Found it")
            return middle_index

        if middle_value > target_value: 
            if verbose:
                print("Target_value may be in the first half of the list")
            index_of_end_of_search_area = middle_index

        if middle_value < target_value: 
            if verbose:
                print("Target_value may be in the second half of the list")
            index_of_start_of_search_area = middle_index + 1

        if index_of_start_of_search_area > index_of_end_of_search_area:
            if verbose:
                print("Target value is not here")
            return None
