class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        res = []
        
        def dfs(index, total):
            if index == len(nums):
                if total == target:
                    res.append("1")
                    return
                else:
                    return 
            

            dfs(index + 1, total - nums[index + 1])
            dfs(index + 1, total + nums[index + 1])

    
        dfs(0, target - nums[0])
        dfs(0, target + nums[0])
        return len(res)

test = Solution()

print(test.findTargetSumWays(nums = [1, 1, 1, 1, 1], target = 3))
            