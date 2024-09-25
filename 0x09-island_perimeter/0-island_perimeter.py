#!/usr/bin/python3
""" island perimeter """


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid """

    p = 0
    row_len = len(grid)
    for i in range(row_len):
        col_len = len(grid[i])
        for j in range(col_len):
            if grid[i][j] == 1:
                p += 4
                if j > 0 and grid[i][j - 1] == 1:
                    p -= 2
                if i > 0 and grid[i - 1][j] == 1:
                    p -= 2
    return p
