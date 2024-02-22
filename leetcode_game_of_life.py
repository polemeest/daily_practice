from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        state = {}
        for i, v in enumerate(board):
            for j, vv in enumerate(v):
                live = 0
                for ii in range(max(0, i - 1), min(n, i + 2)):
                    for jj in range(max(0, j - 1), min(m, j + 2)):
                        if ii == i and jj == j:
                            continue
                        live += board[ii][jj]
                state[(i, j)] = live
        
        for key, value in state.items():
            if board[key[0]][key[1]] == 0:
                if value == 3:
                    board[key[0]][key[1]] = 1
            else:
                if value < 2:
                    board[key[0]][key[1]] = 0
                elif value > 3:
                    board[key[0]][key[1]] = 0
                    
        print(board)
            
    # Any live cell with fewer than two live neighbors dies as if caused by under-population.
    # Any live cell with two or three live neighbors lives on to the next generation.
    # Any live cell with more than three live neighbors dies, as if by over-population.
    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.



a = Solution()
a.gameOfLife(board = [[0,1,0],
                      [0,0,1],
                      [1,1,1],
                      [0,0,0]])


# live = board[(i - 1)][j - 1] + board[i][j - 1] + board[(i + 1)][j - 1] \
                    #  + board[i - 1][j] + board[i + 1][j] \ 
                    #  + board[i - 1][j + 1] + board[i][j + 1] + board[i + 1][j + 1]
