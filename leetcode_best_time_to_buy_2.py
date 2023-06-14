from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value = prices[0]
        profit = 0
        for v in prices:
            if v < value:
                value = v
            if v > value:
                profit += v - value
                value = v
        return profit


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n=len(prices)
#         # dp=[[0]*2 for i in range(n+1)]
#         ahd=[0]*2
#         for i in range(n-1,-1,-1):
#             curr=[0]*2
#             for j in range(1,-1,-1):
#                 if j==1:
#                     curr[j]=max(ahd[j],ahd[0]-prices[i])
#                 else:
#                     curr[j]=max(ahd[j],ahd[1]+prices[i])
#             ahd=curr
#         return ahd[1]



a = b = c = d = Solution()
assert(a.maxProfit([7,1,5,3,6,4]), 7)
assert(b.maxProfit([1,2,3,4,5]), 4)
assert(c.maxProfit([7,6,4,3,1]), 0)
assert(d.maxProfit([6,1,3,2,4,7]), 7)