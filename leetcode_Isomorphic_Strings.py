class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        for index, letter in enumerate(s):
            t = t.replace(t[index], letter, 1)
        return set(s) == set(t) 
        
        
a = Solution()
print(a.isIsomorphic(s = "foo", t = "bar"))