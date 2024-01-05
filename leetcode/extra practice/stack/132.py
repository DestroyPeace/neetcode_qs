"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""

# First use of monotonically decreasing stack. Essentially, pop the stack each time it
# begins to increase to find the maximum values at the start. This is essential to finding some
# k value and then finding possible j values. 

import heapq
import collections 
import math

List = list         

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """stack = collections.deque([nums[0]])
        prev_min = float("inf")

        for num in nums[1:]:
            # Using the heuristic that given some x, y, z values and knowing that 
            # y < x, therefore given z < y => z < x as well.
            # 
            # We have to use < due to the condition that nums[i] < nums[k] < nums[j] 
            if num < stack[-1]: 
                stack.append(num) 
            
            else:
                # New max has been detected.
                prev_min = min(stack)
                stack = [num]

            print(stack, prev_min)
            if len(stack) > 1 and max(stack[1:]) > prev_min:
                return True 

        return False"""

        stack = [] # pair [num, curLeftMin], mono-decreasing stack
        curMin = nums[0]

        for n in nums:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n < stack[-1][0] and n > stack[-1][1]:
                return True

            stack.append([n, curMin]) 
            curMin = min(n, curMin)

        return False


test = Solution()
print(test.find132pattern(nums = [3,5,0,3,4]))
