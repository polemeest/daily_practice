class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return False
        for let in ransomNote:
            if let not in magazine:
                return False
            magazine = magazine.replace(let, '', 1)
        return True
                    
        
        
a = Solution()
print(a.canConstruct(ransomNote = "a", magazine = "b"))