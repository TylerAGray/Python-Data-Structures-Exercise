def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
    >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
    {'x': 9, 'y': 8, 'z': 7}
    
    If there are fewer values than keys, remaining keys should have value
    of None:
    
    >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
    {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

    >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
    {'a': 1, 'b': 2, 'c': 3}
    """
    # Create an empty dictionary to store key-value pairs
    result = {}

    # Iterate through keys and values and add them to the dictionary
    for i, key in enumerate(keys):
        # Check if there are values left to assign
        if i < len(values):
            # Assign the value to the corresponding key
            result[key] = values[i]
        else:
            # If there are no more values, assign None to the remaining keys
            result[key] = None

    return result
