import heapq
import collections 
import math

List = list

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.res = 0 
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.visited = []

        # Identifying all of the potential islands.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if [i, j] in self.visited: 
                    continue 
                    
                # Island has been identified.
                if grid[i][j] == 1:
                    self.visited.append([i, j])
                    self.res += self.bfs(grid, [[i, j]])

        return self.res

    def bfs(self, grid, stack, enclave = True): 
        total = 1

        while stack: 
            # Assuming the current node is a working option
            row, col = stack.pop()

            for dy, dx in self.directions: 
                # Non enclave found as path to boundary has also been found. 
                if row + dy not in range(len(grid)):
                    enclave = False 
                    continue 

                elif col + dx not in range(len(grid[0])):
                    enclave = False 
                    continue 

                if [row + dy, col + dx] not in self.visited and grid[row + dy][col + dx] == 1:
                    self.visited.append([row + dy, col + dx])
                    total += 1
                    stack.append([row + dy, col + dx]) 
                
        # We don't stop as we attempt to identify all of the other neighbours
        if enclave:
            return total
        else:
            return 0
                        

        
test = Solution()
print(test.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
