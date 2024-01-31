class Solution:
    def isHappy(self, n: int) -> bool:
        ints = {n, }

        def recursion(number: int) -> bool:
            nonlocal ints
            if number == 1:
                return True
            elif number in ints:
                return False
            ints.add(number)
            return recursion(sum(int(i) ** 2 for i in str(number)))

        return recursion(sum(int(i) ** 2 for i in str(n)))


a = Solution()
print(a.isHappy(2))
