"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
"""


import heapq
import collections 
import math

List = list         
        
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        for i in range(len(words) - 1, -1, -1):
            if words[i] != "":
                return len(words[i])



test = Solution()
print(test.lengthOfLastWord("   fly me   to   the moon  "))
