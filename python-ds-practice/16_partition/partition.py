def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    # Initialize two lists to store items that passed and failed the predicate test
    true_list = []
    false_list = []

    # Iterate through each item in the input list
    for val in lst:
        # Check if the item passed the predicate test
        if fn(val):
            true_list.append(val)  # If so, add it to the true_list
        else:
            false_list.append(val)  # If not, add it to the false_list

    # Return a list containing the true_list and false_list
    return [true_list, false_list]
