def mode(nums):
    """Return most-common number in list along with its index.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

    >>> mode([1, 2, 1])
    (1, [0, 2])

    >>> mode([2, 2, 3, 3, 2])
    (2, [0, 1, 4])
    """
    # Make frequency counter of num:freq
    counts = {}

    # Iterate through each number in the input list
    for num in nums:
        # Increment the count for the current number in the dictionary
        counts[num] = counts.get(num, 0) + 1

    # find the highest value (the most frequent number)
    max_value = max(counts.values())

    # now we need to see at which index the highest value is at
    # Initialize an empty list to store indices of the mode value
    mode_indices = []

    # Iterate through each (num, freq) pair in the counts dictionary
    for (num, freq) in counts.items():
        # Check if the frequency equals the maximum value
        if freq == max_value:
            # If so, append the index of the current number to the mode_indices list
            mode_indices.append(num)

    # Return the mode value along with its indices
    return max_value, mode_indices
