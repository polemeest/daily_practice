from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
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

assert a.merge(intervals=[[15, 18], [1, 3], [2, 6], [8, 10], ]) == \
    [[1, 6], [8, 10], [15, 18]], f"expected {[[1, 6], [8, 10], [15, 18]]}, \
        got {a.merge(intervals=[[15, 18], [1, 3], [2, 6], [8, 10], ])}"

assert a.merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]], f"expected {[[1, 5]]}\
    , got {a.merge(intervals=[[1, 4], [4, 5]])}"

assert a.merge(intervals=[[1, 4], [2, 3]]) == [[1, 4]], f"expected {[[1, 4]]}\
    , got {a.merge(intervals=[[1, 4], [2, 3]])}"

assert a.merge(intervals=[[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == \
    [[1, 10]], f"expected {[[1, 10]]}, got \
        {a.merge(intervals=[[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]])}"
