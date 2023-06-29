from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        L = 0
        R = len(height) - 1
        maxL = height[L]
        maxR = height[R]
        result = 0

        while L < R:
            if maxL <= maxR:
                L += 1
                maxL = max(maxL, height[L])
                result += maxL - height[L]

            else:
                R -= 1
                maxR = max(maxR, height[R])
                result += maxR - height[R]

        return result






a = b = c = d = Solution()
print(b.trap([4,2,0,3,2,5]))
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))



''' FUN GRAPHICAL WAY:

        matrix = [[0] * len(height) for _ in range(max(height))]

        for i in range(len(height)):
            for j in range(-height[i], 0):
                matrix[j][i] = 1

        for i in matrix:
            l = i.index(1)
            for r in range(l, len(i)):
                if i[r] == 1 and r - l < 2:
                    l = r
                elif i[r] == 1 and r - l >= 2:
                    i[l + 1: r] = [2] * (r - l - 1)
                    l = r

        return sum(i.count(2) for i in matrix)



        '''