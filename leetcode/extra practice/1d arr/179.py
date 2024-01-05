"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
"""

import heapq
import collections 
import math

List = list         

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key = cmp_to_key(compare))

        return str(int("".join(nums)))

test = Solution()
print(test.largestNumber([3,30,34,5,9]))