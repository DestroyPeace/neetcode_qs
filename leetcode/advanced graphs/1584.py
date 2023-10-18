# Minimum spanning tree

# Prim's algo or Kruskal's algos are used and are both featured in further maths, however
# prim's algo is easier to implement and typically more time efficient.

# The manhattan distance is the abs(x1 - x2) + abs(y1 - y2)

# Time complexity of prim's is O(n^2log(n)) for the edges having two possible connections for each n 
# and the prim's adding the log(n). It is similar to Djikstra's and uses a minheap

# Ideally, no cycles are wanted. It'll take n-1 edges for a given n number of nodes.

import heapq

List = list 

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # First problem is getting all of the edges as well as to minimise the total cost of the edges.
        # Perform BFS for a given node.

        # A visit hash set is used as well as a frontier which is a minheap that is used.

        # Stopping condition is when the len(visit) == n - 1
        # The reason you can start at any node is due to the fact that you'll be adding multiple values
        # and the constraint that every node has to be connected at least once. This means that
        # a given node could be connected to every other single node or that it may be the longest path and
        # therefore still has to be included and then you can find the other possible edges by checking the frontier.
    
        N = len(points)

        frontier = {i: [] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]

            for j in range(i + 1, N):
                x2, y2 = points[j]

                distance = abs(x1 - x2) + abs(y1 - y2)
                frontier[i].append([distance, j])
                frontier[j].append([distance, i])

        # Prims

        res = 0
        visit = set()

        min_heap = [[0,0]]

        while len(visit) < N:
            cost, i = heapq.heappop(min_heap)

            if i in visit:
                continue 

            res += cost
            visit.add(i)

            for neiCost, nei in frontier[i]:
                if nei not in visit:
                    heapq.heappush(min_heap, [neiCost, nei])

        return res
    
test = Solution()
print(test.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))