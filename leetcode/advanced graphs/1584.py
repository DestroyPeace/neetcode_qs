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
    
        visit = [points[0]]
        frontier = []

        for point in points:
                if point not in visit:
                    frontier.append([abs(visit[0][0] - point[0]) + abs(visit[0][1] - point[1]), point])

        # Creating a min_heap
        heapq.heapify(frontier)

        res = 0


        while len(visit) != len(points):
        # Calculating each of the costs from the current visit list.
        
            # From the now fully updated heap, we take the smallest value and add it to our total.
            
            print(f"visit: {visit}, frontier: {frontier}")
            visit.append(frontier[0][1])
            res += frontier[0][0]

            for point in points:
                if point not in visit:
                    # Calculating manhattan distance as [cost, point]
                    heapq.heappush(frontier, [abs(visit[-1][0] - point[0]) + abs(visit[0][1] - point[1]), point])
            # Removing the closest next point, and since we don't need to keep track of the distances connected
            # If distances had to be connected, another array considering the connection could be used e.g:
            # [cost, starting_point, next_point], but since we are allowed multiple connections from one node,
            # just such that there is all unique paths, we don't need to keep track of it.

            heapq.heappop(frontier)
        return res 
    
test = Solution()
print(test.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))