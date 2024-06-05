def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # Initialize count to keep track of parentheses balance
    count = 0

    # Iterate through each character in the string
    for p in parens:
        # If the character is an opening parenthesis, increment count
        if p == '(':
            count += 1
        # If the character is a closing parenthesis, decrement count
        elif p == ')':
            count -= 1

        # If the count becomes negative, there are too many closing parens, return False
        if count < 0:
            return False

    # If the count is zero, it means all parentheses were balanced
    return count == 0
