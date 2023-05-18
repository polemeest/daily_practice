class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        log = {}
        for index, num in enumerate(nums):
            res = target - num
            if res in log:
                return [log[res], index]
            log[num] = index