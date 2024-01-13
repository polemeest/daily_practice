from typing import List
class Solution:
    def check_row(self, row: list, num: int) -> bool:
        if row.count(num) <= 1:
            return True
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num.isdigit():
                    col = [x[j] for x in board]
                    ti = 3 * (i // 3) 
                    tj = 3 * (j // 3)
                    box = [x for y in board[ti : ti + 3] for x in y[tj: tj + 3]]
                    if not self.check_row(row, num) \
                    or not self.check_row(col, num) \
                    or not self.check_row(box, num):
                        return False
        return True





a = Solution()
print(a.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))