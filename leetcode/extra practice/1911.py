List = list 

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """# Basically, these are assuming if the first number was added (sumEven), 
        # or the first number was subtracted. 

        sumEven, sumOdd = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            tmpEven = max(sumOdd + nums[i], sumEven)
            tmpOdd = max(sumEven - nums[i], sumOdd)

            sumEven, sumOdd = tmpEven, tmpOdd
        
        # You always start off on even. 
        return sumEven """

        dp = {}

        def dfs(i, even):
            if i == len(nums):
                return 0
            
            if (i, even) in dp:
                return dp[(i, even)]
            
            total = nums[i] if even else (-1 * nums[i])

            dp[(i, even)] = max((total + dfs(i + 1, not even)), dfs(i + 1, even))

            return dp[(i, even)]
        
        return dfs(0, True)
