class Solution:
    def romanToInt(self, s: str) -> int:
        dict_map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        value = 0
        for index, letter in enumerate(s, 1):
            if index == len(s):
                value += dict_map[letter]
            elif dict_map[letter] < dict_map[s[index]]:
                value -= dict_map[s[index - 1]]
            else:
                value += dict_map[letter]

        return value
