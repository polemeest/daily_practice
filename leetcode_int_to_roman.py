class Solution:
    def intToRoman(self, num: int) -> str:
        roman_string = ''
        dict_map = {
            1 : 'I',
            4 : 'IV', 5 : 'V',
            9 : 'IX', 10 : 'X',
            40 : 'XL', 50 : 'L',
            90 : 'XC', 100 : 'C',
            400 : 'CD', 500 : 'D',
            900 : 'CM', 1000 : 'M'
        }

        for k, v in reversed(dict_map.items()):
            while num > 0 :
                if k <= num:
                    roman_string += v
                    num -= k
                else:
                    break


        return roman_string



a = b = c = d = Solution()
print(a.intToRoman(3))
print(b.intToRoman(13))
print(c.intToRoman(432))
print(d.intToRoman(5892))