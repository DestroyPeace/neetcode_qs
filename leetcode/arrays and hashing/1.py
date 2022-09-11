class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        seen = {}
        
        for i, n in enumerate(nums):
            if n in seen:
                return [seen[n], i]
        
            seen[target - n] = i
        