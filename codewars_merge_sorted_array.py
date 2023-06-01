from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        end = n + m - 1

        while n > 0:
            if m >= 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[end] = nums1[m - 1]
                m -= 1
            else:
                nums1[end] = nums2[n - 1]
                n -= 1
            end -= 1
        print(nums1)

a = Solution()
a.merge([1,2,3,0,0,0], 3, [2,5,6], 3)