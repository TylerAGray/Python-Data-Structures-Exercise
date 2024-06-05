def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
def flip_case(phrase, to_swap):
    to_swap = to_swap.lower()  # Convert the target character to lowercase to make the comparison case-insensitive
    out = ""  # Initialize an empty string to store the output

    for ltr in phrase:  # Iterate through each character in the input phrase
        if ltr.lower() == to_swap:  # Check if the lowercase version of the current character matches the lowercase target character
            ltr = ltr.swapcase()  # If so, swap the case of the current character
        out += ltr  # Append the current character (either original or swapped) to the output string

    return out  # Return the final output string
