from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal = -1
        # for i in range(-1, -len(nums) - 1, -1):
        #     if any(i + j == goal for j in range(0, nums[i] + 1)):
        #         goal = i
        # return True if any((-len(nums) - 1) + j == goal for j in range(0, nums[0] + 1)) else False

        # n=len(nums)
        # dp=[False for _ in range(n-1)]
        # dp+=[True]
        # for i in range(n-2,-1,-1):
        #     for j in range(i,min(n,i+nums[i]+1)):
        #         if dp[j]:
        #             dp[i]=True
        #             break
        #         #print(i,j,dp)
        # return dp[0]

        goal = -1
        for i in range(-1, -len(nums) - 1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == -len(nums)

a = b = c = Solution()
print(a.canJump([0, 1]))
print(b.canJump([2,3,1,1,4]))
print(c.canJump([2,0,0]))