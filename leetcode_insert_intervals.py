
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.extend([newInterval])
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for index in range(1, len(intervals)):
            last = res[-1][1]
            if intervals[index][0] <= last:
                res[-1][1] = max(last, intervals[index][1])
            else:
                res.append(intervals[index])
        return res

a = Solution()
print(a.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))