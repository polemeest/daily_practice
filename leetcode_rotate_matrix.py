from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i, v in enumerate(matrix):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for item in matrix:
            item = item.reverse()

        # holderMap,m={},len(matrix)
        # for i in range(m):
        #     for j in range(m):
        #         if (i,j) in holderMap:
        #             v=holderMap[(i,j)]
        #         else:
        #             v=matrix[i][j]
        #         if j>= i:
        #             holderMap[(j,m-1-i)]=matrix[j][m-1-i]
        #         matrix[j][m-1-i]=v




a = Solution()
a.rotate([[1,2,3],[4,5,6],[7,8,9]])
