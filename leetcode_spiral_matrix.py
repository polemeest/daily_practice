from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ## pointers
        res = []
        left = top = 0
        right, bottom = len(matrix[0]) - 1, len(matrix) - 1
        ## main loop
        while top <= bottom and left <= right:
            ## horizontal to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            ## vertical to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            ## horizontal to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            ## vertical to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
    
a = Solution()
print(a.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))






a = Solution()
print(a.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))