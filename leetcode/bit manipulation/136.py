class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0

        for n in nums:
            res ^= n

        return res
    
test = Solution()

print(test.singleNumber([1, 1, 2, 2, 3]))