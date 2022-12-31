from collections import deque

class Solution:
    def numIslands(self, grid: str) -> int:
        # No islands exist 
        if not grid:
            return 0 

        # Calculating number of rows and columsn
        rows, cols = len(grid), len(grid[0])

        # Creating a set whereby we store the coordinates of each island visited.
        visited = set()

        # Return value.
        islands = 0

        # Using our bread first search algoirthm, where 
        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))


            while q:
                row, col = q.popleft()

                # Creating each direction (adjacent squares and no diaganols)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # Delta row and delta cols
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # Base checking that the indices are in the bounds.
                    if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == "1":
                        q.append((r, c))
                        visited.append((r, c))

        # Iterating throguh each of the possible coordinates and checking if they are 
        # an island or water.
        for r in range(rows):
            for c in range(cols):
                # Finding the first island to use BFS on.
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                       
        return islands 

