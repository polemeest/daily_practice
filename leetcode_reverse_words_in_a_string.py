class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])



a = b = c = d = Solution()

print(a.reverseWords('the sky is blue'))
print(b.reverseWords("  hello world  "))
print(c.reverseWords("a good   example"))