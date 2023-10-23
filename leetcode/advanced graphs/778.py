List = list 

"""
n x n square matrix of integers. 
grid[i][j] represents elevation at (i, j)

At t, the depth of the water is t. 

You can swim from a square to another 4 directionally adjacent square if the elevation of both
squares are at most t. You can swim infinite distances in zero time.

Return the least time until you reach the right square (n -1, n - 1) from (0, 0)

This is once again a Djikstra's algo. A greedy djikstra's algo n^2log(n).

Djikstra's algo is used when you want to minimise the total time taken.
Try the min path first. T
"""

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Simple base case.
        if len(grid) == 1:
            return grid[0][0]

        visit = set() 

        # Stating off on the first (0, 0)
        min_heap = [(grid[0][0], 0, 0)]
        heapq.heapify(min_heap)
        
        height, row, column = heapq.heappop(min_heap)
        while (row, column) != (len(grid) - 1, len(grid) - 1):
            neighbours = []

            if row - 1 in range(len(grid)) and (row - 1, column) not in visit:
                neighbours.append((max(grid[row - 1][column], height), row - 1, column))
                visit.add((row - 1, column))
            
            if column - 1 in range(len(grid)) and (row, column - 1) not in visit:
                neighbours.append((max(grid[row][column - 1], height), row, column - 1))
                visit.add((row, column - 1))
            
            if row + 1 in range(len(grid)) and (row + 1, column) not in visit:
                neighbours.append((max(grid[row + 1][column], height), row + 1, column))
                visit.add((row + 1, column))

            if column + 1 in range(len(grid)) and (row, column + 1) not in visit:
                neighbours.append((max(grid[row][column + 1], height), row, column + 1))
                visit.add((row, column + 1))

            for neighbour in neighbours: 
                heapq.heappush(min_heap, neighbour) 

            height, row, column = heapq.heappop(min_heap)
        
        return height 
        # Checking the neighbours and adding them to the min_heap

test = Solution()
print(test.swimInWater(grid = [[0,2],[1,3]]))