def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    # Convert the list into a set to remove duplicates
    unique_nums = set()
    # Iterate through the list
    for num in nums:
        # If the current number is already in the set, it's a duplicate
        if num in unique_nums:
            return num
        # Otherwise, add it to the set
        else:
            unique_nums.add(num)
    # If no duplicates are found, return None
    return None

