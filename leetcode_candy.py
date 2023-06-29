from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        l2r = [1] * len(ratings)
        r2l = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                l2r[i] = l2r[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                r2l[i] = r2l[i + 1] + 1

        return sum(max(x, y) for x, y in zip(l2r, r2l))



a = b = c = d = Solution()
print(a.candy([1,0,2])) # 5
print(b.candy([1,2,2])) # 4