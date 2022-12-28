class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization - Return empty string if one is there. 
        # For each position, retrieve the cache value which is equal to the number of possible solutions
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            # Bad test case. 
            if s[i] == "0":
                return 0

            res = dfs(i + 1) 
            print(res)
            
            # Three checks:

            # 1) Is there another character to iterate after our next character e.g a double digit
            # 2) Is the concatenation of the two strings in the range of 10 to 27?
            if ((i + 1 < len(s)) and int(s[i] +  s[i + 1]) in range(10, 27)):
                res += dfs(i + 2)
            
            # Storing in cache for later use.
            dp[i] = res

            return res
        
        return dfs(0)





        """
        INITIAL ATTEMPT - WASN'T ABLE TO SOLVE 
        if s == "0":
            return 0

        if len(s) == 1:
            return 1

        global res
        res = 0

        def dfs(l, r, started_at_1 = False):
            global res
            # False base cases. 
            if s[l:r + 1].startswith("0") or int(s[l:r + 1]) > 26:
                return False
            
            if r == len(s) - 1:
                res += 1
                return True 

            if started_at_1:   
                dfs(l + 1, r + 1)

            dfs(l + 1, r + 2)


        dfs(0, 0)
        dfs(0, 1, started_at_1 = True)

        return res"""

print(Solution().numDecodings("2101"))
            
            