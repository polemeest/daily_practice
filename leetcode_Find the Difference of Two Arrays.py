from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]

        




a = Solution()
print(a.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2])) ## [[1,3],[4,6]]