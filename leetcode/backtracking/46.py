class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """
        from itertools import permutations
        # Getting a list[tuple(int...)] and having to convert the variable into
        # list[list[int]]
        res = list(permutations(nums, len(nums)))
        final_res = []

        for value in res:
            temp_res = []

            for number in value:
                temp_res.append(number)

            final_res.append(temp_res)"""

        return permutations(nums)

test = Solution()
print(test.permute([1,2,3]))
    

