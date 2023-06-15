from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        memory = start = steps = tank = 0
        while gas[start] < cost[start]:
            memory = start = start + 1
            # if start > 10000:
            #     return -1
        while steps != len(cost):
            tank += gas[start % len(gas)]
            tank -= cost[start % len(cost)]
            start, steps = start + 1, steps + 1
            if tank < 0:
                memory += 1
                start = memory
                steps = tank = 0
        return memory






a = b = c = Solution()
# print(a.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
# print(b.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
print(c.canCompleteCircuit(gas = [5,1,2,3,4], cost = [4,4,1,5,1]))

