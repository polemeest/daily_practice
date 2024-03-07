from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                curr_el = board[r][c]
                print(curr_el, ": ", end=" ")

                for rr in range(max(0, r-1), r+2):
                    for cc in range(max(0, c-1), c+2):
                        #print(rr, cc)
                        try:
                            print(board[rr][cc], end=' ')
                        except IndexError:
                            pass
                print()
        
        
        
        # n, m = len(board), len(board[0])
        # state = {}
        # for i, v in enumerate(board):
        #     for j, vv in enumerate(v):
        #         live = 0
        #         for ii in range(max(0, i - 1), min(n, i + 2)):
        #             for jj in range(max(0, j - 1), min(m, j + 2)):
        #                 if ii == i and jj == j:
        #                     continue
        #                 live += board[ii][jj]
        #         state[(i, j)] = live
        
        # for key, value in state.items():
        #     if board[key[0]][key[1]] == 0:
        #         if value == 3:
        #             board[key[0]][key[1]] = 1
        #     else:
        #         if value < 2:
        #             board[key[0]][key[1]] = 0
        #         elif value > 3:
        #             board[key[0]][key[1]] = 0
                    
        # print(board)
            
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


# for i in range(len(board)):
#     for j in range(len(board[0])):
#         for ii in range(len(something)):
#             for jj in range(len(something)):
#                 pass



# for i in range(len(board)):
#     for j in range(len(board[0])):
#         element = board[i][j] # i = j = 1 == 0 // # i = 0, j = 1 == 1
#         for ii in range(i - 1, i + 2):  # [i-1:i+1]
#             for jj in range(j - 1, j + 2):  # [j-1:j+1]



        # для ячейки под индексом i мы ДОЛЖНЫ посмотреть все ячейки [i-1:i+1]
        # для ячейки под индексом j мы ДОЛЖНЫ посмотреть все ячейки [j-1:j+1]

        # для element при i=j=0                    board[0][1], 
        #                             board[1][0], board[1][1]

        # для element при i=j=1       board[0][0], board[0][1], board[0][2],
        #                             board[1][0], board[1][1], board[1][2]
        #                             board[2][0], board[2][1], board[2][2]