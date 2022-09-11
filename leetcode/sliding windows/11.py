"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        @annotations
        INITIAL METHOD
        res = 0
        r = len(height) - 1

        for l, v in enumerate(height):
            a = (r - l) * min(height[r], v)

            res = max(a, res)
        
        return res"""


        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            a = min(height[l], height[r]) * (r - l)
            res = max(a, res)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
        return res
            
test = Solution()
print(test.maxArea([2,3,4,5,18,17,6]))
