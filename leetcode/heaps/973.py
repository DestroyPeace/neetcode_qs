"""

TIME COMPLEXITY: O(KLOG(N))
SPACE COMPLEXITY: O(2N)

BETTER COMPARED TO SORTING THE LIST AS KLOG(N) < NLOG(N) FOR SHORT NUMBERS OF K.


"""

import heapq
import math

List = list

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = [

        ]

        res = []

        for x, y in points:
            min_heap.append([math.sqrt(x ** 2 + y ** 2), x, y])
        
        heapq.heapify(min_heap)

        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1:])

        return res
    
test = Solution()
print(test.kClosest(points = [[1,3],[-2,2]], k = 1))