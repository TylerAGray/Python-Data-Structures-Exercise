def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

    >>> two_oldest_ages([1, 2, 10, 8])
    (8, 10)

    >>> two_oldest_ages([6, 1, 9, 10, 4])
    (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

    >>> two_oldest_ages([1, 5, 5, 2])
    (2, 5)
    """

    # Convert the list of ages into a set to get unique ages
    uniq_ages = set(ages)
    
    # Sort the unique ages and select the last two elements
    oldest = sorted(uniq_ages)[-2:]
    
    # Return a tuple containing the second-oldest and oldest ages
    return tuple(oldest)
