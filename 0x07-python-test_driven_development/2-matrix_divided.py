#!/usr/bin/python3
"""Creating a function that divides elements of a matrix"""


def matrix_divided(matrix, div):
    """Takes a matrix and div as arguments
    
    Divides elements of a matrix

    Args:
        Matrix
        Div
    Returns:
        new matrix of divided elements
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(element, (float, int)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
