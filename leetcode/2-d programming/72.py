class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        
        # REMOVAL OF EVERYTHING BASE CASES
        if word1 == "":
            return len(word2)
        
        if word2 == "":
            return len(word1)
        
        dp =  [[]]

        def dfs(i, j, operation = 0):
            if (i, j) in cache:
                return cache[(i, j)]

            # Base Case - NO OPERATIONS NECESSARY MOVE ON
            if word1[i] == word2[j]:
                dfs(i + 1, j + 1)

            if word1[i] != word2[j]:

               """
               # TRY ALL THREE OPTIONS:

                # INSERTION - +1 in operations but increments word1 in the presumption that the letter has
                # been inserted to the left of the current index, in effect - i - 1 + 1 = i.

                dfs(i, j + 1, operation + 1)
            
                # DELETION - +1 in operations and shift the i to the right without shifting the right in
                # the presumption that the rest of the words are correct by deleting it.

                dfs(i + 1, j, operation + 1)

                # REPLACEMENT - +1 in operations by switching it, therefore you can move both by assuming 
                # that they're the same. 

                dfs(i + 1, j + 1, operation + 1)
                """

               cache[(i, j)] = dfs(i + 1, j + 1, operation + 1) + 
        


                