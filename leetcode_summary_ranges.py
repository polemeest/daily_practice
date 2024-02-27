from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        temp = []
        l = 0
        for r, v in enumerate(nums):
            if nums[(r + 1) % len(nums)] - v != 1:
                temp.append([nums[l], v] if nums[l] != v else [v])
                l = r + 1
        return ["->".join((str(lst[0]), str(lst[-1]))) if len(lst) > 1
                else str(lst[0]) for lst in temp]
    
        # if not nums: return []
        # temp, l = [], nums[0]
        # for r, v in enumerate(nums):
        #     if nums[(r + 1) % len(nums)] - v != 1:
        #         temp.append(f"{str(l)}->{str(v)}" if l != v else str(v))
        #         l = nums[(r + 1) % len(nums)]
        # return temp

a = Solution()
print(a.summaryRanges(nums = [0,1,2,4,5,7]))
print(a.summaryRanges(nums = [0,2,3,4,6,8,9]))
