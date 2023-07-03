class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        cache = {

        }

        def dfs(index, total):

            # Checking if the entire array has been passed
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
                
            # Checking if it's in cache
            if (index, total) in cache:
                return cache[(index, total)]

            cache[(index, total)] = (dfs(index + 1, total - nums[index])) + (dfs(index + 1 , total + nums[index]))

            return cache[(index, total)]

        return dfs(0, 0)


        """
        DFS - Own solution

        res = []
        
        def dfs(index, total):
            # Checking if the entire array has been passed
            if index == len(nums) - 1:

                if total == target:
                    res.append("1")
                    return
                else:
                    return 

            # Calculate if coin is taken (equivalent to a -)
            dfs(index + 1, total - nums[index + 1])
            # Calculate if coin is not taken (equivalent to a +)
            dfs(index + 1, total + nums[index + 1])

    
        # Calculate the first path where the value is subtracted
        dfs(0, 0 - nums[0])

        # Calculate the second path where the coin is added
        dfs(0, 0 + nums[0])
        return len(res)"""


        """
        DEBUG CODE
        
        def dfs(index, total, steps):
            # Checking if the entire array has been passed
            if index == len(nums) - 1:
                print(total, target, steps)

                if total == target:
                    res.append("1")
                    return
                else:
                    return 

            # Calculate if coin is taken (equivalent to a -)
            dfs(index + 1, total - nums[index + 1], steps[::] + ["-", total - nums[index + 1]])

            # Calculate if coin is not taken (equivalent to a +)
            dfs(index + 1, total + nums[index + 1], steps[::] + ["+", total + nums[index + 1]])

    
        # Calculate the first path where the value is subtracted
        dfs(0, 0 - nums[0], ["-", 0 - nums[0]])

        # Calculate the second path where the coin is added
        dfs(0, 0 + nums[0], ["+", 0 + nums[0]])
        return len(res)"""

test = Solution()
print(test.findTargetSumWays(nums = [1, 1, 1, 1, 1], target = 3))
            