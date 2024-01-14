import heapq
import collections 
import math

from itertools import combinations 

List = list        

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(list(comb) for comb in combinations(range(1, n + 1), k))
        
        
test = Solution()
print(test.combine(n = 1, k = 1))
