class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hmap, s = {}, s.split()
        if len(set(pattern)) != len(set(s)) or len(s) != len(pattern):
            return False
        for index, letter in enumerate(pattern):
            if letter in hmap and not hmap[letter] == s[index] :
                return False
            hmap[letter] = s[index]
        return True
        
        
a = Solution()
print(a.wordPattern(pattern = "abba", s = "dog cat cat dog"))