class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = set(range(len(nums) + 1))

        return (res - set(nums)).pop()
    
print(Solution().missingNumber([3, 0 , 1]))
