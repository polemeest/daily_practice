from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = l = r = 0
        while r < len(nums) - 1:
            best = 0
            for i in range(l, r + 1):
                best = max(best, i + nums[i])    
            l, r, steps = r + 1, best, steps + 1
        return steps

a = Solution()
a.jump(nums = [2,3,1,1,4])