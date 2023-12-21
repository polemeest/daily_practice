class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap = {}
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        for index, letter in enumerate(t):
            if letter in hmap and not hmap[letter] == s[index] :
                return False
            hmap[letter] = s[index]
        return True
        
        
a = Solution()
print(a.isIsomorphic(s = "foo", t = "bar"))