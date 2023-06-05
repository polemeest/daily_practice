from typing import List
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         log = []
#         for i, v in enumerate(nums):
#             log.append((v, (i + k) % len(nums)))
#         log.sort(key=lambda x: x[1])
#         for i, v in enumerate(nums):
#             nums[i] = log[i][0]
#         print(log, nums)

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         log = sorted([(v, (i + k) % len(nums)) for i, v in enumerate(nums)], key=lambda x: x[1])
#         for i, v in enumerate(nums):
#             nums[i] = log[i][0]
#         print(log, nums)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        while n != 0 and k != 0:
            leftover = n % k
            # Shift most of the array by k, using the first k elements as temporary storage
            for i in range(k, n - leftover):
                nums[i], nums[i % k] = nums[i % k], nums[i]
            # Fix the leftover end of the array
            for i in range(leftover):
                nums[i], nums[n - leftover + i] = nums[n - leftover + i], nums[i]
            # Shift the first k elements right by k - n % k
            if leftover == 0:
                break
            k, n = k - leftover, k


a = Solution()
a.rotate([1,2,3,4,5,6,7], 3)