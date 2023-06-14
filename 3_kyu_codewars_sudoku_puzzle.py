def sudoku(puzzle, step):
    """return the solved puzzle as a 2d array of 9 x 9"""
    for x in range(9):
        for y in range(9):
            if puzzle[x][y] == 0:
                for n in range(1, 10):
                    if is_possible(x, y, n, puzzle):
                        puzzle[x][y] = n
                        if sudoku(puzzle, step + 1):
                            return puzzle, step
                        else:
                            puzzle[x][y] = 0
                    else:
                        puzzle[x][y] = 0
                return print(step)
    return puzzle


def is_possible(x, y, n, puzzle):
    for i in range(9):
        if puzzle[x][i] == n:
            return False
    for i in range(9):
        if puzzle[i][y] == n:
            return False
    x0, y0 = (x // 3) * 3, (y // 3) * 3
    for x in range(3):
        for y in range(3):
            if puzzle[x + x0][y + y0] == n:
                return False
    return True


# def sudoku(P):

#     for row, col in [(r, c) for r in range(9) for c in range(9) if not P[r][c]]:

#         rr, cc = (row // 3) * 3, (col // 3) * 3

#         use = {1,2,3,4,5,6,7,8,9} - ({P[row][c] for c in range(9)} | {P[r][col] for r in range(9)} | {P[rr+r][cc+c] for r in range(3) for c in range(3)})

#         if len(use) == 1:
#             P[row][col] = use.pop()
#             return sudoku(P)
#     return P

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku(puzzle))
