#!/usr/bin/python3
""" Rotate a 2D matrix 90 degrees clockwise """


def rotate_2d_matrix(matrix):
    """ Rotate a 2D matrix 90 degrees clockwise """

    length = len(matrix)

    for i in range(length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
