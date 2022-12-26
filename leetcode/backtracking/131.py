class Solution:
    def partition(self, s: str) -> str:
        res = []
        partition = []

        def backtrack(i):
            # If every character has been added 
            # a valid partition exists.
            if i >= len(s):
                res.append(partition.copy())
                return 
            
            # Checking every letter AFTER the current
            # index.
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    

                    # Adding the new partitioned string.
                    partition.append(s[i:j+1])

                    # Finding other partitionable letters starting from the end
                    # of the newly appended partitioned word.
                    backtrack(j + 1)

                    # Removing the partition after the function has been called.
                    partition.pop()
        
        backtrack(0)
        return res

    def isPali(self, s, i, j):
        return s[i:j+1] == "".join(reversed(s[i:j+1]))

test = Solution()
print(test.partition("aab"))
            
        