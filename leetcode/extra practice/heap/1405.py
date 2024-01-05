"""
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.
"""

import heapq
import collections 
import math

List = list       

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, max_heap = [], []
        
        # Default is the min heap therefore we use negative to make it a max heap.
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:

            # Won't work if a min heap consists of a 0.
            if count != 0:
                heapq.heappush(max_heap, (count, char))
            
        while max_heap:
            count, char = heapq.heappop(max_heap) 

            if len(res) > 1 and res[-1] == res[-2] == char: 
                if not max_heap: 
                    break 

                count_2, char_2 = heapq.heappop(max_heap)

                res.append(char_2)
                count_2 += 1

                if count_2:
                    heapq.heappush(max_heap, (count_2, char_2))

            else: 
                res.append(char)
                count += 1

            if count:
                heapq.heappush(max_heap, (count, char))
            
        return "".join(res) 
        
test = Solution()
