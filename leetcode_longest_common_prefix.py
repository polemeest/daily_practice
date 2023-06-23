from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for loop in range(len(min(strs))):
            local = strs[0][loop]
            for item in range(1, len(strs)):
                if local != strs[item][loop]:
                    return prefix
            prefix += local
        return prefix


# class Solution:
#     def longestCommonPrefix(self, v: List[str]) -> str:
#         ans=""
#         v=sorted(v)
#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans


a = b = c = d = Solution()

print(a.longestCommonPrefix(["flower","flow","flight"]))