def is_possible(puzzle, row, col, val):
    for i in range(8):
        if puzzle[i] == val:
            return (0)
    for i in range(8):
        if puzzle[col][i] == val:
            return (0)
    for i in range(3):
        for j in range(3):
            if puzzle[col + i][row + j] == val:
            	return (0)
    return (1)

def solve(puzzle, row, col):
    val = 1
    while col < 8:
        while row < 8:
            if puzzle[col][row] == 0 and is_possible(puzzle, row, col, val):
                puzzle[col][row] = val
                if solve(puzzle, row, col):
                    return (1)
                puzzle[col][row] = 0
            else:
                val += 1
            row += 1
        col += 1
    return (0)

def sudoku(puzzle):
    solve(puzzle, 0, 0)
    return puzzle