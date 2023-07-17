class Solution:
    def minCostClimbingStairs(self, cost: int) -> int:
        """cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])"""

        res = []
        initial_length = len(cost)
        cost.append(0)

        def dfs(index, t):
            if index >= initial_length:
                res.append(t)
            
            if index + 2 < initial_length:
                dfs(index + 2, t + cost[index + 2])   
                         
            dfs(index + 1, t)

        dfs(0, 0)
        dfs(1, 0)
        return min(res)


test = Solution()
print(test.minCostClimbingStairs([10, 15, 20, 10, 10, 10, 123, 41]))
