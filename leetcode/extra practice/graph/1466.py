import heapq
import collections 
import math

List = list 

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {
            (a,b) for a, b in connections
        }

        neighbours = {
            city: [] for city in range(n)
        }

        visit = set()
        changes = 0

        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        q = collections.deque([0])

        visit.add(0)

        while q:
            city = q.popleft() 

            for nei in neighbours[city]:
                if nei in visit:
                    continue 

                if (city, nei) in edges: 
                    changes += 1
                
                q.append(nei)
                visit.add(nei)
        
        return changes
        
test = Solution()
print(test.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))