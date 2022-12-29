class Solution:
    def wordBreak(self, s: str, wordDict: str) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True 

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # If this is true, that means there's enough characters to compare
                # because we are decrementing (don't forget!)
                if i + len(word) <= len(s) and s[i : i + len(word)] == word: 
                    dp[i] = dp[i + len(word)]

                if dp[i]:
                    break 
        
        print(dp)
        return dp[0]

        """test = []
        word = ""

        def word_split(word, string):
            res = "".join(s.split(word))

            # False case. That means this wasn't used to split as the word hasn't changed.
            if res == string:
                return string
            else:
                return res
        
        for word in wordDict:
            s = word_split(word, s)
        


        return True if not s else False
        """

            

test = Solution()
print(test.wordBreak("cars", ["car", "ca", "rs"]))
