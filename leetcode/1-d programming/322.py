class Solution:
    def coinChange(self, coins, amount):
        dp = {}

        if amount == 0:
            return 0
        
        res = []

        def dfs(val, times):
            if val > amount:
                return 

            if val == amount: 
                res.append(times)

            if val not in dp:
                dp[val] = times 


            for num in coins:
                if val + num in dp:
                    res.append(min(times + 1, dp[val + num]))
                else:
                    dfs(val + num, times + 1)
            
        for num in coins:
            dfs(num, 1)

        return min(res) if res else -1

test = Solution()
print(test.coinChange([1, 2, 5], 11))