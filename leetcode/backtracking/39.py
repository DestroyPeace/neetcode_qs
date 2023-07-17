class Solution:
    def combinationSum(self, candidates, target):
        """
        FIRST ATTEMPT - DOESN'T WORK IDK WHY
        def dfs(res, index, val, target):
            val += candidates[index]
            res.append(candidates[index])

            # First checking if any of the conditions have been met.
            if val == target:
                print(val, target, res)
                return res
            
            if val > target:
                return 

            # Repeating the step.
            dfs(res, index, val, target)

            # Moving onto the next value in the candidates list
            dfs(res, index + 1, val, target)

        return dfs([], 0, 0, target)
        """

        res = []

        def dfs(i, cur, total):
            if total == target: 
                res.append(cur.copy())
                return 
            
            if i >= len(candidates) or total > target:
                return 
            
            # Adding the same number
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # Haven't added any new numbers meaning that the total doesn't need to be changed.
            cur.pop()
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)

        return res 


test = Solution()
print(test.combinationSum(candidates = [2,3,6,7], target = 7))