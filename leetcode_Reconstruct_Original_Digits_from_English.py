class Solution:
    def originalDigits(self, s: str) -> str:
        hash_map = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        res = ""
        while s:
        for key in hash_map:
            count = 0
            for letter in key:
                if letter in s:
                    count += 1
            if count == len(key):
                for letter in key:
                    s = s.replace(letter, '', 1)
                res += str(hash_map[key])
        return res

a = Solution()
print(a.originalDigits(s = "zerozero"))