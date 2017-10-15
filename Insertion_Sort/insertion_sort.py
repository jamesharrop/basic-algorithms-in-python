def insertion_sort(my_list):
    """
    Performs an insertion sort.

    Args:
        my_list: a list to be sorted.

    Returns:
        A sorted list

    Raises:
        TypeError: There are mixed types in the list which are not orderable
    """

    for location in range(1, len(my_list)): # Skip the first item - so range starts at 1

        current_item = my_list[location] # this is the first item which has not been sorted yet

        working_location = location

        # now work backwards through the sorted items to find the correct location
        # for the current_item

        for sorted_location in range(location - 1, -1, -1):

            compare_with = my_list[sorted_location]

            if current_item < compare_with:
                # then swap items at sorted_location and working_location
                my_list[sorted_location] = current_item
                my_list[working_location] = compare_with
                working_location -= 1
                # here we could print the list to show the progress so far
                # print(my_list)

    return my_list
