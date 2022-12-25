class Solution:
    def combinationSum2(self, candidates: int, target: int) -> int:
        # Sorting the numbers so that they are able to add up and not suddenly go massively
        # over. 
        candidates = sorted(candidates)
        res = []

        def backtrack(sub, index, total):
            if total == 0:
                res.append(sub.copy())
                return
            
            if total < 0:
                return 

            prev = -1
            for i in range(index, len(candidates)):
                if candidates[i] == prev:
                    continue

                sub.append(candidates[i])
                backtrack(sub, i + 1 , total - candidates[i])

                sub.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res
            
        
        

            
            


test = Solution()
print(test.combinationSum2([10, 1, 2, 7, 6, 1, 5], target = 8))


            
            