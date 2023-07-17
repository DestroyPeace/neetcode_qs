class Solution:
    def climbStairs(self, n: int) -> int:
        """a, b = 0, 1

        for _ in range(n):
            a, b = b, a + b

        return b"""
        
        cache = {

        }

        res = []

        def dfs(num): 
            if num == n:
                res.append(num)
                return 
            
            if num > n:
                return 

            dfs(num + 1)
            dfs(num + 2)

        dfs(0)
        return len(res)

                


test = Solution()
print(test.climbStairs(3))