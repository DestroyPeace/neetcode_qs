import heapq
import collections 
import math

List = list 

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums): 
            # Found the start of a stack.
            if nums[l] == 0 and nums[r] == 0: 
                res += (r - l + 1)

                r += 1
            else:
                # The sliding window has been removed.
                r += 1
                l = r 
                
        return res 

        
test = Solution()
print(test.zeroFilledSubarray(nums = [0,0,0,2,0,0]))
