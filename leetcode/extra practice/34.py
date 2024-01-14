import heapq
import collections 
import math

List = list         

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False) 

        return [left, right]
    
    def binary_search(self, nums: List[int], target: int, left_bias: bool): 
        l, r = 0, len(nums) - 1 
        i = - 1

        while l <= r: 
            m = (l + r) // 2 

            # Search to the right of the current position 
            if target > nums[m]:
                l = m + 1 
            elif target < nums[m]:
                r = m - 1 
            else: 
                i = m

                if left_bias:
                    r = m - 1 
                
                else:
                    l = m + 1
        
        return i 



                
        
test = Solution()
