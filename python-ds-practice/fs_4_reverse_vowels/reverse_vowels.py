def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in the string, but all
    vowels (y is not considered a vowel here) should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en A Streng'

    >>> reverse_vowels("aeiou")
    'uoiea'

    >>> reverse_vowels("why try, shy fly?")
    'why try, shy fly?'
    """
    # Set of vowels
    vowels = set("aeiouAEIOU")
    # Convert the string into a list so that it's mutable
    string = list(s)
    # Initialize two pointers, one from the beginning and one from the end
    i, j = 0, len(s) - 1

    # Continue until the pointers meet or cross each other
    while i < j:
        # If character at index i is not a vowel, move i pointer to the right
        if string[i].lower() not in vowels:
            i += 1
        # If character at index j is not a vowel, move j pointer to the left
        elif string[j].lower() not in vowels:
            j -= 1
        # If both characters are vowels, swap them and move pointers inward
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    # Convert the list back to a string
    return "".join(string)
