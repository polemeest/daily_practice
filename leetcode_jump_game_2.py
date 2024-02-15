from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        steps = 1
        l, r = 0, nums[0]
        while r < len(nums) - 1:
            window = nums[l:r + 1]
            best = r
            for i, val in enumerate(window, l):
                best = max(best, i + val)    
            l, steps, r = r, steps + 1, best

        return steps

a = Solution()
a.jump(nums = [2,3,1,1,4])