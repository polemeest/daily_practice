from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # coordinates = set()
        # for row, v in enumerate(matrix):
        #     for col, vv in enumerate(v):
        #         if vv == 0:
        #             coordinates.add((row, col))
        # for item in coordinates:
        #     row, col = item
        #     for i, v in enumerate(matrix[row]):
        #         matrix[row][i] = 0
        #     for i, v in enumerate(matrix):
        #         matrix[i][col] = 0

        # print(matrix)



a = Solution()
a.setZeroes(matrix = [   [0,1,2,0],
                         [3,4,5,2],
                         [1,3,1,5],
                         [1,3,1,5],
                    ])