def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    # Generate a list of factors using list comprehension
    # Iterate from 1 to num // 2 (inclusive) and filter out numbers that evenly divide num
    n_list = [n for n in range(1, num // 2 + 1) if num % n == 0]

    # Append the given number 'num' itself to the list of factors
    n_list.append(num)

    # Return the list of factors
    return n_list
