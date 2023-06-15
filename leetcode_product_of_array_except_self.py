from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer



a = b = c = d = Solution()

# print(a.productExceptSelf([0, 4, 0]))
# print(b.productExceptSelf([-1,1,0,-3,3]))
print(c.productExceptSelf([1,2,3,4]))
print(d.productExceptSelf([1, 0]))