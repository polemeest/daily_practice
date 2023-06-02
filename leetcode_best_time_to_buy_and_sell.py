from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        profit = 0
        for n in prices:
            if n < price:
                price = n
            profit = max(profit, n - price)
        return profit


a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))