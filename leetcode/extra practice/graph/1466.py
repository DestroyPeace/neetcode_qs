import heapq
import collections 
import math

List = list 

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        global changes

        edges = {
            (a,b) for a, b in connections
        }

        neighbours = {
            city: [] for city in range(n)
        }

        visit = set()
        changes = 0

        # Identifying all of the neighbours. 
        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        def dfs(city): 
            global changes
            for neighbour in neighbours[city]: 
                
                # This neighbour has already been visited and this means that it already
                # is already going to 0 and has already been accounted for.
                if neighbour in visit:
                    continue 
                
                # This means the graph is currently backwards, and knowing that 
                # the current city is able to go to 0, we must be able to traverse backwards.
                if (neighbour, city) not in edges: 
                    changes += 1

                visit.add(neighbour) 
                dfs(neighbour)
        
        visit.add(0)
        dfs(0)

        return changes

        
test = Solution()
print(test.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))