class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = []
        store = 0
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap.append(nums[i])
                nums[store] = nums[i]
                store += 1
        return store


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 1
        store = nums[0]
        for i in range(len(nums)):
            if nums[i] != store:
                nums[ind] = nums[i]
                store = nums[i]
                ind += 1
        return ind


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[ind] = nums[i]
                ind += 1
        return ind