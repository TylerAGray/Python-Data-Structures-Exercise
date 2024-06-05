def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # Initialize total sum
    total = 0

    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the element from the TL-to-BR diagonal
        total += matrix[i][i]
        # Add the element from the BL-to-TR diagonal
        total += matrix[i][-1 - i]

    # Return the total sum of both diagonals
    return total
