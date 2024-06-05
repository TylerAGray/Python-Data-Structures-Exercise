def remove_every_other(lst):
    """Return a new list of other item.

    >>> lst = [1, 2, 3, 4, 5]

    >>> remove_every_other(lst)
    [1, 3, 5]

    This should return a list, not mutate the original:

    >>> lst
    [1, 2, 3, 4, 5]
    """
    # Use list slicing to return every other item starting from index 0
    return lst[::2]
