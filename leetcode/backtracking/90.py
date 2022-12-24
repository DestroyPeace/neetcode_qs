class Solution:
    def subsetsWithDup(self, nums: int) -> int:
        
        data = []

        for num in nums:
            if num not in data:
                data.append(num)

        res = []
        sub = []

        def dfs(i):
            if i >= len(data):
                res.append(sub.copy())
                return 
            
            # Begin the recursive DFS with the first option in the branch - choosing a number.
            sub.append(data[i])
            dfs(i + 1)

            # Now, redoing the operation but without choosing the first number / first branch.
            sub.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

test = Solution()
print(test.subsetsWithDup([1, 2, 2]))
        
