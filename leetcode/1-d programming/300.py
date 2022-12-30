class Solution:
    def lengthOfLIS(self, nums: int) -> int:
        cache = [1 for i in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                print(i, j, cache)
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], 1 + cache[j])

        return max(cache)


        """
        OTHER SOLUTION DIDNT WORK
        res = []

        def dfs(sub, index, c): 
            for i in range(index, len(nums)):
                if sub[-1] < nums[i]:
                    sub.append(nums[i])
            
            return sub
                


        for i in range(len(nums)):
            res.append(dfs([float("-inf")], i, 0))
        

        return len(sorted(res, key = len, reverse = True)[0]) - 1"""
        


        """res = 1
        l, r = 0, 0
        c = 0

        while l >= 0 and r <= len(nums) - 1:
            print(l, r)

            print(nums[l], nums[r], nums[l] < nums[r], c, res )
            if nums[l] < nums[r]:
                c += 1
                res = max(c, res)

                l = r
                r += 1
            else:
                c = 0
                l = r 
                r += 1

        return res"""

print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
