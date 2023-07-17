class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # BASE CASES:

        if word1 == word2:
            return 0
        
        if word1 == "":
            return len(word2)
        
        if word2 == "":
            return len(word1)
        
        # INIT THE INITIAL ARRAY
        dp = [[[] for col in range(len(word2) + 1)] for row in range(len(word1) + 1)]

        # SET THE OUTER BOUNDS TO RESPECTIVE VALUES E.G CHANGING EVERY SINGLE VALUE
        for i in range(len(word1) - 1, -1, -1):
            dp[i][-1] = len(word1) - i 
        
        for j in range(0, len(word2)):
            dp[-1][j] = len(word2) - j

        dp[-1][-1] = 0


        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):

                # Take the min of each of the neighbouring operations
                if word1[i] != word2[j]:
                    dp[i][j] = min([dp[i + 1][j], dp[i][j + 1], dp[i +1][j + 1]]) + 1
                
                else:
                    dp[i][j] = dp[i + 1][j + 1]

        return dp[0][0]

test = Solution()
print(test.minDistance(word1 = "intention", word2 = "execution"))
        


                