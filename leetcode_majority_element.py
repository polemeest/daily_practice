
from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ''' Bayer-Moore Majority Vote algorithm '''
        count = 0
        answer = None
        for i in nums:
            if count == 0:
                answer = i
            count += (1 if answer == i else -1)
        print(answer)


        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        print(max(hashmap))


        return Counter(nums).most_common()[0][0]

a = Solution()
print(a.majorityElement([3,2,3]))
