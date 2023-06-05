from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 2
        for i in range(2, len(nums)):
            if nums[i] == nums[index - 2]:
                continue
            else:
                nums[index] = nums[i]
                index += 1




        return index, nums if len(nums) > 2 else len(nums)


        #     if len nums < 2:
        #     return len(nums)
        # else:
        #     start = 0
        #     end = 2


a = Solution()
print(a.removeDuplicates([0,0,1,1,1,1,2,3,3]))