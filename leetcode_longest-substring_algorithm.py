class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = length = 0
        memory = {}
        for right in range(len(s)):
            letter = s[right]
            if letter in memory and memory[letter] >= left:
                left = memory[letter] + 1
            else:
                length = max(length, right - left + 1)
            memory[letter] = right
        return length