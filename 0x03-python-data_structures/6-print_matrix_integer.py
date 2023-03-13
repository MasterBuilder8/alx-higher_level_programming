#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 1
        length = len(row)

        for element in row:
            if i == length:
                print('{:d}'.format(element), end='')
            else:
                print('{:d}'.format(element), end='')
                i += 1

                print()
