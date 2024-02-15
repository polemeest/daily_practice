from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = dict()
        for i, val in enumerate(nums):
            if val not in hash_map:
                hash_map[val] = [i]
            else:
                for j in hash_map[val]:
                    if abs(i - j) <= k:
                        return True
                hash_map[val].append(i)
        return False
    
a = Solution()
print(a.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))