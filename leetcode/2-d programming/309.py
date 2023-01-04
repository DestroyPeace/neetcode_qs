class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = {} # key = (i, can_buy) : val = max_profit 

        def dfs(index , buying):
            if index not in range(len(prices)):
                return 0

            if (index, buying) in dp:
                return dp[(index, buying)]
            
            cooldown = dfs(index + 1, buying )
            if buying:
                buy = dfs(index + 1, not buying) - prices[index]

                # Skipping - e.g didnt buy anything
                cooldown = dfs(index + 1, buying)
                dp[(index, buying)] = max(buy, cooldown)
            
            else:
                sell = dfs(index + 2, not buying) + prices[index] 
                dp[(index, buying)] = max(sell, cooldown) 
            
            return dp[(index, buying)]
        
        return dfs(0, True)




        """if len(prices) == 1:
            return 0
        
        result = []

        def dfs(stack, index, res):
            if index not in range(len(prices)):
                return res

            # Buying.
            if not stack:
                stack.append(prices[index])
                dfs(stack.copy(), index + 1, res)
            
            # Skipping this one:
            if stack[-1] > prices[index]:
                dfs(stack.copy(), index + 1, res)

            # Selling.
            if stack[-1] < prices[index]:
                val = stack.pop()
                res += (prices[index] - val)
                result.append(res)
                dfs(stack.copy(), index + 2, res)
        
        for index in range(len(prices)):
            dfs([], index, 0)
        
        if result:
            return max(result)
        else:
            return 0"""

print(Solution().maxProfit(prices = [6,1,6,4,3,0,2]))