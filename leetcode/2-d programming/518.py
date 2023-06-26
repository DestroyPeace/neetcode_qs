class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        
        # Creating the array with the amount as the y value, and the coins as the x value
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]

        # Seting the first value to 0 as 0 of each coin will always give a value of 0.
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
               dp[a][i] = dp[a][i + 1]


    
print(Solution().change(6, [1, 2, 3]))



