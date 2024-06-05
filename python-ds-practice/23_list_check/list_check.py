def list_check(lst):
    """Are all items in lst a list?

    >>> list_check([[1], [2, 3]])
    True

    >>> list_check([[1], "nope"])
    False
    """
    # Check if all items in the list are lists using all() and isinstance()
    return all(isinstance(item, list) for item in lst)
