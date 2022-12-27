class Solution:
    def longestPalindrome(self, s):
        """l, r = 0, 1

        palindromes = []
        max_len = 0

        while l <= r:
            word = s[l:r + 1]

            if len(word) > max_len and word == reversed(word):
                palindromes.append(word)
                max_len = len(word)
            
            elif """

        res = ""
        res_len = 0

        # Starting from the middle.
        for i in range(len(s)):
            # Assuming an odd length

            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:

                # Checking if it's worth computing by comparing the lengths - OPTIMISATION.
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1

                
                l -= 1
                r += 1
        
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                # Checking if it's worth computing by comparing the lengths - OPTIMISATION.
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1

                
                l -= 1
                r += 1
            
        return res

print(Solution().longestPalindrome("cbbd"))

    
                
