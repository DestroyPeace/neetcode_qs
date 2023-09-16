import heapq

List = list 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        if gas == cost:
            return 0

        diff = [gas[i] - cost[i] for i in range(len(gas))]
        # Choosing the new starting index
        for start in range(len(diff)):
            total = diff[start]

            # Choosing starting position
            if diff[start] > 0:
                pos = start

                for _ in range(len(diff) - 1):
                    # Checking the next index
                    if pos + 1 in range(len(diff)):
                        pos += 1

                    # Means we've reached the end of the array.
                    else:
                        pos = 0
                    
                    total += diff[pos]

                    if total < 0:
                        break
                
                # CURR POS == START
                if gas[pos] == gas[start - 1]:
                    return start

        return -1
        
test = Solution()
print(test.canCompleteCircuit([3,1,1], [1,2,2]))

