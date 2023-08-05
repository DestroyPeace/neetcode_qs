class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        MEMOIZATION
        
        if p == ".*" and s:
            return True 
        
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(s) and j >= len(p):
                return True 
            
            if j >= len(p):
                return False 
            
            match_case = i in range(len(s)) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) <= len(p) and p[j + 1] == "*":
                cache[(i, j)] = (dfs(i, j + 2) or   # NOT USING THE STAR
                    (match_case and dfs(i + 1, j))) # CHECKING IF THE LETTERS MATCH AND USING THE STAR

                return cache[(i, j)]
        
            # If no star charaacter

            if match_case:
                cache[(i, j)] = dfs(i + 1, j + 1)

                return cache[(i, j)]
            
            cache[(i, j)] = False
            return False 
        
        return dfs(0, 0)"""


                


    
