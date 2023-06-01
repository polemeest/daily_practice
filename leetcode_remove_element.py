class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = 0
        for el in nums:
            if el != val:
                nums[ind] = el
                ind += 1
        return ind