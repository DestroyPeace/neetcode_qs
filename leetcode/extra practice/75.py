import heapq
import collections 
import math

List = list 
        
"""
Using the idea of a bucketsort algorithm.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        res = 0
        # Creating the bucket: 

        bucket = { 
            i: 0 for i in range(3)
        }

        for num in nums:
            bucket[num] += 1
        
        # Modifying the list in place: 
        for colour in bucket:
            nums[res: res + bucket[colour]] = [colour for _ in range(bucket[colour])]
            res += bucket[colour] 
            
test = Solution()
print(test.sortColors(nums = [2,0,2,1,1,0]))
