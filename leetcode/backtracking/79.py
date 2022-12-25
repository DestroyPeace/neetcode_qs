class Solution:
    def exist(self, board: str, word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, index):
            if index == len(word):
                return True
            
            # Lots of invalid base cases.
            if (
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or
                 word[index] != board[r][c] or
                 (r, c) in path):

                 return False

            path.add((r, c))

            # Checking each of the adjacent squares using brute force and checking all of them.

            res = (dfs(r + 1, c, index + 1) or
                    dfs(r - 1, c, index + 1) or 
                    dfs(r, c + 1, index + 1) or 
                    dfs(r, c - 1, index + 1))

            path.remove((r, c)) # No longer visting the path.
            
            return res
            
        # Calling the function.
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False
        
test = Solution()

print(test.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))