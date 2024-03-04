from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: (x[1], x[0]))
        res = 0
        l, r = 0, 1

        while r < len(points):
            left = points[l]
            right = points[r]
            if left[1] >= right[0]:
                r += 1
            else:
                res += 1
                l = r
                r += 1
        if l < r:
            res += 1
        return res


a = Solution()
print(a.findMinArrowShots(points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))
print(a.findMinArrowShots(points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
print(a.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))
print(a.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]]))
print(a.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))