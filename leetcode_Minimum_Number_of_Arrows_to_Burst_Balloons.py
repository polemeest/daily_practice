from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        left = points[0]
        res = 1
        for right in points[1:]:
            if right[0] > left[1]:
                res += 1
                left = right
            else:
                left[1] = min(left[1], right[1])
        return res
    

a = Solution()
print(a.findMinArrowShots(points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))
print(a.findMinArrowShots(points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
print(a.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))
print(a.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]]))
print(a.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))