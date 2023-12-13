from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        store = 0
        while l < r:
            h = min(height[l], height[r])
            store = max(store, h * (r - l))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return store
            
        
        
a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))
        