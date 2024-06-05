def sum_floats(nums):
    """Return sum of floating point numbers in nums.

        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9

        >>> sum_floats([1, 2, 3])
        0
    """
# Use a list comprehension to iterate through each element in the input list `nums`
# Check if each element is a float using `isinstance`
# Only include the element in the list if it's a float
# Use `sum()` to calculate the sum of all the floating-point numbers in the list

    return sum([num for num in nums if isinstance(num, float)])
