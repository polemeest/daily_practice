from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 0
        l = 0
        cur_sum = 0

        for r, num in enumerate(nums):
            cur_sum += num
            while l <= r and cur_sum >= target:
                res = r - l + 1 if not res else min(res, r - l + 1)
                cur_sum -= nums[l]
                l += 1

        return res
        
        
        
a = Solution()
print(a.minSubArrayLen(7, [2,3,1,2,4,3]))