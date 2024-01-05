List = list 

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def dfs(index):
            
            # If there are no days left to travel, it'll cost 0.
            if index == len(days):
                return 0 
            
            if index in dp:
                return dp[index] 

            dp[index] = float("inf")

            for d, c in zip([1, 7, 30], costs):
                j = index 

                # Tells us the next day we have to purchase a travel ticket.
                while j < len(days) and days[j] < days[index] + d: 
                    j += 1

                dp[index] = min(dp[index], c + dfs(j))



            return dp[index]

        return dfs(0)
