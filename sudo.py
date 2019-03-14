def check_row(grid, r, c, val):
    for i in range(0, 9):
        if grid[r][i] == val:
            return False
    return True

def check_col(grid, r, c, val):
    for i in range(0, 9):
        if grid[i][c] == val:
            return False
    return True

def check_3_by_3(grid, r, c, val):
    r_start = r // 3 * 3
    c_start = c // 3 * 3
    for i in range(r_start, r_start + 3):
        for j in range(c_start, c_start + 3):
            if grid[i][j] == val:
                return False
    return True

def validate_cell(grid, r, c, val):
    if check_row(grid, r, c, val) == False:
        return False
    elif check_col(grid, r, c, val) == False:
        return False
    elif check_3_by_3(grid, r, c, val) == False:
        return False
    else:
        return True

import numpy as np

grid = [
    [0, 0, 1, 0, 0, 0, 0, 5, 3],
    [0, 2, 0, 0, 0, 7, 6, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 8],
    [0, 0, 0, 0, 5, 0, 7, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 5, 0, 6, 0, 0, 0, 0],
    [1, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 4, 5, 0, 0, 0, 8, 0],
    [2, 5, 0, 0, 0, 4, 1, 0, 0]
]

def solve_sudoku(grid, i):
    if i == 81:
        print(np.array(grid))
        print()
    else:
        r = i // 9
        c = i % 9
        if grid[r][c] > 0:
            solve_sudoku(grid, i + 1)
        else:
            for val in range(1, 10):
                if validate_cell(grid, r, c, val):
                    grid[r][c] = val
                    solve_sudoku(grid, i+1)
                    grid[r][c] = 0
solve_sudoku(grid, 0)
