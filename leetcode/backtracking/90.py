class Solution:
    def subsetsWithDup(self, nums: int) -> int:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return 

            # The two cases that are possible: 

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # All subsets that don't include nums[i]

            # Removing the latest added value to ensure that the subset is different.
            subset.pop()

            # Also ensuring that we don't fall out of bounds. Ensure that the index checker
            # goes first.
            while nums[i] == nums[i + 1] and i + 1 < len(nums):
                i += 1
            
            # Allows us to get the [] value as well as any other values.
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res



test = Solution()
print(test.subsetsWithDup([1,2,2]))
        
