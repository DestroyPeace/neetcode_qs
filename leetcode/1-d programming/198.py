class Solution:
    def rob(self, nums: int) -> int:
        """res_1, res_2 = 0, 0

        for i in range(len(nums)):
            # EVEN
            if i % 2 == 0:
                res_2 += nums[i]
            else:
                res_1 += nums[i]
        
        return max(res_1, res_2)"""


        """
        Another attempted solution - using backtracking however doesn't work due to
        recursive recall error? For some reason
        def dfs(index, cost):
            # Call to return to the head of the recursive stack.
            if index >= len(nums) - 2:
                return int(cost)
            

            # Returning the cost.
            
            return dfs(index + 2, cost + nums[index + 2])

        return max(dfs(0, nums[0]), dfs(1, nums[1]))"""

        # Sliding windows problem 
        rob_1, rob_2 = 0, 0

        for n in nums:
            temp = max(n + rob_1, rob_2)

            rob_1 = rob_2
            rob_2 = temp
        
        return rob_2


test = Solution()
print(test.rob([1, 2, 3, 1]))

