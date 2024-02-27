from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counter = 0
        begin = 0
        nums = sorted(list(set(nums)))
        n = len(nums)

        for i in range(n):
            if nums[(i + 1) % n] - nums[i] != 1:
                counter = max(counter, begin - i + 1)
                begin = i + 1
        counter = max(counter, begin - i + 1)
        print(counter)

        return counter


a = Solution()
print(a.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))