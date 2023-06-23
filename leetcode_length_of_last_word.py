class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        leng = 0
        start = False
        i = len(s) - 1
        while True:
            if start == False and leng > 0:
                break
            start = True if s[i] != ' ' else False
            if start:
                leng += 1
            i -= 1
        return leng



        # return len(s.split()[-1])

        # # class Solution:
        # # def lengthOfLastWord(self, s: str) -> int:
        # #     leng = 0
        # #     i = len(s) - 1
        # #     while i >= 0:
        # #         if s[i] != ' ':
        # #             leng += 1
        # #         elif leng > 0:
        # #             break
        # #         i -= 1
        # #     return leng



a = b = c = d = Solution()

print(a.lengthOfLastWord("   fly me   to   the moon  "))