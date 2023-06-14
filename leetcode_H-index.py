from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, v in enumerate(citations):
            if i >= v:
                return i
        return len(citations)


a = b = c = Solution()
print(a.hIndex([3,0,6,1,5]))
print(b.hIndex([1,3,1]))
print(c.hIndex([0]))