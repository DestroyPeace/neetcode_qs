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
        # Identifying all the 10 letter sequences 
        res = []

        # Base case 
        if len(s) < 10:
            return 0 
        
        # Identifying all of the varying levels - we have to accept that it'll be a list 
        # due to the fact that certain variations where it's just one letter will have multiple
        # varying "checks" but each of them are differing in their index.

        check = [
            s[i: i + 10] for i in range(len(s) - 9)
        ]
        
        for c in check:
            temp = 0 
            
            for i in range(len(s) - 9): 
                if s[i: i + 10] == c and c not in res:
                    temp += 1

            # Using the heuristic that splitting it will remove all of the copies therefore
            # if the length is less than 10 less therefore we know that there must be at least 2.
            if temp > 1: 
                res.append(c) 

        return res 
        


        
test = Solution()
print(test.findRepeatedDnaSequences(s = "AAAAAAAAAAA"))
 