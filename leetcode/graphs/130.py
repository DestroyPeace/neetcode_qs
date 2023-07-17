class Solution:
    def solve(self, board) -> None:

        visited = set()
        rows, cols = len(board), len(board[0])

        if rows == 1 or cols == 1:
            return

        def dfs(row, col, flipped = False):
            # First checking if the coordinates are in the boundary.
            if (row not in range(rows) or col not in range(cols)):
                return

            # Double base check due to recursion.
            # 2) Checking fi the value is a "O"
            if ((row, col)) in visited:
                return 
            
            if board[row][col] == "X":
                return 

            visited.add((row, col))
            # Checking if coord is on the boundary by first checking if it's not flipped.
            if (
                (not flipped) and
                (row in range(rows) and col == 0) or
                (row in range(rows) and col == cols - 1) or
                (col in range(cols) and row == 0) or 
                (col in range(cols) and row == rows - 1) 
            ):
                flipped = True 

            # If any adjacent squares are not flippable; change to x
            if not flipped:
                board[row][col] = "X"

            # Now repeating it for each of the four directions.

            dfs(row + 1, col, flipped)
            dfs(row - 1, col, flipped)
            dfs(row, col + 1, flipped)
            dfs(row, col - 1, flipped)
        
 
        # Finding the dfs of each boundary. 
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)
        
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and board[row][col] == "O":
                    dfs(row, col)



test = Solution().solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])

print(test)