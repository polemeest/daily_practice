# from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))  # noqa
        if not word1 or not word2:
            return word2 or word1
        result = ""
        min_l, left = min(len(word1), len(word2)), len(word1) > len(word2)
        for i in range(min_l):
            result += word1[i]
            result += word2[i]

        return result + word1[i+1:] if left else result + word2[i+1:]

        # p_1 = p_2 = 0

        # while p_1 < len(word1) or p_2 < len(word2):
        #     if p_1 < len(word1):
        #         result += word1[p_1]
        #         p_1 += 1
        #     if p_2 < len(word2):
        #         result += word2[p_2]
        #         p_2 += 1
        # return result


a = Solution()
print(a.mergeAlternately(word1="abc", word2="pqr"))
print(a.mergeAlternately(word1="ab", word2="pqrs"))
