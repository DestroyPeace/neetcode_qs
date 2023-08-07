class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])

        return res
        

        """
        SUM METHOD        
        
        
        """

        """
        SET INTERFERENCE TECHNIQUE

        res = set(range(len(nums) + 1))

        return (res - set(nums)).pop()
    """
print(Solution().missingNumber([3, 0 , 1]))
