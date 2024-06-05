def freq_counter(coll):
    """Returns frequency counter mapping of coll."""
    # Initialize an empty dictionary to store the frequencies of elements
    counts = {}
    # Iterate over each element in the collection
    for x in coll:
        # Update the count of the current element in the dictionary
        # If the element is not present, set its count to 1; otherwise, increment its count
        counts[x] = counts.get(x, 0) + 1
    # Return the frequency counter mapping
    return counts

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

    >>> same_frequency(551122, 221515)
    True

    >>> same_frequency(321142, 3212215)
    False

    >>> same_frequency(1212, 2211)
    True
    """
    # Convert both numbers to strings to treat each digit separately
    # Then, call freq_counter to get the frequency counter mapping for each number
    # Finally, check if the frequency counter mappings for both numbers are equal
    return freq_counter(str(num1)) == freq_counter(str(num2))
