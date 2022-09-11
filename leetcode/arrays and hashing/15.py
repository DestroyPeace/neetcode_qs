"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for a in range(len(nums) - 2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            # TWOSUM 

            l, r = a + 1, len(nums) - 1

            while l < r:
                print(a, l , r)
                t = nums[l] + nums[r] + nums[a]
                if t == 0 and [nums[a], nums[l], nums[r]] not in res:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                else:
                    r -= 1

        return res



        """for l in range(len(nums)):
            while l < r:
                t = nums[l] + nums[r]
                
                if t in s:
                    if not(sorted([nums[r], nums[l], t]) in r):
                        r.append(sorted([nums[r], nums[l], t]))"""
                    
test = Solution()
print(test.threeSum([0, 0, 0, 0]))