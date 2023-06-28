class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        hashmap = [[] for i in range(numRows)]
        flag = '>'
        index = 0
        for letter in s:
            hashmap[index].append(letter)

            if index == numRows - 1:
                flag = '<'
            elif index == 0:
                flag = '>'

            if flag == '>':
                index += 1
            else:
                index -= 1

        return ''.join(''.join(lst) for lst in hashmap)


a = b = c = d = Solution()

print(c.convert(s='ABC', numRows=1))
print(a.convert(s = "PAYPALISHIRING", numRows = 3)) # "PAHNAPLSIIGYIR"
print(b.convert(s = "PAYPALISHIRING", numRows = 4)) # "PINALSIGYAHRPI"
