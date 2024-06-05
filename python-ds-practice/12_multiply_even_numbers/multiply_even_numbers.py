def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
    >>> multiply_even_numbers([2, 3, 4, 5, 6])
    48
    
    >>> multiply_even_numbers([3, 4, 5])
    4
    
    If there are no even numbers, return 1.
    
    >>> multiply_even_numbers([1, 3, 5])
    1
    """
    product = 1  # Initialize the product to 1
    for num in nums:  # Iterate through each number in the list
        if num % 2 == 0:  # Check if the number is even
            product *= num  # Multiply the product by the even number
    return product if product != 1 else 1  # Return the product, or 1 if there are no even numbers
