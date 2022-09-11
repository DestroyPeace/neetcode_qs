import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        seen_1 = collections.defaultdict()
        seen_2 = collections.defaultdict()
        l = 0
        res = 0
        res_seen = collections.defaultdict()

        for chr in t:
            seen_1[chr] = seen_1.get(chr, 0) + 1
        
        for chr in s:
            seen_2[chr] = seen_1.get(chr, 0) + 1
        
        if seen_2.items() <= seen_1.items():
            return ""
        
        