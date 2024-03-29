class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            l, r = i, i
            # Checking if a palindrome exists and that it's within bounds.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1 # if len(s[l:r + 1]) == 1 else 2 # Adding 2 for each palindrome 

                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i + 1

            # Checking if a palindrome exists and that it's within bounds.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1 # if len(s[l:r + 1]) == 1 else 2 # Adding 2 for each palindrome 

                l -= 1
                r += 1

        return res

print(Solution().countSubstrings("aaa"))