from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for str in strs:
            hash_map[''.join(sorted(str))].append(str)
        return list(hash_map.values())

        # for str in strs:
        #     counter = (0, * 26)
        #     for letter in str:
        #         counter[ord(letter) - ord("a")] += 1
        #     hash_map[counter].append(str)

a = Solution()
a.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
