import heapq
import math

List = list

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # point[0] = x coordinate and point[1] = y - coordinate. 
        res = []

        distance_index = {math.sqrt(point[0] ** 2 + point[1] ** 2): point for point in points}
        distances = []
        
        for key in distance_index:
            distances.append(key)
        
        heapq.heapify(distances)

        for _ in range(k):
            res.append(distance_index[heapq.heappop(distances)])

        return res
    
test = Solution()
print(test.kClosest(points = [[1,3],[-2,2]], k = 1))