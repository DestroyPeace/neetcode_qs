class Solution:
    def canPartition(self, nums: int) -> bool:
        """if sum(nums) % 2 != 0:
            return False 

        def backtrack(target, index):
            if index >= len(nums):
                return False

            if nums[index] == target:
                return True 

            backtrack(target - nums[index], index + 1)
        


        for i in range(len(nums)):
            if backtrack(sum(nums) / 2, i):
                return True 

        return False"""

        if sum(nums) % 2 != 0:
            return False 

        dp = set()
        dp.add(0)
        target = sum(nums) / 2

        for i in range(len(nums)):
            next_dp = dp.copy()
            for t in dp:
                next_dp.add(t + nums[i])

            dp = next_dp

        return target in dp

        
        






print(Solution().canPartition([3, 3, 3, 4, 5]))