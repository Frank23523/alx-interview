#!/usr/bin/python3
"""0-island_perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check upper cell
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1

                # Check lower cell
                if i < rows - 1 and grid[i+1][j] == 1:
                    perimeter -= 1

                # Check left cell
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1

                # Check right cell
                if j < cols - 1 and grid[i][j+1] == 1:
                    perimeter -= 1

    return perimeter
