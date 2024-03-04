from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        my = [[0] * len(matrix) for i in range(len(matrix[0]))]

        for i, v in enumerate(my):
            for j, vv in enumerate(v):
                my[j][i] = matrix[i][j]
        return my
    f

a = Solution()
print(a.transpose([[1,2,3],[4,5,6]]))