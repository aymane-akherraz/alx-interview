#!/usr/bin/python3
""" Pascal Triangle Interview Challenge """


def pascal_triangle(n):
    """ Returns a list of lists of numbers representing the pascal triangle """
    if n <= 0:
        return []

    pl_triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pl_triangle[i - 1][j] + pl_triangle[i - 1][j - 1])
        pl_triangle.append(row)

    return pl_triangle
