def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

    >>> vowel_count('rithm school')
    {'i': 1, 'o': 2}
        
    >>> vowel_count('HOW ARE YOU? i am great!') 
    {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # Set of vowels
    VOWELS = set('aeiouAEIOU')

    # Convert the phrase to lowercase to make the comparison case-insensitive
    phrase = phrase.lower()

    # Initialize an empty dictionary to store the count of each vowel
    counter = {}

    # Iterate through each character in the phrase
    for ltr in phrase:
        # Check if the character is a vowel by checking if it's in the set of vowels
        if ltr in VOWELS:
            # If the vowel is already in the dictionary, increment its count; otherwise, set its count to 1
            counter[ltr] = counter.get(ltr, 0) + 1

    # Return the dictionary containing the count of each vowel
    return counter
