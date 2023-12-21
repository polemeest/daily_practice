class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not (len(s) == len(t) and set(s) == set(t)):
            return False
        hmap = {}
        for letter in set(s):
            hmap[letter] = s.count(letter)
            if t.count(letter) != hmap[letter]:
                return False
        return True
        
a = Solution()
print(a.isAnagram(s = "anagram", t = "nagaram"))