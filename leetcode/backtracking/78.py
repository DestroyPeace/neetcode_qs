class Solution:
    def subsets(self, nums) -> int:
        """from itertools import combinations
        
        temp_res = []
        final_res = []

        for l in range(len(nums) + 1):
            temp_res.extend(combinations(nums, l))
        


        for value in temp_res:
            temp = []

            for num in value:
                temp.append(num)

            final_res.append(temp)

        return final_res
        """

        res = []
        sub = []

        def dfs(i):
            # We've reached the end of the list and therefore the possible subsets.
            if i >= len(nums):
                # Appending onto the result which will be returned.
                res.append(sub.copy())
                return 
            
            # Creating the copy of the values with the first number in nums at the start
            sub.append(nums[i])
            dfs(i + 1)

            # Creating the second branch where the values have been popped. 
            sub.pop()
            dfs(i + 1)

        dfs(0)
        return res

test = Solution()
print(test.subsets(nums = [1, 2, 3]))

