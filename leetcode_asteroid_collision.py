from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -i:
                    stack.pop()
                if stack and stack[-1] == -i:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(i)
        return stack
a = Solution()
print(a.asteroidCollision([8,-8]))
print(a.asteroidCollision([8,5,-10,-2]))
print(a.asteroidCollision([-2,-2,1,-2]))
print(a.asteroidCollision([5,10,-5]))
print(a.asteroidCollision([10,2,-5]))
print(a.asteroidCollision([-2,-1,1,2]))