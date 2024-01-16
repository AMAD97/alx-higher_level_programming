#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
    - matrix: List of lists containing integers or floats.
    - div: Number (integer or float) to divide each element of the matrix by.

    Returns:
    - New matrix with elements rounded to 2 decimal places after division.

    Raises:
    - TypeError: If matrix is not a list of lists of integers or floats.
                If each row of the matrix does not have the same size.
                If div is not a number (integer or float).
    - ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
result = matrix_divided(matrix, 3)
print(result)
