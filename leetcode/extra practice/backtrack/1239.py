from collections import Counter 

List = list

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        char_set = set()

        def overlap(char_set, s):
            c = Counter(char_set) + Counter(s)

            return max(c.values()) > 1

        def backtrack(i):
            # Assuming we have fully finished our route.
            if i == len(arr):
                return len(char_set) 
            
            res = 0 

            if not overlap(char_set, arr[i]):
                for c in arr[i]:
                    char_set.add(c)
                
                res = backtrack(i + 1)

                for c  in arr[i]:
                    char_set.remove(c)
                
            return max(res, backtrack(i + 1))
        
        return backtrack(0)
