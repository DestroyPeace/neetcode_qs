class Solution:
    def coinChange(self, coins, amount):
        # Recurrence relation
        # Default values memoization
        dp = [float("inf")] * (amount + 1)

        dp[0] = 0 

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    # Adding the extra coin we need for (1 + dp[a - coins])
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] < float("inf") else -1
        

        """# BACKTRACKING MEMO ALGO Taken from comment section - 

        memo = {}
        def dfs(amount):
            # If we have found our solution, return 0
            if amount == 0:
                return 0

            # If we haven't found our amount, return highest.
            if amount < 0:
                return float("inf")

            # Using memoization
            if amount in memo:

                # Prevents continuation of code.
                return memo[amount]
            
            # Iterating through every possible value
            memo[amount] = min(1 + dfs(amount - c) for c in coins )
            return memo[amount]
        
        mini = dfs(amount)
        return mini if mini < float("inf") else -1

"""

        """
        MY SOLUTION - HAS ISSUES 

        1) Returns wrong values due to implementing memoization.
        2) When it does return the right values it's too slow. 

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

        return min(res) if res else -1"""

test = Solution()
print(test.coinChange([1, 2, 5], 11))