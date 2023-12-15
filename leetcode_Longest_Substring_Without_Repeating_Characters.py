class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_s = ''
        l = 0
        res = 0
        for ind, let in enumerate(s):
            if let not in s_s:
                s_s += let
                res = max(res, len(s_s))
            else:
                l = s.index(let, l) + 1
                s_s = s[l: ind + 1]
        return res, s_s
        
a = Solution()
for i in ('abcabcbb', 'bbbbb', 'pwwkew'):
    print(a.lengthOfLongestSubstring(i))