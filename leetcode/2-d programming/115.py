class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {

        }

        def dfs(i, j, word = ""):
            # When the target has been completed.
            if j == len(t):
                return 1
            
            # Checking if the next index is out of range
            if i == len(s):

                # No solutions have been found as t has not been incremented upwards to the boundary case yet.
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            # Check the letters against one another:
            if s[i] == t[j]:
                # Two possible solutions:

                # USE THE LETTER AND INCREMENT TARGET
                # DON'T USE THE LETTER AND INCREMENT - FLOYD'S HARE CYCLE ALGO GUARANTEES CYCLE DETECTED

                dp[(i, j)] = dfs(i + 1, j + 1, word = word + s[i]) + dfs(i + 1, j, word = word)

            # If the next letter isn't equal to the target, skip the current index and keep target index.
            else:
                dp[(i, j)] = dfs(i + 1, j) 

            return dp[(i, j)]
            
        dfs(0, 0)

        return dp[(0, 0)]
    
        """
            
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)

            else:
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]
    
        dfs(0, 0)

        return cache[(0, 0)]
    
        """
test = Solution()
print(test.numDistinct(s = "babgbag", t = "bag"))