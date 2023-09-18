import heapq

List = list 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        if gas == cost:
            return 0

        total = 0
        res = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0: 
                total = 0
                res = i  + 1

        return res
        
test = Solution()
print(test.canCompleteCircuit([3,1,1], [1,2,2]))

