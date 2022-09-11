from collections import defaultdict

"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        res, l, max_f = 0, 0, 0

        for r, v in enumerate(s):
            seen[v] = seen.get(v, 0) + 1
            max_f = max(max_f, seen[v])

            if (r - l + 1) - max_f > k:
                seen[s[l]] -= 1
                l += 1

            res = r - l + 1

        return res 

test = Solution()
print(test.characterReplacement("ABAB", 2))