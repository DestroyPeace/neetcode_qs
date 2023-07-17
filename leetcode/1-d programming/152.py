class Solution:
    def maxProduct(self, nums: int) -> int:
        min_prod = max_prod = res = nums[0]

        for i in range(1, len(nums)):
            n = nums[i] 

            # If a negative number is detected.
            if n < 0:
                min_prod, max_prod = max_prod, min_prod
            
            min_prod = min(min_prod * n, n)
            max_prod = max(max_prod * n, n)

            res = max(res, max_prod)

        return res
