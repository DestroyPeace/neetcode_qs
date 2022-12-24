class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        """
        1) Itertools "cheating"
        from itertools import permutations
        # Getting a list[tuple(int...)] and having to convert the variable into
        # list[list[int]]
        res = list(permutations(nums, len(nums)))
        final_res = []

        for value in res:
            temp_res = []

            for number in value:
                temp_res.append(number)

            final_res.append(temp_res)
            
            """

        """
        2) Simplified itertools without importing 
        return permutations(nums)
        """
        
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]] # deepy copy

        # Ensuring that each number is popped at least once.
        for _ in range(len(nums)):
            n = nums.pop(0)

            # Finding all of the numbers that make up said number. 
            perms = self.permute(nums)

            # Checking each of these numbers and adding them onto the permutation
            for perm in perms:
                perm.append(n)

            res.extend(perms)
            
            # Acting like a queue and moving it to the end of the value now.
            nums.append(n)
        
        return res


test = Solution()
print(test.permute([1,2,3]))
    

