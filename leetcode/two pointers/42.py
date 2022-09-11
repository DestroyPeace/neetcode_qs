"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        max_l, max_r, res = 0, 0, 0

        l, r = 0, len(height)

        while l < r:
            if height[l] <= height[r]:
                l += 1
                max_l = max(height[l], max_l)
            else:
                r -= 1
                max_r = max(height[r], max_r)
            