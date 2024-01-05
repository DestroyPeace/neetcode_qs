"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
"""

import heapq
import collections 
import math

List = list         

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = collections.defaultdict(int) 
        ans = set()

        for i in range(len(s) - 9):
            if cnt[s[i:i+10]] == 1: 
                ans.add(s[i:i+10])
            else:
                cnt[s[i:i+10]] += 1
        
        return list(ans)



        


        
test = Solution()
print(test.findRepeatedDnaSequences(s = "AAAAAAAAAAA"))
 