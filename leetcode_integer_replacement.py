class Solution:
    def integerReplacement(self, n: int) -> int:
        step = 0

        def recursion(n: int, step: int) -> int:
            if n <= 1:
                return step
            if n % 2 == 0:
                n = n // 2
                step = recursion(n, step + 1)
            else:
                step = min(recursion(n - 1, step + 1), recursion(n + 1, step + 1))
            return step
        
        step = recursion(n, step)

        return step
        


a = Solution()
print(a.integerReplacement(n = 7))