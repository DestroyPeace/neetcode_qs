from collections import deque

class Solution:
    def orangesRotting(self, grid: int) -> int:
        q = deque()
        time, fresh = 0, 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                # Checking for any fresh fruit.
                if grid[r][c] == 1:
                    fresh += 1

                elif grid[r][c] == 2:
                    # Appending coords of rotten fruit.
                    q.append((r, c))
        
        # BFS Implementation because DFS doesn't account for other processes.

        # If there aren't any fresh oranges left, we can stop.
        while q and fresh > 0:

            # Not using a while q to iterate because we need to account for minutes of time
            # and minutes of action, and appending new coordinates in the same time.
            
            # This keeps a constant time for our deque to ensure that we don't do everything
            # in 1 minute for example.

            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    # Ensuring that it's in bounds and that the fruit is fresh.
                    if ((r not in range(rows)) or (c not in  range(cols))) or grid[r][c] != 1:
                        
                        # We skip this iteration as a result.
                        continue 
                    
                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r, c))
            
            # Each pass of the deque we increment by 1.
            time += 1

        if fresh == 0:
            return time
        else:
            return -1
