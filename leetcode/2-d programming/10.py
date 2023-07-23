class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == ".*" and s:
            return True 
        
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True 
            
            if j >= len(p):
                return False 
            
            match_case = i in range(len(s)) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) <= len(p) and p[j + 1] == "*":
                return (dfs(i, j + 2) or   # USING THE STAR
                    match_case and dfs(i + 1, j)) # CHECKING FI THE LETTERS MATCH AND USING THE STAR

            # If no star charaacter

            if match_case:
                return dfs(i + 1, j + 1)
            
            return False 


                


    
