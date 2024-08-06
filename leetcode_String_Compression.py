from typing import List


class Solution:
    def repeat(self, chars: list, repeats: int, index: int, last_index: int):
        if repeats > 1:
            if repeats > 9:
                repeats = ".".join(str(repeats)).split(".")
                for ind, num in enumerate(repeats, 1):
                    chars[last_index + ind] = num
            else:
                chars[index - 1] = str(repeats)

    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        last_char = chars[0]
        last_index = 0
        repeats = 1

        for index, item in enumerate(chars):
            if index == 0:
                continue
            if item == last_char:
                repeats += 1
                chars[index] = ""
            else:
                self.repeat(chars, repeats, index, last_index)
                repeats, last_char, last_index = 1, item, index
        self.repeat(chars, repeats, 0, last_index)
        print(chars)
        while "" in chars:
            chars.remove("")
        print(chars)
        return len(chars)



a = Solution()
print(a.compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(a.compress(chars = ["a","a","a","b","b","a","a"]))
print(a.compress(chars = ["a","a","a","b","b","a","a","c","c","c"]))
print(a.compress(chars = ["a"]))
