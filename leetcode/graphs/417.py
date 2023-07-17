class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visit, prevHeight):
            # If the coordinate has been visited / is less than previous / not in range.
            if ((r, c) in visit or (r not in range(rows) or c not in range(cols) or heights[r][c] < prevHeight)):
                return 

            visit.add((r, c))

            # Checking all adjacent squares.
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Starting at each edge case for the columns. This is the horizontal dir.
        for c  in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

        """
        rows, cols = len(heights), len(heights[0])


        HASHMAP -> {(ROW, COLUMN): (PACIFIC, ATLANTIC)}
        res = []
        hash = {

        }

        def dfs(original_coord, new_coord):
            old_r, old_c = original_coord
            nr, nc = new_coord

            # Checking boundaries.
            if (nr == 0 or nc == 0) or (nc == rows - 1 or nc == cols - 1)
                if (nr, nc) == (rows - 1, cols - 1) and not all(hash[(nr, nc)]):
                    # Setting current values as true
                    hash[(row, col)] = [True, True]

                if (row, col) == (0, cols - 1) and not all(hash[(row, col)]):
                    hash[(row, col)] = [True, True]


        
        for value in hash:
            if all(hash[value]):
                res.append(hash[value])

        return res
        """