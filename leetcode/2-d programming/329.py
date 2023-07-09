class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        dp = {}

        # CREATING DP WITH ALL OF THE POSSIBLE PATHS FROM EACH POINT
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                val = matrix[i][j]
                res = 0

                # COUNTING NUMBER OF VALID NEIGHBOURS 

                # UP
                if i - 1 > 0 and val < matrix[i - 1][j]:
                    res += 1
                
                # RIGHT
                if j + 1 < len(matrix) - 1 and val < matrix[i][j + 1]:
                    res += 1

                # DOWN
                if i + 1 < len(matrix) - 1 and val < matrix[i - 1][j]:
                    res += 1

                # LEFT
                if j - 1 > 0 and val < matrix[i][j - 1]:
                    res += 1

                dp[(i, j)] = res 

        # CHECKING THROUGH EVERY STARTING POINT 
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                final_res = 0

        def dfs(i, j):
            value = matrix[i][j]

            if i - 1 > 0 and dp[(i, j)] > 0:
                dfs(i, j)
                
            # RIGHT
            if j + 1 < len(matrix) - 1 and val < matrix[i][j + 1]:
                res += 1

            # DOWN
            if i + 1 < len(matrix) - 1 and val < matrix[i - 1][j]:
                res += 1

            # LEFT
            if j - 1 > 0 and val < matrix[i][j - 1]:
                res += 1

                

                    
