class Solution:
    def combinationSum(self, candidates, target):
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
            dfs(res, index + 1, val, target)
            dfs(res, index, val, target)

            # Moving onto the next value in the candidates list

        return dfs([], 0, 0, target)

test = Solution()
print(test.combinationSum(candidates = [2,3,6,7], target = 7))