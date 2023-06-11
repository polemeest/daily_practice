from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        left = right = 0
        while right < len(nums) - 1:
            max_step = 0
            for i in range(left, right + 1):
                max_step = max(max_step, i + nums[i])
            left = right + 1
            right = max_step
            steps += 1
        return steps





# (a := hashmap[i:i + nums[i] + 1])






a = b = c = Solution()

print(a.jump([1, 1, 1, 1]))
print(b.jump([1,2,3]))
print(c.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))