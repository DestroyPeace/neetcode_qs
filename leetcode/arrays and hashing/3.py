class Solution:
    def lengthOfLongestSubstring(self, string):
        l = 0
        res = 1

        for r, v in enumerate(string):
            while r != 0 and v in string[l:r] and l < r:
                l += 1

            res = max(res, r - l + 1)

        return res

test =  Solution()
print(test.lengthOfLongestSubstring("pwwkew"))
