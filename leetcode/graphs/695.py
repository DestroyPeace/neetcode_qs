from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid):
        areas = []
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col, area):
            q = deque() 
            visited.add((row, col))
            q.append((row, col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                        area += 1
                        q.append((r, c))
                        visited.add((r, c))

            return area
                        
        
        for row in range(rows):
            for col in range(cols):
                
                # Detected our first new island. 
                if grid[row][col] == 1 and (row, col) not in visited:
                    areas.append(bfs(row, col, 1))

        return max(areas) if areas else 0
